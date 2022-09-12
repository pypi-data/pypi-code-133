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
#     /delphix-source-type-aggregate-ingested-size.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_14.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_14 import common

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

class SourceTypeAggregateIngestedSize(TypedObject):
    """
    *(extends* :py:class:`v1_11_14.web.vo.TypedObject` *)* An aggregation for a
    type of source.
    """
    def __init__(self, undef_enabled=True):
        super(SourceTypeAggregateIngestedSize, self).__init__()
        self._type = ("SourceTypeAggregateIngestedSize", True)
        self._aggregate_size = (self.__undef__, True)
        self._container_type = (self.__undef__, True)
        self._aggregate_label = (self.__undef__, True)
        self._manual_query = (self.__undef__, True)

    API_VERSION = "1.11.14"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceTypeAggregateIngestedSize, cls).from_dict(data, dirty, undef_enabled)
        obj._aggregate_size = (data.get("aggregateSize", obj.__undef__), dirty)
        if obj._aggregate_size[0] is not None and obj._aggregate_size[0] is not obj.__undef__:
            assert isinstance(obj._aggregate_size[0], float), ("Expected one of ['number', 'null'], but got %s of type %s" % (obj._aggregate_size[0], type(obj._aggregate_size[0])))
            common.validate_format(obj._aggregate_size[0], "None", None, None)
        obj._container_type = (data.get("containerType", obj.__undef__), dirty)
        if obj._container_type[0] is not None and obj._container_type[0] is not obj.__undef__:
            assert isinstance(obj._container_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container_type[0], type(obj._container_type[0])))
            assert obj._container_type[0] in ['APPDATA_CONTAINER', 'ASE_DB_CONTAINER', 'ORACLE_DB_CONTAINER', 'MSSQL_DB_CONTAINER', 'MYSQL_DB_CONTAINER', 'PGSQL_DB_CONTAINER'], "Expected enum ['APPDATA_CONTAINER', 'ASE_DB_CONTAINER', 'ORACLE_DB_CONTAINER', 'MSSQL_DB_CONTAINER', 'MYSQL_DB_CONTAINER', 'PGSQL_DB_CONTAINER'] but got %s" % obj._container_type[0]
            common.validate_format(obj._container_type[0], "None", None, None)
        obj._aggregate_label = (data.get("aggregateLabel", obj.__undef__), dirty)
        if obj._aggregate_label[0] is not None and obj._aggregate_label[0] is not obj.__undef__:
            assert isinstance(obj._aggregate_label[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._aggregate_label[0], type(obj._aggregate_label[0])))
            common.validate_format(obj._aggregate_label[0], "None", None, None)
        obj._manual_query = (data.get("manualQuery", obj.__undef__), dirty)
        if obj._manual_query[0] is not None and obj._manual_query[0] is not obj.__undef__:
            assert isinstance(obj._manual_query[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._manual_query[0], type(obj._manual_query[0])))
            common.validate_format(obj._manual_query[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceTypeAggregateIngestedSize, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "aggregate_size" == "type" or (self.aggregate_size is not self.__undef__ and (not (dirty and not self._aggregate_size[1]))):
            dct["aggregateSize"] = dictify(self.aggregate_size)
        if dirty and "aggregateSize" in dct:
            del dct["aggregateSize"]
        if "container_type" == "type" or (self.container_type is not self.__undef__ and (not (dirty and not self._container_type[1]))):
            dct["containerType"] = dictify(self.container_type)
        if dirty and "containerType" in dct:
            del dct["containerType"]
        if "aggregate_label" == "type" or (self.aggregate_label is not self.__undef__ and (not (dirty and not self._aggregate_label[1]))):
            dct["aggregateLabel"] = dictify(self.aggregate_label)
        if dirty and "aggregateLabel" in dct:
            del dct["aggregateLabel"]
        if "manual_query" == "type" or (self.manual_query is not self.__undef__ and (not (dirty and not self._manual_query[1]))):
            dct["manualQuery"] = dictify(self.manual_query)
        if dirty and "manualQuery" in dct:
            del dct["manualQuery"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._aggregate_size = (self._aggregate_size[0], True)
        self._container_type = (self._container_type[0], True)
        self._aggregate_label = (self._aggregate_label[0], True)
        self._manual_query = (self._manual_query[0], True)

    def is_dirty(self):
        return any([self._aggregate_size[1], self._container_type[1], self._aggregate_label[1], self._manual_query[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceTypeAggregateIngestedSize):
            return False
        return super(SourceTypeAggregateIngestedSize, self).__eq__(other) and \
               self.aggregate_size == other.aggregate_size and \
               self.container_type == other.container_type and \
               self.aggregate_label == other.aggregate_label and \
               self.manual_query == other.manual_query

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            super(SourceTypeAggregateIngestedSize, self).__hash__(),
            self.aggregate_size,
            self.container_type,
            self.aggregate_label,
            self.manual_query,
        )

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def aggregate_size(self):
        """
        The aggregate ingested source size for a type of source. This value
        will be null if we do not collect data on that type of source.

        :rtype: ``float`` *or* ``null``
        """
        return self._aggregate_size[0]

    @property
    def container_type(self):
        """
        Type of container. *(permitted values: APPDATA_CONTAINER,
        ASE_DB_CONTAINER, ORACLE_DB_CONTAINER, MSSQL_DB_CONTAINER,
        MYSQL_DB_CONTAINER, PGSQL_DB_CONTAINER)*

        :rtype: ``TEXT_TYPE``
        """
        return self._container_type[0]

    @property
    def aggregate_label(self):
        """
        Human readable description of containerType. E.g. Oracle.

        :rtype: ``TEXT_TYPE``
        """
        return self._aggregate_label[0]

    @property
    def manual_query(self):
        """
        Query that can be executed on the source to return the Usage. If this
        field is null, refer to the Delphix Pricing Guide for more information.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._manual_query[0]

