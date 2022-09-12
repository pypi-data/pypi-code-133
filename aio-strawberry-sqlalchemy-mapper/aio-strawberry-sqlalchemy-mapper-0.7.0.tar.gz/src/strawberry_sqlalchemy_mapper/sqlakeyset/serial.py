"""Bookmark (de)serialization logic."""

import base64
import csv
import datetime
import decimal
import uuid
from io import StringIO

import dateutil.parser


class InvalidPage(Exception):
    """
    An invalid page marker (in either tuple or bookmark string form) was
    provided to a paging method.
    """


class BadBookmark(InvalidPage):
    """A bookmark string failed to parse"""


class PageSerializationError(Exception):
    """Generic serialization error."""


class UnregisteredType(Exception):
    """An unregistered type was encountered when serializing a bookmark."""


class ConfigurationError(Exception):
    """An error to do with configuring custom bookmark types."""


NONE = "x"
TRUE = "true"
FALSE = "false"
STRING = "s"
BINARY = "b"
INTEGER = "i"
FLOAT = "f"
DECIMAL = "n"
DATE = "d"
DATETIME = "dt"
TIME = "t"
UUID = "uuid"


def parsedate(x):
    return dateutil.parser.parse(x).date()


def binencode(x):
    return base64.b64encode(x).decode("utf-8")


def bindecode(x):
    return base64.b64decode(x.encode("utf-8"))


TYPES = [
    (str, "s"),
    (int, "i"),
    (float, "f"),
    (bytes, "b", bindecode, binencode),
    (decimal.Decimal, "n"),
    (uuid.UUID, "uuid"),
    (datetime.datetime, "dt", dateutil.parser.parse),
    (datetime.date, "d", parsedate),
    (datetime.time, "t"),
]

BUILTINS = {
    "x": None,
    "true": True,
    "false": False,
}
BUILTINS_INV = {v: k for k, v in BUILTINS.items()}


class Serial:
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.serializers = {}
        self.deserializers = {}
        for definition in TYPES:
            self.register_type(*definition)

    def register_type(self, type, code, deserializer=None, serializer=None):
        if serializer is None:
            serializer = str
        if deserializer is None:
            deserializer = type
        if type in self.serializers:
            raise ConfigurationError("Type {type} already has a serializer registered.")
        if code in self.deserializers:
            raise ConfigurationError("Type code {code} is already in use.")
        self.serializers[type] = lambda x: (code, serializer(x))
        self.deserializers[code] = deserializer

    def split(self, joined):
        s = StringIO(joined)
        r = csv.reader(s, **self.kwargs)
        row = next(r)
        return row

    def join(self, string_list):
        s = StringIO()
        w = csv.writer(s, **self.kwargs)
        w.writerow(string_list)
        return s.getvalue()

    def serialize_values(self, values):
        if values is None:
            return ""
        return self.join(self.serialize_value(_) for _ in values)

    def unserialize_values(self, s):
        if s == "":
            return None

        return [self.unserialize_value(_) for _ in self.split(s)]

    def serialize_value(self, x):
        try:
            serializer = self.serializers[type(x)]
        except KeyError:
            pass  # fall through to builtins
        else:
            try:
                c, x = serializer(x)
            except Exception as e:
                raise PageSerializationError(
                    "Custom bookmark serializer " "encountered error"
                ) from e
            else:
                return f"{c}:{x}"

        try:
            return BUILTINS_INV[x]
        except KeyError:
            raise UnregisteredType(
                "Don't know how to serialize type of {} ({}). "
                "Use custom_bookmark_type to register it.".format(x, type(x))
            )

    def unserialize_value(self, x):
        try:
            c, v = x.split(":", 1)
        except ValueError:
            c = x
            v = None

        try:
            deserializer = self.deserializers[c]
        except KeyError:
            pass  # fall through to builtins
        else:
            try:
                return deserializer(v)
            except Exception as e:
                raise BadBookmark(
                    "Custom bookmark deserializer" "encountered error"
                ) from e

        try:
            return BUILTINS[c]
        except KeyError:
            raise BadBookmark(f"unrecognized value {x}")
