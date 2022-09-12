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
#     /delphix-replication-spec-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_7 import common

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

class ReplicationSpecRuntime(TypedObject):
    """
    *(extends* :py:class:`v1_11_7.web.vo.TypedObject` *)* Runtime properties
    for a replication spec.
    """
    def __init__(self, undef_enabled=True):
        super(ReplicationSpecRuntime, self).__init__()
        self._type = ("ReplicationSpecRuntime", True)
        self._next_scheduled_execution = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ReplicationSpecRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._next_scheduled_execution = (data.get("nextScheduledExecution", obj.__undef__), dirty)
        if obj._next_scheduled_execution[0] is not None and obj._next_scheduled_execution[0] is not obj.__undef__:
            assert isinstance(obj._next_scheduled_execution[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._next_scheduled_execution[0], type(obj._next_scheduled_execution[0])))
            common.validate_format(obj._next_scheduled_execution[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ReplicationSpecRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "next_scheduled_execution" == "type" or (self.next_scheduled_execution is not self.__undef__ and (not (dirty and not self._next_scheduled_execution[1]))):
            dct["nextScheduledExecution"] = dictify(self.next_scheduled_execution)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._next_scheduled_execution = (self._next_scheduled_execution[0], True)

    def is_dirty(self):
        return any([self._next_scheduled_execution[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ReplicationSpecRuntime):
            return False
        return super(ReplicationSpecRuntime, self).__eq__(other) and \
               self.next_scheduled_execution == other.next_scheduled_execution

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def next_scheduled_execution(self):
        """
        Date of the next execution of this replication spec according to the
        schedule.

        :rtype: ``TEXT_TYPE``
        """
        return self._next_scheduled_execution[0]

    @next_scheduled_execution.setter
    def next_scheduled_execution(self, value):
        self._next_scheduled_execution = (value, True)

