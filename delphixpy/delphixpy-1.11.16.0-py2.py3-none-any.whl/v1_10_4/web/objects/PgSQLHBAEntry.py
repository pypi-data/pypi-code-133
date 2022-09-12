# coding: utf8
#
# Copyright 2022 by Delphix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This class has been automatically generated from:
#     /delphix-pgsql-hba-entry.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_4 import common

class __Undef(object):
    def __repr__(self):
        return "undef"

    def __setattr__(self, name, value):
        raise Exception('Cannot modify attributes of __Undef.')

_UNDEFINED = __Undef()

try:
    TEXT_TYPE = unicode
except NameError:
    TEXT_TYPE = str

class PgSQLHBAEntry(TypedObject):
    """
    *(extends* :py:class:`v1_10_4.web.vo.TypedObject` *)* An entry in the
    PostgreSQL host-based authentication file (pg_hba.conf).
    """
    def __init__(self, undef_enabled=True):
        super(PgSQLHBAEntry, self).__init__()
        self._type = ("PgSQLHBAEntry", True)
        self._entry_type = (self.__undef__, True)
        self._database = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._address = (self.__undef__, True)
        self._auth_method = (self.__undef__, True)
        self._auth_options = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PgSQLHBAEntry, cls).from_dict(data, dirty, undef_enabled)
        obj._entry_type = (data.get("entryType", obj.__undef__), dirty)
        if obj._entry_type[0] is not None and obj._entry_type[0] is not obj.__undef__:
            assert isinstance(obj._entry_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._entry_type[0], type(obj._entry_type[0])))
            assert obj._entry_type[0] in ['local', 'host', 'hostssl', 'hostnossl'], "Expected enum ['local', 'host', 'hostssl', 'hostnossl'] but got %s" % obj._entry_type[0]
            common.validate_format(obj._entry_type[0], "None", None, None)
        obj._database = (data.get("database", obj.__undef__), dirty)
        if obj._database[0] is not None and obj._database[0] is not obj.__undef__:
            assert isinstance(obj._database[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database[0], type(obj._database[0])))
            common.validate_format(obj._database[0], "None", None, 63)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "None", None, 63)
        obj._address = (data.get("address", obj.__undef__), dirty)
        if obj._address[0] is not None and obj._address[0] is not obj.__undef__:
            assert isinstance(obj._address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._address[0], type(obj._address[0])))
            common.validate_format(obj._address[0], "None", None, None)
        obj._auth_method = (data.get("authMethod", obj.__undef__), dirty)
        if obj._auth_method[0] is not None and obj._auth_method[0] is not obj.__undef__:
            assert isinstance(obj._auth_method[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._auth_method[0], type(obj._auth_method[0])))
            assert obj._auth_method[0] in ['trust', 'reject', 'md5', 'password', 'gss', 'sspi', 'krb5', 'ident', 'peer', 'ldap', 'radius', 'cert', 'pam'], "Expected enum ['trust', 'reject', 'md5', 'password', 'gss', 'sspi', 'krb5', 'ident', 'peer', 'ldap', 'radius', 'cert', 'pam'] but got %s" % obj._auth_method[0]
            common.validate_format(obj._auth_method[0], "None", None, None)
        obj._auth_options = (data.get("authOptions", obj.__undef__), dirty)
        if obj._auth_options[0] is not None and obj._auth_options[0] is not obj.__undef__:
            assert isinstance(obj._auth_options[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._auth_options[0], type(obj._auth_options[0])))
            common.validate_format(obj._auth_options[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PgSQLHBAEntry, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "entry_type" == "type" or (self.entry_type is not self.__undef__ and (not (dirty and not self._entry_type[1]) or isinstance(self.entry_type, list) or belongs_to_parent)):
            dct["entryType"] = dictify(self.entry_type)
        if "database" == "type" or (self.database is not self.__undef__ and (not (dirty and not self._database[1]) or isinstance(self.database, list) or belongs_to_parent)):
            dct["database"] = dictify(self.database)
        elif belongs_to_parent and self.database is self.__undef__:
            dct["database"] = "all"
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        elif belongs_to_parent and self.user is self.__undef__:
            dct["user"] = "all"
        if "address" == "type" or (self.address is not self.__undef__ and (not (dirty and not self._address[1]) or isinstance(self.address, list) or belongs_to_parent)):
            dct["address"] = dictify(self.address)
        if "auth_method" == "type" or (self.auth_method is not self.__undef__ and (not (dirty and not self._auth_method[1]) or isinstance(self.auth_method, list) or belongs_to_parent)):
            dct["authMethod"] = dictify(self.auth_method)
        if "auth_options" == "type" or (self.auth_options is not self.__undef__ and (not (dirty and not self._auth_options[1]) or isinstance(self.auth_options, list) or belongs_to_parent)):
            dct["authOptions"] = dictify(self.auth_options)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._entry_type = (self._entry_type[0], True)
        self._database = (self._database[0], True)
        self._user = (self._user[0], True)
        self._address = (self._address[0], True)
        self._auth_method = (self._auth_method[0], True)
        self._auth_options = (self._auth_options[0], True)

    def is_dirty(self):
        return any([self._entry_type[1], self._database[1], self._user[1], self._address[1], self._auth_method[1], self._auth_options[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PgSQLHBAEntry):
            return False
        return super(PgSQLHBAEntry, self).__eq__(other) and \
               self.entry_type == other.entry_type and \
               self.database == other.database and \
               self.user == other.user and \
               self.address == other.address and \
               self.auth_method == other.auth_method and \
               self.auth_options == other.auth_options

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def entry_type(self):
        """
        The connection type of this entry. *(permitted values: local, host,
        hostssl, hostnossl)*

        :rtype: ``TEXT_TYPE``
        """
        return self._entry_type[0]

    @entry_type.setter
    def entry_type(self, value):
        self._entry_type = (value, True)

    @property
    def database(self):
        """
        *(default value: all)* The database name this entry matches.

        :rtype: ``TEXT_TYPE``
        """
        return self._database[0]

    @database.setter
    def database(self, value):
        self._database = (value, True)

    @property
    def user(self):
        """
        *(default value: all)* The database username this entry matches.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def address(self):
        """
        The client machine address that this entry matches.

        :rtype: ``TEXT_TYPE``
        """
        return self._address[0]

    @address.setter
    def address(self, value):
        self._address = (value, True)

    @property
    def auth_method(self):
        """
        The authentication method to use when connecting via this entry.
        *(permitted values: trust, reject, md5, password, gss, sspi, krb5,
        ident, peer, ldap, radius, cert, pam)*

        :rtype: ``TEXT_TYPE``
        """
        return self._auth_method[0]

    @auth_method.setter
    def auth_method(self, value):
        self._auth_method = (value, True)

    @property
    def auth_options(self):
        """
        Options for the authentication method.

        :rtype: ``TEXT_TYPE``
        """
        return self._auth_options[0]

    @auth_options.setter
    def auth_options(self, value):
        self._auth_options = (value, True)

