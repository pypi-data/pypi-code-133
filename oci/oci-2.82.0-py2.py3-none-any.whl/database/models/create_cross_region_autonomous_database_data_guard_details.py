# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCrossRegionAutonomousDatabaseDataGuardDetails(CreateAutonomousDatabaseBase):
    """
    Details to create an Autonomous Data Guard association for an existing Autonomous Database where the standby is in a different (remote) region from the source primary database.
    *IMPORTANT*
    Note the following for creating standby databases in cross-region Autonomous Data Guard associations:
    - To create your standby database in a region different from the region of the primary, use the API endpoint of the region in which the standby will be located. For example, if the primary database is in the IAD region, and you want to create the standby in the PHX region, make the API call using the PHX endpoint (https://database.us-phoenix-1.oraclecloud.com). See `API Endpoints`__ for the list of Database Service API endpoints.
    - In the request to create the standby database, the `sourceId` value should be the OCID of the primary database.
    The following parameters are required for the cross-region standby database and must contain the same values as the source Autonomous Database:
    - dbName
    - cpuCoreCount
    - dataStorageSizeInTB
    - dbVersion
    The following parameters are optional for the cross-region standby database. If included in the request, these parameters contain the same values as the source Autonomous Database:
    - customerContacts
    - scheduledOperations
    - isAutoScalingForStorageEnabled
    - definedTags
    - freeformTags
    - licenseModel
    - whitelistedIps
    - isMtlsConnectionRequired
    Example I - Creating a cross-region standby with required parameters only:
    `{
    \"compartmentId\": \"ocid.compartment.oc1..<var>&lt;unique_ID&gt;</var>\",
    \"cpuCoreCount\": 1,
    \"dbName\": \"adatabasedb1\",
    \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..<var>&lt;unique_ID&gt;</var>\",
    \"dataStorageSizeInTBs\": 1,
    \"source\": \"CROSS_REGION_DATAGUARD\",
    \"adminPassword\" : \"<var>&lt;password&gt;</var>\",
    }`
    Example II - Creating a cross-region standby that specifies optional parameters in addition to the required parameters:
    `{
    \"compartmentId\": \"ocid.compartment.oc1..<var>&lt;unique_ID&gt;</var>\",
    \"cpuCoreCount\": 1,
    \"dbName\": \"adatabasedb1\",
    \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..<var>&lt;unique_ID&gt;</var>\",
    \"dataStorageSizeInTBs\": 1,
    \"source\": \"CROSS_REGION_DATAGUARD\",
    \"adminPassword\" : \"<var>&lt;password&gt;</var>\",
    \"dbVersion\": \"19c\",
    \"licenseModel\": \"LICENSE_INCLUDED\",
    \"isAutoScalingForStorageEnabled\": \"true\"
    }`

    __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCrossRegionAutonomousDatabaseDataGuardDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateCrossRegionAutonomousDatabaseDataGuardDetails.source` attribute
        of this class is ``CROSS_REGION_DATAGUARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type compartment_id: str

        :param character_set:
            The value to assign to the character_set property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type ncharacter_set: str

        :param db_name:
            The value to assign to the db_name property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type ocpu_count: float

        :param db_workload:
            The value to assign to the db_workload property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type data_storage_size_in_tbs: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type data_storage_size_in_gbs: int

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_free_tier: bool

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type kms_key_id: str

        :param vault_id:
            The value to assign to the vault_id property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type vault_id: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_preview_version_with_service_terms_accepted:
            The value to assign to the is_preview_version_with_service_terms_accepted property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_preview_version_with_service_terms_accepted: bool

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_auto_scaling_enabled: bool

        :param is_dedicated:
            The value to assign to the is_dedicated property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type autonomous_container_database_id: str

        :param is_access_control_enabled:
            The value to assign to the is_access_control_enabled property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_access_control_enabled: bool

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type whitelisted_ips: list[str]

        :param are_primary_whitelisted_ips_used:
            The value to assign to the are_primary_whitelisted_ips_used property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type are_primary_whitelisted_ips_used: bool

        :param standby_whitelisted_ips:
            The value to assign to the standby_whitelisted_ips property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type standby_whitelisted_ips: list[str]

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_data_guard_enabled: bool

        :param is_local_data_guard_enabled:
            The value to assign to the is_local_data_guard_enabled property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_local_data_guard_enabled: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type nsg_ids: list[str]

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type private_endpoint_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param db_version:
            The value to assign to the db_version property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
            Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "CLONE_TO_REFRESHABLE", "CROSS_REGION_DATAGUARD"
        :type source: str

        :param customer_contacts:
            The value to assign to the customer_contacts property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        :param is_mtls_connection_required:
            The value to assign to the is_mtls_connection_required property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_mtls_connection_required: bool

        :param autonomous_maintenance_schedule_type:
            The value to assign to the autonomous_maintenance_schedule_type property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
            Allowed values for this property are: "EARLY", "REGULAR"
        :type autonomous_maintenance_schedule_type: str

        :param scheduled_operations:
            The value to assign to the scheduled_operations property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type scheduled_operations: list[oci.database.models.ScheduledOperationDetails]

        :param is_auto_scaling_for_storage_enabled:
            The value to assign to the is_auto_scaling_for_storage_enabled property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type is_auto_scaling_for_storage_enabled: bool

        :param max_cpu_core_count:
            The value to assign to the max_cpu_core_count property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type max_cpu_core_count: int

        :param database_edition:
            The value to assign to the database_edition property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type database_edition: str

        :param source_id:
            The value to assign to the source_id property of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type source_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'db_workload': 'str',
            'data_storage_size_in_tbs': 'int',
            'data_storage_size_in_gbs': 'int',
            'is_free_tier': 'bool',
            'kms_key_id': 'str',
            'vault_id': 'str',
            'admin_password': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'is_preview_version_with_service_terms_accepted': 'bool',
            'is_auto_scaling_enabled': 'bool',
            'is_dedicated': 'bool',
            'autonomous_container_database_id': 'str',
            'is_access_control_enabled': 'bool',
            'whitelisted_ips': 'list[str]',
            'are_primary_whitelisted_ips_used': 'bool',
            'standby_whitelisted_ips': 'list[str]',
            'is_data_guard_enabled': 'bool',
            'is_local_data_guard_enabled': 'bool',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_version': 'str',
            'source': 'str',
            'customer_contacts': 'list[CustomerContact]',
            'is_mtls_connection_required': 'bool',
            'autonomous_maintenance_schedule_type': 'str',
            'scheduled_operations': 'list[ScheduledOperationDetails]',
            'is_auto_scaling_for_storage_enabled': 'bool',
            'max_cpu_core_count': 'int',
            'database_edition': 'str',
            'source_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'db_workload': 'dbWorkload',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'is_free_tier': 'isFreeTier',
            'kms_key_id': 'kmsKeyId',
            'vault_id': 'vaultId',
            'admin_password': 'adminPassword',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'is_preview_version_with_service_terms_accepted': 'isPreviewVersionWithServiceTermsAccepted',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'is_dedicated': 'isDedicated',
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'is_access_control_enabled': 'isAccessControlEnabled',
            'whitelisted_ips': 'whitelistedIps',
            'are_primary_whitelisted_ips_used': 'arePrimaryWhitelistedIpsUsed',
            'standby_whitelisted_ips': 'standbyWhitelistedIps',
            'is_data_guard_enabled': 'isDataGuardEnabled',
            'is_local_data_guard_enabled': 'isLocalDataGuardEnabled',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_endpoint_label': 'privateEndpointLabel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_version': 'dbVersion',
            'source': 'source',
            'customer_contacts': 'customerContacts',
            'is_mtls_connection_required': 'isMtlsConnectionRequired',
            'autonomous_maintenance_schedule_type': 'autonomousMaintenanceScheduleType',
            'scheduled_operations': 'scheduledOperations',
            'is_auto_scaling_for_storage_enabled': 'isAutoScalingForStorageEnabled',
            'max_cpu_core_count': 'maxCpuCoreCount',
            'database_edition': 'databaseEdition',
            'source_id': 'sourceId'
        }

        self._compartment_id = None
        self._character_set = None
        self._ncharacter_set = None
        self._db_name = None
        self._cpu_core_count = None
        self._ocpu_count = None
        self._db_workload = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._is_free_tier = None
        self._kms_key_id = None
        self._vault_id = None
        self._admin_password = None
        self._display_name = None
        self._license_model = None
        self._is_preview_version_with_service_terms_accepted = None
        self._is_auto_scaling_enabled = None
        self._is_dedicated = None
        self._autonomous_container_database_id = None
        self._is_access_control_enabled = None
        self._whitelisted_ips = None
        self._are_primary_whitelisted_ips_used = None
        self._standby_whitelisted_ips = None
        self._is_data_guard_enabled = None
        self._is_local_data_guard_enabled = None
        self._subnet_id = None
        self._nsg_ids = None
        self._private_endpoint_label = None
        self._freeform_tags = None
        self._defined_tags = None
        self._db_version = None
        self._source = None
        self._customer_contacts = None
        self._is_mtls_connection_required = None
        self._autonomous_maintenance_schedule_type = None
        self._scheduled_operations = None
        self._is_auto_scaling_for_storage_enabled = None
        self._max_cpu_core_count = None
        self._database_edition = None
        self._source_id = None
        self._source = 'CROSS_REGION_DATAGUARD'

    @property
    def source_id(self):
        """
        **[Required]** Gets the source_id of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        The `OCID`__ of the source Autonomous Database that will be used to create a new standby database for the Data Guard association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_id of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        The `OCID`__ of the source Autonomous Database that will be used to create a new standby database for the Data Guard association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this CreateCrossRegionAutonomousDatabaseDataGuardDetails.
        :type: str
        """
        self._source_id = source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
