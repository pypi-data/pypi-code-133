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
#     /delphix-connectivity-connector.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_5 import factory
from delphixpy.v1_10_5 import common

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

class ConnectorConnectivity(TypedObject):
    """
    *(extends* :py:class:`v1_10_5.web.vo.TypedObject` *)* Mechanism to test
    Connector connectivity of arbitrary hosts.
    """
    def __init__(self, undef_enabled=True):
        super(ConnectorConnectivity, self).__init__()
        self._type = ("ConnectorConnectivity", True)
        self._address = (self.__undef__, True)
        self._proxy = (self.__undef__, True)
        self._port = (self.__undef__, True)
        self._username = (self.__undef__, True)
        self._credentials = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ConnectorConnectivity, cls).from_dict(data, dirty, undef_enabled)
        if "address" not in data:
            raise ValueError("Missing required property \"address\".")
        obj._address = (data.get("address", obj.__undef__), dirty)
        if obj._address[0] is not None and obj._address[0] is not obj.__undef__:
            assert isinstance(obj._address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._address[0], type(obj._address[0])))
            common.validate_format(obj._address[0], "host", None, None)
        obj._proxy = (data.get("proxy", obj.__undef__), dirty)
        if obj._proxy[0] is not None and obj._proxy[0] is not obj.__undef__:
            assert isinstance(obj._proxy[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._proxy[0], type(obj._proxy[0])))
            common.validate_format(obj._proxy[0], "objectReference", None, None)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        if "username" not in data:
            raise ValueError("Missing required property \"username\".")
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "None", None, None)
        if "credentials" not in data:
            raise ValueError("Missing required property \"credentials\".")
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._credentials[0], "PasswordCredential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ConnectorConnectivity, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "address" == "type" or (self.address is not self.__undef__ and (not (dirty and not self._address[1]) or isinstance(self.address, list) or belongs_to_parent)):
            dct["address"] = dictify(self.address)
        if "proxy" == "type" or (self.proxy is not self.__undef__ and (not (dirty and not self._proxy[1]) or isinstance(self.proxy, list) or belongs_to_parent)):
            dct["proxy"] = dictify(self.proxy)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]))):
            dct["port"] = dictify(self.port)
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]) or isinstance(self.username, list) or belongs_to_parent)):
            dct["username"] = dictify(self.username)
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._address = (self._address[0], True)
        self._proxy = (self._proxy[0], True)
        self._port = (self._port[0], True)
        self._username = (self._username[0], True)
        self._credentials = (self._credentials[0], True)

    def is_dirty(self):
        return any([self._address[1], self._proxy[1], self._port[1], self._username[1], self._credentials[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ConnectorConnectivity):
            return False
        return super(ConnectorConnectivity, self).__eq__(other) and \
               self.address == other.address and \
               self.proxy == other.proxy and \
               self.port == other.port and \
               self.username == other.username and \
               self.credentials == other.credentials

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def address(self):
        """
        Target host name or IP address.

        :rtype: ``TEXT_TYPE``
        """
        return self._address[0]

    @address.setter
    def address(self, value):
        self._address = (value, True)

    @property
    def proxy(self):
        """
        Host to use as a proxy for credential validation.

        :rtype: ``TEXT_TYPE``
        """
        return self._proxy[0]

    @proxy.setter
    def proxy(self, value):
        self._proxy = (value, True)

    @property
    def port(self):
        """
        *(default value: 9100)* Connector port on remote server.

        :rtype: ``int``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

    @property
    def username(self):
        """
        User name.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

    @property
    def credentials(self):
        """
        User credentials.

        :rtype: :py:class:`v1_10_5.web.vo.PasswordCredential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

