# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoringSource(object):
    """
    A compartment-specific list of metric namespaces to retrieve data from.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoringSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoringSource.
        :type compartment_id: str

        :param namespace_details:
            The value to assign to the namespace_details property of this MonitoringSource.
        :type namespace_details: oci.sch.models.MonitoringSourceNamespaceDetails

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'namespace_details': 'MonitoringSourceNamespaceDetails'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'namespace_details': 'namespaceDetails'
        }

        self._compartment_id = None
        self._namespace_details = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoringSource.
        The `OCID`__ of the compartment containing the metric namespaces you want to use for the Monitoring source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoringSource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoringSource.
        The `OCID`__ of the compartment containing the metric namespaces you want to use for the Monitoring source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoringSource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def namespace_details(self):
        """
        **[Required]** Gets the namespace_details of this MonitoringSource.

        :return: The namespace_details of this MonitoringSource.
        :rtype: oci.sch.models.MonitoringSourceNamespaceDetails
        """
        return self._namespace_details

    @namespace_details.setter
    def namespace_details(self, namespace_details):
        """
        Sets the namespace_details of this MonitoringSource.

        :param namespace_details: The namespace_details of this MonitoringSource.
        :type: oci.sch.models.MonitoringSourceNamespaceDetails
        """
        self._namespace_details = namespace_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
