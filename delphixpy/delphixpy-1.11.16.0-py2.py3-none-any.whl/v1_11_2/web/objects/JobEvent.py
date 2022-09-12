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
#     /delphix-job-event.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_2 import factory
from delphixpy.v1_11_2 import common

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

class JobEvent(TypedObject):
    """
    *(extends* :py:class:`v1_11_2.web.vo.TypedObject` *)* Represents a job
    event object. This can either be a state change or a progress update.
    """
    def __init__(self, undef_enabled=True):
        super(JobEvent, self).__init__()
        self._type = ("JobEvent", True)
        self._timestamp = (self.__undef__, True)
        self._state = (self.__undef__, True)
        self._percent_complete = (self.__undef__, True)
        self._message_code = (self.__undef__, True)
        self._message_details = (self.__undef__, True)
        self._message_action = (self.__undef__, True)
        self._message_command_output = (self.__undef__, True)
        self._diagnoses = (self.__undef__, True)
        self._event_type = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JobEvent, cls).from_dict(data, dirty, undef_enabled)
        obj._timestamp = (data.get("timestamp", obj.__undef__), dirty)
        if obj._timestamp[0] is not None and obj._timestamp[0] is not obj.__undef__:
            assert isinstance(obj._timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timestamp[0], type(obj._timestamp[0])))
            common.validate_format(obj._timestamp[0], "date", None, None)
        obj._state = (data.get("state", obj.__undef__), dirty)
        if obj._state[0] is not None and obj._state[0] is not obj.__undef__:
            assert isinstance(obj._state[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._state[0], type(obj._state[0])))
            assert obj._state[0] in ['INITIAL', 'RUNNING', 'SUSPENDED', 'CANCELED', 'COMPLETED', 'FAILED', 'RETRYABLE'], "Expected enum ['INITIAL', 'RUNNING', 'SUSPENDED', 'CANCELED', 'COMPLETED', 'FAILED', 'RETRYABLE'] but got %s" % obj._state[0]
            common.validate_format(obj._state[0], "None", None, None)
        obj._percent_complete = (data.get("percentComplete", obj.__undef__), dirty)
        if obj._percent_complete[0] is not None and obj._percent_complete[0] is not obj.__undef__:
            assert isinstance(obj._percent_complete[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._percent_complete[0], type(obj._percent_complete[0])))
            common.validate_format(obj._percent_complete[0], "None", None, None)
        obj._message_code = (data.get("messageCode", obj.__undef__), dirty)
        if obj._message_code[0] is not None and obj._message_code[0] is not obj.__undef__:
            assert isinstance(obj._message_code[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message_code[0], type(obj._message_code[0])))
            common.validate_format(obj._message_code[0], "None", None, None)
        obj._message_details = (data.get("messageDetails", obj.__undef__), dirty)
        if obj._message_details[0] is not None and obj._message_details[0] is not obj.__undef__:
            assert isinstance(obj._message_details[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message_details[0], type(obj._message_details[0])))
            common.validate_format(obj._message_details[0], "None", None, None)
        obj._message_action = (data.get("messageAction", obj.__undef__), dirty)
        if obj._message_action[0] is not None and obj._message_action[0] is not obj.__undef__:
            assert isinstance(obj._message_action[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message_action[0], type(obj._message_action[0])))
            common.validate_format(obj._message_action[0], "None", None, None)
        obj._message_command_output = (data.get("messageCommandOutput", obj.__undef__), dirty)
        if obj._message_command_output[0] is not None and obj._message_command_output[0] is not obj.__undef__:
            assert isinstance(obj._message_command_output[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message_command_output[0], type(obj._message_command_output[0])))
            common.validate_format(obj._message_command_output[0], "None", None, None)
        obj._diagnoses = []
        for item in data.get("diagnoses") or []:
            obj._diagnoses.append(factory.create_object(item))
            factory.validate_type(obj._diagnoses[-1], "DiagnosisResult")
        obj._diagnoses = (obj._diagnoses, dirty)
        obj._event_type = (data.get("eventType", obj.__undef__), dirty)
        if obj._event_type[0] is not None and obj._event_type[0] is not obj.__undef__:
            assert isinstance(obj._event_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._event_type[0], type(obj._event_type[0])))
            assert obj._event_type[0] in ['INFO', 'WARNING', 'ERROR'], "Expected enum ['INFO', 'WARNING', 'ERROR'] but got %s" % obj._event_type[0]
            common.validate_format(obj._event_type[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JobEvent, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "timestamp" == "type" or (self.timestamp is not self.__undef__ and (not (dirty and not self._timestamp[1]))):
            dct["timestamp"] = dictify(self.timestamp)
        if "state" == "type" or (self.state is not self.__undef__ and (not (dirty and not self._state[1]))):
            dct["state"] = dictify(self.state)
        if "percent_complete" == "type" or (self.percent_complete is not self.__undef__ and (not (dirty and not self._percent_complete[1]))):
            dct["percentComplete"] = dictify(self.percent_complete)
        if "message_code" == "type" or (self.message_code is not self.__undef__ and (not (dirty and not self._message_code[1]))):
            dct["messageCode"] = dictify(self.message_code)
        if "message_details" == "type" or (self.message_details is not self.__undef__ and (not (dirty and not self._message_details[1]))):
            dct["messageDetails"] = dictify(self.message_details)
        if "message_action" == "type" or (self.message_action is not self.__undef__ and (not (dirty and not self._message_action[1]))):
            dct["messageAction"] = dictify(self.message_action)
        if "message_command_output" == "type" or (self.message_command_output is not self.__undef__ and (not (dirty and not self._message_command_output[1]))):
            dct["messageCommandOutput"] = dictify(self.message_command_output)
        if "diagnoses" == "type" or (self.diagnoses is not self.__undef__ and (not (dirty and not self._diagnoses[1]))):
            dct["diagnoses"] = dictify(self.diagnoses)
        if "event_type" == "type" or (self.event_type is not self.__undef__ and (not (dirty and not self._event_type[1]))):
            dct["eventType"] = dictify(self.event_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._timestamp = (self._timestamp[0], True)
        self._state = (self._state[0], True)
        self._percent_complete = (self._percent_complete[0], True)
        self._message_code = (self._message_code[0], True)
        self._message_details = (self._message_details[0], True)
        self._message_action = (self._message_action[0], True)
        self._message_command_output = (self._message_command_output[0], True)
        self._diagnoses = (self._diagnoses[0], True)
        self._event_type = (self._event_type[0], True)

    def is_dirty(self):
        return any([self._timestamp[1], self._state[1], self._percent_complete[1], self._message_code[1], self._message_details[1], self._message_action[1], self._message_command_output[1], self._diagnoses[1], self._event_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JobEvent):
            return False
        return super(JobEvent, self).__eq__(other) and \
               self.timestamp == other.timestamp and \
               self.state == other.state and \
               self.percent_complete == other.percent_complete and \
               self.message_code == other.message_code and \
               self.message_details == other.message_details and \
               self.message_action == other.message_action and \
               self.message_command_output == other.message_command_output and \
               self.diagnoses == other.diagnoses and \
               self.event_type == other.event_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def timestamp(self):
        """
        Time the event occurred.

        :rtype: ``TEXT_TYPE``
        """
        return self._timestamp[0]

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = (value, True)

    @property
    def state(self):
        """
        New state of the job. *(permitted values: INITIAL, RUNNING, SUSPENDED,
        CANCELED, COMPLETED, FAILED, RETRYABLE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._state[0]

    @state.setter
    def state(self, value):
        self._state = (value, True)

    @property
    def percent_complete(self):
        """
        Completion percentage.

        :rtype: ``float``
        """
        return self._percent_complete[0]

    @percent_complete.setter
    def percent_complete(self, value):
        self._percent_complete = (value, True)

    @property
    def message_code(self):
        """
        Message ID associated with the event.

        :rtype: ``TEXT_TYPE``
        """
        return self._message_code[0]

    @message_code.setter
    def message_code(self, value):
        self._message_code = (value, True)

    @property
    def message_details(self):
        """
        Localized message details.

        :rtype: ``TEXT_TYPE``
        """
        return self._message_details[0]

    @message_details.setter
    def message_details(self, value):
        self._message_details = (value, True)

    @property
    def message_action(self):
        """
        Localized message action.

        :rtype: ``TEXT_TYPE``
        """
        return self._message_action[0]

    @message_action.setter
    def message_action(self, value):
        self._message_action = (value, True)

    @property
    def message_command_output(self):
        """
        Command output associated with the event, if applicable.

        :rtype: ``TEXT_TYPE``
        """
        return self._message_command_output[0]

    @message_command_output.setter
    def message_command_output(self, value):
        self._message_command_output = (value, True)

    @property
    def diagnoses(self):
        """
        Results of diagnostic checks run, if any, if the job failed.

        :rtype: ``list`` of :py:class:`v1_11_2.web.vo.DiagnosisResult`
        """
        return self._diagnoses[0]

    @diagnoses.setter
    def diagnoses(self, value):
        self._diagnoses = (value, True)

    @property
    def event_type(self):
        """
        Type of event. *(permitted values: INFO, WARNING, ERROR)*

        :rtype: ``TEXT_TYPE``
        """
        return self._event_type[0]

    @event_type.setter
    def event_type(self, value):
        self._event_type = (value, True)

