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
#     /delphix-interface-address.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_10.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_10 import common

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

class InterfaceAddress(TypedObject):
    """
    *(extends* :py:class:`v1_11_10.web.vo.TypedObject` *)* IP address assigned
    to a network interface.
    """
    def __init__(self, undef_enabled=True):
        super(InterfaceAddress, self).__init__()
        self._type = ("InterfaceAddress", True)
        self._address_type = (self.__undef__, True)
        self._address = (self.__undef__, True)
        self._state = (self.__undef__, True)
        self._enable_ssh = (self.__undef__, True)
        self._session_in_use = (self.__undef__, True)

    API_VERSION = "1.11.10"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(InterfaceAddress, cls).from_dict(data, dirty, undef_enabled)
        obj._address_type = (data.get("addressType", obj.__undef__), dirty)
        if obj._address_type[0] is not None and obj._address_type[0] is not obj.__undef__:
            assert isinstance(obj._address_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._address_type[0], type(obj._address_type[0])))
            assert obj._address_type[0] in ['STATIC', 'DHCP'], "Expected enum ['STATIC', 'DHCP'] but got %s" % obj._address_type[0]
            common.validate_format(obj._address_type[0], "None", None, None)
        obj._address = (data.get("address", obj.__undef__), dirty)
        if obj._address[0] is not None and obj._address[0] is not obj.__undef__:
            assert isinstance(obj._address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._address[0], type(obj._address[0])))
            common.validate_format(obj._address[0], "cidrAddress", None, None)
        obj._state = (data.get("state", obj.__undef__), dirty)
        if obj._state[0] is not None and obj._state[0] is not obj.__undef__:
            assert isinstance(obj._state[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._state[0], type(obj._state[0])))
            assert obj._state[0] in ['OK', 'TENTATIVE', 'DUPLICATE', 'INACCESSIBLE'], "Expected enum ['OK', 'TENTATIVE', 'DUPLICATE', 'INACCESSIBLE'] but got %s" % obj._state[0]
            common.validate_format(obj._state[0], "None", None, None)
        obj._enable_ssh = (data.get("enableSSH", obj.__undef__), dirty)
        if obj._enable_ssh[0] is not None and obj._enable_ssh[0] is not obj.__undef__:
            assert isinstance(obj._enable_ssh[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_ssh[0], type(obj._enable_ssh[0])))
            common.validate_format(obj._enable_ssh[0], "None", None, None)
        obj._session_in_use = (data.get("sessionInUse", obj.__undef__), dirty)
        if obj._session_in_use[0] is not None and obj._session_in_use[0] is not obj.__undef__:
            assert isinstance(obj._session_in_use[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._session_in_use[0], type(obj._session_in_use[0])))
            common.validate_format(obj._session_in_use[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(InterfaceAddress, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "address_type" == "type" or (self.address_type is not self.__undef__ and (not (dirty and not self._address_type[1]) or isinstance(self.address_type, list) or belongs_to_parent)):
            dct["addressType"] = dictify(self.address_type)
        elif belongs_to_parent and self.address_type is self.__undef__:
            dct["addressType"] = "STATIC"
        if "address" == "type" or (self.address is not self.__undef__ and (not (dirty and not self._address[1]) or isinstance(self.address, list) or belongs_to_parent)):
            dct["address"] = dictify(self.address)
        if "state" == "type" or (self.state is not self.__undef__ and (not (dirty and not self._state[1]))):
            dct["state"] = dictify(self.state)
        if "enable_ssh" == "type" or (self.enable_ssh is not self.__undef__ and (not (dirty and not self._enable_ssh[1]) or isinstance(self.enable_ssh, list) or belongs_to_parent)):
            dct["enableSSH"] = dictify(self.enable_ssh)
        elif belongs_to_parent and self.enable_ssh is self.__undef__:
            dct["enableSSH"] = True
        if "session_in_use" == "type" or (self.session_in_use is not self.__undef__ and (not (dirty and not self._session_in_use[1]))):
            dct["sessionInUse"] = dictify(self.session_in_use)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._address_type = (self._address_type[0], True)
        self._address = (self._address[0], True)
        self._state = (self._state[0], True)
        self._enable_ssh = (self._enable_ssh[0], True)
        self._session_in_use = (self._session_in_use[0], True)

    def is_dirty(self):
        return any([self._address_type[1], self._address[1], self._state[1], self._enable_ssh[1], self._session_in_use[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, InterfaceAddress):
            return False
        return super(InterfaceAddress, self).__eq__(other) and \
               self.address_type == other.address_type and \
               self.address == other.address and \
               self.state == other.state and \
               self.enable_ssh == other.enable_ssh and \
               self.session_in_use == other.session_in_use

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def address_type(self):
        """
        *(default value: STATIC)* The type of address (STATIC or DHCP).
        *(permitted values: STATIC, DHCP)*

        :rtype: ``TEXT_TYPE``
        """
        return self._address_type[0]

    @address_type.setter
    def address_type(self, value):
        self._address_type = (value, True)

    @property
    def address(self):
        """
        The address in Classless Inter-Domain Routing (CIDR) notation.

        :rtype: ``TEXT_TYPE``
        """
        return self._address[0]

    @address.setter
    def address(self, value):
        self._address = (value, True)

    @property
    def state(self):
        """
        The state of the address. *(permitted values: OK, TENTATIVE, DUPLICATE,
        INACCESSIBLE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._state[0]

    @state.setter
    def state(self, value):
        self._state = (value, True)

    @property
    def enable_ssh(self):
        """
        *(default value: True)* True if this address should accept incoming SSH
        connections.

        :rtype: ``bool``
        """
        return self._enable_ssh[0]

    @enable_ssh.setter
    def enable_ssh(self, value):
        self._enable_ssh = (value, True)

    @property
    def session_in_use(self):
        """
        True if the API session is established over this address. This property
        helps a client make informative decisions about which address should
        not be modified without affecting the session over which it is
        connected.

        :rtype: ``bool``
        """
        return self._session_in_use[0]

    @session_in_use.setter
    def session_in_use(self, value):
        self._session_in_use = (value, True)

