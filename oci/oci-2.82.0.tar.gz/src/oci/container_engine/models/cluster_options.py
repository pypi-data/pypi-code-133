# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterOptions(object):
    """
    Options for creating or updating clusters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kubernetes_versions:
            The value to assign to the kubernetes_versions property of this ClusterOptions.
        :type kubernetes_versions: list[str]

        :param cluster_pod_network_options:
            The value to assign to the cluster_pod_network_options property of this ClusterOptions.
        :type cluster_pod_network_options: list[oci.container_engine.models.ClusterPodNetworkOptionDetails]

        """
        self.swagger_types = {
            'kubernetes_versions': 'list[str]',
            'cluster_pod_network_options': 'list[ClusterPodNetworkOptionDetails]'
        }

        self.attribute_map = {
            'kubernetes_versions': 'kubernetesVersions',
            'cluster_pod_network_options': 'clusterPodNetworkOptions'
        }

        self._kubernetes_versions = None
        self._cluster_pod_network_options = None

    @property
    def kubernetes_versions(self):
        """
        Gets the kubernetes_versions of this ClusterOptions.
        Available Kubernetes versions.


        :return: The kubernetes_versions of this ClusterOptions.
        :rtype: list[str]
        """
        return self._kubernetes_versions

    @kubernetes_versions.setter
    def kubernetes_versions(self, kubernetes_versions):
        """
        Sets the kubernetes_versions of this ClusterOptions.
        Available Kubernetes versions.


        :param kubernetes_versions: The kubernetes_versions of this ClusterOptions.
        :type: list[str]
        """
        self._kubernetes_versions = kubernetes_versions

    @property
    def cluster_pod_network_options(self):
        """
        Gets the cluster_pod_network_options of this ClusterOptions.
        Available CNIs and network options for existing and new node pools of the cluster


        :return: The cluster_pod_network_options of this ClusterOptions.
        :rtype: list[oci.container_engine.models.ClusterPodNetworkOptionDetails]
        """
        return self._cluster_pod_network_options

    @cluster_pod_network_options.setter
    def cluster_pod_network_options(self, cluster_pod_network_options):
        """
        Sets the cluster_pod_network_options of this ClusterOptions.
        Available CNIs and network options for existing and new node pools of the cluster


        :param cluster_pod_network_options: The cluster_pod_network_options of this ClusterOptions.
        :type: list[oci.container_engine.models.ClusterPodNetworkOptionDetails]
        """
        self._cluster_pod_network_options = cluster_pod_network_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
