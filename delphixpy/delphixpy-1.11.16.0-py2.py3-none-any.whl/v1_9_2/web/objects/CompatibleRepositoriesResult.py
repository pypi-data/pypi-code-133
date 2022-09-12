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
#     /delphix-compatible-repositories-result.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_2 import factory
from delphixpy.v1_9_2 import common

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

class CompatibleRepositoriesResult(TypedObject):
    """
    *(extends* :py:class:`v1_9_2.web.vo.TypedObject` *)* Result of a compatible
    repositories request.
    """
    def __init__(self, undef_enabled=True):
        super(CompatibleRepositoriesResult, self).__init__()
        self._type = ("CompatibleRepositoriesResult", True)
        self._repositories = (self.__undef__, True)
        self._criteria = (self.__undef__, True)

    API_VERSION = "1.9.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CompatibleRepositoriesResult, cls).from_dict(data, dirty, undef_enabled)
        if "repositories" not in data:
            raise ValueError("Missing required property \"repositories\".")
        obj._repositories = []
        for item in data.get("repositories") or []:
            obj._repositories.append(factory.create_object(item))
            factory.validate_type(obj._repositories[-1], "SourceRepository")
        obj._repositories = (obj._repositories, dirty)
        if "criteria" not in data:
            raise ValueError("Missing required property \"criteria\".")
        if "criteria" in data and data["criteria"] is not None:
            obj._criteria = (factory.create_object(data["criteria"], "CompatibilityCriteria"), dirty)
            factory.validate_type(obj._criteria[0], "CompatibilityCriteria")
        else:
            obj._criteria = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CompatibleRepositoriesResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "repositories" == "type" or (self.repositories is not self.__undef__ and (not (dirty and not self._repositories[1]) or isinstance(self.repositories, list) or belongs_to_parent)):
            dct["repositories"] = dictify(self.repositories, prop_is_list_or_vo=True)
        if "criteria" == "type" or (self.criteria is not self.__undef__ and (not (dirty and not self._criteria[1]) or isinstance(self.criteria, list) or belongs_to_parent)):
            dct["criteria"] = dictify(self.criteria, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._repositories = (self._repositories[0], True)
        self._criteria = (self._criteria[0], True)

    def is_dirty(self):
        return any([self._repositories[1], self._criteria[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CompatibleRepositoriesResult):
            return False
        return super(CompatibleRepositoriesResult, self).__eq__(other) and \
               self.repositories == other.repositories and \
               self.criteria == other.criteria

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def repositories(self):
        """
        The list of compatible repositories.

        :rtype: ``list`` of :py:class:`v1_9_2.web.vo.SourceRepository`
        """
        return self._repositories[0]

    @repositories.setter
    def repositories(self, value):
        self._repositories = (value, True)

    @property
    def criteria(self):
        """
        The criteria matched to select compatible repositories.

        :rtype: :py:class:`v1_9_2.web.vo.CompatibilityCriteria`
        """
        return self._criteria[0]

    @criteria.setter
    def criteria(self, value):
        self._criteria = (value, True)

