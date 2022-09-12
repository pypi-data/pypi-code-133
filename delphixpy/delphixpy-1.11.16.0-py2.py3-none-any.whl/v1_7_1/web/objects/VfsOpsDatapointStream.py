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
#     /delphix-analytics-vfs-ops-datapoint-stream.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.DatapointStream import DatapointStream
from delphixpy.v1_7_1 import common

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

class VfsOpsDatapointStream(DatapointStream):
    """
    *(extends* :py:class:`v1_7_1.web.vo.DatapointStream` *)* A stream of
    datapoints from a VFS_OPS analytics slice.
    """
    def __init__(self, undef_enabled=True):
        super(VfsOpsDatapointStream, self).__init__()
        self._type = ("VfsOpsDatapointStream", True)
        self._cached = (self.__undef__, True)
        self._op = (self.__undef__, True)
        self._path = (self.__undef__, True)
        self._sync = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(VfsOpsDatapointStream, cls).from_dict(data, dirty, undef_enabled)
        obj._cached = (data.get("cached", obj.__undef__), dirty)
        if obj._cached[0] is not None and obj._cached[0] is not obj.__undef__:
            assert isinstance(obj._cached[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._cached[0], type(obj._cached[0])))
            common.validate_format(obj._cached[0], "None", None, None)
        obj._op = (data.get("op", obj.__undef__), dirty)
        if obj._op[0] is not None and obj._op[0] is not obj.__undef__:
            assert isinstance(obj._op[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._op[0], type(obj._op[0])))
            assert obj._op[0] in ['read', 'write'], "Expected enum ['read', 'write'] but got %s" % obj._op[0]
            common.validate_format(obj._op[0], "None", None, None)
        obj._path = (data.get("path", obj.__undef__), dirty)
        if obj._path[0] is not None and obj._path[0] is not obj.__undef__:
            assert isinstance(obj._path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._path[0], type(obj._path[0])))
            common.validate_format(obj._path[0], "unixpath", None, None)
        obj._sync = (data.get("sync", obj.__undef__), dirty)
        if obj._sync[0] is not None and obj._sync[0] is not obj.__undef__:
            assert isinstance(obj._sync[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._sync[0], type(obj._sync[0])))
            common.validate_format(obj._sync[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(VfsOpsDatapointStream, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cached" == "type" or (self.cached is not self.__undef__ and (not (dirty and not self._cached[1]))):
            dct["cached"] = dictify(self.cached)
        if "op" == "type" or (self.op is not self.__undef__ and (not (dirty and not self._op[1]))):
            dct["op"] = dictify(self.op)
        if "path" == "type" or (self.path is not self.__undef__ and (not (dirty and not self._path[1]))):
            dct["path"] = dictify(self.path)
        if "sync" == "type" or (self.sync is not self.__undef__ and (not (dirty and not self._sync[1]))):
            dct["sync"] = dictify(self.sync)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cached = (self._cached[0], True)
        self._op = (self._op[0], True)
        self._path = (self._path[0], True)
        self._sync = (self._sync[0], True)

    def is_dirty(self):
        return any([self._cached[1], self._op[1], self._path[1], self._sync[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, VfsOpsDatapointStream):
            return False
        return super(VfsOpsDatapointStream, self).__eq__(other) and \
               self.cached == other.cached and \
               self.op == other.op and \
               self.path == other.path and \
               self.sync == other.sync

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cached(self):
        """
        Whether reads were cached.

        :rtype: ``bool``
        """
        return self._cached[0]

    @cached.setter
    def cached(self, value):
        self._cached = (value, True)

    @property
    def op(self):
        """
        I/O operation type. *(permitted values: read, write)*

        :rtype: ``TEXT_TYPE``
        """
        return self._op[0]

    @op.setter
    def op(self, value):
        self._op = (value, True)

    @property
    def path(self):
        """
        Path of the affected file.

        :rtype: ``TEXT_TYPE``
        """
        return self._path[0]

    @path.setter
    def path(self, value):
        self._path = (value, True)

    @property
    def sync(self):
        """
        Whether writes were synchronous.

        :rtype: ``bool``
        """
        return self._sync[0]

    @sync.setter
    def sync(self, value):
        self._sync = (value, True)

