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

from delphixpy.v1_7_0.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_7_0 import factory
from delphixpy.v1_7_0 import common

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
    *(extends* :py:class:`v1_7_0.web.vo.PersistentObject` *)* A profile that
    describes a set of actions to take in response to an alert being generated.
    """
    def __init__(self, undef_enabled=True):
        super(AlertProfile, self).__init__()
        self._type = ("AlertProfile", True)
        self._actions = (self.__undef__, True)
        self._event_filter = (self.__undef__, True)
        self._severity_filter = (self.__undef__, True)
        self._target_filter = (self.__undef__, True)

    API_VERSION = "1.7.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AlertProfile, cls).from_dict(data, dirty, undef_enabled)
        obj._actions = []
        for item in data.get("actions") or []:
            obj._actions.append(factory.create_object(item))
            factory.validate_type(obj._actions[-1], "AlertAction")
        obj._actions = (obj._actions, dirty)
        obj._event_filter = []
        for item in data.get("eventFilter") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._event_filter.append(item)
        obj._event_filter = (obj._event_filter, dirty)
        obj._severity_filter = []
        for item in data.get("severityFilter") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            assert item in ['INFORMATIONAL', 'WARNING', 'CRITICAL', 'AUDIT'], "Expected enum ['INFORMATIONAL', 'WARNING', 'CRITICAL', 'AUDIT'] but got %s" % item
            common.validate_format(item, "None", None, None)
            obj._severity_filter.append(item)
        obj._severity_filter = (obj._severity_filter, dirty)
        obj._target_filter = []
        for item in data.get("targetFilter") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._target_filter.append(item)
        obj._target_filter = (obj._target_filter, dirty)
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
        if "actions" == "type" or (self.actions is not self.__undef__ and (not (dirty and not self._actions[1]) or isinstance(self.actions, list) or belongs_to_parent)):
            dct["actions"] = dictify(self.actions, prop_is_list_or_vo=True)
        if "event_filter" == "type" or (self.event_filter is not self.__undef__ and (not (dirty and not self._event_filter[1]) or isinstance(self.event_filter, list) or belongs_to_parent)):
            dct["eventFilter"] = dictify(self.event_filter, prop_is_list_or_vo=True)
        if "severity_filter" == "type" or (self.severity_filter is not self.__undef__ and (not (dirty and not self._severity_filter[1]) or isinstance(self.severity_filter, list) or belongs_to_parent)):
            dct["severityFilter"] = dictify(self.severity_filter, prop_is_list_or_vo=True)
        if "target_filter" == "type" or (self.target_filter is not self.__undef__ and (not (dirty and not self._target_filter[1]) or isinstance(self.target_filter, list) or belongs_to_parent)):
            dct["targetFilter"] = dictify(self.target_filter, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._actions = (self._actions[0], True)
        self._event_filter = (self._event_filter[0], True)
        self._severity_filter = (self._severity_filter[0], True)
        self._target_filter = (self._target_filter[0], True)

    def is_dirty(self):
        return any([self._actions[1], self._event_filter[1], self._severity_filter[1], self._target_filter[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AlertProfile):
            return False
        return super(AlertProfile, self).__eq__(other) and \
               self.actions == other.actions and \
               self.event_filter == other.event_filter and \
               self.severity_filter == other.severity_filter and \
               self.target_filter == other.target_filter

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def actions(self):
        """
        List of actions to take. Only alerts visible to the user and matching
        the optional filters are included. If there are multiple actions with
        the same result (such as emailing a user), only one result is acted
        upon.

        :rtype: ``list`` of :py:class:`v1_7_0.web.vo.AlertAction`
        """
        return self._actions[0]

    @actions.setter
    def actions(self, value):
        self._actions = (value, True)

    @property
    def event_filter(self):
        """
        Optional list of event types. If non-empty, only alerts of the given
        event type are included. Each event type is a string representing the
        event class of the corresponding alerts. Wildcards are supported to
        include classes of events.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._event_filter[0]

    @event_filter.setter
    def event_filter(self, value):
        self._event_filter = (value, True)

    @property
    def severity_filter(self):
        """
        Optional list of severity levels. If non-empty, only alerts of the
        given severity are included.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._severity_filter[0]

    @severity_filter.setter
    def severity_filter(self, value):
        self._severity_filter = (value, True)

    @property
    def target_filter(self):
        """
        Optional list of object references. If non-empty, only alerts related
        to one of the targets or its children are included.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._target_filter[0]

    @target_filter.setter
    def target_filter(self, value):
        self._target_filter = (value, True)

