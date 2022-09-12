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
#     /delphix-deletion-dependency-prerequisite.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_12.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_12 import common

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

class DeletionDependencyPrerequisite(TypedObject):
    """
    *(extends* :py:class:`v1_11_12.web.vo.TypedObject` *)* The prerequisite
    operation that must be completed before deleting a dependency object.
    """
    def __init__(self, undef_enabled=True):
        super(DeletionDependencyPrerequisite, self).__init__()
        self._type = ("DeletionDependencyPrerequisite", True)
        self._target_type = (self.__undef__, True)
        self._target_reference = (self.__undef__, True)
        self._operation_type = (self.__undef__, True)
        self._namespace_name = (self.__undef__, True)
        self._display_name = (self.__undef__, True)
        self._locked = (self.__undef__, True)

    API_VERSION = "1.11.12"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DeletionDependencyPrerequisite, cls).from_dict(data, dirty, undef_enabled)
        if "targetType" not in data:
            raise ValueError("Missing required property \"targetType\".")
        obj._target_type = (data.get("targetType", obj.__undef__), dirty)
        if obj._target_type[0] is not None and obj._target_type[0] is not obj.__undef__:
            assert isinstance(obj._target_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_type[0], type(obj._target_type[0])))
            assert obj._target_type[0] in ['Container', 'TimeflowSnapshot', 'JSDataContainer', 'JSDataTemplate'], "Expected enum ['Container', 'TimeflowSnapshot', 'JSDataContainer', 'JSDataTemplate'] but got %s" % obj._target_type[0]
            common.validate_format(obj._target_type[0], "None", None, None)
        if "targetReference" not in data:
            raise ValueError("Missing required property \"targetReference\".")
        obj._target_reference = (data.get("targetReference", obj.__undef__), dirty)
        if obj._target_reference[0] is not None and obj._target_reference[0] is not obj.__undef__:
            assert isinstance(obj._target_reference[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_reference[0], type(obj._target_reference[0])))
            common.validate_format(obj._target_reference[0], "objectReference", None, None)
        if "operationType" not in data:
            raise ValueError("Missing required property \"operationType\".")
        obj._operation_type = (data.get("operationType", obj.__undef__), dirty)
        if obj._operation_type[0] is not None and obj._operation_type[0] is not obj.__undef__:
            assert isinstance(obj._operation_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._operation_type[0], type(obj._operation_type[0])))
            assert obj._operation_type[0] in ['REFRESH', 'REMOVE_KEEP_FOR', 'TAKE_SNAPSHOT'], "Expected enum ['REFRESH', 'REMOVE_KEEP_FOR', 'TAKE_SNAPSHOT'] but got %s" % obj._operation_type[0]
            common.validate_format(obj._operation_type[0], "None", None, None)
        obj._namespace_name = (data.get("namespaceName", obj.__undef__), dirty)
        if obj._namespace_name[0] is not None and obj._namespace_name[0] is not obj.__undef__:
            assert isinstance(obj._namespace_name[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._namespace_name[0], type(obj._namespace_name[0])))
            common.validate_format(obj._namespace_name[0], "None", None, None)
        obj._display_name = (data.get("displayName", obj.__undef__), dirty)
        if obj._display_name[0] is not None and obj._display_name[0] is not obj.__undef__:
            assert isinstance(obj._display_name[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._display_name[0], type(obj._display_name[0])))
            common.validate_format(obj._display_name[0], "None", None, None)
        obj._locked = (data.get("locked", obj.__undef__), dirty)
        if obj._locked[0] is not None and obj._locked[0] is not obj.__undef__:
            assert isinstance(obj._locked[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._locked[0], type(obj._locked[0])))
            common.validate_format(obj._locked[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DeletionDependencyPrerequisite, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "target_type" == "type" or (self.target_type is not self.__undef__ and (not (dirty and not self._target_type[1]) or isinstance(self.target_type, list) or belongs_to_parent)):
            dct["targetType"] = dictify(self.target_type)
        if "target_reference" == "type" or (self.target_reference is not self.__undef__ and (not (dirty and not self._target_reference[1]) or isinstance(self.target_reference, list) or belongs_to_parent)):
            dct["targetReference"] = dictify(self.target_reference)
        if "operation_type" == "type" or (self.operation_type is not self.__undef__ and (not (dirty and not self._operation_type[1]) or isinstance(self.operation_type, list) or belongs_to_parent)):
            dct["operationType"] = dictify(self.operation_type)
        if "namespace_name" == "type" or (self.namespace_name is not self.__undef__ and (not (dirty and not self._namespace_name[1]))):
            dct["namespaceName"] = dictify(self.namespace_name)
        if "display_name" == "type" or (self.display_name is not self.__undef__ and (not (dirty and not self._display_name[1]))):
            dct["displayName"] = dictify(self.display_name)
        if "locked" == "type" or (self.locked is not self.__undef__ and (not (dirty and not self._locked[1]))):
            dct["locked"] = dictify(self.locked)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._target_type = (self._target_type[0], True)
        self._target_reference = (self._target_reference[0], True)
        self._operation_type = (self._operation_type[0], True)
        self._namespace_name = (self._namespace_name[0], True)
        self._display_name = (self._display_name[0], True)
        self._locked = (self._locked[0], True)

    def is_dirty(self):
        return any([self._target_type[1], self._target_reference[1], self._operation_type[1], self._namespace_name[1], self._display_name[1], self._locked[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DeletionDependencyPrerequisite):
            return False
        return super(DeletionDependencyPrerequisite, self).__eq__(other) and \
               self.target_type == other.target_type and \
               self.target_reference == other.target_reference and \
               self.operation_type == other.operation_type and \
               self.namespace_name == other.namespace_name and \
               self.display_name == other.display_name and \
               self.locked == other.locked

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def target_type(self):
        """
        The type of the object that the prerequisite operation must perform on.
        *(permitted values: Container, TimeflowSnapshot, JSDataContainer,
        JSDataTemplate)*

        :rtype: ``TEXT_TYPE``
        """
        return self._target_type[0]

    @target_type.setter
    def target_type(self, value):
        self._target_type = (value, True)

    @property
    def target_reference(self):
        """
        The reference of the object that prerequisite operation must perform
        on.

        :rtype: ``TEXT_TYPE``
        """
        return self._target_reference[0]

    @target_reference.setter
    def target_reference(self, value):
        self._target_reference = (value, True)

    @property
    def operation_type(self):
        """
        The type of the prerequisite operation. *(permitted values: REFRESH,
        REMOVE_KEEP_FOR, TAKE_SNAPSHOT)*

        :rtype: ``TEXT_TYPE``
        """
        return self._operation_type[0]

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = (value, True)

    @property
    def namespace_name(self):
        """
        The name of the Namespace this object belongs to.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._namespace_name[0]

    @namespace_name.setter
    def namespace_name(self, value):
        self._namespace_name = (value, True)

    @property
    def display_name(self):
        """
        The user-facing display name of the dependency prerequisite object.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._display_name[0]

    @display_name.setter
    def display_name(self, value):
        self._display_name = (value, True)

    @property
    def locked(self):
        """
        Whether this object is locked. Set it to true to skip this prerequisite
        operation.

        :rtype: ``bool``
        """
        return self._locked[0]

    @locked.setter
    def locked(self, value):
        self._locked = (value, True)

