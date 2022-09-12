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
#     /delphix-mysql-snapshot.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.TimeflowSnapshot import TimeflowSnapshot
from delphixpy import factory
from delphixpy import common

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

class MySQLSnapshot(TimeflowSnapshot):
    """
    *(extends* :py:class:`delphixpy.web.vo.TimeflowSnapshot` *)* Provisionable
    snapshot of a MySQL TimeFlow.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLSnapshot, self).__init__()
        self._type = ("MySQLSnapshot", True)
        self._internal_version = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._first_change_point = (self.__undef__, True)
        self._latest_change_point = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLSnapshot, cls).from_dict(data, dirty, undef_enabled)
        if "internalVersion" in data and data["internalVersion"] is not None:
            obj._internal_version = (factory.create_object(data["internalVersion"], "MySQLVersion"), dirty)
            factory.validate_type(obj._internal_version[0], "MySQLVersion")
        else:
            obj._internal_version = (obj.__undef__, dirty)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "MySQLSnapshotRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "MySQLSnapshotRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        if "firstChangePoint" in data and data["firstChangePoint"] is not None:
            obj._first_change_point = (factory.create_object(data["firstChangePoint"], "MySQLTimeflowPoint"), dirty)
            factory.validate_type(obj._first_change_point[0], "MySQLTimeflowPoint")
        else:
            obj._first_change_point = (obj.__undef__, dirty)
        if "latestChangePoint" in data and data["latestChangePoint"] is not None:
            obj._latest_change_point = (factory.create_object(data["latestChangePoint"], "MySQLTimeflowPoint"), dirty)
            factory.validate_type(obj._latest_change_point[0], "MySQLTimeflowPoint")
        else:
            obj._latest_change_point = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLSnapshot, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "internal_version" == "type" or (self.internal_version is not self.__undef__ and (not (dirty and not self._internal_version[1]))):
            dct["internalVersion"] = dictify(self.internal_version)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "first_change_point" == "type" or (self.first_change_point is not self.__undef__ and (not (dirty and not self._first_change_point[1]))):
            dct["firstChangePoint"] = dictify(self.first_change_point)
        if "latest_change_point" == "type" or (self.latest_change_point is not self.__undef__ and (not (dirty and not self._latest_change_point[1]))):
            dct["latestChangePoint"] = dictify(self.latest_change_point)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._internal_version = (self._internal_version[0], True)
        self._runtime = (self._runtime[0], True)
        self._first_change_point = (self._first_change_point[0], True)
        self._latest_change_point = (self._latest_change_point[0], True)

    def is_dirty(self):
        return any([self._internal_version[1], self._runtime[1], self._first_change_point[1], self._latest_change_point[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLSnapshot):
            return False
        return super(MySQLSnapshot, self).__eq__(other) and \
               self.internal_version == other.internal_version and \
               self.runtime == other.runtime and \
               self.first_change_point == other.first_change_point and \
               self.latest_change_point == other.latest_change_point

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def internal_version(self):
        """
        Version of the source database at the time the snapshot was taken.

        :rtype: :py:class:`delphixpy.web.vo.MySQLVersion`
        """
        return self._internal_version[0]

    @internal_version.setter
    def internal_version(self, value):
        self._internal_version = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of the snapshot.

        :rtype: :py:class:`delphixpy.web.vo.MySQLSnapshotRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def first_change_point(self):
        """
        The location within the parent TimeFlow at which this snapshot was
        initiated.

        :rtype: :py:class:`delphixpy.web.vo.MySQLTimeflowPoint`
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

        :rtype: :py:class:`delphixpy.web.vo.MySQLTimeflowPoint`
        """
        return self._latest_change_point[0]

    @latest_change_point.setter
    def latest_change_point(self, value):
        self._latest_change_point = (value, True)

