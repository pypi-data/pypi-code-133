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
#     /delphix-user-interface-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_8.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_8 import common

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

class UserInterfaceConfig(TypedObject):
    """
    *(extends* :py:class:`v1_11_8.web.vo.TypedObject` *)* User Interface
    Configuration.
    """
    def __init__(self, undef_enabled=True):
        super(UserInterfaceConfig, self).__init__()
        self._type = ("UserInterfaceConfig", True)
        self._analytics_enabled = (self.__undef__, True)

    API_VERSION = "1.11.8"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(UserInterfaceConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._analytics_enabled = (data.get("analyticsEnabled", obj.__undef__), dirty)
        if obj._analytics_enabled[0] is not None and obj._analytics_enabled[0] is not obj.__undef__:
            assert isinstance(obj._analytics_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._analytics_enabled[0], type(obj._analytics_enabled[0])))
            common.validate_format(obj._analytics_enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(UserInterfaceConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "analytics_enabled" == "type" or (self.analytics_enabled is not self.__undef__ and (not (dirty and not self._analytics_enabled[1]) or isinstance(self.analytics_enabled, list) or belongs_to_parent)):
            dct["analyticsEnabled"] = dictify(self.analytics_enabled)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._analytics_enabled = (self._analytics_enabled[0], True)

    def is_dirty(self):
        return any([self._analytics_enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, UserInterfaceConfig):
            return False
        return super(UserInterfaceConfig, self).__eq__(other) and \
               self.analytics_enabled == other.analytics_enabled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def analytics_enabled(self):
        """
        Indicates whether user-interface analytics are enabled or not.

        :rtype: ``bool``
        """
        return self._analytics_enabled[0]

    @analytics_enabled.setter
    def analytics_enabled(self, value):
        self._analytics_enabled = (value, True)

