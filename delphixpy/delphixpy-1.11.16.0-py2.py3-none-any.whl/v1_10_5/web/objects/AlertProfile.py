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
#     /delphix-alert-profile.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_10_5 import factory
from delphixpy.v1_10_5 import common

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

class AlertProfile(PersistentObject):
    """
    *(extends* :py:class:`v1_10_5.web.vo.PersistentObject` *)* A profile that
    describes a set of actions to take in response to an alert being generated.
    """
    def __init__(self, undef_enabled=True):
        super(AlertProfile, self).__init__()
        self._type = ("AlertProfile", True)
        self._filter_spec = (self.__undef__, True)
        self._actions = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AlertProfile, cls).from_dict(data, dirty, undef_enabled)
        if "filterSpec" in data and data["filterSpec"] is not None:
            obj._filter_spec = (factory.create_object(data["filterSpec"], "AlertFilter"), dirty)
            factory.validate_type(obj._filter_spec[0], "AlertFilter")
        else:
            obj._filter_spec = (obj.__undef__, dirty)
        obj._actions = []
        for item in data.get("actions") or []:
            obj._actions.append(factory.create_object(item))
            factory.validate_type(obj._actions[-1], "AlertAction")
        obj._actions = (obj._actions, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AlertProfile, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "filter_spec" == "type" or (self.filter_spec is not self.__undef__ and (not (dirty and not self._filter_spec[1]) or isinstance(self.filter_spec, list) or belongs_to_parent)):
            dct["filterSpec"] = dictify(self.filter_spec, prop_is_list_or_vo=True)
        if "actions" == "type" or (self.actions is not self.__undef__ and (not (dirty and not self._actions[1]) or isinstance(self.actions, list) or belongs_to_parent)):
            dct["actions"] = dictify(self.actions, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._filter_spec = (self._filter_spec[0], True)
        self._actions = (self._actions[0], True)

    def is_dirty(self):
        return any([self._filter_spec[1], self._actions[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AlertProfile):
            return False
        return super(AlertProfile, self).__eq__(other) and \
               self.filter_spec == other.filter_spec and \
               self.actions == other.actions

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def filter_spec(self):
        """
        Specifies which alerts should be matched by this profile.

        :rtype: :py:class:`v1_10_5.web.vo.AlertFilter`
        """
        return self._filter_spec[0]

    @filter_spec.setter
    def filter_spec(self, value):
        self._filter_spec = (value, True)

    @property
    def actions(self):
        """
        List of actions to take. Only alerts visible to the user and matching
        the optional filters are included. If there are multiple actions with
        the same result (such as emailing a user), only one result is acted
        upon.

        :rtype: ``list`` of :py:class:`v1_10_5.web.vo.AlertAction`
        """
        return self._actions[0]

    @actions.setter
    def actions(self, value):
        self._actions = (value, True)

