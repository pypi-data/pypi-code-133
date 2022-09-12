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
#     /delphix-user-auth-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_3 import factory
from delphixpy.v1_10_3 import common

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

class UserAuthInfo(TypedObject):
    """
    *(extends* :py:class:`v1_10_3.web.vo.TypedObject` *)* Summary authorization
    information about the current user.
    """
    def __init__(self, undef_enabled=True):
        super(UserAuthInfo, self).__init__()
        self._type = ("UserAuthInfo", True)
        self._user = (self.__undef__, True)
        self._owner_role = (self.__undef__, True)
        self._provisioner_role = (self.__undef__, True)
        self._jet_stream_user_role = (self.__undef__, True)
        self._authorizations = (self.__undef__, True)

    API_VERSION = "1.10.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(UserAuthInfo, cls).from_dict(data, dirty, undef_enabled)
        if "user" in data and data["user"] is not None:
            obj._user = (factory.create_object(data["user"], "User"), dirty)
            factory.validate_type(obj._user[0], "User")
        else:
            obj._user = (obj.__undef__, dirty)
        obj._owner_role = (data.get("ownerRole", obj.__undef__), dirty)
        if obj._owner_role[0] is not None and obj._owner_role[0] is not obj.__undef__:
            assert isinstance(obj._owner_role[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._owner_role[0], type(obj._owner_role[0])))
            common.validate_format(obj._owner_role[0], "objectReference", None, None)
        obj._provisioner_role = (data.get("provisionerRole", obj.__undef__), dirty)
        if obj._provisioner_role[0] is not None and obj._provisioner_role[0] is not obj.__undef__:
            assert isinstance(obj._provisioner_role[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._provisioner_role[0], type(obj._provisioner_role[0])))
            common.validate_format(obj._provisioner_role[0], "objectReference", None, None)
        obj._jet_stream_user_role = (data.get("jetStreamUserRole", obj.__undef__), dirty)
        if obj._jet_stream_user_role[0] is not None and obj._jet_stream_user_role[0] is not obj.__undef__:
            assert isinstance(obj._jet_stream_user_role[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._jet_stream_user_role[0], type(obj._jet_stream_user_role[0])))
            common.validate_format(obj._jet_stream_user_role[0], "objectReference", None, None)
        obj._authorizations = []
        for item in data.get("authorizations") or []:
            obj._authorizations.append(factory.create_object(item))
            factory.validate_type(obj._authorizations[-1], "Authorization")
        obj._authorizations = (obj._authorizations, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(UserAuthInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]))):
            dct["user"] = dictify(self.user)
        if "owner_role" == "type" or (self.owner_role is not self.__undef__ and (not (dirty and not self._owner_role[1]))):
            dct["ownerRole"] = dictify(self.owner_role)
        if "provisioner_role" == "type" or (self.provisioner_role is not self.__undef__ and (not (dirty and not self._provisioner_role[1]))):
            dct["provisionerRole"] = dictify(self.provisioner_role)
        if "jet_stream_user_role" == "type" or (self.jet_stream_user_role is not self.__undef__ and (not (dirty and not self._jet_stream_user_role[1]))):
            dct["jetStreamUserRole"] = dictify(self.jet_stream_user_role)
        if "authorizations" == "type" or (self.authorizations is not self.__undef__ and (not (dirty and not self._authorizations[1]))):
            dct["authorizations"] = dictify(self.authorizations)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._user = (self._user[0], True)
        self._owner_role = (self._owner_role[0], True)
        self._provisioner_role = (self._provisioner_role[0], True)
        self._jet_stream_user_role = (self._jet_stream_user_role[0], True)
        self._authorizations = (self._authorizations[0], True)

    def is_dirty(self):
        return any([self._user[1], self._owner_role[1], self._provisioner_role[1], self._jet_stream_user_role[1], self._authorizations[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, UserAuthInfo):
            return False
        return super(UserAuthInfo, self).__eq__(other) and \
               self.user == other.user and \
               self.owner_role == other.owner_role and \
               self.provisioner_role == other.provisioner_role and \
               self.jet_stream_user_role == other.jet_stream_user_role and \
               self.authorizations == other.authorizations

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def user(self):
        """
        The currently logged in user.

        :rtype: :py:class:`v1_10_3.web.vo.User`
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def owner_role(self):
        """
        A reference to the system-defined owner role.

        :rtype: ``TEXT_TYPE``
        """
        return self._owner_role[0]

    @owner_role.setter
    def owner_role(self, value):
        self._owner_role = (value, True)

    @property
    def provisioner_role(self):
        """
        A reference to the system-defined provisioner role.

        :rtype: ``TEXT_TYPE``
        """
        return self._provisioner_role[0]

    @provisioner_role.setter
    def provisioner_role(self, value):
        self._provisioner_role = (value, True)

    @property
    def jet_stream_user_role(self):
        """
        A reference to the system-defined Self-Service user role.

        :rtype: ``TEXT_TYPE``
        """
        return self._jet_stream_user_role[0]

    @jet_stream_user_role.setter
    def jet_stream_user_role(self, value):
        self._jet_stream_user_role = (value, True)

    @property
    def authorizations(self):
        """
        The list of authorizations granted to the current user.

        :rtype: ``list`` of :py:class:`v1_10_3.web.vo.Authorization`
        """
        return self._authorizations[0]

    @authorizations.setter
    def authorizations(self, value):
        self._authorizations = (value, True)

