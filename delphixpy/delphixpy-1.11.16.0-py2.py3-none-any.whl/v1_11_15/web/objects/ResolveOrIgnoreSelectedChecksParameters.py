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
#     /delphix-resolve-or-ignore-selected-checks-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_15 import common

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

class ResolveOrIgnoreSelectedChecksParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_15.web.vo.TypedObject` *)* The parameters to
    use as input when marking selected checks as resolved or ignored.
    """
    def __init__(self, undef_enabled=True):
        super(ResolveOrIgnoreSelectedChecksParameters, self).__init__()
        self._type = ("ResolveOrIgnoreSelectedChecksParameters", True)
        self._check_references = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ResolveOrIgnoreSelectedChecksParameters, cls).from_dict(data, dirty, undef_enabled)
        if "checkReferences" not in data:
            raise ValueError("Missing required property \"checkReferences\".")
        obj._check_references = []
        for item in data.get("checkReferences") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._check_references.append(item)
        obj._check_references = (obj._check_references, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ResolveOrIgnoreSelectedChecksParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "check_references" == "type" or (self.check_references is not self.__undef__ and (not (dirty and not self._check_references[1]) or isinstance(self.check_references, list) or belongs_to_parent)):
            dct["checkReferences"] = dictify(self.check_references, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._check_references = (self._check_references[0], True)

    def is_dirty(self):
        return any([self._check_references[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ResolveOrIgnoreSelectedChecksParameters):
            return False
        return super(ResolveOrIgnoreSelectedChecksParameters, self).__eq__(other) and \
               self.check_references == other.check_references

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def check_references(self):
        """
        Input list of checks which will be marked as resolved or ignored.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._check_references[0]

    @check_references.setter
    def check_references(self, value):
        self._check_references = (value, True)

