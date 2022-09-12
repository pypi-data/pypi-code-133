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
#     /delphix-analytics-cpu-util-datapoint-stream.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_1.web.objects.DatapointStream import DatapointStream
from delphixpy.v1_11_1 import common

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

class CpuUtilDatapointStream(DatapointStream):
    """
    *(extends* :py:class:`v1_11_1.web.vo.DatapointStream` *)* A stream of
    datapoints from a CPU_UTIL analytics slice.
    """
    def __init__(self, undef_enabled=True):
        super(CpuUtilDatapointStream, self).__init__()
        self._type = ("CpuUtilDatapointStream", True)
        self._cpu = (self.__undef__, True)

    API_VERSION = "1.11.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CpuUtilDatapointStream, cls).from_dict(data, dirty, undef_enabled)
        obj._cpu = (data.get("cpu", obj.__undef__), dirty)
        if obj._cpu[0] is not None and obj._cpu[0] is not obj.__undef__:
            assert isinstance(obj._cpu[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._cpu[0], type(obj._cpu[0])))
            common.validate_format(obj._cpu[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CpuUtilDatapointStream, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cpu" == "type" or (self.cpu is not self.__undef__ and (not (dirty and not self._cpu[1]))):
            dct["cpu"] = dictify(self.cpu)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cpu = (self._cpu[0], True)

    def is_dirty(self):
        return any([self._cpu[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CpuUtilDatapointStream):
            return False
        return super(CpuUtilDatapointStream, self).__eq__(other) and \
               self.cpu == other.cpu

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cpu(self):
        """
        Which CPU was utilized.

        :rtype: ``int``
        """
        return self._cpu[0]

    @cpu.setter
    def cpu(self, value):
        self._cpu = (value, True)

