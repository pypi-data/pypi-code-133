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
#     /delphix-host-configuration.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_0 import factory
from delphixpy.v1_5_0 import common

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

class HostConfiguration(TypedObject):
    """
    *(extends* :py:class:`v1_5_0.web.vo.TypedObject` *)* The representation of
    the host configuration properties.
    """
    def __init__(self, undef_enabled=True):
        super(HostConfiguration, self).__init__()
        self._type = ("HostConfiguration", True)
        self._discovered = (self.__undef__, True)
        self._last_refreshed = (self.__undef__, True)
        self._last_updated = (self.__undef__, True)
        self._machine = (self.__undef__, True)
        self._operating_system = (self.__undef__, True)

    API_VERSION = "1.5.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HostConfiguration, cls).from_dict(data, dirty, undef_enabled)
        obj._discovered = (data.get("discovered", obj.__undef__), dirty)
        if obj._discovered[0] is not None and obj._discovered[0] is not obj.__undef__:
            assert isinstance(obj._discovered[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._discovered[0], type(obj._discovered[0])))
            common.validate_format(obj._discovered[0], "None", None, None)
        obj._last_refreshed = (data.get("lastRefreshed", obj.__undef__), dirty)
        if obj._last_refreshed[0] is not None and obj._last_refreshed[0] is not obj.__undef__:
            assert isinstance(obj._last_refreshed[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_refreshed[0], type(obj._last_refreshed[0])))
            common.validate_format(obj._last_refreshed[0], "None", None, None)
        obj._last_updated = (data.get("lastUpdated", obj.__undef__), dirty)
        if obj._last_updated[0] is not None and obj._last_updated[0] is not obj.__undef__:
            assert isinstance(obj._last_updated[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_updated[0], type(obj._last_updated[0])))
            common.validate_format(obj._last_updated[0], "None", None, None)
        if "machine" in data and data["machine"] is not None:
            obj._machine = (factory.create_object(data["machine"], "HostMachine"), dirty)
            factory.validate_type(obj._machine[0], "HostMachine")
        else:
            obj._machine = (obj.__undef__, dirty)
        if "operatingSystem" in data and data["operatingSystem"] is not None:
            obj._operating_system = (factory.create_object(data["operatingSystem"], "HostOS"), dirty)
            factory.validate_type(obj._operating_system[0], "HostOS")
        else:
            obj._operating_system = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(HostConfiguration, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "discovered" == "type" or (self.discovered is not self.__undef__ and (not (dirty and not self._discovered[1]))):
            dct["discovered"] = dictify(self.discovered)
        if "last_refreshed" == "type" or (self.last_refreshed is not self.__undef__ and (not (dirty and not self._last_refreshed[1]))):
            dct["lastRefreshed"] = dictify(self.last_refreshed)
        if "last_updated" == "type" or (self.last_updated is not self.__undef__ and (not (dirty and not self._last_updated[1]))):
            dct["lastUpdated"] = dictify(self.last_updated)
        if "machine" == "type" or (self.machine is not self.__undef__ and (not (dirty and not self._machine[1]))):
            dct["machine"] = dictify(self.machine)
        if "operating_system" == "type" or (self.operating_system is not self.__undef__ and (not (dirty and not self._operating_system[1]))):
            dct["operatingSystem"] = dictify(self.operating_system)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._discovered = (self._discovered[0], True)
        self._last_refreshed = (self._last_refreshed[0], True)
        self._last_updated = (self._last_updated[0], True)
        self._machine = (self._machine[0], True)
        self._operating_system = (self._operating_system[0], True)

    def is_dirty(self):
        return any([self._discovered[1], self._last_refreshed[1], self._last_updated[1], self._machine[1], self._operating_system[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HostConfiguration):
            return False
        return super(HostConfiguration, self).__eq__(other) and \
               self.discovered == other.discovered and \
               self.last_refreshed == other.last_refreshed and \
               self.last_updated == other.last_updated and \
               self.machine == other.machine and \
               self.operating_system == other.operating_system

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def discovered(self):
        """
        Indicates whether the host configuration properties were discovered.

        :rtype: ``bool``
        """
        return self._discovered[0]

    @discovered.setter
    def discovered(self, value):
        self._discovered = (value, True)

    @property
    def last_refreshed(self):
        """
        The timestamp when the host was last refreshed.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_refreshed[0]

    @last_refreshed.setter
    def last_refreshed(self, value):
        self._last_refreshed = (value, True)

    @property
    def last_updated(self):
        """
        The timestamp when the host was last updated.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_updated[0]

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = (value, True)

    @property
    def machine(self):
        """
        The host machine information.

        :rtype: :py:class:`v1_5_0.web.vo.HostMachine`
        """
        return self._machine[0]

    @machine.setter
    def machine(self, value):
        self._machine = (value, True)

    @property
    def operating_system(self):
        """
        The host operating system information.

        :rtype: :py:class:`v1_5_0.web.vo.HostOS`
        """
        return self._operating_system[0]

    @operating_system.setter
    def operating_system(self, value):
        self._operating_system = (value, True)

