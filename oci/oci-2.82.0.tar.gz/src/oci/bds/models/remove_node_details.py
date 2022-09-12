# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveNodeDetails(object):
    """
    The information about node to be removed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveNodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this RemoveNodeDetails.
        :type cluster_admin_password: str

        :param is_force_remove_enabled:
            The value to assign to the is_force_remove_enabled property of this RemoveNodeDetails.
        :type is_force_remove_enabled: bool

        :param node_id:
            The value to assign to the node_id property of this RemoveNodeDetails.
        :type node_id: str

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'is_force_remove_enabled': 'bool',
            'node_id': 'str'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'is_force_remove_enabled': 'isForceRemoveEnabled',
            'node_id': 'nodeId'
        }

        self._cluster_admin_password = None
        self._is_force_remove_enabled = None
        self._node_id = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this RemoveNodeDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :return: The cluster_admin_password of this RemoveNodeDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this RemoveNodeDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :param cluster_admin_password: The cluster_admin_password of this RemoveNodeDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def is_force_remove_enabled(self):
        """
        Gets the is_force_remove_enabled of this RemoveNodeDetails.
        Boolean flag specifying whether or not to force remove node if graceful
        removal fails.


        :return: The is_force_remove_enabled of this RemoveNodeDetails.
        :rtype: bool
        """
        return self._is_force_remove_enabled

    @is_force_remove_enabled.setter
    def is_force_remove_enabled(self, is_force_remove_enabled):
        """
        Sets the is_force_remove_enabled of this RemoveNodeDetails.
        Boolean flag specifying whether or not to force remove node if graceful
        removal fails.


        :param is_force_remove_enabled: The is_force_remove_enabled of this RemoveNodeDetails.
        :type: bool
        """
        self._is_force_remove_enabled = is_force_remove_enabled

    @property
    def node_id(self):
        """
        **[Required]** Gets the node_id of this RemoveNodeDetails.
        OCID of the node to be removed.


        :return: The node_id of this RemoveNodeDetails.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this RemoveNodeDetails.
        OCID of the node to be removed.


        :param node_id: The node_id of this RemoveNodeDetails.
        :type: str
        """
        self._node_id = node_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
