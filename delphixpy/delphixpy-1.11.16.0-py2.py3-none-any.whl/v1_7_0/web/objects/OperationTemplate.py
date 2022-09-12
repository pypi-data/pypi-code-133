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
#     /delphix-operation-template.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_0.web.objects.NamedUserObject import NamedUserObject
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

class OperationTemplate(NamedUserObject):
    """
    *(extends* :py:class:`v1_7_0.web.vo.NamedUserObject` *)* Template for
    commonly used operations.
    """
    def __init__(self, undef_enabled=True):
        super(OperationTemplate, self).__init__()
        self._type = ("OperationTemplate", True)
        self._description = (self.__undef__, True)
        self._last_updated = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._operation = (self.__undef__, True)

    API_VERSION = "1.7.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OperationTemplate, cls).from_dict(data, dirty, undef_enabled)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, None)
        obj._last_updated = (data.get("lastUpdated", obj.__undef__), dirty)
        if obj._last_updated[0] is not None and obj._last_updated[0] is not obj.__undef__:
            assert isinstance(obj._last_updated[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_updated[0], type(obj._last_updated[0])))
            common.validate_format(obj._last_updated[0], "date", None, None)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", 1, None)
        if "operation" in data and data["operation"] is not None:
            obj._operation = (factory.create_object(data["operation"], "SourceOperation"), dirty)
            factory.validate_type(obj._operation[0], "SourceOperation")
        else:
            obj._operation = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OperationTemplate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "last_updated" == "type" or (self.last_updated is not self.__undef__ and (not (dirty and not self._last_updated[1]))):
            dct["lastUpdated"] = dictify(self.last_updated)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "operation" == "type" or (self.operation is not self.__undef__ and (not (dirty and not self._operation[1]) or isinstance(self.operation, list) or belongs_to_parent)):
            dct["operation"] = dictify(self.operation, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._description = (self._description[0], True)
        self._last_updated = (self._last_updated[0], True)
        self._name = (self._name[0], True)
        self._operation = (self._operation[0], True)

    def is_dirty(self):
        return any([self._description[1], self._last_updated[1], self._name[1], self._operation[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OperationTemplate):
            return False
        return super(OperationTemplate, self).__eq__(other) and \
               self.description == other.description and \
               self.last_updated == other.last_updated and \
               self.name == other.name and \
               self.operation == other.operation

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def description(self):
        """
        User provided description for this template.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def last_updated(self):
        """
        Most recently modified time.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_updated[0]

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = (value, True)

    @property
    def name(self):
        """
        The name clients should use when setting the parameter's value.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def operation(self):
        """
        Template contents.

        :rtype: :py:class:`v1_7_0.web.vo.SourceOperation`
        """
        return self._operation[0]

    @operation.setter
    def operation(self, value):
        self._operation = (value, True)

