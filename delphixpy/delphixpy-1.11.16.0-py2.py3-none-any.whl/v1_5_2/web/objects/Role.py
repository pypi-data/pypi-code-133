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
#     /delphix-role.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_2.web.objects.UserObject import UserObject
from delphixpy.v1_5_2 import common

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

class Role(UserObject):
    """
    *(extends* :py:class:`v1_5_2.web.vo.UserObject` *)* Describes a role as
    applied to a user on an object.
    """
    def __init__(self, undef_enabled=True):
        super(Role, self).__init__()
        self._type = ("Role", True)
        self._immutable = (self.__undef__, True)
        self._permissions = (self.__undef__, True)

    API_VERSION = "1.5.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Role, cls).from_dict(data, dirty, undef_enabled)
        obj._immutable = (data.get("immutable", obj.__undef__), dirty)
        if obj._immutable[0] is not None and obj._immutable[0] is not obj.__undef__:
            assert isinstance(obj._immutable[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._immutable[0], type(obj._immutable[0])))
            common.validate_format(obj._immutable[0], "None", None, None)
        obj._permissions = []
        for item in data.get("permissions") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._permissions.append(item)
        obj._permissions = (obj._permissions, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Role, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "immutable" == "type" or (self.immutable is not self.__undef__ and (not (dirty and not self._immutable[1]))):
            dct["immutable"] = dictify(self.immutable)
        if "permissions" == "type" or (self.permissions is not self.__undef__ and (not (dirty and not self._permissions[1]) or isinstance(self.permissions, list) or belongs_to_parent)):
            dct["permissions"] = dictify(self.permissions, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._immutable = (self._immutable[0], True)
        self._permissions = (self._permissions[0], True)

    def is_dirty(self):
        return any([self._immutable[1], self._permissions[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Role):
            return False
        return super(Role, self).__eq__(other) and \
               self.immutable == other.immutable and \
               self.permissions == other.permissions

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def immutable(self):
        """
        Determines if the role can be modified or not. Some roles are shipped
        with the Delphix Engine and cannot be changed.

        :rtype: ``bool``
        """
        return self._immutable[0]

    @immutable.setter
    def immutable(self, value):
        self._immutable = (value, True)

    @property
    def permissions(self):
        """
        List of permissions contained in the role.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._permissions[0]

    @permissions.setter
    def permissions(self, value):
        self._permissions = (value, True)

