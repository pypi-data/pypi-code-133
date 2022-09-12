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
#     /delphix-oracle-timeflow.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.Timeflow import Timeflow
from delphixpy.v1_6_1 import factory
from delphixpy.v1_6_1 import common

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

class OracleTimeflow(Timeflow):
    """
    *(extends* :py:class:`v1_6_1.web.vo.Timeflow` *)* TimeFlow representing
    historical data for a particular timeline within a data container.
    """
    def __init__(self, undef_enabled=True):
        super(OracleTimeflow, self).__init__()
        self._type = ("OracleTimeflow", True)
        self._cdb_timeflow = (self.__undef__, True)
        self._incarnation_id = (self.__undef__, True)
        self._parent_point = (self.__undef__, True)
        self._warehouse = (self.__undef__, True)
        self._warehouse_timeflow = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleTimeflow, cls).from_dict(data, dirty, undef_enabled)
        obj._cdb_timeflow = (data.get("cdbTimeflow", obj.__undef__), dirty)
        if obj._cdb_timeflow[0] is not None and obj._cdb_timeflow[0] is not obj.__undef__:
            assert isinstance(obj._cdb_timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cdb_timeflow[0], type(obj._cdb_timeflow[0])))
            common.validate_format(obj._cdb_timeflow[0], "objectReference", None, None)
        obj._incarnation_id = (data.get("incarnationID", obj.__undef__), dirty)
        if obj._incarnation_id[0] is not None and obj._incarnation_id[0] is not obj.__undef__:
            assert isinstance(obj._incarnation_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._incarnation_id[0], type(obj._incarnation_id[0])))
            common.validate_format(obj._incarnation_id[0], "None", None, None)
        if "parentPoint" in data and data["parentPoint"] is not None:
            obj._parent_point = (factory.create_object(data["parentPoint"], "OracleTimeflowPoint"), dirty)
            factory.validate_type(obj._parent_point[0], "OracleTimeflowPoint")
        else:
            obj._parent_point = (obj.__undef__, dirty)
        obj._warehouse = (data.get("warehouse", obj.__undef__), dirty)
        if obj._warehouse[0] is not None and obj._warehouse[0] is not obj.__undef__:
            assert isinstance(obj._warehouse[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._warehouse[0], type(obj._warehouse[0])))
            common.validate_format(obj._warehouse[0], "None", None, None)
        obj._warehouse_timeflow = (data.get("warehouseTimeflow", obj.__undef__), dirty)
        if obj._warehouse_timeflow[0] is not None and obj._warehouse_timeflow[0] is not obj.__undef__:
            assert isinstance(obj._warehouse_timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._warehouse_timeflow[0], type(obj._warehouse_timeflow[0])))
            common.validate_format(obj._warehouse_timeflow[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleTimeflow, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cdb_timeflow" == "type" or (self.cdb_timeflow is not self.__undef__ and (not (dirty and not self._cdb_timeflow[1]))):
            dct["cdbTimeflow"] = dictify(self.cdb_timeflow)
        if "incarnation_id" == "type" or (self.incarnation_id is not self.__undef__ and (not (dirty and not self._incarnation_id[1]))):
            dct["incarnationID"] = dictify(self.incarnation_id)
        if "parent_point" == "type" or (self.parent_point is not self.__undef__ and (not (dirty and not self._parent_point[1]))):
            dct["parentPoint"] = dictify(self.parent_point)
        if "warehouse" == "type" or (self.warehouse is not self.__undef__ and (not (dirty and not self._warehouse[1]))):
            dct["warehouse"] = dictify(self.warehouse)
        if "warehouse_timeflow" == "type" or (self.warehouse_timeflow is not self.__undef__ and (not (dirty and not self._warehouse_timeflow[1]))):
            dct["warehouseTimeflow"] = dictify(self.warehouse_timeflow)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cdb_timeflow = (self._cdb_timeflow[0], True)
        self._incarnation_id = (self._incarnation_id[0], True)
        self._parent_point = (self._parent_point[0], True)
        self._warehouse = (self._warehouse[0], True)
        self._warehouse_timeflow = (self._warehouse_timeflow[0], True)

    def is_dirty(self):
        return any([self._cdb_timeflow[1], self._incarnation_id[1], self._parent_point[1], self._warehouse[1], self._warehouse_timeflow[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleTimeflow):
            return False
        return super(OracleTimeflow, self).__eq__(other) and \
               self.cdb_timeflow == other.cdb_timeflow and \
               self.incarnation_id == other.incarnation_id and \
               self.parent_point == other.parent_point and \
               self.warehouse == other.warehouse and \
               self.warehouse_timeflow == other.warehouse_timeflow

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cdb_timeflow(self):
        """
        Reference to the mirror CDB TimeFlow if this is a PDB TimeFlow.

        :rtype: ``TEXT_TYPE``
        """
        return self._cdb_timeflow[0]

    @cdb_timeflow.setter
    def cdb_timeflow(self, value):
        self._cdb_timeflow = (value, True)

    @property
    def incarnation_id(self):
        """
        Oracle-specific incarnation identifier for this TimeFlow.

        :rtype: ``TEXT_TYPE``
        """
        return self._incarnation_id[0]

    @incarnation_id.setter
    def incarnation_id(self, value):
        self._incarnation_id = (value, True)

    @property
    def parent_point(self):
        """
        The origin point on the parent TimeFlow from which this TimeFlow was
        provisioned. This will not be present for TimeFlows derived from linked
        sources.

        :rtype: :py:class:`v1_6_1.web.vo.OracleTimeflowPoint`
        """
        return self._parent_point[0]

    @parent_point.setter
    def parent_point(self, value):
        self._parent_point = (value, True)

    @property
    def warehouse(self):
        """
        Set to true if the TimeFlow represents a warehouse.

        :rtype: ``bool``
        """
        return self._warehouse[0]

    @warehouse.setter
    def warehouse(self, value):
        self._warehouse = (value, True)

    @property
    def warehouse_timeflow(self):
        """
        Reference to the TimeFlow of the warehouse that this TimeFlow is a part
        of.

        :rtype: ``TEXT_TYPE``
        """
        return self._warehouse_timeflow[0]

    @warehouse_timeflow.setter
    def warehouse_timeflow(self, value):
        self._warehouse_timeflow = (value, True)

