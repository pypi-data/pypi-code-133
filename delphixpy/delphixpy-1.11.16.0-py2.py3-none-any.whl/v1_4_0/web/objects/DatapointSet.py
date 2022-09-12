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
#     /delphix-analytics-datapoint-set.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_0 import factory
from delphixpy.v1_4_0 import common

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

class DatapointSet(TypedObject):
    """
    *(extends* :py:class:`v1_4_0.web.vo.TypedObject` *)* A set of datapoints
    from a particular analytics slice.
    """
    def __init__(self, undef_enabled=True):
        super(DatapointSet, self).__init__()
        self._type = ("DatapointSet", True)
        self._collection_events = (self.__undef__, True)
        self._datapoint_streams = (self.__undef__, True)
        self._resolution = (self.__undef__, True)

    API_VERSION = "1.4.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DatapointSet, cls).from_dict(data, dirty, undef_enabled)
        obj._collection_events = []
        for item in data.get("collectionEvents") or []:
            obj._collection_events.append(factory.create_object(item))
            factory.validate_type(obj._collection_events[-1], "StatisticSliceEvent")
        obj._collection_events = (obj._collection_events, dirty)
        obj._datapoint_streams = []
        for item in data.get("datapointStreams") or []:
            obj._datapoint_streams.append(factory.create_object(item))
            factory.validate_type(obj._datapoint_streams[-1], "DatapointStream")
        obj._datapoint_streams = (obj._datapoint_streams, dirty)
        obj._resolution = (data.get("resolution", obj.__undef__), dirty)
        if obj._resolution[0] is not None and obj._resolution[0] is not obj.__undef__:
            assert isinstance(obj._resolution[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._resolution[0], type(obj._resolution[0])))
            common.validate_format(obj._resolution[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DatapointSet, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "collection_events" == "type" or (self.collection_events is not self.__undef__ and (not (dirty and not self._collection_events[1]))):
            dct["collectionEvents"] = dictify(self.collection_events)
        if "datapoint_streams" == "type" or (self.datapoint_streams is not self.__undef__ and (not (dirty and not self._datapoint_streams[1]))):
            dct["datapointStreams"] = dictify(self.datapoint_streams)
        if "resolution" == "type" or (self.resolution is not self.__undef__ and (not (dirty and not self._resolution[1]))):
            dct["resolution"] = dictify(self.resolution)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._collection_events = (self._collection_events[0], True)
        self._datapoint_streams = (self._datapoint_streams[0], True)
        self._resolution = (self._resolution[0], True)

    def is_dirty(self):
        return any([self._collection_events[1], self._datapoint_streams[1], self._resolution[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DatapointSet):
            return False
        return super(DatapointSet, self).__eq__(other) and \
               self.collection_events == other.collection_events and \
               self.datapoint_streams == other.datapoint_streams and \
               self.resolution == other.resolution

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def collection_events(self):
        """
        Events encountered during the requested time window related to this
        slice's status.

        :rtype: ``list`` of :py:class:`v1_4_0.web.vo.StatisticSliceEvent`
        """
        return self._collection_events[0]

    @collection_events.setter
    def collection_events(self, value):
        self._collection_events = (value, True)

    @property
    def datapoint_streams(self):
        """
        The set of datapoint streams in the result.

        :rtype: ``list`` of :py:class:`v1_4_0.web.vo.DatapointStream`
        """
        return self._datapoint_streams[0]

    @datapoint_streams.setter
    def datapoint_streams(self, value):
        self._datapoint_streams = (value, True)

    @property
    def resolution(self):
        """
        The amount of time each datapoint spans.

        :rtype: ``int``
        """
        return self._resolution[0]

    @resolution.setter
    def resolution(self, value):
        self._resolution = (value, True)

