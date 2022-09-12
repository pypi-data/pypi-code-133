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
#     /delphix-alert-not-filter.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_1.web.objects.AlertFilter import AlertFilter
from delphixpy.v1_10_1 import factory
from delphixpy.v1_10_1 import common

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

class NotFilter(AlertFilter):
    """
    *(extends* :py:class:`v1_10_1.web.vo.AlertFilter` *)* A container filter
    that inverts the logic of another filter.
    """
    def __init__(self, undef_enabled=True):
        super(NotFilter, self).__init__()
        self._type = ("NotFilter", True)
        self._sub_filter = (self.__undef__, True)

    API_VERSION = "1.10.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NotFilter, cls).from_dict(data, dirty, undef_enabled)
        if "subFilter" in data and data["subFilter"] is not None:
            obj._sub_filter = (factory.create_object(data["subFilter"], "AlertFilter"), dirty)
            factory.validate_type(obj._sub_filter[0], "AlertFilter")
        else:
            obj._sub_filter = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NotFilter, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "sub_filter" == "type" or (self.sub_filter is not self.__undef__ and (not (dirty and not self._sub_filter[1]) or isinstance(self.sub_filter, list) or belongs_to_parent)):
            dct["subFilter"] = dictify(self.sub_filter, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._sub_filter = (self._sub_filter[0], True)

    def is_dirty(self):
        return any([self._sub_filter[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NotFilter):
            return False
        return super(NotFilter, self).__eq__(other) and \
               self.sub_filter == other.sub_filter

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def sub_filter(self):
        """
        Filter whose logic is to be inverted.

        :rtype: :py:class:`v1_10_1.web.vo.AlertFilter`
        """
        return self._sub_filter[0]

    @sub_filter.setter
    def sub_filter(self, value):
        self._sub_filter = (value, True)

