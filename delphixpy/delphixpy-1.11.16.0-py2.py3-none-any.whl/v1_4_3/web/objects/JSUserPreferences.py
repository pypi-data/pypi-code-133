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
#     /delphix-js-user-preferences.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_4_3 import common

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

class JSUserPreferences(PersistentObject):
    """
    *(extends* :py:class:`v1_4_3.web.vo.PersistentObject` *)* A Jet Stream
    user's preferences.
    """
    def __init__(self, undef_enabled=True):
        super(JSUserPreferences, self).__init__()
        self._type = ("JSUserPreferences", True)
        self._breakdowns = (self.__undef__, True)
        self._enabled = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSUserPreferences, cls).from_dict(data, dirty, undef_enabled)
        obj._breakdowns = []
        for item in data.get("breakdowns") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._breakdowns.append(item)
        obj._breakdowns = (obj._breakdowns, dirty)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSUserPreferences, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "breakdowns" == "type" or (self.breakdowns is not self.__undef__ and (not (dirty and not self._breakdowns[1]) or isinstance(self.breakdowns, list) or belongs_to_parent)):
            dct["breakdowns"] = dictify(self.breakdowns, prop_is_list_or_vo=True)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]))):
            dct["enabled"] = dictify(self.enabled)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._breakdowns = (self._breakdowns[0], True)
        self._enabled = (self._enabled[0], True)

    def is_dirty(self):
        return any([self._breakdowns[1], self._enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSUserPreferences):
            return False
        return super(JSUserPreferences, self).__eq__(other) and \
               self.breakdowns == other.breakdowns and \
               self.enabled == other.enabled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def breakdowns(self):
        """
        The properties configured for breaking down application templates.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._breakdowns[0]

    @breakdowns.setter
    def breakdowns(self, value):
        self._breakdowns = (value, True)

    @property
    def enabled(self):
        """
        Indicates whether Jet Stream is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

