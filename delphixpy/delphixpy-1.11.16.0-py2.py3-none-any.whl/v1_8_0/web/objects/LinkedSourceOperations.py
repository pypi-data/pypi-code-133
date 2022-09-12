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
#     /delphix-linked-source-operations.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_8_0 import factory
from delphixpy.v1_8_0 import common

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

class LinkedSourceOperations(TypedObject):
    """
    *(extends* :py:class:`v1_8_0.web.vo.TypedObject` *)* Describes operations
    which are performed on linked sources at various times.
    """
    def __init__(self, undef_enabled=True):
        super(LinkedSourceOperations, self).__init__()
        self._type = ("LinkedSourceOperations", True)
        self._post_sync = (self.__undef__, True)
        self._pre_sync = (self.__undef__, True)

    API_VERSION = "1.8.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(LinkedSourceOperations, cls).from_dict(data, dirty, undef_enabled)
        obj._post_sync = []
        for item in data.get("postSync") or []:
            obj._post_sync.append(factory.create_object(item))
            factory.validate_type(obj._post_sync[-1], "SourceOperation")
        obj._post_sync = (obj._post_sync, dirty)
        obj._pre_sync = []
        for item in data.get("preSync") or []:
            obj._pre_sync.append(factory.create_object(item))
            factory.validate_type(obj._pre_sync[-1], "SourceOperation")
        obj._pre_sync = (obj._pre_sync, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(LinkedSourceOperations, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "post_sync" == "type" or (self.post_sync is not self.__undef__ and (not (dirty and not self._post_sync[1]) or isinstance(self.post_sync, list) or belongs_to_parent)):
            dct["postSync"] = dictify(self.post_sync, prop_is_list_or_vo=True)
        if "pre_sync" == "type" or (self.pre_sync is not self.__undef__ and (not (dirty and not self._pre_sync[1]) or isinstance(self.pre_sync, list) or belongs_to_parent)):
            dct["preSync"] = dictify(self.pre_sync, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._post_sync = (self._post_sync[0], True)
        self._pre_sync = (self._pre_sync[0], True)

    def is_dirty(self):
        return any([self._post_sync[1], self._pre_sync[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, LinkedSourceOperations):
            return False
        return super(LinkedSourceOperations, self).__eq__(other) and \
               self.post_sync == other.post_sync and \
               self.pre_sync == other.pre_sync

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def post_sync(self):
        """
        Operations to perform after syncing a linked source.

        :rtype: ``list`` of :py:class:`v1_8_0.web.vo.SourceOperation`
        """
        return self._post_sync[0]

    @post_sync.setter
    def post_sync(self, value):
        self._post_sync = (value, True)

    @property
    def pre_sync(self):
        """
        Operations to perform before syncing from a linked source. These
        operations can quiesce any data prior to syncing.

        :rtype: ``list`` of :py:class:`v1_8_0.web.vo.SourceOperation`
        """
        return self._pre_sync[0]

    @pre_sync.setter
    def pre_sync(self, value):
        self._pre_sync = (value, True)

