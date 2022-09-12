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
#     /delphix-analytics-path-descendant-constraint.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.PathConstraint import PathConstraint
from delphixpy.v1_11_3 import common

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

class PathDescendantConstraint(PathConstraint):
    """
    *(extends* :py:class:`v1_11_3.web.vo.PathConstraint` *)* Constraint placed
    on a filesystem path axis of a particular analytics slice.
    """
    def __init__(self, undef_enabled=True):
        super(PathDescendantConstraint, self).__init__()
        self._type = ("PathDescendantConstraint", True)
        self._descendant_of = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PathDescendantConstraint, cls).from_dict(data, dirty, undef_enabled)
        obj._descendant_of = (data.get("descendantOf", obj.__undef__), dirty)
        if obj._descendant_of[0] is not None and obj._descendant_of[0] is not obj.__undef__:
            assert isinstance(obj._descendant_of[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._descendant_of[0], type(obj._descendant_of[0])))
            common.validate_format(obj._descendant_of[0], "unixpath", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PathDescendantConstraint, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "descendant_of" == "type" or (self.descendant_of is not self.__undef__ and (not (dirty and not self._descendant_of[1]) or isinstance(self.descendant_of, list) or belongs_to_parent)):
            dct["descendantOf"] = dictify(self.descendant_of)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._descendant_of = (self._descendant_of[0], True)

    def is_dirty(self):
        return any([self._descendant_of[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PathDescendantConstraint):
            return False
        return super(PathDescendantConstraint, self).__eq__(other) and \
               self.descendant_of == other.descendant_of

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def descendant_of(self):
        """
        The axis values must be a descendant of this path.

        :rtype: ``TEXT_TYPE``
        """
        return self._descendant_of[0]

    @descendant_of.setter
    def descendant_of(self, value):
        self._descendant_of = (value, True)

