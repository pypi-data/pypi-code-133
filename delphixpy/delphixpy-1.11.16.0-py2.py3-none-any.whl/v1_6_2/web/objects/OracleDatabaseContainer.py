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
#     /delphix-oracle-db-container.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_2.web.objects.DatabaseContainer import DatabaseContainer
from delphixpy.v1_6_2 import factory
from delphixpy.v1_6_2 import common

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

class OracleDatabaseContainer(DatabaseContainer):
    """
    *(extends* :py:class:`v1_6_2.web.vo.DatabaseContainer` *)* Data container
    for Oracle databases, both linked and virtual.
    """
    def __init__(self, undef_enabled=True):
        super(OracleDatabaseContainer, self).__init__()
        self._type = ("OracleDatabaseContainer", True)
        self._content_type = (self.__undef__, True)
        self._cross_platform_ready = (self.__undef__, True)
        self._database_fraction = (self.__undef__, True)
        self._diagnose_no_logging_faults = (self.__undef__, True)
        self._endianness = (self.__undef__, True)
        self._live_source = (self.__undef__, True)
        self._performance_mode = (self.__undef__, True)
        self._physical_standby = (self.__undef__, True)
        self._pre_provisioning_enabled = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._sourcing_policy = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleDatabaseContainer, cls).from_dict(data, dirty, undef_enabled)
        obj._content_type = (data.get("contentType", obj.__undef__), dirty)
        if obj._content_type[0] is not None and obj._content_type[0] is not obj.__undef__:
            assert isinstance(obj._content_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._content_type[0], type(obj._content_type[0])))
            assert obj._content_type[0] in ['PDB', 'ROOT_CDB', 'AUX_CDB', 'NON_CDB'], "Expected enum ['PDB', 'ROOT_CDB', 'AUX_CDB', 'NON_CDB'] but got %s" % obj._content_type[0]
            common.validate_format(obj._content_type[0], "None", None, None)
        obj._cross_platform_ready = (data.get("crossPlatformReady", obj.__undef__), dirty)
        if obj._cross_platform_ready[0] is not None and obj._cross_platform_ready[0] is not obj.__undef__:
            assert isinstance(obj._cross_platform_ready[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._cross_platform_ready[0], type(obj._cross_platform_ready[0])))
            common.validate_format(obj._cross_platform_ready[0], "None", None, None)
        obj._database_fraction = (data.get("databaseFraction", obj.__undef__), dirty)
        if obj._database_fraction[0] is not None and obj._database_fraction[0] is not obj.__undef__:
            assert isinstance(obj._database_fraction[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._database_fraction[0], type(obj._database_fraction[0])))
            common.validate_format(obj._database_fraction[0], "None", None, None)
        obj._diagnose_no_logging_faults = (data.get("diagnoseNoLoggingFaults", obj.__undef__), dirty)
        if obj._diagnose_no_logging_faults[0] is not None and obj._diagnose_no_logging_faults[0] is not obj.__undef__:
            assert isinstance(obj._diagnose_no_logging_faults[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._diagnose_no_logging_faults[0], type(obj._diagnose_no_logging_faults[0])))
            common.validate_format(obj._diagnose_no_logging_faults[0], "None", None, None)
        obj._endianness = (data.get("endianness", obj.__undef__), dirty)
        if obj._endianness[0] is not None and obj._endianness[0] is not obj.__undef__:
            assert isinstance(obj._endianness[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._endianness[0], type(obj._endianness[0])))
            assert obj._endianness[0] in ['BIG_ENDIAN', 'LITTLE_ENDIAN'], "Expected enum ['BIG_ENDIAN', 'LITTLE_ENDIAN'] but got %s" % obj._endianness[0]
            common.validate_format(obj._endianness[0], "None", None, None)
        obj._live_source = (data.get("liveSource", obj.__undef__), dirty)
        if obj._live_source[0] is not None and obj._live_source[0] is not obj.__undef__:
            assert isinstance(obj._live_source[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._live_source[0], type(obj._live_source[0])))
            common.validate_format(obj._live_source[0], "None", None, None)
        obj._performance_mode = (data.get("performanceMode", obj.__undef__), dirty)
        if obj._performance_mode[0] is not None and obj._performance_mode[0] is not obj.__undef__:
            assert isinstance(obj._performance_mode[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._performance_mode[0], type(obj._performance_mode[0])))
            assert obj._performance_mode[0] in ['ENABLED', 'DISABLED'], "Expected enum ['ENABLED', 'DISABLED'] but got %s" % obj._performance_mode[0]
            common.validate_format(obj._performance_mode[0], "None", None, None)
        obj._physical_standby = (data.get("physicalStandby", obj.__undef__), dirty)
        if obj._physical_standby[0] is not None and obj._physical_standby[0] is not obj.__undef__:
            assert isinstance(obj._physical_standby[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._physical_standby[0], type(obj._physical_standby[0])))
            common.validate_format(obj._physical_standby[0], "None", None, None)
        obj._pre_provisioning_enabled = (data.get("preProvisioningEnabled", obj.__undef__), dirty)
        if obj._pre_provisioning_enabled[0] is not None and obj._pre_provisioning_enabled[0] is not obj.__undef__:
            assert isinstance(obj._pre_provisioning_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._pre_provisioning_enabled[0], type(obj._pre_provisioning_enabled[0])))
            common.validate_format(obj._pre_provisioning_enabled[0], "None", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "OracleDBContainerRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "OracleDBContainerRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        if "sourcingPolicy" in data and data["sourcingPolicy"] is not None:
            obj._sourcing_policy = (factory.create_object(data["sourcingPolicy"], "OracleSourcingPolicy"), dirty)
            factory.validate_type(obj._sourcing_policy[0], "OracleSourcingPolicy")
        else:
            obj._sourcing_policy = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleDatabaseContainer, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "content_type" == "type" or (self.content_type is not self.__undef__ and (not (dirty and not self._content_type[1]))):
            dct["contentType"] = dictify(self.content_type)
        if "cross_platform_ready" == "type" or (self.cross_platform_ready is not self.__undef__ and (not (dirty and not self._cross_platform_ready[1]))):
            dct["crossPlatformReady"] = dictify(self.cross_platform_ready)
        if "database_fraction" == "type" or (self.database_fraction is not self.__undef__ and (not (dirty and not self._database_fraction[1]))):
            dct["databaseFraction"] = dictify(self.database_fraction)
        if "diagnose_no_logging_faults" == "type" or (self.diagnose_no_logging_faults is not self.__undef__ and (not (dirty and not self._diagnose_no_logging_faults[1]) or isinstance(self.diagnose_no_logging_faults, list) or belongs_to_parent)):
            dct["diagnoseNoLoggingFaults"] = dictify(self.diagnose_no_logging_faults)
        elif belongs_to_parent and self.diagnose_no_logging_faults is self.__undef__:
            dct["diagnoseNoLoggingFaults"] = True
        if "endianness" == "type" or (self.endianness is not self.__undef__ and (not (dirty and not self._endianness[1]))):
            dct["endianness"] = dictify(self.endianness)
        if "live_source" == "type" or (self.live_source is not self.__undef__ and (not (dirty and not self._live_source[1]))):
            dct["liveSource"] = dictify(self.live_source)
        if "performance_mode" == "type" or (self.performance_mode is not self.__undef__ and (not (dirty and not self._performance_mode[1]) or isinstance(self.performance_mode, list) or belongs_to_parent)):
            dct["performanceMode"] = dictify(self.performance_mode)
        elif belongs_to_parent and self.performance_mode is self.__undef__:
            dct["performanceMode"] = "DISABLED"
        if "physical_standby" == "type" or (self.physical_standby is not self.__undef__ and (not (dirty and not self._physical_standby[1]))):
            dct["physicalStandby"] = dictify(self.physical_standby)
        if "pre_provisioning_enabled" == "type" or (self.pre_provisioning_enabled is not self.__undef__ and (not (dirty and not self._pre_provisioning_enabled[1]) or isinstance(self.pre_provisioning_enabled, list) or belongs_to_parent)):
            dct["preProvisioningEnabled"] = dictify(self.pre_provisioning_enabled)
        elif belongs_to_parent and self.pre_provisioning_enabled is self.__undef__:
            dct["preProvisioningEnabled"] = False
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "sourcing_policy" == "type" or (self.sourcing_policy is not self.__undef__ and (not (dirty and not self._sourcing_policy[1]) or isinstance(self.sourcing_policy, list) or belongs_to_parent)):
            dct["sourcingPolicy"] = dictify(self.sourcing_policy, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._content_type = (self._content_type[0], True)
        self._cross_platform_ready = (self._cross_platform_ready[0], True)
        self._database_fraction = (self._database_fraction[0], True)
        self._diagnose_no_logging_faults = (self._diagnose_no_logging_faults[0], True)
        self._endianness = (self._endianness[0], True)
        self._live_source = (self._live_source[0], True)
        self._performance_mode = (self._performance_mode[0], True)
        self._physical_standby = (self._physical_standby[0], True)
        self._pre_provisioning_enabled = (self._pre_provisioning_enabled[0], True)
        self._runtime = (self._runtime[0], True)
        self._sourcing_policy = (self._sourcing_policy[0], True)

    def is_dirty(self):
        return any([self._content_type[1], self._cross_platform_ready[1], self._database_fraction[1], self._diagnose_no_logging_faults[1], self._endianness[1], self._live_source[1], self._performance_mode[1], self._physical_standby[1], self._pre_provisioning_enabled[1], self._runtime[1], self._sourcing_policy[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleDatabaseContainer):
            return False
        return super(OracleDatabaseContainer, self).__eq__(other) and \
               self.content_type == other.content_type and \
               self.cross_platform_ready == other.cross_platform_ready and \
               self.database_fraction == other.database_fraction and \
               self.diagnose_no_logging_faults == other.diagnose_no_logging_faults and \
               self.endianness == other.endianness and \
               self.live_source == other.live_source and \
               self.performance_mode == other.performance_mode and \
               self.physical_standby == other.physical_standby and \
               self.pre_provisioning_enabled == other.pre_provisioning_enabled and \
               self.runtime == other.runtime and \
               self.sourcing_policy == other.sourcing_policy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def content_type(self):
        """
        Indicates whether this container is for a PDB, CDB root, auxiliary CDB,
        or non-CDB. *(permitted values: PDB, ROOT_CDB, AUX_CDB, NON_CDB)*

        :rtype: ``TEXT_TYPE``
        """
        return self._content_type[0]

    @content_type.setter
    def content_type(self, value):
        self._content_type = (value, True)

    @property
    def cross_platform_ready(self):
        """
        Indicates whether or not this container is ready for cross-platform
        provisioning.

        :rtype: ``bool``
        """
        return self._cross_platform_ready[0]

    @cross_platform_ready.setter
    def cross_platform_ready(self, value):
        self._cross_platform_ready = (value, True)

    @property
    def database_fraction(self):
        """
        Indicates whether or not the database in this container consists only
        of transportable tablespaces.

        :rtype: ``bool``
        """
        return self._database_fraction[0]

    @database_fraction.setter
    def database_fraction(self, value):
        self._database_fraction = (value, True)

    @property
    def diagnose_no_logging_faults(self):
        """
        *(default value: True)* If true, NOLOGGING operations on this container
        are treated as faults and cannot be resolved manually. Otherwise, these
        operations are ignored.

        :rtype: ``bool``
        """
        return self._diagnose_no_logging_faults[0]

    @diagnose_no_logging_faults.setter
    def diagnose_no_logging_faults(self, value):
        self._diagnose_no_logging_faults = (value, True)

    @property
    def endianness(self):
        """
        Native endianness of the original database source system. *(permitted
        values: BIG_ENDIAN, LITTLE_ENDIAN)*

        :rtype: ``TEXT_TYPE``
        """
        return self._endianness[0]

    @endianness.setter
    def endianness(self, value):
        self._endianness = (value, True)

    @property
    def live_source(self):
        """
        Indicates whether or not this container has an associated LiveSource.

        :rtype: ``bool``
        """
        return self._live_source[0]

    @live_source.setter
    def live_source(self, value):
        self._live_source = (value, True)

    @property
    def performance_mode(self):
        """
        *(default value: DISABLED)* Whether to enable high performance mode.
        *(permitted values: ENABLED, DISABLED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._performance_mode[0]

    @performance_mode.setter
    def performance_mode(self, value):
        self._performance_mode = (value, True)

    @property
    def physical_standby(self):
        """
        Indicates whether or not the database in this container is a physical
        standby.

        :rtype: ``bool``
        """
        return self._physical_standby[0]

    @physical_standby.setter
    def physical_standby(self, value):
        self._physical_standby = (value, True)

    @property
    def pre_provisioning_enabled(self):
        """
        If true, pre-provisioning will be performed after every sync.

        :rtype: ``bool``
        """
        return self._pre_provisioning_enabled[0]

    @pre_provisioning_enabled.setter
    def pre_provisioning_enabled(self, value):
        self._pre_provisioning_enabled = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this container.

        :rtype: :py:class:`v1_6_2.web.vo.OracleDBContainerRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def sourcing_policy(self):
        """
        Policies for managing LogSync and SnapSync across sources.

        :rtype: :py:class:`v1_6_2.web.vo.OracleSourcingPolicy`
        """
        return self._sourcing_policy[0]

    @sourcing_policy.setter
    def sourcing_policy(self, value):
        self._sourcing_policy = (value, True)

