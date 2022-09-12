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
#     /delphix-snapshot-policy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.SchedulePolicy import SchedulePolicy
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

class SnapshotPolicy(SchedulePolicy):
    """
    *(extends* :py:class:`v1_10_2.web.vo.SchedulePolicy` *)* This policy
    creates snapshots of a container with externally managed sources (virtual
    databases) according to a schedule.
    """
    def __init__(self, undef_enabled=True):
        super(SnapshotPolicy, self).__init__()
        self._type = ("SnapshotPolicy", True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SnapshotPolicy, cls).from_dict(data, dirty, undef_enabled)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SnapshotPolicy, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        pass

    def is_dirty(self):
        return False

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SnapshotPolicy):
            return False
        return super(SnapshotPolicy, self).__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

