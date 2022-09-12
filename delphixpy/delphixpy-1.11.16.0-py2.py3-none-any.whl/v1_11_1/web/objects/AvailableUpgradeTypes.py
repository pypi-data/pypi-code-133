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
#     /delphix-upgrade-available-types.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_1 import common

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

class AvailableUpgradeTypes(TypedObject):
    """
    *(extends* :py:class:`v1_11_1.web.vo.TypedObject` *)* Container of
    available upgrade types.
    """
    def __init__(self, undef_enabled=True):
        super(AvailableUpgradeTypes, self).__init__()
        self._type = ("AvailableUpgradeTypes", True)
        self._upgrade_types = (self.__undef__, True)

    API_VERSION = "1.11.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AvailableUpgradeTypes, cls).from_dict(data, dirty, undef_enabled)
        obj._upgrade_types = []
        for item in data.get("upgradeTypes") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            assert item in ['DEFERRED', 'FINISH_DEFERRED', 'FULL'], "Expected enum ['DEFERRED', 'FINISH_DEFERRED', 'FULL'] but got %s" % item
            common.validate_format(item, "None", None, None)
            obj._upgrade_types.append(item)
        obj._upgrade_types = (obj._upgrade_types, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AvailableUpgradeTypes, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "upgrade_types" == "type" or (self.upgrade_types is not self.__undef__ and (not (dirty and not self._upgrade_types[1]))):
            dct["upgradeTypes"] = dictify(self.upgrade_types)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._upgrade_types = (self._upgrade_types[0], True)

    def is_dirty(self):
        return any([self._upgrade_types[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AvailableUpgradeTypes):
            return False
        return super(AvailableUpgradeTypes, self).__eq__(other) and \
               self.upgrade_types == other.upgrade_types

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def upgrade_types(self):
        """
        Set of available upgrade types.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._upgrade_types[0]

    @upgrade_types.setter
    def upgrade_types(self, value):
        self._upgrade_types = (value, True)

