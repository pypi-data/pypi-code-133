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
#     /delphix-session.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_15 import factory
from delphixpy.v1_11_15 import common

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

class APISession(TypedObject):
    """
    *(extends* :py:class:`v1_11_15.web.vo.TypedObject` *)* Describes a Delphix
    web service session and is the result of an initial handshake.
    """
    def __init__(self, undef_enabled=True):
        super(APISession, self).__init__()
        self._type = ("APISession", True)
        self._version = (self.__undef__, True)
        self._locale = (self.__undef__, True)
        self._client = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(APISession, cls).from_dict(data, dirty, undef_enabled)
        if "version" not in data:
            raise ValueError("Missing required property \"version\".")
        if "version" in data and data["version"] is not None:
            obj._version = (factory.create_object(data["version"], "APIVersion"), dirty)
            factory.validate_type(obj._version[0], "APIVersion")
        else:
            obj._version = (obj.__undef__, dirty)
        obj._locale = (data.get("locale", obj.__undef__), dirty)
        if obj._locale[0] is not None and obj._locale[0] is not obj.__undef__:
            assert isinstance(obj._locale[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._locale[0], type(obj._locale[0])))
            common.validate_format(obj._locale[0], "locale", None, None)
        obj._client = (data.get("client", obj.__undef__), dirty)
        if obj._client[0] is not None and obj._client[0] is not obj.__undef__:
            assert isinstance(obj._client[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._client[0], type(obj._client[0])))
            common.validate_format(obj._client[0], "None", None, 64)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(APISession, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]) or isinstance(self.version, list) or belongs_to_parent)):
            dct["version"] = dictify(self.version, prop_is_list_or_vo=True)
        if "locale" == "type" or (self.locale is not self.__undef__ and (not (dirty and not self._locale[1]))):
            dct["locale"] = dictify(self.locale)
        if "client" == "type" or (self.client is not self.__undef__ and (not (dirty and not self._client[1]))):
            dct["client"] = dictify(self.client)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._version = (self._version[0], True)
        self._locale = (self._locale[0], True)
        self._client = (self._client[0], True)

    def is_dirty(self):
        return any([self._version[1], self._locale[1], self._client[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, APISession):
            return False
        return super(APISession, self).__eq__(other) and \
               self.version == other.version and \
               self.locale == other.locale and \
               self.client == other.client

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def version(self):
        """
        Version of the API to use.

        :rtype: :py:class:`v1_11_15.web.vo.APIVersion`
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

    @property
    def locale(self):
        """
        Locale as an IETF BCP 47 language tag, defaults to 'en-US'.

        :rtype: ``TEXT_TYPE``
        """
        return self._locale[0]

    @locale.setter
    def locale(self, value):
        self._locale = (value, True)

    @property
    def client(self):
        """
        Client software identification token.

        :rtype: ``TEXT_TYPE``
        """
        return self._client[0]

    @client.setter
    def client(self, value):
        self._client = (value, True)

