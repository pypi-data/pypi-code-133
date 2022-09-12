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
#     /delphix-replication-source-state.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_3.web.objects.UserObject import UserObject
from delphixpy.v1_9_3 import common

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

class ReplicationSourceState(UserObject):
    """
    *(extends* :py:class:`v1_9_3.web.vo.UserObject` *)* State of a replication
    spec.
    """
    def __init__(self, undef_enabled=True):
        super(ReplicationSourceState, self).__init__()
        self._type = ("ReplicationSourceState", True)
        self._last_point = (self.__undef__, True)
        self._active_point = (self.__undef__, True)
        self._spec = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ReplicationSourceState, cls).from_dict(data, dirty, undef_enabled)
        obj._last_point = (data.get("lastPoint", obj.__undef__), dirty)
        if obj._last_point[0] is not None and obj._last_point[0] is not obj.__undef__:
            assert isinstance(obj._last_point[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_point[0], type(obj._last_point[0])))
            common.validate_format(obj._last_point[0], "objectReference", None, None)
        obj._active_point = (data.get("activePoint", obj.__undef__), dirty)
        if obj._active_point[0] is not None and obj._active_point[0] is not obj.__undef__:
            assert isinstance(obj._active_point[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._active_point[0], type(obj._active_point[0])))
            common.validate_format(obj._active_point[0], "objectReference", None, None)
        obj._spec = (data.get("spec", obj.__undef__), dirty)
        if obj._spec[0] is not None and obj._spec[0] is not obj.__undef__:
            assert isinstance(obj._spec[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._spec[0], type(obj._spec[0])))
            common.validate_format(obj._spec[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ReplicationSourceState, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "last_point" == "type" or (self.last_point is not self.__undef__ and (not (dirty and not self._last_point[1]))):
            dct["lastPoint"] = dictify(self.last_point)
        if "active_point" == "type" or (self.active_point is not self.__undef__ and (not (dirty and not self._active_point[1]))):
            dct["activePoint"] = dictify(self.active_point)
        if "spec" == "type" or (self.spec is not self.__undef__ and (not (dirty and not self._spec[1]))):
            dct["spec"] = dictify(self.spec)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._last_point = (self._last_point[0], True)
        self._active_point = (self._active_point[0], True)
        self._spec = (self._spec[0], True)

    def is_dirty(self):
        return any([self._last_point[1], self._active_point[1], self._spec[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ReplicationSourceState):
            return False
        return super(ReplicationSourceState, self).__eq__(other) and \
               self.last_point == other.last_point and \
               self.active_point == other.active_point and \
               self.spec == other.spec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def last_point(self):
        """
        The last serialization point sent. This can be null prior to the first
        replication run.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_point[0]

    @last_point.setter
    def last_point(self, value):
        self._last_point = (value, True)

    @property
    def active_point(self):
        """
        The active serialization point, currently being sent or about to be
        sent to replication targets.

        :rtype: ``TEXT_TYPE``
        """
        return self._active_point[0]

    @active_point.setter
    def active_point(self, value):
        self._active_point = (value, True)

    @property
    def spec(self):
        """
        A reference to the replication specification responsible for the
        current state.

        :rtype: ``TEXT_TYPE``
        """
        return self._spec[0]

    @spec.setter
    def spec(self, value):
        self._spec = (value, True)

