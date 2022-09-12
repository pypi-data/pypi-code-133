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
#     /delphix-js-operation-endpoint.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_0 import common

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

class JSOperationEndpoint(TypedObject):
    """
    *(extends* :py:class:`v1_6_0.web.vo.TypedObject` *)* The first and last
    JSOperation for a given data layout or branch.
    """
    def __init__(self, undef_enabled=True):
        super(JSOperationEndpoint, self).__init__()
        self._type = ("JSOperationEndpoint", True)
        self._first = (self.__undef__, True)
        self._last = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSOperationEndpoint, cls).from_dict(data, dirty, undef_enabled)
        obj._first = (data.get("first", obj.__undef__), dirty)
        if obj._first[0] is not None and obj._first[0] is not obj.__undef__:
            assert isinstance(obj._first[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._first[0], type(obj._first[0])))
            common.validate_format(obj._first[0], "objectReference", None, None)
        obj._last = (data.get("last", obj.__undef__), dirty)
        if obj._last[0] is not None and obj._last[0] is not obj.__undef__:
            assert isinstance(obj._last[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last[0], type(obj._last[0])))
            common.validate_format(obj._last[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSOperationEndpoint, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "first" == "type" or (self.first is not self.__undef__ and (not (dirty and not self._first[1]))):
            dct["first"] = dictify(self.first)
        if "last" == "type" or (self.last is not self.__undef__ and (not (dirty and not self._last[1]))):
            dct["last"] = dictify(self.last)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._first = (self._first[0], True)
        self._last = (self._last[0], True)

    def is_dirty(self):
        return any([self._first[1], self._last[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSOperationEndpoint):
            return False
        return super(JSOperationEndpoint, self).__eq__(other) and \
               self.first == other.first and \
               self.last == other.last

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def first(self):
        """
        The first JSOperation.

        :rtype: ``TEXT_TYPE``
        """
        return self._first[0]

    @first.setter
    def first(self, value):
        self._first = (value, True)

    @property
    def last(self):
        """
        The last JSOperation.

        :rtype: ``TEXT_TYPE``
        """
        return self._last[0]

    @last.setter
    def last(self, value):
        self._last = (value, True)

