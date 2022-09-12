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
#     /delphix-timeflow-snapshot.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.ReadonlyNamedUserObject import ReadonlyNamedUserObject
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

class TimeflowSnapshot(ReadonlyNamedUserObject):
    """
    *(extends* :py:class:`v1_7_1.web.vo.ReadonlyNamedUserObject` *)* Snapshot
    of a point within a TimeFlow that is used as the basis for provisioning.
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowSnapshot, self).__init__()
        self._type = ("TimeflowSnapshot", True)
        self._consistency = (self.__undef__, True)
        self._container = (self.__undef__, True)
        self._creation_time = (self.__undef__, True)
        self._first_change_point = (self.__undef__, True)
        self._latest_change_point = (self.__undef__, True)
        self._missing_non_logged_data = (self.__undef__, True)
        self._retention = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._temporary = (self.__undef__, True)
        self._timeflow = (self.__undef__, True)
        self._timezone = (self.__undef__, True)
        self._version = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowSnapshot, cls).from_dict(data, dirty, undef_enabled)
        obj._consistency = (data.get("consistency", obj.__undef__), dirty)
        if obj._consistency[0] is not None and obj._consistency[0] is not obj.__undef__:
            assert isinstance(obj._consistency[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._consistency[0], type(obj._consistency[0])))
            common.validate_format(obj._consistency[0], "None", None, None)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._creation_time = (data.get("creationTime", obj.__undef__), dirty)
        if obj._creation_time[0] is not None and obj._creation_time[0] is not obj.__undef__:
            assert isinstance(obj._creation_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._creation_time[0], type(obj._creation_time[0])))
            common.validate_format(obj._creation_time[0], "date", None, None)
        if "firstChangePoint" in data and data["firstChangePoint"] is not None:
            obj._first_change_point = (factory.create_object(data["firstChangePoint"], "TimeflowPoint"), dirty)
            factory.validate_type(obj._first_change_point[0], "TimeflowPoint")
        else:
            obj._first_change_point = (obj.__undef__, dirty)
        if "latestChangePoint" in data and data["latestChangePoint"] is not None:
            obj._latest_change_point = (factory.create_object(data["latestChangePoint"], "TimeflowPoint"), dirty)
            factory.validate_type(obj._latest_change_point[0], "TimeflowPoint")
        else:
            obj._latest_change_point = (obj.__undef__, dirty)
        obj._missing_non_logged_data = (data.get("missingNonLoggedData", obj.__undef__), dirty)
        if obj._missing_non_logged_data[0] is not None and obj._missing_non_logged_data[0] is not obj.__undef__:
            assert isinstance(obj._missing_non_logged_data[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._missing_non_logged_data[0], type(obj._missing_non_logged_data[0])))
            common.validate_format(obj._missing_non_logged_data[0], "None", None, None)
        obj._retention = (data.get("retention", obj.__undef__), dirty)
        if obj._retention[0] is not None and obj._retention[0] is not obj.__undef__:
            assert isinstance(obj._retention[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._retention[0], type(obj._retention[0])))
            common.validate_format(obj._retention[0], "None", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "SnapshotRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "SnapshotRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        obj._temporary = (data.get("temporary", obj.__undef__), dirty)
        if obj._temporary[0] is not None and obj._temporary[0] is not obj.__undef__:
            assert isinstance(obj._temporary[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._temporary[0], type(obj._temporary[0])))
            common.validate_format(obj._temporary[0], "None", None, None)
        obj._timeflow = (data.get("timeflow", obj.__undef__), dirty)
        if obj._timeflow[0] is not None and obj._timeflow[0] is not obj.__undef__:
            assert isinstance(obj._timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timeflow[0], type(obj._timeflow[0])))
            common.validate_format(obj._timeflow[0], "objectReference", None, None)
        obj._timezone = (data.get("timezone", obj.__undef__), dirty)
        if obj._timezone[0] is not None and obj._timezone[0] is not obj.__undef__:
            assert isinstance(obj._timezone[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timezone[0], type(obj._timezone[0])))
            common.validate_format(obj._timezone[0], "None", None, None)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowSnapshot, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "consistency" == "type" or (self.consistency is not self.__undef__ and (not (dirty and not self._consistency[1]))):
            dct["consistency"] = dictify(self.consistency)
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]))):
            dct["container"] = dictify(self.container)
        if "creation_time" == "type" or (self.creation_time is not self.__undef__ and (not (dirty and not self._creation_time[1]))):
            dct["creationTime"] = dictify(self.creation_time)
        if "first_change_point" == "type" or (self.first_change_point is not self.__undef__ and (not (dirty and not self._first_change_point[1]))):
            dct["firstChangePoint"] = dictify(self.first_change_point)
        if "latest_change_point" == "type" or (self.latest_change_point is not self.__undef__ and (not (dirty and not self._latest_change_point[1]))):
            dct["latestChangePoint"] = dictify(self.latest_change_point)
        if "missing_non_logged_data" == "type" or (self.missing_non_logged_data is not self.__undef__ and (not (dirty and not self._missing_non_logged_data[1]))):
            dct["missingNonLoggedData"] = dictify(self.missing_non_logged_data)
        if "retention" == "type" or (self.retention is not self.__undef__ and (not (dirty and not self._retention[1]) or isinstance(self.retention, list) or belongs_to_parent)):
            dct["retention"] = dictify(self.retention)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "temporary" == "type" or (self.temporary is not self.__undef__ and (not (dirty and not self._temporary[1]))):
            dct["temporary"] = dictify(self.temporary)
        if "timeflow" == "type" or (self.timeflow is not self.__undef__ and (not (dirty and not self._timeflow[1]))):
            dct["timeflow"] = dictify(self.timeflow)
        if "timezone" == "type" or (self.timezone is not self.__undef__ and (not (dirty and not self._timezone[1]))):
            dct["timezone"] = dictify(self.timezone)
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]))):
            dct["version"] = dictify(self.version)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._consistency = (self._consistency[0], True)
        self._container = (self._container[0], True)
        self._creation_time = (self._creation_time[0], True)
        self._first_change_point = (self._first_change_point[0], True)
        self._latest_change_point = (self._latest_change_point[0], True)
        self._missing_non_logged_data = (self._missing_non_logged_data[0], True)
        self._retention = (self._retention[0], True)
        self._runtime = (self._runtime[0], True)
        self._temporary = (self._temporary[0], True)
        self._timeflow = (self._timeflow[0], True)
        self._timezone = (self._timezone[0], True)
        self._version = (self._version[0], True)

    def is_dirty(self):
        return any([self._consistency[1], self._container[1], self._creation_time[1], self._first_change_point[1], self._latest_change_point[1], self._missing_non_logged_data[1], self._retention[1], self._runtime[1], self._temporary[1], self._timeflow[1], self._timezone[1], self._version[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowSnapshot):
            return False
        return super(TimeflowSnapshot, self).__eq__(other) and \
               self.consistency == other.consistency and \
               self.container == other.container and \
               self.creation_time == other.creation_time and \
               self.first_change_point == other.first_change_point and \
               self.latest_change_point == other.latest_change_point and \
               self.missing_non_logged_data == other.missing_non_logged_data and \
               self.retention == other.retention and \
               self.runtime == other.runtime and \
               self.temporary == other.temporary and \
               self.timeflow == other.timeflow and \
               self.timezone == other.timezone and \
               self.version == other.version

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def consistency(self):
        """
        A value in the set {CONSISTENT, INCONSISTENT, CRASH_CONSISTENT}
        indicating what type of recovery strategies must be invoked when
        provisioning from this snapshot.

        :rtype: ``TEXT_TYPE``
        """
        return self._consistency[0]

    @consistency.setter
    def consistency(self, value):
        self._consistency = (value, True)

    @property
    def container(self):
        """
        Reference to the database of which this TimeFlow is a part.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def creation_time(self):
        """
        Point in time at which this snapshot was created. This may be different
        from the time corresponding to the TimeFlow.

        :rtype: ``TEXT_TYPE``
        """
        return self._creation_time[0]

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = (value, True)

    @property
    def first_change_point(self):
        """
        The location within the parent TimeFlow at which this snapshot was
        initiated. No recovery earlier than this point needs to be applied in
        order to provision a database from this snapshot. If "firstChangePoint"
        equals "latestChangePoint", then no recovery needs to be applied in
        order to provision a database.

        :rtype: :py:class:`v1_7_1.web.vo.TimeflowPoint`
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

        :rtype: :py:class:`v1_7_1.web.vo.TimeflowPoint`
        """
        return self._latest_change_point[0]

    @latest_change_point.setter
    def latest_change_point(self, value):
        self._latest_change_point = (value, True)

    @property
    def missing_non_logged_data(self):
        """
        Boolean value indicating if a virtual database provisioned from this
        snapshot will be missing nologging changes.

        :rtype: ``bool``
        """
        return self._missing_non_logged_data[0]

    @missing_non_logged_data.setter
    def missing_non_logged_data(self, value):
        self._missing_non_logged_data = (value, True)

    @property
    def retention(self):
        """
        Retention policy, in days. A value of -1 indicates the snapshot should
        be kept forever.

        :rtype: ``int``
        """
        return self._retention[0]

    @retention.setter
    def retention(self, value):
        self._retention = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of the snapshot.

        :rtype: :py:class:`v1_7_1.web.vo.SnapshotRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def temporary(self):
        """
        Boolean value indicating that this snapshot is in a transient state and
        should not be user visible.

        :rtype: ``bool``
        """
        return self._temporary[0]

    @temporary.setter
    def temporary(self, value):
        self._temporary = (value, True)

    @property
    def timeflow(self):
        """
        TimeFlow of which this snapshot is a part.

        :rtype: ``TEXT_TYPE``
        """
        return self._timeflow[0]

    @timeflow.setter
    def timeflow(self, value):
        self._timeflow = (value, True)

    @property
    def timezone(self):
        """
        Time zone of the source database at the time the snapshot was taken.

        :rtype: ``TEXT_TYPE``
        """
        return self._timezone[0]

    @timezone.setter
    def timezone(self, value):
        self._timezone = (value, True)

    @property
    def version(self):
        """
        Version of database source repository at the time the snapshot was
        taken.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

