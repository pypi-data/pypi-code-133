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
#     /delphix-js-data-layout.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_0.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_8_0 import common

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

class JSDataLayout(NamedUserObject):
    """
    *(extends* :py:class:`v1_8_0.web.vo.NamedUserObject` *)* A Jet Stream data
    layout comprised of a set of data sources and configuration information.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataLayout, self).__init__()
        self._type = ("JSDataLayout", True)
        self._active_branch = (self.__undef__, True)
        self._first_operation = (self.__undef__, True)
        self._last_operation = (self.__undef__, True)
        self._last_updated = (self.__undef__, True)
        self._notes = (self.__undef__, True)
        self._properties = (self.__undef__, True)

    API_VERSION = "1.8.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataLayout, cls).from_dict(data, dirty, undef_enabled)
        obj._active_branch = (data.get("activeBranch", obj.__undef__), dirty)
        if obj._active_branch[0] is not None and obj._active_branch[0] is not obj.__undef__:
            assert isinstance(obj._active_branch[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._active_branch[0], type(obj._active_branch[0])))
            common.validate_format(obj._active_branch[0], "objectReference", None, None)
        obj._first_operation = (data.get("firstOperation", obj.__undef__), dirty)
        if obj._first_operation[0] is not None and obj._first_operation[0] is not obj.__undef__:
            assert isinstance(obj._first_operation[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._first_operation[0], type(obj._first_operation[0])))
            common.validate_format(obj._first_operation[0], "objectReference", None, None)
        obj._last_operation = (data.get("lastOperation", obj.__undef__), dirty)
        if obj._last_operation[0] is not None and obj._last_operation[0] is not obj.__undef__:
            assert isinstance(obj._last_operation[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_operation[0], type(obj._last_operation[0])))
            common.validate_format(obj._last_operation[0], "objectReference", None, None)
        obj._last_updated = (data.get("lastUpdated", obj.__undef__), dirty)
        if obj._last_updated[0] is not None and obj._last_updated[0] is not obj.__undef__:
            assert isinstance(obj._last_updated[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_updated[0], type(obj._last_updated[0])))
            common.validate_format(obj._last_updated[0], "date", None, None)
        obj._notes = (data.get("notes", obj.__undef__), dirty)
        if obj._notes[0] is not None and obj._notes[0] is not obj.__undef__:
            assert isinstance(obj._notes[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._notes[0], type(obj._notes[0])))
            common.validate_format(obj._notes[0], "None", None, 4096)
        obj._properties = (data.get("properties", obj.__undef__), dirty)
        if obj._properties[0] is not None and obj._properties[0] is not obj.__undef__:
            assert isinstance(obj._properties[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._properties[0], type(obj._properties[0])))
            common.validate_format(obj._properties[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataLayout, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "active_branch" == "type" or (self.active_branch is not self.__undef__ and (not (dirty and not self._active_branch[1]))):
            dct["activeBranch"] = dictify(self.active_branch)
        if "first_operation" == "type" or (self.first_operation is not self.__undef__ and (not (dirty and not self._first_operation[1]))):
            dct["firstOperation"] = dictify(self.first_operation)
        if "last_operation" == "type" or (self.last_operation is not self.__undef__ and (not (dirty and not self._last_operation[1]))):
            dct["lastOperation"] = dictify(self.last_operation)
        if "last_updated" == "type" or (self.last_updated is not self.__undef__ and (not (dirty and not self._last_updated[1]))):
            dct["lastUpdated"] = dictify(self.last_updated)
        if "notes" == "type" or (self.notes is not self.__undef__ and (not (dirty and not self._notes[1]) or isinstance(self.notes, list) or belongs_to_parent)):
            dct["notes"] = dictify(self.notes)
        if "properties" == "type" or (self.properties is not self.__undef__ and (not (dirty and not self._properties[1]) or isinstance(self.properties, list) or belongs_to_parent)):
            dct["properties"] = dictify(self.properties, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._active_branch = (self._active_branch[0], True)
        self._first_operation = (self._first_operation[0], True)
        self._last_operation = (self._last_operation[0], True)
        self._last_updated = (self._last_updated[0], True)
        self._notes = (self._notes[0], True)
        self._properties = (self._properties[0], True)

    def is_dirty(self):
        return any([self._active_branch[1], self._first_operation[1], self._last_operation[1], self._last_updated[1], self._notes[1], self._properties[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataLayout):
            return False
        return super(JSDataLayout, self).__eq__(other) and \
               self.active_branch == other.active_branch and \
               self.first_operation == other.first_operation and \
               self.last_operation == other.last_operation and \
               self.last_updated == other.last_updated and \
               self.notes == other.notes and \
               self.properties == other.properties

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def active_branch(self):
        """
        The active branch of the data layout.

        :rtype: ``TEXT_TYPE``
        """
        return self._active_branch[0]

    @active_branch.setter
    def active_branch(self, value):
        self._active_branch = (value, True)

    @property
    def first_operation(self):
        """
        The first JSOperation on this data layout by data time.

        :rtype: ``TEXT_TYPE``
        """
        return self._first_operation[0]

    @first_operation.setter
    def first_operation(self, value):
        self._first_operation = (value, True)

    @property
    def last_operation(self):
        """
        The last JSOperation on this data layout by data time.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_operation[0]

    @last_operation.setter
    def last_operation(self, value):
        self._last_operation = (value, True)

    @property
    def last_updated(self):
        """
        Timestamp of the last update to the application.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_updated[0]

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = (value, True)

    @property
    def notes(self):
        """
        Notes for this data layout.

        :rtype: ``TEXT_TYPE``
        """
        return self._notes[0]

    @notes.setter
    def notes(self, value):
        self._notes = (value, True)

    @property
    def properties(self):
        """
        Key/value pairs used to specify attributes for this data layout.

        :rtype: ``dict``
        """
        return self._properties[0]

    @properties.setter
    def properties(self, value):
        self._properties = (value, True)

