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
#     /delphix-authorization.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.ReadonlyNamedUserObject import ReadonlyNamedUserObject
from delphixpy.v1_11_0 import common

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

class Authorization(ReadonlyNamedUserObject):
    """
    *(extends* :py:class:`v1_11_0.web.vo.ReadonlyNamedUserObject` *)* Describes
    a role as applied to a user on an object.
    """
    def __init__(self, undef_enabled=True):
        super(Authorization, self).__init__()
        self._type = ("Authorization", True)
        self._user = (self.__undef__, True)
        self._role = (self.__undef__, True)
        self._target = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Authorization, cls).from_dict(data, dirty, undef_enabled)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "objectReference", None, None)
        obj._role = (data.get("role", obj.__undef__), dirty)
        if obj._role[0] is not None and obj._role[0] is not obj.__undef__:
            assert isinstance(obj._role[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._role[0], type(obj._role[0])))
            common.validate_format(obj._role[0], "objectReference", None, None)
        obj._target = (data.get("target", obj.__undef__), dirty)
        if obj._target[0] is not None and obj._target[0] is not obj.__undef__:
            assert isinstance(obj._target[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target[0], type(obj._target[0])))
            common.validate_format(obj._target[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Authorization, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        if "role" == "type" or (self.role is not self.__undef__ and (not (dirty and not self._role[1]) or isinstance(self.role, list) or belongs_to_parent)):
            dct["role"] = dictify(self.role)
        if "target" == "type" or (self.target is not self.__undef__ and (not (dirty and not self._target[1]) or isinstance(self.target, list) or belongs_to_parent)):
            dct["target"] = dictify(self.target)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._user = (self._user[0], True)
        self._role = (self._role[0], True)
        self._target = (self._target[0], True)

    def is_dirty(self):
        return any([self._user[1], self._role[1], self._target[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Authorization):
            return False
        return super(Authorization, self).__eq__(other) and \
               self.user == other.user and \
               self.role == other.role and \
               self.target == other.target

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def user(self):
        """
        Reference to the user that the authorization applies to.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def role(self):
        """
        Applied role.

        :rtype: ``TEXT_TYPE``
        """
        return self._role[0]

    @role.setter
    def role(self, value):
        self._role = (value, True)

    @property
    def target(self):
        """
        Reference to the object that the authorization applies to.

        :rtype: ``TEXT_TYPE``
        """
        return self._target[0]

    @target.setter
    def target(self, value):
        self._target = (value, True)

