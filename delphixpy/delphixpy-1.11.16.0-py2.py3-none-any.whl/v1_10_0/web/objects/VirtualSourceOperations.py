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

from delphixpy.v1_10_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_0 import factory
from delphixpy.v1_10_0 import common

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
    *(extends* :py:class:`v1_10_0.web.vo.TypedObject` *)* Describes operations
    which are performed on virtual sources at various times.
    """
    def __init__(self, undef_enabled=True):
        super(VirtualSourceOperations, self).__init__()
        self._type = ("VirtualSourceOperations", True)
        self._configure_clone = (self.__undef__, True)
        self._pre_refresh = (self.__undef__, True)
        self._post_refresh = (self.__undef__, True)
        self._pre_rollback = (self.__undef__, True)
        self._post_rollback = (self.__undef__, True)
        self._pre_snapshot = (self.__undef__, True)
        self._post_snapshot = (self.__undef__, True)
        self._pre_start = (self.__undef__, True)
        self._post_start = (self.__undef__, True)
        self._pre_stop = (self.__undef__, True)
        self._post_stop = (self.__undef__, True)

    API_VERSION = "1.10.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(VirtualSourceOperations, cls).from_dict(data, dirty, undef_enabled)
        obj._configure_clone = []
        for item in data.get("configureClone") or []:
            obj._configure_clone.append(factory.create_object(item))
            factory.validate_type(obj._configure_clone[-1], "SourceOperation")
        obj._configure_clone = (obj._configure_clone, dirty)
        obj._pre_refresh = []
        for item in data.get("preRefresh") or []:
            obj._pre_refresh.append(factory.create_object(item))
            factory.validate_type(obj._pre_refresh[-1], "SourceOperation")
        obj._pre_refresh = (obj._pre_refresh, dirty)
        obj._post_refresh = []
        for item in data.get("postRefresh") or []:
            obj._post_refresh.append(factory.create_object(item))
            factory.validate_type(obj._post_refresh[-1], "SourceOperation")
        obj._post_refresh = (obj._post_refresh, dirty)
        obj._pre_rollback = []
        for item in data.get("preRollback") or []:
            obj._pre_rollback.append(factory.create_object(item))
            factory.validate_type(obj._pre_rollback[-1], "SourceOperation")
        obj._pre_rollback = (obj._pre_rollback, dirty)
        obj._post_rollback = []
        for item in data.get("postRollback") or []:
            obj._post_rollback.append(factory.create_object(item))
            factory.validate_type(obj._post_rollback[-1], "SourceOperation")
        obj._post_rollback = (obj._post_rollback, dirty)
        obj._pre_snapshot = []
        for item in data.get("preSnapshot") or []:
            obj._pre_snapshot.append(factory.create_object(item))
            factory.validate_type(obj._pre_snapshot[-1], "SourceOperation")
        obj._pre_snapshot = (obj._pre_snapshot, dirty)
        obj._post_snapshot = []
        for item in data.get("postSnapshot") or []:
            obj._post_snapshot.append(factory.create_object(item))
            factory.validate_type(obj._post_snapshot[-1], "SourceOperation")
        obj._post_snapshot = (obj._post_snapshot, dirty)
        obj._pre_start = []
        for item in data.get("preStart") or []:
            obj._pre_start.append(factory.create_object(item))
            factory.validate_type(obj._pre_start[-1], "SourceOperation")
        obj._pre_start = (obj._pre_start, dirty)
        obj._post_start = []
        for item in data.get("postStart") or []:
            obj._post_start.append(factory.create_object(item))
            factory.validate_type(obj._post_start[-1], "SourceOperation")
        obj._post_start = (obj._post_start, dirty)
        obj._pre_stop = []
        for item in data.get("preStop") or []:
            obj._pre_stop.append(factory.create_object(item))
            factory.validate_type(obj._pre_stop[-1], "SourceOperation")
        obj._pre_stop = (obj._pre_stop, dirty)
        obj._post_stop = []
        for item in data.get("postStop") or []:
            obj._post_stop.append(factory.create_object(item))
            factory.validate_type(obj._post_stop[-1], "SourceOperation")
        obj._post_stop = (obj._post_stop, dirty)
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
        if "pre_refresh" == "type" or (self.pre_refresh is not self.__undef__ and (not (dirty and not self._pre_refresh[1]) or isinstance(self.pre_refresh, list) or belongs_to_parent)):
            dct["preRefresh"] = dictify(self.pre_refresh, prop_is_list_or_vo=True)
        if "post_refresh" == "type" or (self.post_refresh is not self.__undef__ and (not (dirty and not self._post_refresh[1]) or isinstance(self.post_refresh, list) or belongs_to_parent)):
            dct["postRefresh"] = dictify(self.post_refresh, prop_is_list_or_vo=True)
        if "pre_rollback" == "type" or (self.pre_rollback is not self.__undef__ and (not (dirty and not self._pre_rollback[1]) or isinstance(self.pre_rollback, list) or belongs_to_parent)):
            dct["preRollback"] = dictify(self.pre_rollback, prop_is_list_or_vo=True)
        if "post_rollback" == "type" or (self.post_rollback is not self.__undef__ and (not (dirty and not self._post_rollback[1]) or isinstance(self.post_rollback, list) or belongs_to_parent)):
            dct["postRollback"] = dictify(self.post_rollback, prop_is_list_or_vo=True)
        if "pre_snapshot" == "type" or (self.pre_snapshot is not self.__undef__ and (not (dirty and not self._pre_snapshot[1]) or isinstance(self.pre_snapshot, list) or belongs_to_parent)):
            dct["preSnapshot"] = dictify(self.pre_snapshot, prop_is_list_or_vo=True)
        if "post_snapshot" == "type" or (self.post_snapshot is not self.__undef__ and (not (dirty and not self._post_snapshot[1]) or isinstance(self.post_snapshot, list) or belongs_to_parent)):
            dct["postSnapshot"] = dictify(self.post_snapshot, prop_is_list_or_vo=True)
        if "pre_start" == "type" or (self.pre_start is not self.__undef__ and (not (dirty and not self._pre_start[1]) or isinstance(self.pre_start, list) or belongs_to_parent)):
            dct["preStart"] = dictify(self.pre_start, prop_is_list_or_vo=True)
        if "post_start" == "type" or (self.post_start is not self.__undef__ and (not (dirty and not self._post_start[1]) or isinstance(self.post_start, list) or belongs_to_parent)):
            dct["postStart"] = dictify(self.post_start, prop_is_list_or_vo=True)
        if "pre_stop" == "type" or (self.pre_stop is not self.__undef__ and (not (dirty and not self._pre_stop[1]) or isinstance(self.pre_stop, list) or belongs_to_parent)):
            dct["preStop"] = dictify(self.pre_stop, prop_is_list_or_vo=True)
        if "post_stop" == "type" or (self.post_stop is not self.__undef__ and (not (dirty and not self._post_stop[1]) or isinstance(self.post_stop, list) or belongs_to_parent)):
            dct["postStop"] = dictify(self.post_stop, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._configure_clone = (self._configure_clone[0], True)
        self._pre_refresh = (self._pre_refresh[0], True)
        self._post_refresh = (self._post_refresh[0], True)
        self._pre_rollback = (self._pre_rollback[0], True)
        self._post_rollback = (self._post_rollback[0], True)
        self._pre_snapshot = (self._pre_snapshot[0], True)
        self._post_snapshot = (self._post_snapshot[0], True)
        self._pre_start = (self._pre_start[0], True)
        self._post_start = (self._post_start[0], True)
        self._pre_stop = (self._pre_stop[0], True)
        self._post_stop = (self._post_stop[0], True)

    def is_dirty(self):
        return any([self._configure_clone[1], self._pre_refresh[1], self._post_refresh[1], self._pre_rollback[1], self._post_rollback[1], self._pre_snapshot[1], self._post_snapshot[1], self._pre_start[1], self._post_start[1], self._pre_stop[1], self._post_stop[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, VirtualSourceOperations):
            return False
        return super(VirtualSourceOperations, self).__eq__(other) and \
               self.configure_clone == other.configure_clone and \
               self.pre_refresh == other.pre_refresh and \
               self.post_refresh == other.post_refresh and \
               self.pre_rollback == other.pre_rollback and \
               self.post_rollback == other.post_rollback and \
               self.pre_snapshot == other.pre_snapshot and \
               self.post_snapshot == other.post_snapshot and \
               self.pre_start == other.pre_start and \
               self.post_start == other.post_start and \
               self.pre_stop == other.pre_stop and \
               self.post_stop == other.post_stop

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

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._configure_clone[0]

    @configure_clone.setter
    def configure_clone(self, value):
        self._configure_clone = (value, True)

    @property
    def pre_refresh(self):
        """
        Operations to perform before refreshing a virtual source. These
        operations can backup any data or configuration from the running source
        before doing the refresh.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._pre_refresh[0]

    @pre_refresh.setter
    def pre_refresh(self, value):
        self._pre_refresh = (value, True)

    @property
    def post_refresh(self):
        """
        Operations to perform after refreshing a virtual source. These
        operations can be used to restore any data or configuration backed up
        in the preRefresh operations.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._post_refresh[0]

    @post_refresh.setter
    def post_refresh(self, value):
        self._post_refresh = (value, True)

    @property
    def pre_rollback(self):
        """
        Operations to perform before rewinding a virtual source. These
        operations can backup any data or configuration from the running source
        prior to rewinding.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._pre_rollback[0]

    @pre_rollback.setter
    def pre_rollback(self, value):
        self._pre_rollback = (value, True)

    @property
    def post_rollback(self):
        """
        Operations to perform after rewinding a virtual source. These
        operations can be used to automate processes once the rewind is
        complete.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._post_rollback[0]

    @post_rollback.setter
    def post_rollback(self, value):
        self._post_rollback = (value, True)

    @property
    def pre_snapshot(self):
        """
        Operations to perform before snapshotting a virtual source. These
        operations can quiesce any data prior to snapshotting.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._pre_snapshot[0]

    @pre_snapshot.setter
    def pre_snapshot(self, value):
        self._pre_snapshot = (value, True)

    @property
    def post_snapshot(self):
        """
        Operations to perform after snapshotting a virtual source.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._post_snapshot[0]

    @post_snapshot.setter
    def post_snapshot(self, value):
        self._post_snapshot = (value, True)

    @property
    def pre_start(self):
        """
        Operations to perform before starting a virtual source.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._pre_start[0]

    @pre_start.setter
    def pre_start(self, value):
        self._pre_start = (value, True)

    @property
    def post_start(self):
        """
        Operations to perform after starting a virtual source.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._post_start[0]

    @post_start.setter
    def post_start(self, value):
        self._post_start = (value, True)

    @property
    def pre_stop(self):
        """
        Operations to perform before stopping a virtual source.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._pre_stop[0]

    @pre_stop.setter
    def pre_stop(self, value):
        self._pre_stop = (value, True)

    @property
    def post_stop(self):
        """
        Operations to perform after stopping a virtual source.

        :rtype: ``list`` of :py:class:`v1_10_0.web.vo.SourceOperation`
        """
        return self._post_stop[0]

    @post_stop.setter
    def post_stop(self, value):
        self._post_stop = (value, True)

