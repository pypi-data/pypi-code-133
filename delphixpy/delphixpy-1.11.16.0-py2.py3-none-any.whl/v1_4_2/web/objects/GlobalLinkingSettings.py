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
#     /delphix-global-linking-settings.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_2 import common

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

class GlobalLinkingSettings(TypedObject):
    """
    *(extends* :py:class:`v1_4_2.web.vo.TypedObject` *)* System-wide linking
    settings
    """
    def __init__(self, undef_enabled=True):
        super(GlobalLinkingSettings, self).__init__()
        self._type = ("GlobalLinkingSettings", True)
        self._encrypted_linking_enabled_by_default = (self.__undef__, True)

    API_VERSION = "1.4.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(GlobalLinkingSettings, cls).from_dict(data, dirty, undef_enabled)
        obj._encrypted_linking_enabled_by_default = (data.get("encryptedLinkingEnabledByDefault", obj.__undef__), dirty)
        if obj._encrypted_linking_enabled_by_default[0] is not None and obj._encrypted_linking_enabled_by_default[0] is not obj.__undef__:
            assert isinstance(obj._encrypted_linking_enabled_by_default[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._encrypted_linking_enabled_by_default[0], type(obj._encrypted_linking_enabled_by_default[0])))
            common.validate_format(obj._encrypted_linking_enabled_by_default[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(GlobalLinkingSettings, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "encrypted_linking_enabled_by_default" == "type" or (self.encrypted_linking_enabled_by_default is not self.__undef__ and (not (dirty and not self._encrypted_linking_enabled_by_default[1]) or isinstance(self.encrypted_linking_enabled_by_default, list) or belongs_to_parent)):
            dct["encryptedLinkingEnabledByDefault"] = dictify(self.encrypted_linking_enabled_by_default)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._encrypted_linking_enabled_by_default = (self._encrypted_linking_enabled_by_default[0], True)

    def is_dirty(self):
        return any([self._encrypted_linking_enabled_by_default[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, GlobalLinkingSettings):
            return False
        return super(GlobalLinkingSettings, self).__eq__(other) and \
               self.encrypted_linking_enabled_by_default == other.encrypted_linking_enabled_by_default

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def encrypted_linking_enabled_by_default(self):
        """
        True if encrypted linking should be enabled by default on new dSources.

        :rtype: ``bool``
        """
        return self._encrypted_linking_enabled_by_default[0]

    @encrypted_linking_enabled_by_default.setter
    def encrypted_linking_enabled_by_default(self, value):
        self._encrypted_linking_enabled_by_default = (value, True)

