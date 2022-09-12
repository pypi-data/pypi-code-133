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
#     /delphix-network-interface.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.UserObject import UserObject
from delphixpy.v1_11_16 import factory
from delphixpy.v1_11_16 import common

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

class NetworkInterface(UserObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.UserObject` *)* Configuration of an
    IP interface.
    """
    def __init__(self, undef_enabled=True):
        super(NetworkInterface, self).__init__()
        self._type = ("NetworkInterface", True)
        self._device = (self.__undef__, True)
        self._addresses = (self.__undef__, True)
        self._mtu = (self.__undef__, True)
        self._mtu_range = (self.__undef__, True)
        self._mac_address = (self.__undef__, True)
        self._state = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NetworkInterface, cls).from_dict(data, dirty, undef_enabled)
        obj._device = (data.get("device", obj.__undef__), dirty)
        if obj._device[0] is not None and obj._device[0] is not obj.__undef__:
            assert isinstance(obj._device[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._device[0], type(obj._device[0])))
            common.validate_format(obj._device[0], "None", None, None)
        obj._addresses = []
        for item in data.get("addresses") or []:
            obj._addresses.append(factory.create_object(item))
            factory.validate_type(obj._addresses[-1], "InterfaceAddress")
        obj._addresses = (obj._addresses, dirty)
        obj._mtu = (data.get("mtu", obj.__undef__), dirty)
        if obj._mtu[0] is not None and obj._mtu[0] is not obj.__undef__:
            assert isinstance(obj._mtu[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._mtu[0], type(obj._mtu[0])))
            common.validate_format(obj._mtu[0], "None", None, None)
        obj._mtu_range = (data.get("mtuRange", obj.__undef__), dirty)
        if obj._mtu_range[0] is not None and obj._mtu_range[0] is not obj.__undef__:
            assert isinstance(obj._mtu_range[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mtu_range[0], type(obj._mtu_range[0])))
            common.validate_format(obj._mtu_range[0], "None", None, None)
        obj._mac_address = (data.get("macAddress", obj.__undef__), dirty)
        if obj._mac_address[0] is not None and obj._mac_address[0] is not obj.__undef__:
            assert isinstance(obj._mac_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mac_address[0], type(obj._mac_address[0])))
            common.validate_format(obj._mac_address[0], "macAddress", None, None)
        obj._state = (data.get("state", obj.__undef__), dirty)
        if obj._state[0] is not None and obj._state[0] is not obj.__undef__:
            assert isinstance(obj._state[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._state[0], type(obj._state[0])))
            assert obj._state[0] in ['OK', 'DOWN', 'FAILED'], "Expected enum ['OK', 'DOWN', 'FAILED'] but got %s" % obj._state[0]
            common.validate_format(obj._state[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NetworkInterface, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "device" == "type" or (self.device is not self.__undef__ and (not (dirty and not self._device[1]))):
            dct["device"] = dictify(self.device)
        if "addresses" == "type" or (self.addresses is not self.__undef__ and (not (dirty and not self._addresses[1]) or isinstance(self.addresses, list) or belongs_to_parent)):
            dct["addresses"] = dictify(self.addresses, prop_is_list_or_vo=True)
        if "mtu" == "type" or (self.mtu is not self.__undef__ and (not (dirty and not self._mtu[1]) or isinstance(self.mtu, list) or belongs_to_parent)):
            dct["mtu"] = dictify(self.mtu)
        if "mtu_range" == "type" or (self.mtu_range is not self.__undef__ and (not (dirty and not self._mtu_range[1]))):
            dct["mtuRange"] = dictify(self.mtu_range)
        if "mac_address" == "type" or (self.mac_address is not self.__undef__ and (not (dirty and not self._mac_address[1]))):
            dct["macAddress"] = dictify(self.mac_address)
        if "state" == "type" or (self.state is not self.__undef__ and (not (dirty and not self._state[1]))):
            dct["state"] = dictify(self.state)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._device = (self._device[0], True)
        self._addresses = (self._addresses[0], True)
        self._mtu = (self._mtu[0], True)
        self._mtu_range = (self._mtu_range[0], True)
        self._mac_address = (self._mac_address[0], True)
        self._state = (self._state[0], True)

    def is_dirty(self):
        return any([self._device[1], self._addresses[1], self._mtu[1], self._mtu_range[1], self._mac_address[1], self._state[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NetworkInterface):
            return False
        return super(NetworkInterface, self).__eq__(other) and \
               self.device == other.device and \
               self.addresses == other.addresses and \
               self.mtu == other.mtu and \
               self.mtu_range == other.mtu_range and \
               self.mac_address == other.mac_address and \
               self.state == other.state

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def device(self):
        """
        The name of the device over which this interface is configured.

        :rtype: ``TEXT_TYPE``
        """
        return self._device[0]

    @device.setter
    def device(self, value):
        self._device = (value, True)

    @property
    def addresses(self):
        """
        List of IP addresses assigned to the interface.

        :rtype: ``list`` of :py:class:`v1_11_16.web.vo.InterfaceAddress`
        """
        return self._addresses[0]

    @addresses.setter
    def addresses(self, value):
        self._addresses = (value, True)

    @property
    def mtu(self):
        """
        The maximum transmission unit for this interface.

        :rtype: ``int``
        """
        return self._mtu[0]

    @mtu.setter
    def mtu(self, value):
        self._mtu = (value, True)

    @property
    def mtu_range(self):
        """
        The range of possible values for the mtu property.

        :rtype: ``TEXT_TYPE``
        """
        return self._mtu_range[0]

    @mtu_range.setter
    def mtu_range(self, value):
        self._mtu_range = (value, True)

    @property
    def mac_address(self):
        """
        The MAC address associated with this interface.

        :rtype: ``TEXT_TYPE``
        """
        return self._mac_address[0]

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = (value, True)

    @property
    def state(self):
        """
        The state of the interface. *(permitted values: OK, DOWN, FAILED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._state[0]

    @state.setter
    def state(self, value):
        self._state = (value, True)

