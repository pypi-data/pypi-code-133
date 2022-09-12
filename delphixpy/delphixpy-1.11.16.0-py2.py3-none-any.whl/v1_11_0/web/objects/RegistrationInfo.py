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
#     /delphix-registration-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.TypedObject import TypedObject
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

class RegistrationInfo(TypedObject):
    """
    *(extends* :py:class:`v1_11_0.web.vo.TypedObject` *)* The information
    required to register the Delphix Engine.
    """
    def __init__(self, undef_enabled=True):
        super(RegistrationInfo, self).__init__()
        self._type = ("RegistrationInfo", True)
        self._uuid = (self.__undef__, True)
        self._code = (self.__undef__, True)
        self._registration_portal_hostname = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RegistrationInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._uuid = (data.get("uuid", obj.__undef__), dirty)
        if obj._uuid[0] is not None and obj._uuid[0] is not obj.__undef__:
            assert isinstance(obj._uuid[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._uuid[0], type(obj._uuid[0])))
            common.validate_format(obj._uuid[0], "None", None, None)
        obj._code = (data.get("code", obj.__undef__), dirty)
        if obj._code[0] is not None and obj._code[0] is not obj.__undef__:
            assert isinstance(obj._code[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._code[0], type(obj._code[0])))
            common.validate_format(obj._code[0], "None", None, None)
        obj._registration_portal_hostname = (data.get("registrationPortalHostname", obj.__undef__), dirty)
        if obj._registration_portal_hostname[0] is not None and obj._registration_portal_hostname[0] is not obj.__undef__:
            assert isinstance(obj._registration_portal_hostname[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._registration_portal_hostname[0], type(obj._registration_portal_hostname[0])))
            common.validate_format(obj._registration_portal_hostname[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RegistrationInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "uuid" == "type" or (self.uuid is not self.__undef__ and (not (dirty and not self._uuid[1]))):
            dct["uuid"] = dictify(self.uuid)
        if "code" == "type" or (self.code is not self.__undef__ and (not (dirty and not self._code[1]))):
            dct["code"] = dictify(self.code)
        if "registration_portal_hostname" == "type" or (self.registration_portal_hostname is not self.__undef__ and (not (dirty and not self._registration_portal_hostname[1]))):
            dct["registrationPortalHostname"] = dictify(self.registration_portal_hostname)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._uuid = (self._uuid[0], True)
        self._code = (self._code[0], True)
        self._registration_portal_hostname = (self._registration_portal_hostname[0], True)

    def is_dirty(self):
        return any([self._uuid[1], self._code[1], self._registration_portal_hostname[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RegistrationInfo):
            return False
        return super(RegistrationInfo, self).__eq__(other) and \
               self.uuid == other.uuid and \
               self.code == other.code and \
               self.registration_portal_hostname == other.registration_portal_hostname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def uuid(self):
        """
        The UUID for this Delphix Engine.

        :rtype: ``TEXT_TYPE``
        """
        return self._uuid[0]

    @uuid.setter
    def uuid(self, value):
        self._uuid = (value, True)

    @property
    def code(self):
        """
        The registration code for this Delphix Engine.

        :rtype: ``TEXT_TYPE``
        """
        return self._code[0]

    @code.setter
    def code(self, value):
        self._code = (value, True)

    @property
    def registration_portal_hostname(self):
        """
        The registration portal hostname.

        :rtype: ``TEXT_TYPE``
        """
        return self._registration_portal_hostname[0]

    @registration_portal_hostname.setter
    def registration_portal_hostname(self, value):
        self._registration_portal_hostname = (value, True)

