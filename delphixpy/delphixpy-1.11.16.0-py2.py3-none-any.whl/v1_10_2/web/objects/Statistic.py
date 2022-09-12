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
#     /delphix-analytics-statistic.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_2 import factory
from delphixpy.v1_10_2 import common

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

class Statistic(TypedObject):
    """
    *(extends* :py:class:`v1_10_2.web.vo.TypedObject` *)* Multidimensional
    analytics statistics which can be queried for data.
    """
    def __init__(self, undef_enabled=True):
        super(Statistic, self).__init__()
        self._type = ("Statistic", True)
        self._statistic_type = (self.__undef__, True)
        self._explanation = (self.__undef__, True)
        self._min_collection_interval = (self.__undef__, True)
        self._axes = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Statistic, cls).from_dict(data, dirty, undef_enabled)
        obj._statistic_type = (data.get("statisticType", obj.__undef__), dirty)
        if obj._statistic_type[0] is not None and obj._statistic_type[0] is not obj.__undef__:
            assert isinstance(obj._statistic_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._statistic_type[0], type(obj._statistic_type[0])))
            common.validate_format(obj._statistic_type[0], "None", None, None)
        obj._explanation = (data.get("explanation", obj.__undef__), dirty)
        if obj._explanation[0] is not None and obj._explanation[0] is not obj.__undef__:
            assert isinstance(obj._explanation[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._explanation[0], type(obj._explanation[0])))
            common.validate_format(obj._explanation[0], "None", None, None)
        obj._min_collection_interval = (data.get("minCollectionInterval", obj.__undef__), dirty)
        if obj._min_collection_interval[0] is not None and obj._min_collection_interval[0] is not obj.__undef__:
            assert isinstance(obj._min_collection_interval[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._min_collection_interval[0], type(obj._min_collection_interval[0])))
            common.validate_format(obj._min_collection_interval[0], "None", None, None)
        obj._axes = []
        for item in data.get("axes") or []:
            obj._axes.append(factory.create_object(item))
            factory.validate_type(obj._axes[-1], "StatisticAxis")
        obj._axes = (obj._axes, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Statistic, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "statistic_type" == "type" or (self.statistic_type is not self.__undef__ and (not (dirty and not self._statistic_type[1]))):
            dct["statisticType"] = dictify(self.statistic_type)
        if "explanation" == "type" or (self.explanation is not self.__undef__ and (not (dirty and not self._explanation[1]))):
            dct["explanation"] = dictify(self.explanation)
        if "min_collection_interval" == "type" or (self.min_collection_interval is not self.__undef__ and (not (dirty and not self._min_collection_interval[1]))):
            dct["minCollectionInterval"] = dictify(self.min_collection_interval)
        if "axes" == "type" or (self.axes is not self.__undef__ and (not (dirty and not self._axes[1]))):
            dct["axes"] = dictify(self.axes)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._statistic_type = (self._statistic_type[0], True)
        self._explanation = (self._explanation[0], True)
        self._min_collection_interval = (self._min_collection_interval[0], True)
        self._axes = (self._axes[0], True)

    def is_dirty(self):
        return any([self._statistic_type[1], self._explanation[1], self._min_collection_interval[1], self._axes[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Statistic):
            return False
        return super(Statistic, self).__eq__(other) and \
               self.statistic_type == other.statistic_type and \
               self.explanation == other.explanation and \
               self.min_collection_interval == other.min_collection_interval and \
               self.axes == other.axes

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def statistic_type(self):
        """
        The type name for the data this can collect.

        :rtype: ``TEXT_TYPE``
        """
        return self._statistic_type[0]

    @statistic_type.setter
    def statistic_type(self, value):
        self._statistic_type = (value, True)

    @property
    def explanation(self):
        """
        A deeper explanation of the data this can collect.

        :rtype: ``TEXT_TYPE``
        """
        return self._explanation[0]

    @explanation.setter
    def explanation(self, value):
        self._explanation = (value, True)

    @property
    def min_collection_interval(self):
        """
        The smallest unit of time this statistic can measure on.

        :rtype: ``int``
        """
        return self._min_collection_interval[0]

    @min_collection_interval.setter
    def min_collection_interval(self, value):
        self._min_collection_interval = (value, True)

    @property
    def axes(self):
        """
        The set of axes this statistic has.

        :rtype: ``list`` of :py:class:`v1_10_2.web.vo.StatisticAxis`
        """
        return self._axes[0]

    @axes.setter
    def axes(self, value):
        self._axes = (value, True)

