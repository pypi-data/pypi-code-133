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
#     /delphix-timeflow-range-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_1 import factory
from delphixpy.v1_9_1 import common

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

class TimeflowRangeParameters(TypedObject):
    """
    *(extends* :py:class:`v1_9_1.web.vo.TypedObject` *)* The parameters to use
    as input to fetch TimeFlow ranges.
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowRangeParameters, self).__init__()
        self._type = ("TimeflowRangeParameters", True)
        self._start_point = (self.__undef__, True)
        self._end_point = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowRangeParameters, cls).from_dict(data, dirty, undef_enabled)
        if "startPoint" in data and data["startPoint"] is not None:
            obj._start_point = (factory.create_object(data["startPoint"], "TimeflowPoint"), dirty)
            factory.validate_type(obj._start_point[0], "TimeflowPoint")
        else:
            obj._start_point = (obj.__undef__, dirty)
        if "endPoint" in data and data["endPoint"] is not None:
            obj._end_point = (factory.create_object(data["endPoint"], "TimeflowPoint"), dirty)
            factory.validate_type(obj._end_point[0], "TimeflowPoint")
        else:
            obj._end_point = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowRangeParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "start_point" == "type" or (self.start_point is not self.__undef__ and (not (dirty and not self._start_point[1]))):
            dct["startPoint"] = dictify(self.start_point)
        if "end_point" == "type" or (self.end_point is not self.__undef__ and (not (dirty and not self._end_point[1]))):
            dct["endPoint"] = dictify(self.end_point)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._start_point = (self._start_point[0], True)
        self._end_point = (self._end_point[0], True)

    def is_dirty(self):
        return any([self._start_point[1], self._end_point[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowRangeParameters):
            return False
        return super(TimeflowRangeParameters, self).__eq__(other) and \
               self.start_point == other.start_point and \
               self.end_point == other.end_point

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def start_point(self):
        """
        The starting TimeFlow point of the time period to search for TimeFlow
        ranges.

        :rtype: :py:class:`v1_9_1.web.vo.TimeflowPoint`
        """
        return self._start_point[0]

    @start_point.setter
    def start_point(self, value):
        self._start_point = (value, True)

    @property
    def end_point(self):
        """
        The ending TimeFlow point of the time period to search for TimeFlow
        ranges.

        :rtype: :py:class:`v1_9_1.web.vo.TimeflowPoint`
        """
        return self._end_point[0]

    @end_point.setter
    def end_point(self, value):
        self._end_point = (value, True)

