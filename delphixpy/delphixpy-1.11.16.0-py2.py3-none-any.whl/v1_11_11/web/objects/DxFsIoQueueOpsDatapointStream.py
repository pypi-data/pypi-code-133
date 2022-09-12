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
#     /delphix-analytics-dxfs-io-queue-ops-datapoint-stream.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.DatapointStream import DatapointStream
from delphixpy.v1_11_11 import common

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

class DxFsIoQueueOpsDatapointStream(DatapointStream):
    """
    *(extends* :py:class:`v1_11_11.web.vo.DatapointStream` *)* A stream of
    datapoints from a DxFS_IO_QUEUE_OPS analytics slice.
    """
    def __init__(self, undef_enabled=True):
        super(DxFsIoQueueOpsDatapointStream, self).__init__()
        self._type = ("DxFsIoQueueOpsDatapointStream", True)
        self._op = (self.__undef__, True)
        self._priority = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DxFsIoQueueOpsDatapointStream, cls).from_dict(data, dirty, undef_enabled)
        obj._op = (data.get("op", obj.__undef__), dirty)
        if obj._op[0] is not None and obj._op[0] is not obj.__undef__:
            assert isinstance(obj._op[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._op[0], type(obj._op[0])))
            assert obj._op[0] in ['read', 'write', 'claim', 'free', 'ioctl', 'null'], "Expected enum ['read', 'write', 'claim', 'free', 'ioctl', 'null'] but got %s" % obj._op[0]
            common.validate_format(obj._op[0], "None", None, None)
        obj._priority = (data.get("priority", obj.__undef__), dirty)
        if obj._priority[0] is not None and obj._priority[0] is not obj.__undef__:
            assert isinstance(obj._priority[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._priority[0], type(obj._priority[0])))
            assert obj._priority[0] in ['sync', 'cache/agg', 'asyncw', 'asyncr', 'resilver', 'scrub', 'ddt_prefetch'], "Expected enum ['sync', 'cache/agg', 'asyncw', 'asyncr', 'resilver', 'scrub', 'ddt_prefetch'] but got %s" % obj._priority[0]
            common.validate_format(obj._priority[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DxFsIoQueueOpsDatapointStream, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "op" == "type" or (self.op is not self.__undef__ and (not (dirty and not self._op[1]))):
            dct["op"] = dictify(self.op)
        if "priority" == "type" or (self.priority is not self.__undef__ and (not (dirty and not self._priority[1]))):
            dct["priority"] = dictify(self.priority)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._op = (self._op[0], True)
        self._priority = (self._priority[0], True)

    def is_dirty(self):
        return any([self._op[1], self._priority[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DxFsIoQueueOpsDatapointStream):
            return False
        return super(DxFsIoQueueOpsDatapointStream, self).__eq__(other) and \
               self.op == other.op and \
               self.priority == other.priority

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def op(self):
        """
        I/O operation type. *(permitted values: read, write, claim, free,
        ioctl, null)*

        :rtype: ``TEXT_TYPE``
        """
        return self._op[0]

    @op.setter
    def op(self, value):
        self._op = (value, True)

    @property
    def priority(self):
        """
        Priority of the I/O. *(permitted values: sync, cache/agg, asyncw,
        asyncr, resilver, scrub, ddt_prefetch)*

        :rtype: ``TEXT_TYPE``
        """
        return self._priority[0]

    @priority.setter
    def priority(self, value):
        self._priority = (value, True)

