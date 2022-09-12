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
#     /delphix-alert-target-filter.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_4.web.objects.AlertFilter import AlertFilter
from delphixpy.v1_11_4 import common

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

class TargetFilter(AlertFilter):
    """
    *(extends* :py:class:`v1_11_4.web.vo.AlertFilter` *)* An alert filter that
    specifies which targets to match against.
    """
    def __init__(self, undef_enabled=True):
        super(TargetFilter, self).__init__()
        self._type = ("TargetFilter", True)
        self._targets = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TargetFilter, cls).from_dict(data, dirty, undef_enabled)
        obj._targets = []
        for item in data.get("targets") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._targets.append(item)
        obj._targets = (obj._targets, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TargetFilter, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "targets" == "type" or (self.targets is not self.__undef__ and (not (dirty and not self._targets[1]) or isinstance(self.targets, list) or belongs_to_parent)):
            dct["targets"] = dictify(self.targets, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._targets = (self._targets[0], True)

    def is_dirty(self):
        return any([self._targets[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TargetFilter):
            return False
        return super(TargetFilter, self).__eq__(other) and \
               self.targets == other.targets

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def targets(self):
        """
        List of object references. Only alerts related to one of the targets or
        its children are included.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._targets[0]

    @targets.setter
    def targets(self, value):
        self._targets = (value, True)

