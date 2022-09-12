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
#     /delphix-security-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_1 import common

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

class SecurityConfig(TypedObject):
    """
    *(extends* :py:class:`v1_6_1.web.vo.TypedObject` *)* System wide security
    configuration.
    """
    def __init__(self, undef_enabled=True):
        super(SecurityConfig, self).__init__()
        self._type = ("SecurityConfig", True)
        self._banner = (self.__undef__, True)
        self._boot_password = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SecurityConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._banner = (data.get("banner", obj.__undef__), dirty)
        if obj._banner[0] is not None and obj._banner[0] is not obj.__undef__:
            assert isinstance(obj._banner[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._banner[0], type(obj._banner[0])))
            common.validate_format(obj._banner[0], "None", None, None)
        obj._boot_password = (data.get("bootPassword", obj.__undef__), dirty)
        if obj._boot_password[0] is not None and obj._boot_password[0] is not obj.__undef__:
            assert isinstance(obj._boot_password[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._boot_password[0], type(obj._boot_password[0])))
            common.validate_format(obj._boot_password[0], "password", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SecurityConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "banner" == "type" or (self.banner is not self.__undef__ and (not (dirty and not self._banner[1]) or isinstance(self.banner, list) or belongs_to_parent)):
            dct["banner"] = dictify(self.banner)
        if "boot_password" == "type" or (self.boot_password is not self.__undef__ and (not (dirty and not self._boot_password[1]) or isinstance(self.boot_password, list) or belongs_to_parent)):
            dct["bootPassword"] = dictify(self.boot_password)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._banner = (self._banner[0], True)
        self._boot_password = (self._boot_password[0], True)

    def is_dirty(self):
        return any([self._banner[1], self._boot_password[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SecurityConfig):
            return False
        return super(SecurityConfig, self).__eq__(other) and \
               self.banner == other.banner and \
               self.boot_password == other.boot_password

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def banner(self):
        """
        Banner displayed prior to login.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._banner[0]

    @banner.setter
    def banner(self, value):
        self._banner = (value, True)

    @property
    def boot_password(self):
        """
        Password controlling access to bootloader configuration changes during
        startup.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._boot_password[0]

    @boot_password.setter
    def boot_password(self, value):
        self._boot_password = (value, True)

