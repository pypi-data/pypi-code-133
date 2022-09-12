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
#     /delphix-permission.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.ReadonlyNamedUserObject import ReadonlyNamedUserObject
from delphixpy.v1_11_11 import common

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

class Permission(ReadonlyNamedUserObject):
    """
    *(extends* :py:class:`v1_11_11.web.vo.ReadonlyNamedUserObject` *)*
    Describes a permission to perform an operation on an object in the Delphix
    Engine.
    """
    def __init__(self, undef_enabled=True):
        super(Permission, self).__init__()
        self._type = ("Permission", True)
        self._action_type = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Permission, cls).from_dict(data, dirty, undef_enabled)
        obj._action_type = (data.get("actionType", obj.__undef__), dirty)
        if obj._action_type[0] is not None and obj._action_type[0] is not obj.__undef__:
            assert isinstance(obj._action_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._action_type[0], type(obj._action_type[0])))
            common.validate_format(obj._action_type[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Permission, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "action_type" == "type" or (self.action_type is not self.__undef__ and (not (dirty and not self._action_type[1]))):
            dct["actionType"] = dictify(self.action_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._action_type = (self._action_type[0], True)

    def is_dirty(self):
        return any([self._action_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Permission):
            return False
        return super(Permission, self).__eq__(other) and \
               self.action_type == other.action_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def action_type(self):
        """
        Name of the action governed by the permission.

        :rtype: ``TEXT_TYPE``
        """
        return self._action_type[0]

    @action_type.setter
    def action_type(self, value):
        self._action_type = (value, True)

