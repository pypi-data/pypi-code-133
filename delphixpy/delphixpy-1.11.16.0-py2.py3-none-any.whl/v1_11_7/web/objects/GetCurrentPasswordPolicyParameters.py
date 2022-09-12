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
#     /delphix-get-current-password-policy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_7 import common

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

class GetCurrentPasswordPolicyParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_7.web.vo.TypedObject` *)* The parameters to use
    as input when getting the currently active password policy.
    """
    def __init__(self, undef_enabled=True):
        super(GetCurrentPasswordPolicyParameters, self).__init__()
        self._type = ("GetCurrentPasswordPolicyParameters", True)
        self._user_type = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(GetCurrentPasswordPolicyParameters, cls).from_dict(data, dirty, undef_enabled)
        if "userType" not in data:
            raise ValueError("Missing required property \"userType\".")
        obj._user_type = (data.get("userType", obj.__undef__), dirty)
        if obj._user_type[0] is not None and obj._user_type[0] is not obj.__undef__:
            assert isinstance(obj._user_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user_type[0], type(obj._user_type[0])))
            assert obj._user_type[0] in ['SYSTEM', 'DOMAIN'], "Expected enum ['SYSTEM', 'DOMAIN'] but got %s" % obj._user_type[0]
            common.validate_format(obj._user_type[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(GetCurrentPasswordPolicyParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "user_type" == "type" or (self.user_type is not self.__undef__ and (not (dirty and not self._user_type[1]) or isinstance(self.user_type, list) or belongs_to_parent)):
            dct["userType"] = dictify(self.user_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._user_type = (self._user_type[0], True)

    def is_dirty(self):
        return any([self._user_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, GetCurrentPasswordPolicyParameters):
            return False
        return super(GetCurrentPasswordPolicyParameters, self).__eq__(other) and \
               self.user_type == other.user_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def user_type(self):
        """
        Type of user. *(permitted values: SYSTEM, DOMAIN)*

        :rtype: ``TEXT_TYPE``
        """
        return self._user_type[0]

    @user_type.setter
    def user_type(self, value):
        self._user_type = (value, True)

