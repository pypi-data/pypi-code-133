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
#     /delphix-oracle-database-statistic.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_2 import common

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

class OracleDatabaseStatistic(TypedObject):
    """
    *(extends* :py:class:`v1_5_2.web.vo.TypedObject` *)* A row in the database
    performance statistic table.
    """
    def __init__(self, undef_enabled=True):
        super(OracleDatabaseStatistic, self).__init__()
        self._type = ("OracleDatabaseStatistic", True)
        self._statistic_values = (self.__undef__, True)

    API_VERSION = "1.5.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleDatabaseStatistic, cls).from_dict(data, dirty, undef_enabled)
        obj._statistic_values = []
        for item in data.get("statisticValues") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._statistic_values.append(item)
        obj._statistic_values = (obj._statistic_values, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleDatabaseStatistic, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "statistic_values" == "type" or (self.statistic_values is not self.__undef__ and (not (dirty and not self._statistic_values[1]))):
            dct["statisticValues"] = dictify(self.statistic_values)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._statistic_values = (self._statistic_values[0], True)

    def is_dirty(self):
        return any([self._statistic_values[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleDatabaseStatistic):
            return False
        return super(OracleDatabaseStatistic, self).__eq__(other) and \
               self.statistic_values == other.statistic_values

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def statistic_values(self):
        """
        A single performance statistic row.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._statistic_values[0]

    @statistic_values.setter
    def statistic_values(self, value):
        self._statistic_values = (value, True)

