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
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.ExportParameters import ExportParameters
from delphixpy import factory
from delphixpy import common

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

class OracleExportAsmParameters(ExportParameters):
    """
    *(extends* :py:class:`delphixpy.web.vo.ExportParameters` *)* The parameters
    to use as input to export Oracle databases to ASM.
    """
    def __init__(self, undef_enabled=True):
        super(OracleExportAsmParameters, self).__init__()
        self._type = ("OracleExportAsmParameters", True)
        self._source_config = (self.__undef__, True)
        self._data_diskgroup = (self.__undef__, True)
        self._parallel = (self.__undef__, True)
        self._redo_diskgroup = (self.__undef__, True)
        self._source = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleExportAsmParameters, cls).from_dict(data, dirty, undef_enabled)
        if "sourceConfig" not in data:
            raise ValueError("Missing required property \"sourceConfig\".")
        if "sourceConfig" in data and data["sourceConfig"] is not None:
            obj._source_config = (factory.create_object(data["sourceConfig"], "OracleDBConfig"), dirty)
            factory.validate_type(obj._source_config[0], "OracleDBConfig")
        else:
            obj._source_config = (obj.__undef__, dirty)
        if "dataDiskgroup" not in data:
            raise ValueError("Missing required property \"dataDiskgroup\".")
        obj._data_diskgroup = (data.get("dataDiskgroup", obj.__undef__), dirty)
        if obj._data_diskgroup[0] is not None and obj._data_diskgroup[0] is not obj.__undef__:
            assert isinstance(obj._data_diskgroup[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_diskgroup[0], type(obj._data_diskgroup[0])))
            common.validate_format(obj._data_diskgroup[0], "None", None, None)
        obj._parallel = (data.get("parallel", obj.__undef__), dirty)
        if obj._parallel[0] is not None and obj._parallel[0] is not obj.__undef__:
            assert isinstance(obj._parallel[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._parallel[0], type(obj._parallel[0])))
            common.validate_format(obj._parallel[0], "None", None, None)
        obj._redo_diskgroup = (data.get("redoDiskgroup", obj.__undef__), dirty)
        if obj._redo_diskgroup[0] is not None and obj._redo_diskgroup[0] is not obj.__undef__:
            assert isinstance(obj._redo_diskgroup[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._redo_diskgroup[0], type(obj._redo_diskgroup[0])))
            common.validate_format(obj._redo_diskgroup[0], "None", None, None)
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "OracleVirtualSource"), dirty)
            factory.validate_type(obj._source[0], "OracleVirtualSource")
        else:
            obj._source = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleExportAsmParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source_config" == "type" or (self.source_config is not self.__undef__ and (not (dirty and not self._source_config[1]) or isinstance(self.source_config, list) or belongs_to_parent)):
            dct["sourceConfig"] = dictify(self.source_config, prop_is_list_or_vo=True)
        if "data_diskgroup" == "type" or (self.data_diskgroup is not self.__undef__ and (not (dirty and not self._data_diskgroup[1]) or isinstance(self.data_diskgroup, list) or belongs_to_parent)):
            dct["dataDiskgroup"] = dictify(self.data_diskgroup)
        if "parallel" == "type" or (self.parallel is not self.__undef__ and (not (dirty and not self._parallel[1]) or isinstance(self.parallel, list) or belongs_to_parent)):
            dct["parallel"] = dictify(self.parallel)
        elif belongs_to_parent and self.parallel is self.__undef__:
            dct["parallel"] = 8
        if "redo_diskgroup" == "type" or (self.redo_diskgroup is not self.__undef__ and (not (dirty and not self._redo_diskgroup[1]) or isinstance(self.redo_diskgroup, list) or belongs_to_parent)):
            dct["redoDiskgroup"] = dictify(self.redo_diskgroup)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source_config = (self._source_config[0], True)
        self._data_diskgroup = (self._data_diskgroup[0], True)
        self._parallel = (self._parallel[0], True)
        self._redo_diskgroup = (self._redo_diskgroup[0], True)
        self._source = (self._source[0], True)

    def is_dirty(self):
        return any([self._source_config[1], self._data_diskgroup[1], self._parallel[1], self._redo_diskgroup[1], self._source[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleExportAsmParameters):
            return False
        return super(OracleExportAsmParameters, self).__eq__(other) and \
               self.source_config == other.source_config and \
               self.data_diskgroup == other.data_diskgroup and \
               self.parallel == other.parallel and \
               self.redo_diskgroup == other.redo_diskgroup and \
               self.source == other.source

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source_config(self):
        """
        The source config to use when creating the exported DB.

        :rtype: :py:class:`delphixpy.web.vo.OracleDBConfig`
        """
        return self._source_config[0]

    @source_config.setter
    def source_config(self, value):
        self._source_config = (value, True)

    @property
    def data_diskgroup(self):
        """
        The target ASM disk group for data, server parameter and control files.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_diskgroup[0]

    @data_diskgroup.setter
    def data_diskgroup(self, value):
        self._data_diskgroup = (value, True)

    @property
    def parallel(self):
        """
        *(default value: 8)* The number of RMAN channels used to move the VDB
        to ASM.

        :rtype: ``int``
        """
        return self._parallel[0]

    @parallel.setter
    def parallel(self, value):
        self._parallel = (value, True)

    @property
    def redo_diskgroup(self):
        """
        The target ASM disk group for redo log files.

        :rtype: ``TEXT_TYPE``
        """
        return self._redo_diskgroup[0]

    @redo_diskgroup.setter
    def redo_diskgroup(self, value):
        self._redo_diskgroup = (value, True)

    @property
    def source(self):
        """
        The Oracle source that describes an external dataset instance. This can
        be used to specify additional parameters for the VDB to move.
        Otherwise, provision defaults are used.

        :rtype: :py:class:`delphixpy.web.vo.OracleVirtualSource`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

