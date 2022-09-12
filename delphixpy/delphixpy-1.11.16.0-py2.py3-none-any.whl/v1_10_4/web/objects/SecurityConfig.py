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

from delphixpy.v1_10_4.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_4 import common

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
    *(extends* :py:class:`v1_10_4.web.vo.TypedObject` *)* System wide security
    configuration.
    """
    def __init__(self, undef_enabled=True):
        super(SecurityConfig, self).__init__()
        self._type = ("SecurityConfig", True)
        self._banner = (self.__undef__, True)
        self._is_cors_enabled = (self.__undef__, True)
        self._allowed_cors_origins = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SecurityConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._banner = (data.get("banner", obj.__undef__), dirty)
        if obj._banner[0] is not None and obj._banner[0] is not obj.__undef__:
            assert isinstance(obj._banner[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._banner[0], type(obj._banner[0])))
            common.validate_format(obj._banner[0], "None", None, None)
        obj._is_cors_enabled = (data.get("isCORSEnabled", obj.__undef__), dirty)
        if obj._is_cors_enabled[0] is not None and obj._is_cors_enabled[0] is not obj.__undef__:
            assert isinstance(obj._is_cors_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._is_cors_enabled[0], type(obj._is_cors_enabled[0])))
            common.validate_format(obj._is_cors_enabled[0], "None", None, None)
        obj._allowed_cors_origins = (data.get("allowedCORSOrigins", obj.__undef__), dirty)
        if obj._allowed_cors_origins[0] is not None and obj._allowed_cors_origins[0] is not obj.__undef__:
            assert isinstance(obj._allowed_cors_origins[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._allowed_cors_origins[0], type(obj._allowed_cors_origins[0])))
            common.validate_format(obj._allowed_cors_origins[0], "None", None, None)
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
        if "is_cors_enabled" == "type" or (self.is_cors_enabled is not self.__undef__ and (not (dirty and not self._is_cors_enabled[1]) or isinstance(self.is_cors_enabled, list) or belongs_to_parent)):
            dct["isCORSEnabled"] = dictify(self.is_cors_enabled)
        if "allowed_cors_origins" == "type" or (self.allowed_cors_origins is not self.__undef__ and (not (dirty and not self._allowed_cors_origins[1]) or isinstance(self.allowed_cors_origins, list) or belongs_to_parent)):
            dct["allowedCORSOrigins"] = dictify(self.allowed_cors_origins)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._banner = (self._banner[0], True)
        self._is_cors_enabled = (self._is_cors_enabled[0], True)
        self._allowed_cors_origins = (self._allowed_cors_origins[0], True)

    def is_dirty(self):
        return any([self._banner[1], self._is_cors_enabled[1], self._allowed_cors_origins[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SecurityConfig):
            return False
        return super(SecurityConfig, self).__eq__(other) and \
               self.banner == other.banner and \
               self.is_cors_enabled == other.is_cors_enabled and \
               self.allowed_cors_origins == other.allowed_cors_origins

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
    def is_cors_enabled(self):
        """
        Whether or not CORS is enabled. Changing this value requires a stack
        restart for it to take effect.

        :rtype: ``bool``
        """
        return self._is_cors_enabled[0]

    @is_cors_enabled.setter
    def is_cors_enabled(self, value):
        self._is_cors_enabled = (value, True)

    @property
    def allowed_cors_origins(self):
        """
        Allowed origin domains for CORS. Should be a comma separated list. Use
        * for all domains. Defaults to none. Changing this value requires a
        stack restart for it to take effect.

        :rtype: ``TEXT_TYPE``
        """
        return self._allowed_cors_origins[0]

    @allowed_cors_origins.setter
    def allowed_cors_origins(self, value):
        self._allowed_cors_origins = (value, True)

