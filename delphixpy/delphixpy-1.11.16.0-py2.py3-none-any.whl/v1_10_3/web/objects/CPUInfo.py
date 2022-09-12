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
#     /delphix-cpu-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_3 import common

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

class CPUInfo(TypedObject):
    """
    *(extends* :py:class:`v1_10_3.web.vo.TypedObject` *)* Describes a processor
    available to the system.
    """
    def __init__(self, undef_enabled=True):
        super(CPUInfo, self).__init__()
        self._type = ("CPUInfo", True)
        self._speed = (self.__undef__, True)
        self._cores = (self.__undef__, True)

    API_VERSION = "1.10.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CPUInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._speed = (data.get("speed", obj.__undef__), dirty)
        if obj._speed[0] is not None and obj._speed[0] is not obj.__undef__:
            assert isinstance(obj._speed[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._speed[0], type(obj._speed[0])))
            common.validate_format(obj._speed[0], "None", None, None)
        obj._cores = (data.get("cores", obj.__undef__), dirty)
        if obj._cores[0] is not None and obj._cores[0] is not obj.__undef__:
            assert isinstance(obj._cores[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._cores[0], type(obj._cores[0])))
            common.validate_format(obj._cores[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CPUInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "speed" == "type" or (self.speed is not self.__undef__ and (not (dirty and not self._speed[1]))):
            dct["speed"] = dictify(self.speed)
        if "cores" == "type" or (self.cores is not self.__undef__ and (not (dirty and not self._cores[1]))):
            dct["cores"] = dictify(self.cores)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._speed = (self._speed[0], True)
        self._cores = (self._cores[0], True)

    def is_dirty(self):
        return any([self._speed[1], self._cores[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CPUInfo):
            return False
        return super(CPUInfo, self).__eq__(other) and \
               self.speed == other.speed and \
               self.cores == other.cores

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def speed(self):
        """
        Speed of the processor, in hertz.

        :rtype: ``float``
        """
        return self._speed[0]

    @speed.setter
    def speed(self, value):
        self._speed = (value, True)

    @property
    def cores(self):
        """
        Number of cores in the processor.

        :rtype: ``int``
        """
        return self._cores[0]

    @cores.setter
    def cores(self, value):
        self._cores = (value, True)

