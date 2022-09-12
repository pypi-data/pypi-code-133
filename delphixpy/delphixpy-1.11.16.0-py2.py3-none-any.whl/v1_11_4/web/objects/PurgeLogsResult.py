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
#     /delphix-purge-logs-result.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_4.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_4 import factory
from delphixpy.v1_11_4 import common

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

class PurgeLogsResult(TypedObject):
    """
    *(extends* :py:class:`v1_11_4.web.vo.TypedObject` *)* Represents the result
    of a purgeLogs operation.
    """
    def __init__(self, undef_enabled=True):
        super(PurgeLogsResult, self).__init__()
        self._type = ("PurgeLogsResult", True)
        self._affected_snapshots = (self.__undef__, True)
        self._truncate_point = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PurgeLogsResult, cls).from_dict(data, dirty, undef_enabled)
        obj._affected_snapshots = []
        for item in data.get("affectedSnapshots") or []:
            obj._affected_snapshots.append(factory.create_object(item))
            factory.validate_type(obj._affected_snapshots[-1], "TimeflowSnapshot")
        obj._affected_snapshots = (obj._affected_snapshots, dirty)
        if "truncatePoint" in data and data["truncatePoint"] is not None:
            obj._truncate_point = (factory.create_object(data["truncatePoint"], "OracleTimeflowPoint"), dirty)
            factory.validate_type(obj._truncate_point[0], "OracleTimeflowPoint")
        else:
            obj._truncate_point = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PurgeLogsResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "affected_snapshots" == "type" or (self.affected_snapshots is not self.__undef__ and (not (dirty and not self._affected_snapshots[1]))):
            dct["affectedSnapshots"] = dictify(self.affected_snapshots)
        if "truncate_point" == "type" or (self.truncate_point is not self.__undef__ and (not (dirty and not self._truncate_point[1]))):
            dct["truncatePoint"] = dictify(self.truncate_point)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._affected_snapshots = (self._affected_snapshots[0], True)
        self._truncate_point = (self._truncate_point[0], True)

    def is_dirty(self):
        return any([self._affected_snapshots[1], self._truncate_point[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PurgeLogsResult):
            return False
        return super(PurgeLogsResult, self).__eq__(other) and \
               self.affected_snapshots == other.affected_snapshots and \
               self.truncate_point == other.truncate_point

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def affected_snapshots(self):
        """
        List of snapshots which have been rendered unprovisionable because logs
        needed to make them consistent have been deleted.

        :rtype: ``list`` of :py:class:`v1_11_4.web.vo.TimeflowSnapshot`
        """
        return self._affected_snapshots[0]

    @affected_snapshots.setter
    def affected_snapshots(self, value):
        self._affected_snapshots = (value, True)

    @property
    def truncate_point(self):
        """
        TimeFlow point after the last snapshot beyond which TimeFlow will be
        lost as a result of purging logs.

        :rtype: :py:class:`v1_11_4.web.vo.OracleTimeflowPoint`
        """
        return self._truncate_point[0]

    @truncate_point.setter
    def truncate_point(self, value):
        self._truncate_point = (value, True)

