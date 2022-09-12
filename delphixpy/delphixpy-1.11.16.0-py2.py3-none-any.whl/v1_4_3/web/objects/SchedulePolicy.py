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
#     /delphix-schedule-policy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.Policy import Policy
from delphixpy.v1_4_3 import factory
from delphixpy.v1_4_3 import common

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

class SchedulePolicy(Policy):
    """
    *(extends* :py:class:`v1_4_3.web.vo.Policy` *)* The base type for all
    schedule policies.
    """
    def __init__(self, undef_enabled=True):
        super(SchedulePolicy, self).__init__()
        self._type = ("SchedulePolicy", True)
        self._schedule_list = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SchedulePolicy, cls).from_dict(data, dirty, undef_enabled)
        obj._schedule_list = []
        for item in data.get("scheduleList") or []:
            obj._schedule_list.append(factory.create_object(item))
            factory.validate_type(obj._schedule_list[-1], "Schedule")
        obj._schedule_list = (obj._schedule_list, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SchedulePolicy, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "schedule_list" == "type" or (self.schedule_list is not self.__undef__ and (not (dirty and not self._schedule_list[1]) or isinstance(self.schedule_list, list) or belongs_to_parent)):
            dct["scheduleList"] = dictify(self.schedule_list, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._schedule_list = (self._schedule_list[0], True)

    def is_dirty(self):
        return any([self._schedule_list[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SchedulePolicy):
            return False
        return super(SchedulePolicy, self).__eq__(other) and \
               self.schedule_list == other.schedule_list

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def schedule_list(self):
        """
        List of Schedule objects representing when the policy will execute.

        :rtype: ``list`` of :py:class:`v1_4_3.web.vo.Schedule`
        """
        return self._schedule_list[0]

    @schedule_list.setter
    def schedule_list(self, value):
        self._schedule_list = (value, True)

