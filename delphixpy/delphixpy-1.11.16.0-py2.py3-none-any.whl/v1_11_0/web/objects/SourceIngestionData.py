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
#     /delphix-source-ingestion-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_0 import common

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

class SourceIngestionData(TypedObject):
    """
    *(extends* :py:class:`v1_11_0.web.vo.TypedObject` *)* Objects that map each
    Source to information about its ingested size.
    """
    def __init__(self, undef_enabled=True):
        super(SourceIngestionData, self).__init__()
        self._type = ("SourceIngestionData", True)
        self._source_name = (self.__undef__, True)
        self._container_type = (self.__undef__, True)
        self._timestamp = (self.__undef__, True)
        self._fallback_ingested_size_timestamp = (self.__undef__, True)
        self._ingested_size = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceIngestionData, cls).from_dict(data, dirty, undef_enabled)
        obj._source_name = (data.get("sourceName", obj.__undef__), dirty)
        if obj._source_name[0] is not None and obj._source_name[0] is not obj.__undef__:
            assert isinstance(obj._source_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_name[0], type(obj._source_name[0])))
            common.validate_format(obj._source_name[0], "None", None, None)
        obj._container_type = (data.get("containerType", obj.__undef__), dirty)
        if obj._container_type[0] is not None and obj._container_type[0] is not obj.__undef__:
            assert isinstance(obj._container_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container_type[0], type(obj._container_type[0])))
            assert obj._container_type[0] in ['APPDATA_CONTAINER', 'ASE_DB_CONTAINER', 'ORACLE_DB_CONTAINER', 'MSSQL_DB_CONTAINER', 'MYSQL_DB_CONTAINER', 'PGSQL_DB_CONTAINER', 'VMWARE_CONTAINER'], "Expected enum ['APPDATA_CONTAINER', 'ASE_DB_CONTAINER', 'ORACLE_DB_CONTAINER', 'MSSQL_DB_CONTAINER', 'MYSQL_DB_CONTAINER', 'PGSQL_DB_CONTAINER', 'VMWARE_CONTAINER'] but got %s" % obj._container_type[0]
            common.validate_format(obj._container_type[0], "None", None, None)
        obj._timestamp = (data.get("timestamp", obj.__undef__), dirty)
        if obj._timestamp[0] is not None and obj._timestamp[0] is not obj.__undef__:
            assert isinstance(obj._timestamp[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._timestamp[0], type(obj._timestamp[0])))
            common.validate_format(obj._timestamp[0], "date", None, None)
        obj._fallback_ingested_size_timestamp = (data.get("fallbackIngestedSizeTimestamp", obj.__undef__), dirty)
        if obj._fallback_ingested_size_timestamp[0] is not None and obj._fallback_ingested_size_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._fallback_ingested_size_timestamp[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._fallback_ingested_size_timestamp[0], type(obj._fallback_ingested_size_timestamp[0])))
            common.validate_format(obj._fallback_ingested_size_timestamp[0], "date", None, None)
        obj._ingested_size = (data.get("ingestedSize", obj.__undef__), dirty)
        if obj._ingested_size[0] is not None and obj._ingested_size[0] is not obj.__undef__:
            assert isinstance(obj._ingested_size[0], float), ("Expected one of ['number', 'null'], but got %s of type %s" % (obj._ingested_size[0], type(obj._ingested_size[0])))
            common.validate_format(obj._ingested_size[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceIngestionData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source_name" == "type" or (self.source_name is not self.__undef__ and (not (dirty and not self._source_name[1]))):
            dct["sourceName"] = dictify(self.source_name)
        if dirty and "sourceName" in dct:
            del dct["sourceName"]
        if "container_type" == "type" or (self.container_type is not self.__undef__ and (not (dirty and not self._container_type[1]))):
            dct["containerType"] = dictify(self.container_type)
        if dirty and "containerType" in dct:
            del dct["containerType"]
        if "timestamp" == "type" or (self.timestamp is not self.__undef__ and (not (dirty and not self._timestamp[1]))):
            dct["timestamp"] = dictify(self.timestamp)
        if dirty and "timestamp" in dct:
            del dct["timestamp"]
        if "fallback_ingested_size_timestamp" == "type" or (self.fallback_ingested_size_timestamp is not self.__undef__ and (not (dirty and not self._fallback_ingested_size_timestamp[1]))):
            dct["fallbackIngestedSizeTimestamp"] = dictify(self.fallback_ingested_size_timestamp)
        if dirty and "fallbackIngestedSizeTimestamp" in dct:
            del dct["fallbackIngestedSizeTimestamp"]
        if "ingested_size" == "type" or (self.ingested_size is not self.__undef__ and (not (dirty and not self._ingested_size[1]))):
            dct["ingestedSize"] = dictify(self.ingested_size)
        if dirty and "ingestedSize" in dct:
            del dct["ingestedSize"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source_name = (self._source_name[0], True)
        self._container_type = (self._container_type[0], True)
        self._timestamp = (self._timestamp[0], True)
        self._fallback_ingested_size_timestamp = (self._fallback_ingested_size_timestamp[0], True)
        self._ingested_size = (self._ingested_size[0], True)

    def is_dirty(self):
        return any([self._source_name[1], self._container_type[1], self._timestamp[1], self._fallback_ingested_size_timestamp[1], self._ingested_size[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceIngestionData):
            return False
        return super(SourceIngestionData, self).__eq__(other) and \
               self.source_name == other.source_name and \
               self.container_type == other.container_type and \
               self.timestamp == other.timestamp and \
               self.fallback_ingested_size_timestamp == other.fallback_ingested_size_timestamp and \
               self.ingested_size == other.ingested_size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            super(SourceIngestionData, self).__hash__(),
            self.source_name,
            self.container_type,
            self.timestamp,
            self.fallback_ingested_size_timestamp,
            self.ingested_size,
        )

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source_name(self):
        """
        Source name.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_name[0]

    @property
    def container_type(self):
        """
        Container type for this source. *(permitted values: APPDATA_CONTAINER,
        ASE_DB_CONTAINER, ORACLE_DB_CONTAINER, MSSQL_DB_CONTAINER,
        MYSQL_DB_CONTAINER, PGSQL_DB_CONTAINER, VMWARE_CONTAINER)*

        :rtype: ``TEXT_TYPE``
        """
        return self._container_type[0]

    @property
    def timestamp(self):
        """
        Time at which this data was collected. This will be null if the source
        was offline and there was no fallback data to use.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._timestamp[0]

    @property
    def fallback_ingested_size_timestamp(self):
        """
        Collection timestamp of the fallback value that used for the ingested
        size calculation of this object. Will be null if no fallback data was
        used.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._fallback_ingested_size_timestamp[0]

    @property
    def ingested_size(self):
        """
        Ingested size. This value will be null if we do not collect data on
        that type of source or the source was offline and no fallback data was
        used.

        :rtype: ``float`` *or* ``null``
        """
        return self._ingested_size[0]

