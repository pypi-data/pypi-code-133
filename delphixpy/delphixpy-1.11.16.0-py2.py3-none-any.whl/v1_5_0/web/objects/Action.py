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
#     /delphix-action.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_0.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_5_0 import common

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

class Action(PersistentObject):
    """
    *(extends* :py:class:`v1_5_0.web.vo.PersistentObject` *)* Represents an
    action, a permanent record of activity on the server.
    """
    def __init__(self, undef_enabled=True):
        super(Action, self).__init__()
        self._type = ("Action", True)
        self._action_type = (self.__undef__, True)
        self._details = (self.__undef__, True)
        self._end_time = (self.__undef__, True)
        self._parent_action = (self.__undef__, True)
        self._report = (self.__undef__, True)
        self._start_time = (self.__undef__, True)
        self._state = (self.__undef__, True)
        self._title = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._user_agent = (self.__undef__, True)
        self._work_source = (self.__undef__, True)
        self._work_source_name = (self.__undef__, True)

    API_VERSION = "1.5.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Action, cls).from_dict(data, dirty, undef_enabled)
        obj._action_type = (data.get("actionType", obj.__undef__), dirty)
        if obj._action_type[0] is not None and obj._action_type[0] is not obj.__undef__:
            assert isinstance(obj._action_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._action_type[0], type(obj._action_type[0])))
            common.validate_format(obj._action_type[0], "None", None, None)
        obj._details = (data.get("details", obj.__undef__), dirty)
        if obj._details[0] is not None and obj._details[0] is not obj.__undef__:
            assert isinstance(obj._details[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._details[0], type(obj._details[0])))
            common.validate_format(obj._details[0], "None", None, None)
        obj._end_time = (data.get("endTime", obj.__undef__), dirty)
        if obj._end_time[0] is not None and obj._end_time[0] is not obj.__undef__:
            assert isinstance(obj._end_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._end_time[0], type(obj._end_time[0])))
            common.validate_format(obj._end_time[0], "date", None, None)
        obj._parent_action = (data.get("parentAction", obj.__undef__), dirty)
        if obj._parent_action[0] is not None and obj._parent_action[0] is not obj.__undef__:
            assert isinstance(obj._parent_action[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._parent_action[0], type(obj._parent_action[0])))
            common.validate_format(obj._parent_action[0], "objectReference", None, None)
        obj._report = (data.get("report", obj.__undef__), dirty)
        if obj._report[0] is not None and obj._report[0] is not obj.__undef__:
            assert isinstance(obj._report[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._report[0], type(obj._report[0])))
            common.validate_format(obj._report[0], "None", None, None)
        obj._start_time = (data.get("startTime", obj.__undef__), dirty)
        if obj._start_time[0] is not None and obj._start_time[0] is not obj.__undef__:
            assert isinstance(obj._start_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._start_time[0], type(obj._start_time[0])))
            common.validate_format(obj._start_time[0], "date", None, None)
        obj._state = (data.get("state", obj.__undef__), dirty)
        if obj._state[0] is not None and obj._state[0] is not obj.__undef__:
            assert isinstance(obj._state[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._state[0], type(obj._state[0])))
            assert obj._state[0] in ['EXECUTING', 'WAITING', 'COMPLETED', 'FAILED', 'CANCELED'], "Expected enum ['EXECUTING', 'WAITING', 'COMPLETED', 'FAILED', 'CANCELED'] but got %s" % obj._state[0]
            common.validate_format(obj._state[0], "None", None, None)
        obj._title = (data.get("title", obj.__undef__), dirty)
        if obj._title[0] is not None and obj._title[0] is not obj.__undef__:
            assert isinstance(obj._title[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._title[0], type(obj._title[0])))
            common.validate_format(obj._title[0], "None", None, None)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "objectReference", None, None)
        obj._user_agent = (data.get("userAgent", obj.__undef__), dirty)
        if obj._user_agent[0] is not None and obj._user_agent[0] is not obj.__undef__:
            assert isinstance(obj._user_agent[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user_agent[0], type(obj._user_agent[0])))
            common.validate_format(obj._user_agent[0], "None", None, None)
        obj._work_source = (data.get("workSource", obj.__undef__), dirty)
        if obj._work_source[0] is not None and obj._work_source[0] is not obj.__undef__:
            assert isinstance(obj._work_source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._work_source[0], type(obj._work_source[0])))
            assert obj._work_source[0] in ['WEBSERVICE', 'POLICY', 'SYSTEM'], "Expected enum ['WEBSERVICE', 'POLICY', 'SYSTEM'] but got %s" % obj._work_source[0]
            common.validate_format(obj._work_source[0], "None", None, None)
        obj._work_source_name = (data.get("workSourceName", obj.__undef__), dirty)
        if obj._work_source_name[0] is not None and obj._work_source_name[0] is not obj.__undef__:
            assert isinstance(obj._work_source_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._work_source_name[0], type(obj._work_source_name[0])))
            common.validate_format(obj._work_source_name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Action, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "action_type" == "type" or (self.action_type is not self.__undef__ and (not (dirty and not self._action_type[1]))):
            dct["actionType"] = dictify(self.action_type)
        if "details" == "type" or (self.details is not self.__undef__ and (not (dirty and not self._details[1]))):
            dct["details"] = dictify(self.details)
        if "end_time" == "type" or (self.end_time is not self.__undef__ and (not (dirty and not self._end_time[1]))):
            dct["endTime"] = dictify(self.end_time)
        if "parent_action" == "type" or (self.parent_action is not self.__undef__ and (not (dirty and not self._parent_action[1]))):
            dct["parentAction"] = dictify(self.parent_action)
        if "report" == "type" or (self.report is not self.__undef__ and (not (dirty and not self._report[1]))):
            dct["report"] = dictify(self.report)
        if "start_time" == "type" or (self.start_time is not self.__undef__ and (not (dirty and not self._start_time[1]))):
            dct["startTime"] = dictify(self.start_time)
        if "state" == "type" or (self.state is not self.__undef__ and (not (dirty and not self._state[1]))):
            dct["state"] = dictify(self.state)
        if "title" == "type" or (self.title is not self.__undef__ and (not (dirty and not self._title[1]))):
            dct["title"] = dictify(self.title)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]))):
            dct["user"] = dictify(self.user)
        if "user_agent" == "type" or (self.user_agent is not self.__undef__ and (not (dirty and not self._user_agent[1]))):
            dct["userAgent"] = dictify(self.user_agent)
        if "work_source" == "type" or (self.work_source is not self.__undef__ and (not (dirty and not self._work_source[1]))):
            dct["workSource"] = dictify(self.work_source)
        if "work_source_name" == "type" or (self.work_source_name is not self.__undef__ and (not (dirty and not self._work_source_name[1]))):
            dct["workSourceName"] = dictify(self.work_source_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._action_type = (self._action_type[0], True)
        self._details = (self._details[0], True)
        self._end_time = (self._end_time[0], True)
        self._parent_action = (self._parent_action[0], True)
        self._report = (self._report[0], True)
        self._start_time = (self._start_time[0], True)
        self._state = (self._state[0], True)
        self._title = (self._title[0], True)
        self._user = (self._user[0], True)
        self._user_agent = (self._user_agent[0], True)
        self._work_source = (self._work_source[0], True)
        self._work_source_name = (self._work_source_name[0], True)

    def is_dirty(self):
        return any([self._action_type[1], self._details[1], self._end_time[1], self._parent_action[1], self._report[1], self._start_time[1], self._state[1], self._title[1], self._user[1], self._user_agent[1], self._work_source[1], self._work_source_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Action):
            return False
        return super(Action, self).__eq__(other) and \
               self.action_type == other.action_type and \
               self.details == other.details and \
               self.end_time == other.end_time and \
               self.parent_action == other.parent_action and \
               self.report == other.report and \
               self.start_time == other.start_time and \
               self.state == other.state and \
               self.title == other.title and \
               self.user == other.user and \
               self.user_agent == other.user_agent and \
               self.work_source == other.work_source and \
               self.work_source_name == other.work_source_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def action_type(self):
        """
        Action type.

        :rtype: ``TEXT_TYPE``
        """
        return self._action_type[0]

    @action_type.setter
    def action_type(self, value):
        self._action_type = (value, True)

    @property
    def details(self):
        """
        Plain text description of the action.

        :rtype: ``TEXT_TYPE``
        """
        return self._details[0]

    @details.setter
    def details(self, value):
        self._details = (value, True)

    @property
    def end_time(self):
        """
        The time the action completed.

        :rtype: ``TEXT_TYPE``
        """
        return self._end_time[0]

    @end_time.setter
    def end_time(self, value):
        self._end_time = (value, True)

    @property
    def parent_action(self):
        """
        The parent action of this action.

        :rtype: ``TEXT_TYPE``
        """
        return self._parent_action[0]

    @parent_action.setter
    def parent_action(self, value):
        self._parent_action = (value, True)

    @property
    def report(self):
        """
        Report of progress and warnings for some actions.

        :rtype: ``TEXT_TYPE``
        """
        return self._report[0]

    @report.setter
    def report(self, value):
        self._report = (value, True)

    @property
    def start_time(self):
        """
        The time the action occurred. For long running processes, this
        represents the starting time.

        :rtype: ``TEXT_TYPE``
        """
        return self._start_time[0]

    @start_time.setter
    def start_time(self, value):
        self._start_time = (value, True)

    @property
    def state(self):
        """
        State of the action. *(permitted values: EXECUTING, WAITING, COMPLETED,
        FAILED, CANCELED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._state[0]

    @state.setter
    def state(self, value):
        self._state = (value, True)

    @property
    def title(self):
        """
        Action title.

        :rtype: ``TEXT_TYPE``
        """
        return self._title[0]

    @title.setter
    def title(self, value):
        self._title = (value, True)

    @property
    def user(self):
        """
        User who initiated the action.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def user_agent(self):
        """
        Name of client software used to initiate the action.

        :rtype: ``TEXT_TYPE``
        """
        return self._user_agent[0]

    @user_agent.setter
    def user_agent(self, value):
        self._user_agent = (value, True)

    @property
    def work_source(self):
        """
        Origin of the work that caused the action. *(permitted values:
        WEBSERVICE, POLICY, SYSTEM)*

        :rtype: ``TEXT_TYPE``
        """
        return self._work_source[0]

    @work_source.setter
    def work_source(self, value):
        self._work_source = (value, True)

    @property
    def work_source_name(self):
        """
        Name of user or policy that initiated the action.

        :rtype: ``TEXT_TYPE``
        """
        return self._work_source_name[0]

    @work_source_name.setter
    def work_source_name(self, value):
        self._work_source_name = (value, True)

