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
#     /delphix-oracle-timeflow-point.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.TimeflowPoint import TimeflowPoint
from delphixpy.v1_4_3 import common

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

class OracleTimeflowPoint(TimeflowPoint):
    """
    *(extends* :py:class:`v1_4_3.web.vo.TimeflowPoint` *)* A unique point
    within an Oracle database timeflow
    """
    def __init__(self, undef_enabled=True):
        super(OracleTimeflowPoint, self).__init__()
        self._type = ("OracleTimeflowPoint", True)
        self._timeflow = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleTimeflowPoint, cls).from_dict(data, dirty, undef_enabled)
        if "timeflow" not in data:
            raise ValueError("Missing required property \"timeflow\".")
        obj._timeflow = (data.get("timeflow", obj.__undef__), dirty)
        if obj._timeflow[0] is not None and obj._timeflow[0] is not obj.__undef__:
            assert isinstance(obj._timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timeflow[0], type(obj._timeflow[0])))
            common.validate_format(obj._timeflow[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleTimeflowPoint, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "timeflow" == "type" or (self.timeflow is not self.__undef__ and (not (dirty and not self._timeflow[1]) or isinstance(self.timeflow, list) or belongs_to_parent)):
            dct["timeflow"] = dictify(self.timeflow)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._timeflow = (self._timeflow[0], True)

    def is_dirty(self):
        return any([self._timeflow[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleTimeflowPoint):
            return False
        return super(OracleTimeflowPoint, self).__eq__(other) and \
               self.timeflow == other.timeflow

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def timeflow(self):
        """
        Reference to timeflow containing this point.

        :rtype: ``TEXT_TYPE``
        """
        return self._timeflow[0]

    @timeflow.setter
    def timeflow(self, value):
        self._timeflow = (value, True)

