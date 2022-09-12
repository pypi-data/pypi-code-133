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
#     /delphix-alert-owner-filter.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.AlertFilter import AlertFilter
from delphixpy.v1_8_1 import common

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

class TargetOwnerFilter(AlertFilter):
    """
    *(extends* :py:class:`v1_8_1.web.vo.AlertFilter` *)* An alert filter which
    matches when an alert's target is owned by one of the specified users.
    """
    def __init__(self, undef_enabled=True):
        super(TargetOwnerFilter, self).__init__()
        self._type = ("TargetOwnerFilter", True)
        self._owners = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TargetOwnerFilter, cls).from_dict(data, dirty, undef_enabled)
        obj._owners = []
        for item in data.get("owners") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._owners.append(item)
        obj._owners = (obj._owners, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TargetOwnerFilter, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "owners" == "type" or (self.owners is not self.__undef__ and (not (dirty and not self._owners[1]) or isinstance(self.owners, list) or belongs_to_parent)):
            dct["owners"] = dictify(self.owners, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._owners = (self._owners[0], True)

    def is_dirty(self):
        return any([self._owners[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TargetOwnerFilter):
            return False
        return super(TargetOwnerFilter, self).__eq__(other) and \
               self.owners == other.owners

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def owners(self):
        """
        Target owners to match against.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._owners[0]

    @owners.setter
    def owners(self, value):
        self._owners = (value, True)

