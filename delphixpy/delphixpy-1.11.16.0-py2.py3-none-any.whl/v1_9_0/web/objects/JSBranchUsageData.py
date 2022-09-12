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
#     /delphix-js-branch-usage-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_0 import common

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

class JSBranchUsageData(TypedObject):
    """
    *(extends* :py:class:`v1_9_0.web.vo.TypedObject` *)* The space usage
    information for a Jet Stream branch.
    """
    def __init__(self, undef_enabled=True):
        super(JSBranchUsageData, self).__init__()
        self._type = ("JSBranchUsageData", True)
        self._branch = (self.__undef__, True)
        self._data_container = (self.__undef__, True)
        self._unique = (self.__undef__, True)
        self._shared_others = (self.__undef__, True)
        self._shared_self = (self.__undef__, True)

    API_VERSION = "1.9.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSBranchUsageData, cls).from_dict(data, dirty, undef_enabled)
        obj._branch = (data.get("branch", obj.__undef__), dirty)
        if obj._branch[0] is not None and obj._branch[0] is not obj.__undef__:
            assert isinstance(obj._branch[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._branch[0], type(obj._branch[0])))
            common.validate_format(obj._branch[0], "objectReference", None, None)
        obj._data_container = (data.get("dataContainer", obj.__undef__), dirty)
        if obj._data_container[0] is not None and obj._data_container[0] is not obj.__undef__:
            assert isinstance(obj._data_container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_container[0], type(obj._data_container[0])))
            common.validate_format(obj._data_container[0], "None", None, None)
        obj._unique = (data.get("unique", obj.__undef__), dirty)
        if obj._unique[0] is not None and obj._unique[0] is not obj.__undef__:
            assert isinstance(obj._unique[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._unique[0], type(obj._unique[0])))
            common.validate_format(obj._unique[0], "None", None, None)
        obj._shared_others = (data.get("sharedOthers", obj.__undef__), dirty)
        if obj._shared_others[0] is not None and obj._shared_others[0] is not obj.__undef__:
            assert isinstance(obj._shared_others[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._shared_others[0], type(obj._shared_others[0])))
            common.validate_format(obj._shared_others[0], "None", None, None)
        obj._shared_self = (data.get("sharedSelf", obj.__undef__), dirty)
        if obj._shared_self[0] is not None and obj._shared_self[0] is not obj.__undef__:
            assert isinstance(obj._shared_self[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._shared_self[0], type(obj._shared_self[0])))
            common.validate_format(obj._shared_self[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSBranchUsageData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "branch" == "type" or (self.branch is not self.__undef__ and (not (dirty and not self._branch[1]))):
            dct["branch"] = dictify(self.branch)
        if "data_container" == "type" or (self.data_container is not self.__undef__ and (not (dirty and not self._data_container[1]))):
            dct["dataContainer"] = dictify(self.data_container)
        if "unique" == "type" or (self.unique is not self.__undef__ and (not (dirty and not self._unique[1]))):
            dct["unique"] = dictify(self.unique)
        if "shared_others" == "type" or (self.shared_others is not self.__undef__ and (not (dirty and not self._shared_others[1]))):
            dct["sharedOthers"] = dictify(self.shared_others)
        if "shared_self" == "type" or (self.shared_self is not self.__undef__ and (not (dirty and not self._shared_self[1]))):
            dct["sharedSelf"] = dictify(self.shared_self)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._branch = (self._branch[0], True)
        self._data_container = (self._data_container[0], True)
        self._unique = (self._unique[0], True)
        self._shared_others = (self._shared_others[0], True)
        self._shared_self = (self._shared_self[0], True)

    def is_dirty(self):
        return any([self._branch[1], self._data_container[1], self._unique[1], self._shared_others[1], self._shared_self[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSBranchUsageData):
            return False
        return super(JSBranchUsageData, self).__eq__(other) and \
               self.branch == other.branch and \
               self.data_container == other.data_container and \
               self.unique == other.unique and \
               self.shared_others == other.shared_others and \
               self.shared_self == other.shared_self

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def branch(self):
        """
        The Jet Stream branch that this usage information is for.

        :rtype: ``TEXT_TYPE``
        """
        return self._branch[0]

    @branch.setter
    def branch(self, value):
        self._branch = (value, True)

    @property
    def data_container(self):
        """
        The name of the data container that this branch resides on.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_container[0]

    @data_container.setter
    def data_container(self, value):
        self._data_container = (value, True)

    @property
    def unique(self):
        """
        The amount of space that will be freed if this branch is deleted.

        :rtype: ``float``
        """
        return self._unique[0]

    @unique.setter
    def unique(self, value):
        self._unique = (value, True)

    @property
    def shared_others(self):
        """
        The amount of space that cannot be freed on the parent data template
        (or sibling data containers) because it is also being referenced by
        this branch due to restore or create branch operations.

        :rtype: ``float``
        """
        return self._shared_others[0]

    @shared_others.setter
    def shared_others(self, value):
        self._shared_others = (value, True)

    @property
    def shared_self(self):
        """
        The amount of space that cannot be freed up on this branch because it
        is also being referenced by sibling data containers due to restore or
        create branch operations.

        :rtype: ``float``
        """
        return self._shared_self[0]

    @shared_self.setter
    def shared_self(self, value):
        self._shared_self = (value, True)

