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
#     /delphix-network-route.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_11 import common

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

class NetworkRoute(TypedObject):
    """
    *(extends* :py:class:`v1_11_11.web.vo.TypedObject` *)* IP routing table.
    """
    def __init__(self, undef_enabled=True):
        super(NetworkRoute, self).__init__()
        self._type = ("NetworkRoute", True)
        self._destination = (self.__undef__, True)
        self._gateway = (self.__undef__, True)
        self._out_interface = (self.__undef__, True)
        self._protocol = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NetworkRoute, cls).from_dict(data, dirty, undef_enabled)
        obj._destination = (data.get("destination", obj.__undef__), dirty)
        if obj._destination[0] is not None and obj._destination[0] is not obj.__undef__:
            assert isinstance(obj._destination[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._destination[0], type(obj._destination[0])))
            common.validate_format(obj._destination[0], "routeDestination", None, None)
        obj._gateway = (data.get("gateway", obj.__undef__), dirty)
        if obj._gateway[0] is not None and obj._gateway[0] is not obj.__undef__:
            assert isinstance(obj._gateway[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._gateway[0], type(obj._gateway[0])))
            common.validate_format(obj._gateway[0], "ipAddress", None, None)
        obj._out_interface = (data.get("outInterface", obj.__undef__), dirty)
        if obj._out_interface[0] is not None and obj._out_interface[0] is not obj.__undef__:
            assert isinstance(obj._out_interface[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._out_interface[0], type(obj._out_interface[0])))
            common.validate_format(obj._out_interface[0], "objectReference", None, None)
        obj._protocol = (data.get("protocol", obj.__undef__), dirty)
        if obj._protocol[0] is not None and obj._protocol[0] is not obj.__undef__:
            assert isinstance(obj._protocol[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._protocol[0], type(obj._protocol[0])))
            assert obj._protocol[0] in ['KERNEL', 'STATIC', 'DHCP'], "Expected enum ['KERNEL', 'STATIC', 'DHCP'] but got %s" % obj._protocol[0]
            common.validate_format(obj._protocol[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NetworkRoute, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "destination" == "type" or (self.destination is not self.__undef__ and (not (dirty and not self._destination[1]) or isinstance(self.destination, list) or belongs_to_parent)):
            dct["destination"] = dictify(self.destination)
        if "gateway" == "type" or (self.gateway is not self.__undef__ and (not (dirty and not self._gateway[1]) or isinstance(self.gateway, list) or belongs_to_parent)):
            dct["gateway"] = dictify(self.gateway)
        if "out_interface" == "type" or (self.out_interface is not self.__undef__ and (not (dirty and not self._out_interface[1]) or isinstance(self.out_interface, list) or belongs_to_parent)):
            dct["outInterface"] = dictify(self.out_interface)
        if "protocol" == "type" or (self.protocol is not self.__undef__ and (not (dirty and not self._protocol[1]))):
            dct["protocol"] = dictify(self.protocol)
        if dirty and "protocol" in dct:
            del dct["protocol"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._destination = (self._destination[0], True)
        self._gateway = (self._gateway[0], True)
        self._out_interface = (self._out_interface[0], True)
        self._protocol = (self._protocol[0], True)

    def is_dirty(self):
        return any([self._destination[1], self._gateway[1], self._out_interface[1], self._protocol[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NetworkRoute):
            return False
        return super(NetworkRoute, self).__eq__(other) and \
               self.destination == other.destination and \
               self.gateway == other.gateway and \
               self.out_interface == other.out_interface and \
               self.protocol == other.protocol

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def destination(self):
        """
        Destination for the route in Classless Inter-Domain Routing (CIDR)
        notation or the keyword 'default'.

        :rtype: ``TEXT_TYPE``
        """
        return self._destination[0]

    @destination.setter
    def destination(self, value):
        self._destination = (value, True)

    @property
    def gateway(self):
        """
        Next hop for the route.

        :rtype: ``TEXT_TYPE``
        """
        return self._gateway[0]

    @gateway.setter
    def gateway(self, value):
        self._gateway = (value, True)

    @property
    def out_interface(self):
        """
        Output interface to use for the route.

        :rtype: ``TEXT_TYPE``
        """
        return self._out_interface[0]

    @out_interface.setter
    def out_interface(self, value):
        self._out_interface = (value, True)

    @property
    def protocol(self):
        """
        The protocol used to manage the route. *(permitted values: KERNEL,
        STATIC, DHCP)*

        :rtype: ``TEXT_TYPE``
        """
        return self._protocol[0]

    @protocol.setter
    def protocol(self, value):
        self._protocol = (value, True)

