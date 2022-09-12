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
#     /delphix-oracle-pdb-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.OracleBaseDBConfig import OracleBaseDBConfig
from delphixpy.v1_10_2 import common

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

class OraclePDBConfig(OracleBaseDBConfig):
    """
    *(extends* :py:class:`v1_10_2.web.vo.OracleBaseDBConfig` *)* Representation
    of properties for an Oracle pluggable database configuration.
    """
    def __init__(self, undef_enabled=True):
        super(OraclePDBConfig, self).__init__()
        self._type = ("OraclePDBConfig", True)
        self._database_name = (self.__undef__, True)
        self._cdb_config = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OraclePDBConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._database_name = (data.get("databaseName", obj.__undef__), dirty)
        if obj._database_name[0] is not None and obj._database_name[0] is not obj.__undef__:
            assert isinstance(obj._database_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_name[0], type(obj._database_name[0])))
            common.validate_format(obj._database_name[0], "None", None, 30)
        obj._cdb_config = (data.get("cdbConfig", obj.__undef__), dirty)
        if obj._cdb_config[0] is not None and obj._cdb_config[0] is not obj.__undef__:
            assert isinstance(obj._cdb_config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cdb_config[0], type(obj._cdb_config[0])))
            common.validate_format(obj._cdb_config[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OraclePDBConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "database_name" == "type" or (self.database_name is not self.__undef__ and (not (dirty and not self._database_name[1]) or isinstance(self.database_name, list) or belongs_to_parent)):
            dct["databaseName"] = dictify(self.database_name)
        if "cdb_config" == "type" or (self.cdb_config is not self.__undef__ and (not (dirty and not self._cdb_config[1]) or isinstance(self.cdb_config, list) or belongs_to_parent)):
            dct["cdbConfig"] = dictify(self.cdb_config)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._database_name = (self._database_name[0], True)
        self._cdb_config = (self._cdb_config[0], True)

    def is_dirty(self):
        return any([self._database_name[1], self._cdb_config[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OraclePDBConfig):
            return False
        return super(OraclePDBConfig, self).__eq__(other) and \
               self.database_name == other.database_name and \
               self.cdb_config == other.cdb_config

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def database_name(self):
        """
        The name of the database.

        :rtype: ``TEXT_TYPE``
        """
        return self._database_name[0]

    @database_name.setter
    def database_name(self, value):
        self._database_name = (value, True)

    @property
    def cdb_config(self):
        """
        The DB config of an Oracle multitenant database this pluggable database
        belongs to.

        :rtype: ``TEXT_TYPE``
        """
        return self._cdb_config[0]

    @cdb_config.setter
    def cdb_config(self, value):
        self._cdb_config = (value, True)

