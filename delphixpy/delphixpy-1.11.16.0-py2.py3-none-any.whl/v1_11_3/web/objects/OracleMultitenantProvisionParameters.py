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
#     /delphix-oracle-multitenant-provision-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.OracleBaseProvisionParameters import OracleBaseProvisionParameters
from delphixpy.v1_11_3 import factory
from delphixpy.v1_11_3 import common

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

class OracleMultitenantProvisionParameters(OracleBaseProvisionParameters):
    """
    *(extends* :py:class:`v1_11_3.web.vo.OracleBaseProvisionParameters` *)* The
    parameters to use as input to provision Oracle multitenant databases.
    """
    def __init__(self, undef_enabled=True):
        super(OracleMultitenantProvisionParameters, self).__init__()
        self._type = ("OracleMultitenantProvisionParameters", True)
        self._source_config = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._virtual_cdb = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleMultitenantProvisionParameters, cls).from_dict(data, dirty, undef_enabled)
        if "sourceConfig" not in data:
            raise ValueError("Missing required property \"sourceConfig\".")
        if "sourceConfig" in data and data["sourceConfig"] is not None:
            obj._source_config = (factory.create_object(data["sourceConfig"], "OraclePDBConfig"), dirty)
            factory.validate_type(obj._source_config[0], "OraclePDBConfig")
        else:
            obj._source_config = (obj.__undef__, dirty)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "OracleVirtualPdbSource"), dirty)
            factory.validate_type(obj._source[0], "OracleVirtualPdbSource")
        else:
            obj._source = (obj.__undef__, dirty)
        if "virtualCdb" in data and data["virtualCdb"] is not None:
            obj._virtual_cdb = (factory.create_object(data["virtualCdb"], "OracleVirtualCdbProvisionParameters"), dirty)
            factory.validate_type(obj._virtual_cdb[0], "OracleVirtualCdbProvisionParameters")
        else:
            obj._virtual_cdb = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleMultitenantProvisionParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source_config" == "type" or (self.source_config is not self.__undef__ and (not (dirty and not self._source_config[1]) or isinstance(self.source_config, list) or belongs_to_parent)):
            dct["sourceConfig"] = dictify(self.source_config, prop_is_list_or_vo=True)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        if "virtual_cdb" == "type" or (self.virtual_cdb is not self.__undef__ and (not (dirty and not self._virtual_cdb[1]) or isinstance(self.virtual_cdb, list) or belongs_to_parent)):
            dct["virtualCdb"] = dictify(self.virtual_cdb, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source_config = (self._source_config[0], True)
        self._source = (self._source[0], True)
        self._virtual_cdb = (self._virtual_cdb[0], True)

    def is_dirty(self):
        return any([self._source_config[1], self._source[1], self._virtual_cdb[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleMultitenantProvisionParameters):
            return False
        return super(OracleMultitenantProvisionParameters, self).__eq__(other) and \
               self.source_config == other.source_config and \
               self.source == other.source and \
               self.virtual_cdb == other.virtual_cdb

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source_config(self):
        """
        The pluggable database source config including dynamically discovered
        attributes of the source.

        :rtype: :py:class:`v1_11_3.web.vo.OraclePDBConfig`
        """
        return self._source_config[0]

    @source_config.setter
    def source_config(self, value):
        self._source_config = (value, True)

    @property
    def source(self):
        """
        The pluggable database source that describes an external database
        instance.

        :rtype: :py:class:`v1_11_3.web.vo.OracleVirtualPdbSource`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def virtual_cdb(self):
        """
        The new container for the created dataset.

        :rtype: :py:class:`v1_11_3.web.vo.OracleVirtualCdbProvisionParameters`
        """
        return self._virtual_cdb[0]

    @virtual_cdb.setter
    def virtual_cdb(self, value):
        self._virtual_cdb = (value, True)

