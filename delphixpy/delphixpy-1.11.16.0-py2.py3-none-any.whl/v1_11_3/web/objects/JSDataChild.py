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
#     /delphix-js-data-child.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_3 import common

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

class JSDataChild(TypedObject):
    """
    *(extends* :py:class:`v1_11_3.web.vo.TypedObject` *)* A branch with data
    from a specific bookmark or PIT (point in time).
    """
    def __init__(self, undef_enabled=True):
        super(JSDataChild, self).__init__()
        self._type = ("JSDataChild", True)
        self._branch = (self.__undef__, True)
        self._branch_name = (self.__undef__, True)
        self._container_name = (self.__undef__, True)
        self._operation = (self.__undef__, True)
        self._user_name = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataChild, cls).from_dict(data, dirty, undef_enabled)
        obj._branch = (data.get("branch", obj.__undef__), dirty)
        if obj._branch[0] is not None and obj._branch[0] is not obj.__undef__:
            assert isinstance(obj._branch[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._branch[0], type(obj._branch[0])))
            common.validate_format(obj._branch[0], "objectReference", None, None)
        obj._branch_name = (data.get("branchName", obj.__undef__), dirty)
        if obj._branch_name[0] is not None and obj._branch_name[0] is not obj.__undef__:
            assert isinstance(obj._branch_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._branch_name[0], type(obj._branch_name[0])))
            common.validate_format(obj._branch_name[0], "None", None, 256)
        obj._container_name = (data.get("containerName", obj.__undef__), dirty)
        if obj._container_name[0] is not None and obj._container_name[0] is not obj.__undef__:
            assert isinstance(obj._container_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container_name[0], type(obj._container_name[0])))
            common.validate_format(obj._container_name[0], "None", None, 256)
        obj._operation = (data.get("operation", obj.__undef__), dirty)
        if obj._operation[0] is not None and obj._operation[0] is not obj.__undef__:
            assert isinstance(obj._operation[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._operation[0], type(obj._operation[0])))
            assert obj._operation[0] in ['REFRESH', 'RESTORE', 'CREATE_BRANCH', 'RESET'], "Expected enum ['REFRESH', 'RESTORE', 'CREATE_BRANCH', 'RESET'] but got %s" % obj._operation[0]
            common.validate_format(obj._operation[0], "None", None, None)
        obj._user_name = (data.get("userName", obj.__undef__), dirty)
        if obj._user_name[0] is not None and obj._user_name[0] is not obj.__undef__:
            assert isinstance(obj._user_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user_name[0], type(obj._user_name[0])))
            common.validate_format(obj._user_name[0], "None", None, 256)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataChild, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "branch" == "type" or (self.branch is not self.__undef__ and (not (dirty and not self._branch[1]))):
            dct["branch"] = dictify(self.branch)
        if "branch_name" == "type" or (self.branch_name is not self.__undef__ and (not (dirty and not self._branch_name[1]))):
            dct["branchName"] = dictify(self.branch_name)
        if "container_name" == "type" or (self.container_name is not self.__undef__ and (not (dirty and not self._container_name[1]))):
            dct["containerName"] = dictify(self.container_name)
        if "operation" == "type" or (self.operation is not self.__undef__ and (not (dirty and not self._operation[1]))):
            dct["operation"] = dictify(self.operation)
        if "user_name" == "type" or (self.user_name is not self.__undef__ and (not (dirty and not self._user_name[1]))):
            dct["userName"] = dictify(self.user_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._branch = (self._branch[0], True)
        self._branch_name = (self._branch_name[0], True)
        self._container_name = (self._container_name[0], True)
        self._operation = (self._operation[0], True)
        self._user_name = (self._user_name[0], True)

    def is_dirty(self):
        return any([self._branch[1], self._branch_name[1], self._container_name[1], self._operation[1], self._user_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataChild):
            return False
        return super(JSDataChild, self).__eq__(other) and \
               self.branch == other.branch and \
               self.branch_name == other.branch_name and \
               self.container_name == other.container_name and \
               self.operation == other.operation and \
               self.user_name == other.user_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def branch(self):
        """
        Reference to the branch. This will be null if the user does not have
        permission to see it.

        :rtype: ``TEXT_TYPE``
        """
        return self._branch[0]

    @branch.setter
    def branch(self, value):
        self._branch = (value, True)

    @property
    def branch_name(self):
        """
        The name of the branch.

        :rtype: ``TEXT_TYPE``
        """
        return self._branch_name[0]

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = (value, True)

    @property
    def container_name(self):
        """
        The name of the container.

        :rtype: ``TEXT_TYPE``
        """
        return self._container_name[0]

    @container_name.setter
    def container_name(self, value):
        self._container_name = (value, True)

    @property
    def operation(self):
        """
        The operation performed. *(permitted values: REFRESH, RESTORE,
        CREATE_BRANCH, RESET)*

        :rtype: ``TEXT_TYPE``
        """
        return self._operation[0]

    @operation.setter
    def operation(self, value):
        self._operation = (value, True)

    @property
    def user_name(self):
        """
        The username of the owner of the branch. This will be null if there is
        no owner.

        :rtype: ``TEXT_TYPE``
        """
        return self._user_name[0]

    @user_name.setter
    def user_name(self, value):
        self._user_name = (value, True)

