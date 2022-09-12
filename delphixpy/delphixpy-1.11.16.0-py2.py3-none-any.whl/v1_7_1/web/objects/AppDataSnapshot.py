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
#     /delphix-appdata-snapshot.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.TimeflowSnapshot import TimeflowSnapshot
from delphixpy.v1_7_1 import factory
from delphixpy.v1_7_1 import common

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

class AppDataSnapshot(TimeflowSnapshot):
    """
    *(extends* :py:class:`v1_7_1.web.vo.TimeflowSnapshot` *)* Snapshot of an
    AppData TimeFlow.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataSnapshot, self).__init__()
        self._type = ("AppDataSnapshot", True)
        self._first_change_point = (self.__undef__, True)
        self._latest_change_point = (self.__undef__, True)
        self._metadata = (self.__undef__, True)
        self._runtime = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataSnapshot, cls).from_dict(data, dirty, undef_enabled)
        if "firstChangePoint" in data and data["firstChangePoint"] is not None:
            obj._first_change_point = (factory.create_object(data["firstChangePoint"], "AppDataTimeflowPoint"), dirty)
            factory.validate_type(obj._first_change_point[0], "AppDataTimeflowPoint")
        else:
            obj._first_change_point = (obj.__undef__, dirty)
        if "latestChangePoint" in data and data["latestChangePoint"] is not None:
            obj._latest_change_point = (factory.create_object(data["latestChangePoint"], "AppDataTimeflowPoint"), dirty)
            factory.validate_type(obj._latest_change_point[0], "AppDataTimeflowPoint")
        else:
            obj._latest_change_point = (obj.__undef__, dirty)
        if "metadata" in data and data["metadata"] is not None:
            obj._metadata = (data["metadata"], dirty)
        else:
            obj._metadata = (obj.__undef__, dirty)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "AppDataSnapshotRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "AppDataSnapshotRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataSnapshot, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "first_change_point" == "type" or (self.first_change_point is not self.__undef__ and (not (dirty and not self._first_change_point[1]))):
            dct["firstChangePoint"] = dictify(self.first_change_point)
        if "latest_change_point" == "type" or (self.latest_change_point is not self.__undef__ and (not (dirty and not self._latest_change_point[1]))):
            dct["latestChangePoint"] = dictify(self.latest_change_point)
        if "metadata" == "type" or (self.metadata is not self.__undef__ and (not (dirty and not self._metadata[1]))):
            dct["metadata"] = dictify(self.metadata)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._first_change_point = (self._first_change_point[0], True)
        self._latest_change_point = (self._latest_change_point[0], True)
        self._metadata = (self._metadata[0], True)
        self._runtime = (self._runtime[0], True)

    def is_dirty(self):
        return any([self._first_change_point[1], self._latest_change_point[1], self._metadata[1], self._runtime[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataSnapshot):
            return False
        return super(AppDataSnapshot, self).__eq__(other) and \
               self.first_change_point == other.first_change_point and \
               self.latest_change_point == other.latest_change_point and \
               self.metadata == other.metadata and \
               self.runtime == other.runtime

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def first_change_point(self):
        """
        The location within the parent TimeFlow at which this snapshot was
        initiated.

        :rtype: :py:class:`v1_7_1.web.vo.AppDataTimeflowPoint`
        """
        return self._first_change_point[0]

    @first_change_point.setter
    def first_change_point(self, value):
        self._first_change_point = (value, True)

    @property
    def latest_change_point(self):
        """
        The location of the snapshot within the parent TimeFlow represented by
        this snapshot.

        :rtype: :py:class:`v1_7_1.web.vo.AppDataTimeflowPoint`
        """
        return self._latest_change_point[0]

    @latest_change_point.setter
    def latest_change_point(self, value):
        self._latest_change_point = (value, True)

    @property
    def metadata(self):
        """
        The JSON payload conforming to the DraftV4 schema based on the type of
        application data being manipulated.

        :rtype: :py:class:`v1_7_1.web.vo.Json`
        """
        return self._metadata[0]

    @metadata.setter
    def metadata(self, value):
        self._metadata = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of the snapshot.

        :rtype: :py:class:`v1_7_1.web.vo.AppDataSnapshotRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

