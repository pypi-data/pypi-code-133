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
#     /delphix-checklist-item-detail.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_2.web.objects.ChecklistItem import ChecklistItem
from delphixpy.v1_4_2 import common

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

class ChecklistItemDetail(ChecklistItem):
    """
    *(extends* :py:class:`v1_4_2.web.vo.ChecklistItem` *)* Fields to indicate
    detailed status for a specific checklist item.
    """
    def __init__(self, undef_enabled=True):
        super(ChecklistItemDetail, self).__init__()
        self._type = ("ChecklistItemDetail", True)
        self._description = (self.__undef__, True)
        self._message = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._status = (self.__undef__, True)

    API_VERSION = "1.4.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ChecklistItemDetail, cls).from_dict(data, dirty, undef_enabled)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, None)
        obj._message = (data.get("message", obj.__undef__), dirty)
        if obj._message[0] is not None and obj._message[0] is not obj.__undef__:
            assert isinstance(obj._message[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message[0], type(obj._message[0])))
            common.validate_format(obj._message[0], "None", None, None)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            assert obj._status[0] in ['SUCCESS', 'WARNING', 'ERROR'], "Expected enum ['SUCCESS', 'WARNING', 'ERROR'] but got %s" % obj._status[0]
            common.validate_format(obj._status[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ChecklistItemDetail, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]))):
            dct["description"] = dictify(self.description)
        if "message" == "type" or (self.message is not self.__undef__ and (not (dirty and not self._message[1]))):
            dct["message"] = dictify(self.message)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]))):
            dct["name"] = dictify(self.name)
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._description = (self._description[0], True)
        self._message = (self._message[0], True)
        self._name = (self._name[0], True)
        self._status = (self._status[0], True)

    def is_dirty(self):
        return any([self._description[1], self._message[1], self._name[1], self._status[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ChecklistItemDetail):
            return False
        return super(ChecklistItemDetail, self).__eq__(other) and \
               self.description == other.description and \
               self.message == other.message and \
               self.name == other.name and \
               self.status == other.status

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def description(self):
        """
        Description of this status item.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def message(self):
        """
        Status message, if applicable.

        :rtype: ``TEXT_TYPE``
        """
        return self._message[0]

    @message.setter
    def message(self, value):
        self._message = (value, True)

    @property
    def name(self):
        """
        The status item name.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def status(self):
        """
        Status of this item. *(permitted values: SUCCESS, WARNING, ERROR)*

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

    @status.setter
    def status(self, value):
        self._status = (value, True)

