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

from delphixpy.v1_4_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_2 import common

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
    *(extends* :py:class:`v1_4_2.web.vo.TypedObject` *)* IP address assigned to
    a network interface.
    """
    def __init__(self, undef_enabled=True):
        super(InterfaceAddress, self).__init__()
        self._type = ("InterfaceAddress", True)
        self._address = (self.__undef__, True)
        self._address_type = (self.__undef__, True)
        self._state = (self.__undef__, True)

    API_VERSION = "1.4.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(InterfaceAddress, cls).from_dict(data, dirty, undef_enabled)
        obj._address = (data.get("address", obj.__undef__), dirty)
        if obj._address[0] is not None and obj._address[0] is not obj.__undef__:
            assert isinstance(obj._address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._address[0], type(obj._address[0])))
            common.validate_format(obj._address[0], "cidrAddress", None, None)
        obj._address_type = (data.get("addressType", obj.__undef__), dirty)
        if obj._address_type[0] is not None and obj._address_type[0] is not obj.__undef__:
            assert isinstance(obj._address_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._address_type[0], type(obj._address_type[0])))
            assert obj._address_type[0] in ['STATIC', 'DHCP'], "Expected enum ['STATIC', 'DHCP'] but got %s" % obj._address_type[0]
            common.validate_format(obj._address_type[0], "None", None, None)
        obj._state = (data.get("state", obj.__undef__), dirty)
        if obj._state[0] is not None and obj._state[0] is not obj.__undef__:
            assert isinstance(obj._state[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._state[0], type(obj._state[0])))
            assert obj._state[0] in ['OK', 'TENTATIVE', 'DUPLICATE'], "Expected enum ['OK', 'TENTATIVE', 'DUPLICATE'] but got %s" % obj._state[0]
            common.validate_format(obj._state[0], "None", None, None)
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
        if "address" == "type" or (self.address is not self.__undef__ and (not (dirty and not self._address[1]) or isinstance(self.address, list) or belongs_to_parent)):
            dct["address"] = dictify(self.address)
        if "address_type" == "type" or (self.address_type is not self.__undef__ and (not (dirty and not self._address_type[1]) or isinstance(self.address_type, list) or belongs_to_parent)):
            dct["addressType"] = dictify(self.address_type)
        elif belongs_to_parent and self.address_type is self.__undef__:
            dct["addressType"] = "STATIC"
        if "state" == "type" or (self.state is not self.__undef__ and (not (dirty and not self._state[1]))):
            dct["state"] = dictify(self.state)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._address = (self._address[0], True)
        self._address_type = (self._address_type[0], True)
        self._state = (self._state[0], True)

    def is_dirty(self):
        return any([self._address[1], self._address_type[1], self._state[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, InterfaceAddress):
            return False
        return super(InterfaceAddress, self).__eq__(other) and \
               self.address == other.address and \
               self.address_type == other.address_type and \
               self.state == other.state

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

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
    def state(self):
        """
        The state of the address. *(permitted values: OK, TENTATIVE,
        DUPLICATE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._state[0]

    @state.setter
    def state(self, value):
        self._state = (value, True)

