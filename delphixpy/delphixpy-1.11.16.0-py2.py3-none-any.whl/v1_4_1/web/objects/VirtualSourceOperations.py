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
#     /delphix-virtual-source-operations.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_1 import factory
from delphixpy.v1_4_1 import common

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

class VirtualSourceOperations(TypedObject):
    """
    *(extends* :py:class:`v1_4_1.web.vo.TypedObject` *)* Describes operations
    which are performed on virtual sources at various times.
    """
    def __init__(self, undef_enabled=True):
        super(VirtualSourceOperations, self).__init__()
        self._type = ("VirtualSourceOperations", True)
        self._configure_clone = (self.__undef__, True)
        self._post_refresh = (self.__undef__, True)
        self._pre_refresh = (self.__undef__, True)

    API_VERSION = "1.4.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(VirtualSourceOperations, cls).from_dict(data, dirty, undef_enabled)
        obj._configure_clone = []
        for item in data.get("configureClone") or []:
            obj._configure_clone.append(factory.create_object(item))
            factory.validate_type(obj._configure_clone[-1], "Operation")
        obj._configure_clone = (obj._configure_clone, dirty)
        obj._post_refresh = []
        for item in data.get("postRefresh") or []:
            obj._post_refresh.append(factory.create_object(item))
            factory.validate_type(obj._post_refresh[-1], "Operation")
        obj._post_refresh = (obj._post_refresh, dirty)
        obj._pre_refresh = []
        for item in data.get("preRefresh") or []:
            obj._pre_refresh.append(factory.create_object(item))
            factory.validate_type(obj._pre_refresh[-1], "Operation")
        obj._pre_refresh = (obj._pre_refresh, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(VirtualSourceOperations, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "configure_clone" == "type" or (self.configure_clone is not self.__undef__ and (not (dirty and not self._configure_clone[1]) or isinstance(self.configure_clone, list) or belongs_to_parent)):
            dct["configureClone"] = dictify(self.configure_clone, prop_is_list_or_vo=True)
        if "post_refresh" == "type" or (self.post_refresh is not self.__undef__ and (not (dirty and not self._post_refresh[1]) or isinstance(self.post_refresh, list) or belongs_to_parent)):
            dct["postRefresh"] = dictify(self.post_refresh, prop_is_list_or_vo=True)
        if "pre_refresh" == "type" or (self.pre_refresh is not self.__undef__ and (not (dirty and not self._pre_refresh[1]) or isinstance(self.pre_refresh, list) or belongs_to_parent)):
            dct["preRefresh"] = dictify(self.pre_refresh, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._configure_clone = (self._configure_clone[0], True)
        self._post_refresh = (self._post_refresh[0], True)
        self._pre_refresh = (self._pre_refresh[0], True)

    def is_dirty(self):
        return any([self._configure_clone[1], self._post_refresh[1], self._pre_refresh[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, VirtualSourceOperations):
            return False
        return super(VirtualSourceOperations, self).__eq__(other) and \
               self.configure_clone == other.configure_clone and \
               self.post_refresh == other.post_refresh and \
               self.pre_refresh == other.pre_refresh

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def configure_clone(self):
        """
        Operations to perform when initially creating the virtual source and
        every time it is refreshed.

        :rtype: ``list`` of :py:class:`v1_4_1.web.vo.Operation`
        """
        return self._configure_clone[0]

    @configure_clone.setter
    def configure_clone(self, value):
        self._configure_clone = (value, True)

    @property
    def post_refresh(self):
        """
        Operations to perform after refreshing a virtual source. These
        operations can be used to restore any data or configuration backed up
        in the preRefresh operations.

        :rtype: ``list`` of :py:class:`v1_4_1.web.vo.Operation`
        """
        return self._post_refresh[0]

    @post_refresh.setter
    def post_refresh(self, value):
        self._post_refresh = (value, True)

    @property
    def pre_refresh(self):
        """
        Operations to perform before refreshing a virtual source. These
        operations can backup any data or configuration from the running source
        before doing the refresh.

        :rtype: ``list`` of :py:class:`v1_4_1.web.vo.Operation`
        """
        return self._pre_refresh[0]

    @pre_refresh.setter
    def pre_refresh(self, value):
        self._pre_refresh = (value, True)

