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
#     /delphix-source-environment.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.UserObject import UserObject
from delphixpy.v1_7_1 import common

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

class SourceEnvironment(UserObject):
    """
    *(extends* :py:class:`v1_7_1.web.vo.UserObject` *)* The generic source
    environment schema.
    """
    def __init__(self, undef_enabled=True):
        super(SourceEnvironment, self).__init__()
        self._type = ("SourceEnvironment", True)
        self._description = (self.__undef__, True)
        self._enabled = (self.__undef__, True)
        self._primary_user = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceEnvironment, cls).from_dict(data, dirty, undef_enabled)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, 1024)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._primary_user = (data.get("primaryUser", obj.__undef__), dirty)
        if obj._primary_user[0] is not None and obj._primary_user[0] is not obj.__undef__:
            assert isinstance(obj._primary_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._primary_user[0], type(obj._primary_user[0])))
            common.validate_format(obj._primary_user[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceEnvironment, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]))):
            dct["enabled"] = dictify(self.enabled)
        if "primary_user" == "type" or (self.primary_user is not self.__undef__ and (not (dirty and not self._primary_user[1]) or isinstance(self.primary_user, list) or belongs_to_parent)):
            dct["primaryUser"] = dictify(self.primary_user)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._description = (self._description[0], True)
        self._enabled = (self._enabled[0], True)
        self._primary_user = (self._primary_user[0], True)

    def is_dirty(self):
        return any([self._description[1], self._enabled[1], self._primary_user[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceEnvironment):
            return False
        return super(SourceEnvironment, self).__eq__(other) and \
               self.description == other.description and \
               self.enabled == other.enabled and \
               self.primary_user == other.primary_user

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def description(self):
        """
        The environment description.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def enabled(self):
        """
        Indicates whether the source environment is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def primary_user(self):
        """
        A reference to the primary user for this environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._primary_user[0]

    @primary_user.setter
    def primary_user(self, value):
        self._primary_user = (value, True)

