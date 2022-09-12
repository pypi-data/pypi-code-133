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
#     /delphix-mssql-availability-group-listener.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_3 import common

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

class MSSqlAvailabilityGroupListener(TypedObject):
    """
    *(extends* :py:class:`v1_4_3.web.vo.TypedObject` *)* The representation of
    a SQL Server Availability Group Listener.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlAvailabilityGroupListener, self).__init__()
        self._type = ("MSSqlAvailabilityGroupListener", True)
        self._ip_address = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._port = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlAvailabilityGroupListener, cls).from_dict(data, dirty, undef_enabled)
        obj._ip_address = (data.get("ipAddress", obj.__undef__), dirty)
        if obj._ip_address[0] is not None and obj._ip_address[0] is not obj.__undef__:
            assert isinstance(obj._ip_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._ip_address[0], type(obj._ip_address[0])))
            common.validate_format(obj._ip_address[0], "ipAddress", None, None)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlAvailabilityGroupListener, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "ip_address" == "type" or (self.ip_address is not self.__undef__ and (not (dirty and not self._ip_address[1]))):
            dct["ipAddress"] = dictify(self.ip_address)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]))):
            dct["name"] = dictify(self.name)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]))):
            dct["port"] = dictify(self.port)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._ip_address = (self._ip_address[0], True)
        self._name = (self._name[0], True)
        self._port = (self._port[0], True)

    def is_dirty(self):
        return any([self._ip_address[1], self._name[1], self._port[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlAvailabilityGroupListener):
            return False
        return super(MSSqlAvailabilityGroupListener, self).__eq__(other) and \
               self.ip_address == other.ip_address and \
               self.name == other.name and \
               self.port == other.port

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def ip_address(self):
        """
        The IP address of the Availability Group Listener.

        :rtype: ``TEXT_TYPE``
        """
        return self._ip_address[0]

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = (value, True)

    @property
    def name(self):
        """
        The name of the Availability Group Listener.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def port(self):
        """
        The port for the Availability Group Listener.

        :rtype: ``float``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

