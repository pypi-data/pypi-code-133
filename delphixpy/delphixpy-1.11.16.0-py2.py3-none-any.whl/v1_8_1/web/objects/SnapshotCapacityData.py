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
#     /delphix-capacity-snapshot-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_8_1 import common

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

class SnapshotCapacityData(TypedObject):
    """
    *(extends* :py:class:`v1_8_1.web.vo.TypedObject` *)* Capacity metrics for a
    single snapshot.
    """
    def __init__(self, undef_enabled=True):
        super(SnapshotCapacityData, self).__init__()
        self._type = ("SnapshotCapacityData", True)
        self._descendant_vd_bs = (self.__undef__, True)
        self._manual_retention = (self.__undef__, True)
        self._policy_retention = (self.__undef__, True)
        self._snapshot = (self.__undef__, True)
        self._snapshot_timestamp = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SnapshotCapacityData, cls).from_dict(data, dirty, undef_enabled)
        obj._descendant_vd_bs = []
        for item in data.get("descendantVDBs") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._descendant_vd_bs.append(item)
        obj._descendant_vd_bs = (obj._descendant_vd_bs, dirty)
        obj._manual_retention = (data.get("manualRetention", obj.__undef__), dirty)
        if obj._manual_retention[0] is not None and obj._manual_retention[0] is not obj.__undef__:
            assert isinstance(obj._manual_retention[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._manual_retention[0], type(obj._manual_retention[0])))
            common.validate_format(obj._manual_retention[0], "None", None, None)
        obj._policy_retention = (data.get("policyRetention", obj.__undef__), dirty)
        if obj._policy_retention[0] is not None and obj._policy_retention[0] is not obj.__undef__:
            assert isinstance(obj._policy_retention[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._policy_retention[0], type(obj._policy_retention[0])))
            common.validate_format(obj._policy_retention[0], "None", None, None)
        obj._snapshot = (data.get("snapshot", obj.__undef__), dirty)
        if obj._snapshot[0] is not None and obj._snapshot[0] is not obj.__undef__:
            assert isinstance(obj._snapshot[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._snapshot[0], type(obj._snapshot[0])))
            common.validate_format(obj._snapshot[0], "objectReference", None, None)
        obj._snapshot_timestamp = (data.get("snapshotTimestamp", obj.__undef__), dirty)
        if obj._snapshot_timestamp[0] is not None and obj._snapshot_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._snapshot_timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._snapshot_timestamp[0], type(obj._snapshot_timestamp[0])))
            common.validate_format(obj._snapshot_timestamp[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SnapshotCapacityData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "descendant_vd_bs" == "type" or (self.descendant_vd_bs is not self.__undef__ and (not (dirty and not self._descendant_vd_bs[1]))):
            dct["descendantVDBs"] = dictify(self.descendant_vd_bs)
        if "manual_retention" == "type" or (self.manual_retention is not self.__undef__ and (not (dirty and not self._manual_retention[1]))):
            dct["manualRetention"] = dictify(self.manual_retention)
        if "policy_retention" == "type" or (self.policy_retention is not self.__undef__ and (not (dirty and not self._policy_retention[1]))):
            dct["policyRetention"] = dictify(self.policy_retention)
        if "snapshot" == "type" or (self.snapshot is not self.__undef__ and (not (dirty and not self._snapshot[1]))):
            dct["snapshot"] = dictify(self.snapshot)
        if "snapshot_timestamp" == "type" or (self.snapshot_timestamp is not self.__undef__ and (not (dirty and not self._snapshot_timestamp[1]))):
            dct["snapshotTimestamp"] = dictify(self.snapshot_timestamp)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._descendant_vd_bs = (self._descendant_vd_bs[0], True)
        self._manual_retention = (self._manual_retention[0], True)
        self._policy_retention = (self._policy_retention[0], True)
        self._snapshot = (self._snapshot[0], True)
        self._snapshot_timestamp = (self._snapshot_timestamp[0], True)

    def is_dirty(self):
        return any([self._descendant_vd_bs[1], self._manual_retention[1], self._policy_retention[1], self._snapshot[1], self._snapshot_timestamp[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SnapshotCapacityData):
            return False
        return super(SnapshotCapacityData, self).__eq__(other) and \
               self.descendant_vd_bs == other.descendant_vd_bs and \
               self.manual_retention == other.manual_retention and \
               self.policy_retention == other.policy_retention and \
               self.snapshot == other.snapshot and \
               self.snapshot_timestamp == other.snapshot_timestamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def descendant_vd_bs(self):
        """
        List of VDBs that have been provisioned from this snapshot.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._descendant_vd_bs[0]

    @descendant_vd_bs.setter
    def descendant_vd_bs(self, value):
        self._descendant_vd_bs = (value, True)

    @property
    def manual_retention(self):
        """
        The manual retention setting on this snapshot, in days.

        :rtype: ``int``
        """
        return self._manual_retention[0]

    @manual_retention.setter
    def manual_retention(self, value):
        self._manual_retention = (value, True)

    @property
    def policy_retention(self):
        """
        Whether this snapshot is currently being retained due to policy
        settings.

        :rtype: ``bool``
        """
        return self._policy_retention[0]

    @policy_retention.setter
    def policy_retention(self, value):
        self._policy_retention = (value, True)

    @property
    def snapshot(self):
        """
        Reference to the snapshot.

        :rtype: ``TEXT_TYPE``
        """
        return self._snapshot[0]

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = (value, True)

    @property
    def snapshot_timestamp(self):
        """
        Time at which this snapshot was taken.

        :rtype: ``TEXT_TYPE``
        """
        return self._snapshot_timestamp[0]

    @snapshot_timestamp.setter
    def snapshot_timestamp(self, value):
        self._snapshot_timestamp = (value, True)

