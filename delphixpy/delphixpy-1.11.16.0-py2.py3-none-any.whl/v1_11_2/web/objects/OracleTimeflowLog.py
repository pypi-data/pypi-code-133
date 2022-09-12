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
#     /delphix-oracle-timeflow-log.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_2 import common

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

class OracleTimeflowLog(TypedObject):
    """
    *(extends* :py:class:`v1_11_2.web.vo.TypedObject` *)* An Oracle log on a
    TimeFlow.
    """
    def __init__(self, undef_enabled=True):
        super(OracleTimeflowLog, self).__init__()
        self._type = ("OracleTimeflowLog", True)
        self._container = (self.__undef__, True)
        self._timeflow = (self.__undef__, True)
        self._instance_num = (self.__undef__, True)
        self._sequence = (self.__undef__, True)
        self._start_scn = (self.__undef__, True)
        self._end_scn = (self.__undef__, True)
        self._start_timestamp = (self.__undef__, True)
        self._end_timestamp = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleTimeflowLog, cls).from_dict(data, dirty, undef_enabled)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._timeflow = (data.get("timeflow", obj.__undef__), dirty)
        if obj._timeflow[0] is not None and obj._timeflow[0] is not obj.__undef__:
            assert isinstance(obj._timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timeflow[0], type(obj._timeflow[0])))
            common.validate_format(obj._timeflow[0], "objectReference", None, None)
        obj._instance_num = (data.get("instanceNum", obj.__undef__), dirty)
        if obj._instance_num[0] is not None and obj._instance_num[0] is not obj.__undef__:
            assert isinstance(obj._instance_num[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._instance_num[0], type(obj._instance_num[0])))
            common.validate_format(obj._instance_num[0], "None", None, None)
        obj._sequence = (data.get("sequence", obj.__undef__), dirty)
        if obj._sequence[0] is not None and obj._sequence[0] is not obj.__undef__:
            assert isinstance(obj._sequence[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._sequence[0], type(obj._sequence[0])))
            common.validate_format(obj._sequence[0], "None", None, None)
        obj._start_scn = (data.get("startScn", obj.__undef__), dirty)
        if obj._start_scn[0] is not None and obj._start_scn[0] is not obj.__undef__:
            assert isinstance(obj._start_scn[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._start_scn[0], type(obj._start_scn[0])))
            common.validate_format(obj._start_scn[0], "None", None, None)
        obj._end_scn = (data.get("endScn", obj.__undef__), dirty)
        if obj._end_scn[0] is not None and obj._end_scn[0] is not obj.__undef__:
            assert isinstance(obj._end_scn[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._end_scn[0], type(obj._end_scn[0])))
            common.validate_format(obj._end_scn[0], "None", None, None)
        obj._start_timestamp = (data.get("startTimestamp", obj.__undef__), dirty)
        if obj._start_timestamp[0] is not None and obj._start_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._start_timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._start_timestamp[0], type(obj._start_timestamp[0])))
            common.validate_format(obj._start_timestamp[0], "date", None, None)
        obj._end_timestamp = (data.get("endTimestamp", obj.__undef__), dirty)
        if obj._end_timestamp[0] is not None and obj._end_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._end_timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._end_timestamp[0], type(obj._end_timestamp[0])))
            common.validate_format(obj._end_timestamp[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleTimeflowLog, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]))):
            dct["container"] = dictify(self.container)
        if "timeflow" == "type" or (self.timeflow is not self.__undef__ and (not (dirty and not self._timeflow[1]))):
            dct["timeflow"] = dictify(self.timeflow)
        if "instance_num" == "type" or (self.instance_num is not self.__undef__ and (not (dirty and not self._instance_num[1]))):
            dct["instanceNum"] = dictify(self.instance_num)
        if "sequence" == "type" or (self.sequence is not self.__undef__ and (not (dirty and not self._sequence[1]))):
            dct["sequence"] = dictify(self.sequence)
        if "start_scn" == "type" or (self.start_scn is not self.__undef__ and (not (dirty and not self._start_scn[1]))):
            dct["startScn"] = dictify(self.start_scn)
        if "end_scn" == "type" or (self.end_scn is not self.__undef__ and (not (dirty and not self._end_scn[1]))):
            dct["endScn"] = dictify(self.end_scn)
        if "start_timestamp" == "type" or (self.start_timestamp is not self.__undef__ and (not (dirty and not self._start_timestamp[1]))):
            dct["startTimestamp"] = dictify(self.start_timestamp)
        if "end_timestamp" == "type" or (self.end_timestamp is not self.__undef__ and (not (dirty and not self._end_timestamp[1]))):
            dct["endTimestamp"] = dictify(self.end_timestamp)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._timeflow = (self._timeflow[0], True)
        self._instance_num = (self._instance_num[0], True)
        self._sequence = (self._sequence[0], True)
        self._start_scn = (self._start_scn[0], True)
        self._end_scn = (self._end_scn[0], True)
        self._start_timestamp = (self._start_timestamp[0], True)
        self._end_timestamp = (self._end_timestamp[0], True)

    def is_dirty(self):
        return any([self._container[1], self._timeflow[1], self._instance_num[1], self._sequence[1], self._start_scn[1], self._end_scn[1], self._start_timestamp[1], self._end_timestamp[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleTimeflowLog):
            return False
        return super(OracleTimeflowLog, self).__eq__(other) and \
               self.container == other.container and \
               self.timeflow == other.timeflow and \
               self.instance_num == other.instance_num and \
               self.sequence == other.sequence and \
               self.start_scn == other.start_scn and \
               self.end_scn == other.end_scn and \
               self.start_timestamp == other.start_timestamp and \
               self.end_timestamp == other.end_timestamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        Reference to the database to which this log belongs.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def timeflow(self):
        """
        Reference to the TimeFlow of which this log is a part.

        :rtype: ``TEXT_TYPE``
        """
        return self._timeflow[0]

    @timeflow.setter
    def timeflow(self, value):
        self._timeflow = (value, True)

    @property
    def instance_num(self):
        """
        Instance number associated with the log file.

        :rtype: ``int``
        """
        return self._instance_num[0]

    @instance_num.setter
    def instance_num(self, value):
        self._instance_num = (value, True)

    @property
    def sequence(self):
        """
        Sequence number for the log file.

        :rtype: ``int``
        """
        return self._sequence[0]

    @sequence.setter
    def sequence(self, value):
        self._sequence = (value, True)

    @property
    def start_scn(self):
        """
        Start SCN for the log file.

        :rtype: ``int``
        """
        return self._start_scn[0]

    @start_scn.setter
    def start_scn(self, value):
        self._start_scn = (value, True)

    @property
    def end_scn(self):
        """
        End SCN for the log file.

        :rtype: ``int``
        """
        return self._end_scn[0]

    @end_scn.setter
    def end_scn(self, value):
        self._end_scn = (value, True)

    @property
    def start_timestamp(self):
        """
        Start timestamp for the log file.

        :rtype: ``TEXT_TYPE``
        """
        return self._start_timestamp[0]

    @start_timestamp.setter
    def start_timestamp(self, value):
        self._start_timestamp = (value, True)

    @property
    def end_timestamp(self):
        """
        End timestamp for the log file.

        :rtype: ``TEXT_TYPE``
        """
        return self._end_timestamp[0]

    @end_timestamp.setter
    def end_timestamp(self, value):
        self._end_timestamp = (value, True)

