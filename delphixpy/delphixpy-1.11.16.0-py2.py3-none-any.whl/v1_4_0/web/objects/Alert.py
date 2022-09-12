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
#     /delphix-alert.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_0.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_4_0 import common

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

class Alert(PersistentObject):
    """
    *(extends* :py:class:`v1_4_0.web.vo.PersistentObject` *)* An alert
    describing an event for a given object.
    """
    def __init__(self, undef_enabled=True):
        super(Alert, self).__init__()
        self._type = ("Alert", True)
        self._event = (self.__undef__, True)
        self._event_action = (self.__undef__, True)
        self._event_command_output = (self.__undef__, True)
        self._event_description = (self.__undef__, True)
        self._event_response = (self.__undef__, True)
        self._event_severity = (self.__undef__, True)
        self._event_title = (self.__undef__, True)
        self._target = (self.__undef__, True)
        self._target_name = (self.__undef__, True)
        self._target_object_type = (self.__undef__, True)
        self._timestamp = (self.__undef__, True)

    API_VERSION = "1.4.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Alert, cls).from_dict(data, dirty, undef_enabled)
        obj._event = (data.get("event", obj.__undef__), dirty)
        if obj._event[0] is not None and obj._event[0] is not obj.__undef__:
            assert isinstance(obj._event[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event[0], type(obj._event[0])))
            common.validate_format(obj._event[0], "None", None, None)
        obj._event_action = (data.get("eventAction", obj.__undef__), dirty)
        if obj._event_action[0] is not None and obj._event_action[0] is not obj.__undef__:
            assert isinstance(obj._event_action[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_action[0], type(obj._event_action[0])))
            common.validate_format(obj._event_action[0], "None", None, None)
        obj._event_command_output = (data.get("eventCommandOutput", obj.__undef__), dirty)
        if obj._event_command_output[0] is not None and obj._event_command_output[0] is not obj.__undef__:
            assert isinstance(obj._event_command_output[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_command_output[0], type(obj._event_command_output[0])))
            common.validate_format(obj._event_command_output[0], "None", None, None)
        obj._event_description = (data.get("eventDescription", obj.__undef__), dirty)
        if obj._event_description[0] is not None and obj._event_description[0] is not obj.__undef__:
            assert isinstance(obj._event_description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_description[0], type(obj._event_description[0])))
            common.validate_format(obj._event_description[0], "None", None, None)
        obj._event_response = (data.get("eventResponse", obj.__undef__), dirty)
        if obj._event_response[0] is not None and obj._event_response[0] is not obj.__undef__:
            assert isinstance(obj._event_response[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_response[0], type(obj._event_response[0])))
            common.validate_format(obj._event_response[0], "None", None, None)
        obj._event_severity = (data.get("eventSeverity", obj.__undef__), dirty)
        if obj._event_severity[0] is not None and obj._event_severity[0] is not obj.__undef__:
            assert isinstance(obj._event_severity[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_severity[0], type(obj._event_severity[0])))
            assert obj._event_severity[0] in ['INFORMATIONAL', 'WARNING', 'CRITICAL'], "Expected enum ['INFORMATIONAL', 'WARNING', 'CRITICAL'] but got %s" % obj._event_severity[0]
            common.validate_format(obj._event_severity[0], "None", None, None)
        obj._event_title = (data.get("eventTitle", obj.__undef__), dirty)
        if obj._event_title[0] is not None and obj._event_title[0] is not obj.__undef__:
            assert isinstance(obj._event_title[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_title[0], type(obj._event_title[0])))
            common.validate_format(obj._event_title[0], "None", None, None)
        obj._target = (data.get("target", obj.__undef__), dirty)
        if obj._target[0] is not None and obj._target[0] is not obj.__undef__:
            assert isinstance(obj._target[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target[0], type(obj._target[0])))
            common.validate_format(obj._target[0], "objectReference", None, None)
        obj._target_name = (data.get("targetName", obj.__undef__), dirty)
        if obj._target_name[0] is not None and obj._target_name[0] is not obj.__undef__:
            assert isinstance(obj._target_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_name[0], type(obj._target_name[0])))
            common.validate_format(obj._target_name[0], "None", None, None)
        obj._target_object_type = (data.get("targetObjectType", obj.__undef__), dirty)
        if obj._target_object_type[0] is not None and obj._target_object_type[0] is not obj.__undef__:
            assert isinstance(obj._target_object_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_object_type[0], type(obj._target_object_type[0])))
            common.validate_format(obj._target_object_type[0], "type", None, None)
        obj._timestamp = (data.get("timestamp", obj.__undef__), dirty)
        if obj._timestamp[0] is not None and obj._timestamp[0] is not obj.__undef__:
            assert isinstance(obj._timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timestamp[0], type(obj._timestamp[0])))
            common.validate_format(obj._timestamp[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Alert, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "event" == "type" or (self.event is not self.__undef__ and (not (dirty and not self._event[1]))):
            dct["event"] = dictify(self.event)
        if "event_action" == "type" or (self.event_action is not self.__undef__ and (not (dirty and not self._event_action[1]))):
            dct["eventAction"] = dictify(self.event_action)
        if "event_command_output" == "type" or (self.event_command_output is not self.__undef__ and (not (dirty and not self._event_command_output[1]))):
            dct["eventCommandOutput"] = dictify(self.event_command_output)
        if "event_description" == "type" or (self.event_description is not self.__undef__ and (not (dirty and not self._event_description[1]))):
            dct["eventDescription"] = dictify(self.event_description)
        if "event_response" == "type" or (self.event_response is not self.__undef__ and (not (dirty and not self._event_response[1]))):
            dct["eventResponse"] = dictify(self.event_response)
        if "event_severity" == "type" or (self.event_severity is not self.__undef__ and (not (dirty and not self._event_severity[1]))):
            dct["eventSeverity"] = dictify(self.event_severity)
        if "event_title" == "type" or (self.event_title is not self.__undef__ and (not (dirty and not self._event_title[1]))):
            dct["eventTitle"] = dictify(self.event_title)
        if "target" == "type" or (self.target is not self.__undef__ and (not (dirty and not self._target[1]))):
            dct["target"] = dictify(self.target)
        if "target_name" == "type" or (self.target_name is not self.__undef__ and (not (dirty and not self._target_name[1]))):
            dct["targetName"] = dictify(self.target_name)
        if "target_object_type" == "type" or (self.target_object_type is not self.__undef__ and (not (dirty and not self._target_object_type[1]))):
            dct["targetObjectType"] = dictify(self.target_object_type)
        if "timestamp" == "type" or (self.timestamp is not self.__undef__ and (not (dirty and not self._timestamp[1]))):
            dct["timestamp"] = dictify(self.timestamp)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._event = (self._event[0], True)
        self._event_action = (self._event_action[0], True)
        self._event_command_output = (self._event_command_output[0], True)
        self._event_description = (self._event_description[0], True)
        self._event_response = (self._event_response[0], True)
        self._event_severity = (self._event_severity[0], True)
        self._event_title = (self._event_title[0], True)
        self._target = (self._target[0], True)
        self._target_name = (self._target_name[0], True)
        self._target_object_type = (self._target_object_type[0], True)
        self._timestamp = (self._timestamp[0], True)

    def is_dirty(self):
        return any([self._event[1], self._event_action[1], self._event_command_output[1], self._event_description[1], self._event_response[1], self._event_severity[1], self._event_title[1], self._target[1], self._target_name[1], self._target_object_type[1], self._timestamp[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Alert):
            return False
        return super(Alert, self).__eq__(other) and \
               self.event == other.event and \
               self.event_action == other.event_action and \
               self.event_command_output == other.event_command_output and \
               self.event_description == other.event_description and \
               self.event_response == other.event_response and \
               self.event_severity == other.event_severity and \
               self.event_title == other.event_title and \
               self.target == other.target and \
               self.target_name == other.target_name and \
               self.target_object_type == other.target_object_type and \
               self.timestamp == other.timestamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def event(self):
        """
        Event class

        :rtype: ``TEXT_TYPE``
        """
        return self._event[0]

    @event.setter
    def event(self, value):
        self._event = (value, True)

    @property
    def event_action(self):
        """
        Event recommended action

        :rtype: ``TEXT_TYPE``
        """
        return self._event_action[0]

    @event_action.setter
    def event_action(self, value):
        self._event_action = (value, True)

    @property
    def event_command_output(self):
        """
        Additional text associated with the event. This text is not localized
        and is only provided for certain alerts. For example, if an alert is
        caused by a post script failure, the output of the post script may be
        included here to assist with debugging the failure.

        :rtype: ``TEXT_TYPE``
        """
        return self._event_command_output[0]

    @event_command_output.setter
    def event_command_output(self, value):
        self._event_command_output = (value, True)

    @property
    def event_description(self):
        """
        Event description

        :rtype: ``TEXT_TYPE``
        """
        return self._event_description[0]

    @event_description.setter
    def event_description(self, value):
        self._event_description = (value, True)

    @property
    def event_response(self):
        """
        Event response

        :rtype: ``TEXT_TYPE``
        """
        return self._event_response[0]

    @event_response.setter
    def event_response(self, value):
        self._event_response = (value, True)

    @property
    def event_severity(self):
        """
        Event severity *(permitted values: INFORMATIONAL, WARNING, CRITICAL)*

        :rtype: ``TEXT_TYPE``
        """
        return self._event_severity[0]

    @event_severity.setter
    def event_severity(self, value):
        self._event_severity = (value, True)

    @property
    def event_title(self):
        """
        Event title

        :rtype: ``TEXT_TYPE``
        """
        return self._event_title[0]

    @event_title.setter
    def event_title(self, value):
        self._event_title = (value, True)

    @property
    def target(self):
        """
        Reference to target object

        :rtype: ``TEXT_TYPE``
        """
        return self._target[0]

    @target.setter
    def target(self, value):
        self._target = (value, True)

    @property
    def target_name(self):
        """
        Name of target object

        :rtype: ``TEXT_TYPE``
        """
        return self._target_name[0]

    @target_name.setter
    def target_name(self, value):
        self._target_name = (value, True)

    @property
    def target_object_type(self):
        """
        Type of target object

        :rtype: ``TEXT_TYPE``
        """
        return self._target_object_type[0]

    @target_object_type.setter
    def target_object_type(self, value):
        self._target_object_type = (value, True)

    @property
    def timestamp(self):
        """
        Time at which event occurred

        :rtype: ``TEXT_TYPE``
        """
        return self._timestamp[0]

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = (value, True)

