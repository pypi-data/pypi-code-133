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
#     /delphix-mssql-timeflow.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_2.web.objects.Timeflow import Timeflow
from delphixpy.v1_8_2 import factory
from delphixpy.v1_8_2 import common

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

class MSSqlTimeflow(Timeflow):
    """
    *(extends* :py:class:`v1_8_2.web.vo.Timeflow` *)* TimeFlow representing
    historical data for a particular timeline within a data container.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlTimeflow, self).__init__()
        self._type = ("MSSqlTimeflow", True)
        self._database_guid = (self.__undef__, True)
        self._parent_point = (self.__undef__, True)

    API_VERSION = "1.8.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlTimeflow, cls).from_dict(data, dirty, undef_enabled)
        obj._database_guid = (data.get("databaseGuid", obj.__undef__), dirty)
        if obj._database_guid[0] is not None and obj._database_guid[0] is not obj.__undef__:
            assert isinstance(obj._database_guid[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_guid[0], type(obj._database_guid[0])))
            common.validate_format(obj._database_guid[0], "None", None, None)
        if "parentPoint" in data and data["parentPoint"] is not None:
            obj._parent_point = (factory.create_object(data["parentPoint"], "MSSqlTimeflowPoint"), dirty)
            factory.validate_type(obj._parent_point[0], "MSSqlTimeflowPoint")
        else:
            obj._parent_point = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlTimeflow, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "database_guid" == "type" or (self.database_guid is not self.__undef__ and (not (dirty and not self._database_guid[1]))):
            dct["databaseGuid"] = dictify(self.database_guid)
        if "parent_point" == "type" or (self.parent_point is not self.__undef__ and (not (dirty and not self._parent_point[1]))):
            dct["parentPoint"] = dictify(self.parent_point)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._database_guid = (self._database_guid[0], True)
        self._parent_point = (self._parent_point[0], True)

    def is_dirty(self):
        return any([self._database_guid[1], self._parent_point[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlTimeflow):
            return False
        return super(MSSqlTimeflow, self).__eq__(other) and \
               self.database_guid == other.database_guid and \
               self.parent_point == other.parent_point

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def database_guid(self):
        """
        MSSQL-specific recovery branch identifier for this TimeFlow.

        :rtype: ``TEXT_TYPE``
        """
        return self._database_guid[0]

    @database_guid.setter
    def database_guid(self, value):
        self._database_guid = (value, True)

    @property
    def parent_point(self):
        """
        The origin point on the parent TimeFlow from which this TimeFlow was
        provisioned. This will not be present for TimeFlows derived from linked
        sources.

        :rtype: :py:class:`v1_8_2.web.vo.MSSqlTimeflowPoint`
        """
        return self._parent_point[0]

    @parent_point.setter
    def parent_point(self, value):
        self._parent_point = (value, True)

