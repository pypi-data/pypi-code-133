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
#     /delphix-masking-service-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_0.web.objects.UserObject import UserObject
from delphixpy.v1_7_0 import factory
from delphixpy.v1_7_0 import common

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

class MaskingServiceConfig(UserObject):
    """
    *(extends* :py:class:`v1_7_0.web.vo.UserObject` *)* Configuration for the
    Masking Service this Engine communicates with.
    """
    def __init__(self, undef_enabled=True):
        super(MaskingServiceConfig, self).__init__()
        self._type = ("MaskingServiceConfig", True)
        self._credentials = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._port = (self.__undef__, True)
        self._server = (self.__undef__, True)
        self._username = (self.__undef__, True)

    API_VERSION = "1.7.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MaskingServiceConfig, cls).from_dict(data, dirty, undef_enabled)
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "Credential"), dirty)
            factory.validate_type(obj._credentials[0], "Credential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        obj._server = (data.get("server", obj.__undef__), dirty)
        if obj._server[0] is not None and obj._server[0] is not obj.__undef__:
            assert isinstance(obj._server[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._server[0], type(obj._server[0])))
            common.validate_format(obj._server[0], "host", None, None)
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MaskingServiceConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials, prop_is_list_or_vo=True)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]))):
            dct["name"] = dictify(self.name)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]) or isinstance(self.port, list) or belongs_to_parent)):
            dct["port"] = dictify(self.port)
        if "server" == "type" or (self.server is not self.__undef__ and (not (dirty and not self._server[1]) or isinstance(self.server, list) or belongs_to_parent)):
            dct["server"] = dictify(self.server)
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]) or isinstance(self.username, list) or belongs_to_parent)):
            dct["username"] = dictify(self.username)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._credentials = (self._credentials[0], True)
        self._name = (self._name[0], True)
        self._port = (self._port[0], True)
        self._server = (self._server[0], True)
        self._username = (self._username[0], True)

    def is_dirty(self):
        return any([self._credentials[1], self._name[1], self._port[1], self._server[1], self._username[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MaskingServiceConfig):
            return False
        return super(MaskingServiceConfig, self).__eq__(other) and \
               self.credentials == other.credentials and \
               self.name == other.name and \
               self.port == other.port and \
               self.server == other.server and \
               self.username == other.username

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def credentials(self):
        """
        Password to use when authenticating to the server.

        :rtype: :py:class:`v1_7_0.web.vo.Credential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

    @property
    def name(self):
        """
        Object name.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def port(self):
        """
        Port number to use.

        :rtype: ``int``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

    @property
    def server(self):
        """
        IP address or hostname of server hosting Masking Service.

        :rtype: ``TEXT_TYPE``
        """
        return self._server[0]

    @server.setter
    def server(self, value):
        self._server = (value, True)

    @property
    def username(self):
        """
        Username to use when authenticating to the server.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

