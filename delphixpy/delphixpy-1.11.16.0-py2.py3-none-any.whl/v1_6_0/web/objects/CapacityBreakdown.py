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
#     /delphix-capacity-breakdown.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_0 import common

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

class CapacityBreakdown(TypedObject):
    """
    *(extends* :py:class:`v1_6_0.web.vo.TypedObject` *)* Storage stats
    breakdown.
    """
    def __init__(self, undef_enabled=True):
        super(CapacityBreakdown, self).__init__()
        self._type = ("CapacityBreakdown", True)
        self._active_space = (self.__undef__, True)
        self._actual_space = (self.__undef__, True)
        self._descendant_space = (self.__undef__, True)
        self._log_space = (self.__undef__, True)
        self._manual_space = (self.__undef__, True)
        self._policy_space = (self.__undef__, True)
        self._sync_space = (self.__undef__, True)
        self._timeflow_unvirtualized_space = (self.__undef__, True)
        self._unvirtualized_space = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CapacityBreakdown, cls).from_dict(data, dirty, undef_enabled)
        obj._active_space = (data.get("activeSpace", obj.__undef__), dirty)
        if obj._active_space[0] is not None and obj._active_space[0] is not obj.__undef__:
            assert isinstance(obj._active_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._active_space[0], type(obj._active_space[0])))
            common.validate_format(obj._active_space[0], "None", None, None)
        obj._actual_space = (data.get("actualSpace", obj.__undef__), dirty)
        if obj._actual_space[0] is not None and obj._actual_space[0] is not obj.__undef__:
            assert isinstance(obj._actual_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._actual_space[0], type(obj._actual_space[0])))
            common.validate_format(obj._actual_space[0], "None", None, None)
        obj._descendant_space = (data.get("descendantSpace", obj.__undef__), dirty)
        if obj._descendant_space[0] is not None and obj._descendant_space[0] is not obj.__undef__:
            assert isinstance(obj._descendant_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._descendant_space[0], type(obj._descendant_space[0])))
            common.validate_format(obj._descendant_space[0], "None", None, None)
        obj._log_space = (data.get("logSpace", obj.__undef__), dirty)
        if obj._log_space[0] is not None and obj._log_space[0] is not obj.__undef__:
            assert isinstance(obj._log_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._log_space[0], type(obj._log_space[0])))
            common.validate_format(obj._log_space[0], "None", None, None)
        obj._manual_space = (data.get("manualSpace", obj.__undef__), dirty)
        if obj._manual_space[0] is not None and obj._manual_space[0] is not obj.__undef__:
            assert isinstance(obj._manual_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._manual_space[0], type(obj._manual_space[0])))
            common.validate_format(obj._manual_space[0], "None", None, None)
        obj._policy_space = (data.get("policySpace", obj.__undef__), dirty)
        if obj._policy_space[0] is not None and obj._policy_space[0] is not obj.__undef__:
            assert isinstance(obj._policy_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._policy_space[0], type(obj._policy_space[0])))
            common.validate_format(obj._policy_space[0], "None", None, None)
        obj._sync_space = (data.get("syncSpace", obj.__undef__), dirty)
        if obj._sync_space[0] is not None and obj._sync_space[0] is not obj.__undef__:
            assert isinstance(obj._sync_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._sync_space[0], type(obj._sync_space[0])))
            common.validate_format(obj._sync_space[0], "None", None, None)
        obj._timeflow_unvirtualized_space = (data.get("timeflowUnvirtualizedSpace", obj.__undef__), dirty)
        if obj._timeflow_unvirtualized_space[0] is not None and obj._timeflow_unvirtualized_space[0] is not obj.__undef__:
            assert isinstance(obj._timeflow_unvirtualized_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._timeflow_unvirtualized_space[0], type(obj._timeflow_unvirtualized_space[0])))
            common.validate_format(obj._timeflow_unvirtualized_space[0], "None", None, None)
        obj._unvirtualized_space = (data.get("unvirtualizedSpace", obj.__undef__), dirty)
        if obj._unvirtualized_space[0] is not None and obj._unvirtualized_space[0] is not obj.__undef__:
            assert isinstance(obj._unvirtualized_space[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._unvirtualized_space[0], type(obj._unvirtualized_space[0])))
            common.validate_format(obj._unvirtualized_space[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CapacityBreakdown, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "active_space" == "type" or (self.active_space is not self.__undef__ and (not (dirty and not self._active_space[1]))):
            dct["activeSpace"] = dictify(self.active_space)
        if "actual_space" == "type" or (self.actual_space is not self.__undef__ and (not (dirty and not self._actual_space[1]))):
            dct["actualSpace"] = dictify(self.actual_space)
        if "descendant_space" == "type" or (self.descendant_space is not self.__undef__ and (not (dirty and not self._descendant_space[1]))):
            dct["descendantSpace"] = dictify(self.descendant_space)
        if "log_space" == "type" or (self.log_space is not self.__undef__ and (not (dirty and not self._log_space[1]))):
            dct["logSpace"] = dictify(self.log_space)
        if "manual_space" == "type" or (self.manual_space is not self.__undef__ and (not (dirty and not self._manual_space[1]))):
            dct["manualSpace"] = dictify(self.manual_space)
        if "policy_space" == "type" or (self.policy_space is not self.__undef__ and (not (dirty and not self._policy_space[1]))):
            dct["policySpace"] = dictify(self.policy_space)
        if "sync_space" == "type" or (self.sync_space is not self.__undef__ and (not (dirty and not self._sync_space[1]))):
            dct["syncSpace"] = dictify(self.sync_space)
        if "timeflow_unvirtualized_space" == "type" or (self.timeflow_unvirtualized_space is not self.__undef__ and (not (dirty and not self._timeflow_unvirtualized_space[1]))):
            dct["timeflowUnvirtualizedSpace"] = dictify(self.timeflow_unvirtualized_space)
        if "unvirtualized_space" == "type" or (self.unvirtualized_space is not self.__undef__ and (not (dirty and not self._unvirtualized_space[1]))):
            dct["unvirtualizedSpace"] = dictify(self.unvirtualized_space)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._active_space = (self._active_space[0], True)
        self._actual_space = (self._actual_space[0], True)
        self._descendant_space = (self._descendant_space[0], True)
        self._log_space = (self._log_space[0], True)
        self._manual_space = (self._manual_space[0], True)
        self._policy_space = (self._policy_space[0], True)
        self._sync_space = (self._sync_space[0], True)
        self._timeflow_unvirtualized_space = (self._timeflow_unvirtualized_space[0], True)
        self._unvirtualized_space = (self._unvirtualized_space[0], True)

    def is_dirty(self):
        return any([self._active_space[1], self._actual_space[1], self._descendant_space[1], self._log_space[1], self._manual_space[1], self._policy_space[1], self._sync_space[1], self._timeflow_unvirtualized_space[1], self._unvirtualized_space[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CapacityBreakdown):
            return False
        return super(CapacityBreakdown, self).__eq__(other) and \
               self.active_space == other.active_space and \
               self.actual_space == other.actual_space and \
               self.descendant_space == other.descendant_space and \
               self.log_space == other.log_space and \
               self.manual_space == other.manual_space and \
               self.policy_space == other.policy_space and \
               self.sync_space == other.sync_space and \
               self.timeflow_unvirtualized_space == other.timeflow_unvirtualized_space and \
               self.unvirtualized_space == other.unvirtualized_space

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def active_space(self):
        """
        Amount of space used for the active copy of the container.

        :rtype: ``float``
        """
        return self._active_space[0]

    @active_space.setter
    def active_space(self, value):
        self._active_space = (value, True)

    @property
    def actual_space(self):
        """
        Actual space used by the container.

        :rtype: ``float``
        """
        return self._actual_space[0]

    @actual_space.setter
    def actual_space(self, value):
        self._actual_space = (value, True)

    @property
    def descendant_space(self):
        """
        Amount of space used for snapshots from which VDBs have been
        provisioned.

        :rtype: ``float``
        """
        return self._descendant_space[0]

    @descendant_space.setter
    def descendant_space(self, value):
        self._descendant_space = (value, True)

    @property
    def log_space(self):
        """
        Amount of space used by logs.

        :rtype: ``float``
        """
        return self._log_space[0]

    @log_space.setter
    def log_space(self, value):
        self._log_space = (value, True)

    @property
    def manual_space(self):
        """
        Amount of space used for snapshots held by manual retention settings.

        :rtype: ``float``
        """
        return self._manual_space[0]

    @manual_space.setter
    def manual_space(self, value):
        self._manual_space = (value, True)

    @property
    def policy_space(self):
        """
        Amount of space used for snapshots held by policy settings.

        :rtype: ``float``
        """
        return self._policy_space[0]

    @policy_space.setter
    def policy_space(self, value):
        self._policy_space = (value, True)

    @property
    def sync_space(self):
        """
        Amount of space used by snapshots.

        :rtype: ``float``
        """
        return self._sync_space[0]

    @sync_space.setter
    def sync_space(self, value):
        self._sync_space = (value, True)

    @property
    def timeflow_unvirtualized_space(self):
        """
        Unvirtualized space used by the TimeFlow.

        :rtype: ``float``
        """
        return self._timeflow_unvirtualized_space[0]

    @timeflow_unvirtualized_space.setter
    def timeflow_unvirtualized_space(self, value):
        self._timeflow_unvirtualized_space = (value, True)

    @property
    def unvirtualized_space(self):
        """
        Unvirtualized space used by the container.

        :rtype: ``float``
        """
        return self._unvirtualized_space[0]

    @unvirtualized_space.setter
    def unvirtualized_space(self, value):
        self._unvirtualized_space = (value, True)

