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
#     /delphix-capacity-aggregate-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_1 import factory
from delphixpy.v1_6_1 import common

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

class AggregateCapacityData(TypedObject):
    """
    *(extends* :py:class:`v1_6_1.web.vo.TypedObject` *)* Capacity data for an
    aggregation of containers.
    """
    def __init__(self, undef_enabled=True):
        super(AggregateCapacityData, self).__init__()
        self._type = ("AggregateCapacityData", True)
        self._source = (self.__undef__, True)
        self._timestamp = (self.__undef__, True)
        self._virtual = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AggregateCapacityData, cls).from_dict(data, dirty, undef_enabled)
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "CapacityBreakdown"), dirty)
            factory.validate_type(obj._source[0], "CapacityBreakdown")
        else:
            obj._source = (obj.__undef__, dirty)
        obj._timestamp = (data.get("timestamp", obj.__undef__), dirty)
        if obj._timestamp[0] is not None and obj._timestamp[0] is not obj.__undef__:
            assert isinstance(obj._timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timestamp[0], type(obj._timestamp[0])))
            common.validate_format(obj._timestamp[0], "date", None, None)
        if "virtual" in data and data["virtual"] is not None:
            obj._virtual = (factory.create_object(data["virtual"], "CapacityBreakdown"), dirty)
            factory.validate_type(obj._virtual[0], "CapacityBreakdown")
        else:
            obj._virtual = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AggregateCapacityData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]))):
            dct["source"] = dictify(self.source)
        if "timestamp" == "type" or (self.timestamp is not self.__undef__ and (not (dirty and not self._timestamp[1]))):
            dct["timestamp"] = dictify(self.timestamp)
        if "virtual" == "type" or (self.virtual is not self.__undef__ and (not (dirty and not self._virtual[1]))):
            dct["virtual"] = dictify(self.virtual)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source = (self._source[0], True)
        self._timestamp = (self._timestamp[0], True)
        self._virtual = (self._virtual[0], True)

    def is_dirty(self):
        return any([self._source[1], self._timestamp[1], self._virtual[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AggregateCapacityData):
            return False
        return super(AggregateCapacityData, self).__eq__(other) and \
               self.source == other.source and \
               self.timestamp == other.timestamp and \
               self.virtual == other.virtual

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source(self):
        """
        Statistics for dSources in this aggregation.

        :rtype: :py:class:`v1_6_1.web.vo.CapacityBreakdown`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def timestamp(self):
        """
        Time at which this information was sampled.

        :rtype: ``TEXT_TYPE``
        """
        return self._timestamp[0]

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = (value, True)

    @property
    def virtual(self):
        """
        Statistics for VDBs in this aggregation.

        :rtype: :py:class:`v1_6_1.web.vo.CapacityBreakdown`
        """
        return self._virtual[0]

    @virtual.setter
    def virtual(self, value):
        self._virtual = (value, True)

