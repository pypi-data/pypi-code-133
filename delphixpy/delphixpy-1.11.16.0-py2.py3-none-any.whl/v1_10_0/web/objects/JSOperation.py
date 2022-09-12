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
#     /delphix-js-operation.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_0.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_10_0 import factory
from delphixpy.v1_10_0 import common

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

class JSOperation(NamedUserObject):
    """
    *(extends* :py:class:`v1_10_0.web.vo.NamedUserObject` *)* An operation that
    occurred on a Self-Service data layout.
    """
    def __init__(self, undef_enabled=True):
        super(JSOperation, self).__init__()
        self._type = ("JSOperation", True)
        self._data_layout = (self.__undef__, True)
        self._branch = (self.__undef__, True)
        self._start_time = (self.__undef__, True)
        self._end_time = (self.__undef__, True)
        self._data_time = (self.__undef__, True)
        self._operation = (self.__undef__, True)
        self._description = (self.__undef__, True)
        self._bookmark = (self.__undef__, True)
        self._data_parent = (self.__undef__, True)
        self._root_action = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._force_option = (self.__undef__, True)

    API_VERSION = "1.10.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSOperation, cls).from_dict(data, dirty, undef_enabled)
        obj._data_layout = (data.get("dataLayout", obj.__undef__), dirty)
        if obj._data_layout[0] is not None and obj._data_layout[0] is not obj.__undef__:
            assert isinstance(obj._data_layout[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_layout[0], type(obj._data_layout[0])))
            common.validate_format(obj._data_layout[0], "objectReference", None, None)
        obj._branch = (data.get("branch", obj.__undef__), dirty)
        if obj._branch[0] is not None and obj._branch[0] is not obj.__undef__:
            assert isinstance(obj._branch[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._branch[0], type(obj._branch[0])))
            common.validate_format(obj._branch[0], "objectReference", None, None)
        obj._start_time = (data.get("startTime", obj.__undef__), dirty)
        if obj._start_time[0] is not None and obj._start_time[0] is not obj.__undef__:
            assert isinstance(obj._start_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._start_time[0], type(obj._start_time[0])))
            common.validate_format(obj._start_time[0], "date", None, None)
        obj._end_time = (data.get("endTime", obj.__undef__), dirty)
        if obj._end_time[0] is not None and obj._end_time[0] is not obj.__undef__:
            assert isinstance(obj._end_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._end_time[0], type(obj._end_time[0])))
            common.validate_format(obj._end_time[0], "date", None, None)
        obj._data_time = (data.get("dataTime", obj.__undef__), dirty)
        if obj._data_time[0] is not None and obj._data_time[0] is not obj.__undef__:
            assert isinstance(obj._data_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_time[0], type(obj._data_time[0])))
            common.validate_format(obj._data_time[0], "date", None, None)
        obj._operation = (data.get("operation", obj.__undef__), dirty)
        if obj._operation[0] is not None and obj._operation[0] is not obj.__undef__:
            assert isinstance(obj._operation[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._operation[0], type(obj._operation[0])))
            common.validate_format(obj._operation[0], "None", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, None)
        obj._bookmark = (data.get("bookmark", obj.__undef__), dirty)
        if obj._bookmark[0] is not None and obj._bookmark[0] is not obj.__undef__:
            assert isinstance(obj._bookmark[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._bookmark[0], type(obj._bookmark[0])))
            common.validate_format(obj._bookmark[0], "objectReference", None, None)
        if "dataParent" in data and data["dataParent"] is not None:
            obj._data_parent = (factory.create_object(data["dataParent"], "JSDataParent"), dirty)
            factory.validate_type(obj._data_parent[0], "JSDataParent")
        else:
            obj._data_parent = (obj.__undef__, dirty)
        obj._root_action = (data.get("rootAction", obj.__undef__), dirty)
        if obj._root_action[0] is not None and obj._root_action[0] is not obj.__undef__:
            assert isinstance(obj._root_action[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._root_action[0], type(obj._root_action[0])))
            common.validate_format(obj._root_action[0], "objectReference", None, None)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "objectReference", None, None)
        obj._force_option = (data.get("forceOption", obj.__undef__), dirty)
        if obj._force_option[0] is not None and obj._force_option[0] is not obj.__undef__:
            assert isinstance(obj._force_option[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._force_option[0], type(obj._force_option[0])))
            common.validate_format(obj._force_option[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSOperation, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "data_layout" == "type" or (self.data_layout is not self.__undef__ and (not (dirty and not self._data_layout[1]))):
            dct["dataLayout"] = dictify(self.data_layout)
        if "branch" == "type" or (self.branch is not self.__undef__ and (not (dirty and not self._branch[1]))):
            dct["branch"] = dictify(self.branch)
        if "start_time" == "type" or (self.start_time is not self.__undef__ and (not (dirty and not self._start_time[1]))):
            dct["startTime"] = dictify(self.start_time)
        if "end_time" == "type" or (self.end_time is not self.__undef__ and (not (dirty and not self._end_time[1]))):
            dct["endTime"] = dictify(self.end_time)
        if "data_time" == "type" or (self.data_time is not self.__undef__ and (not (dirty and not self._data_time[1]))):
            dct["dataTime"] = dictify(self.data_time)
        if "operation" == "type" or (self.operation is not self.__undef__ and (not (dirty and not self._operation[1]))):
            dct["operation"] = dictify(self.operation)
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]))):
            dct["description"] = dictify(self.description)
        if "bookmark" == "type" or (self.bookmark is not self.__undef__ and (not (dirty and not self._bookmark[1]))):
            dct["bookmark"] = dictify(self.bookmark)
        if "data_parent" == "type" or (self.data_parent is not self.__undef__ and (not (dirty and not self._data_parent[1]))):
            dct["dataParent"] = dictify(self.data_parent)
        if "root_action" == "type" or (self.root_action is not self.__undef__ and (not (dirty and not self._root_action[1]))):
            dct["rootAction"] = dictify(self.root_action)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]))):
            dct["user"] = dictify(self.user)
        if "force_option" == "type" or (self.force_option is not self.__undef__ and (not (dirty and not self._force_option[1]))):
            dct["forceOption"] = dictify(self.force_option)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._data_layout = (self._data_layout[0], True)
        self._branch = (self._branch[0], True)
        self._start_time = (self._start_time[0], True)
        self._end_time = (self._end_time[0], True)
        self._data_time = (self._data_time[0], True)
        self._operation = (self._operation[0], True)
        self._description = (self._description[0], True)
        self._bookmark = (self._bookmark[0], True)
        self._data_parent = (self._data_parent[0], True)
        self._root_action = (self._root_action[0], True)
        self._user = (self._user[0], True)
        self._force_option = (self._force_option[0], True)

    def is_dirty(self):
        return any([self._data_layout[1], self._branch[1], self._start_time[1], self._end_time[1], self._data_time[1], self._operation[1], self._description[1], self._bookmark[1], self._data_parent[1], self._root_action[1], self._user[1], self._force_option[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSOperation):
            return False
        return super(JSOperation, self).__eq__(other) and \
               self.data_layout == other.data_layout and \
               self.branch == other.branch and \
               self.start_time == other.start_time and \
               self.end_time == other.end_time and \
               self.data_time == other.data_time and \
               self.operation == other.operation and \
               self.description == other.description and \
               self.bookmark == other.bookmark and \
               self.data_parent == other.data_parent and \
               self.root_action == other.root_action and \
               self.user == other.user and \
               self.force_option == other.force_option

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def data_layout(self):
        """
        The data layout that this operation was performed on.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_layout[0]

    @data_layout.setter
    def data_layout(self, value):
        self._data_layout = (value, True)

    @property
    def branch(self):
        """
        The branch that this operation was performed on.

        :rtype: ``TEXT_TYPE``
        """
        return self._branch[0]

    @branch.setter
    def branch(self, value):
        self._branch = (value, True)

    @property
    def start_time(self):
        """
        The time the operation started.

        :rtype: ``TEXT_TYPE``
        """
        return self._start_time[0]

    @start_time.setter
    def start_time(self, value):
        self._start_time = (value, True)

    @property
    def end_time(self):
        """
        The time the operation finished. It will be null if the operation is in
        progress.

        :rtype: ``TEXT_TYPE``
        """
        return self._end_time[0]

    @end_time.setter
    def end_time(self, value):
        self._end_time = (value, True)

    @property
    def data_time(self):
        """
        The time that the data represented by this operation was active. It
        will be null if the operation is in progress.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_time[0]

    @data_time.setter
    def data_time(self, value):
        self._data_time = (value, True)

    @property
    def operation(self):
        """
        The operation performed. *(permitted values: REFRESH, RESET,
        CREATE_BRANCH, DELETE_BRANCH, CREATE_BOOKMARK, DELETE_BOOKMARK, ENABLE,
        DISABLE, ACTIVATE, DEACTIVATE, RECOVER, RESTORE, UNDO, LOCK, UNLOCK,
        HISTORY)*

        :rtype: ``TEXT_TYPE``
        """
        return self._operation[0]

    @operation.setter
    def operation(self, value):
        self._operation = (value, True)

    @property
    def description(self):
        """
        Plain text description of the operation.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def bookmark(self):
        """
        The bookmark that was created.

        :rtype: ``TEXT_TYPE``
        """
        return self._bookmark[0]

    @bookmark.setter
    def bookmark(self, value):
        self._bookmark = (value, True)

    @property
    def data_parent(self):
        """
        The data parent of the operation.

        :rtype: :py:class:`v1_10_0.web.vo.JSDataParent`
        """
        return self._data_parent[0]

    @data_parent.setter
    def data_parent(self, value):
        self._data_parent = (value, True)

    @property
    def root_action(self):
        """
        The root action that spawned this operation.

        :rtype: ``TEXT_TYPE``
        """
        return self._root_action[0]

    @root_action.setter
    def root_action(self, value):
        self._root_action = (value, True)

    @property
    def user(self):
        """
        The user who performed the operation.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def force_option(self):
        """
        Was this operation perfomed with the force option, which means no pre-
        operation snapshot was taken.

        :rtype: ``bool``
        """
        return self._force_option[0]

    @force_option.setter
    def force_option(self, value):
        self._force_option = (value, True)

