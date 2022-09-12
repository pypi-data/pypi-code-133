# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportDataAssetDetails(object):
    """
    The details of what needs to be exported.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportDataAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_scope:
            The value to assign to the export_scope property of this ExportDataAssetDetails.
        :type export_scope: list[oci.data_catalog.models.DataAssetExportScope]

        """
        self.swagger_types = {
            'export_scope': 'list[DataAssetExportScope]'
        }

        self.attribute_map = {
            'export_scope': 'exportScope'
        }

        self._export_scope = None

    @property
    def export_scope(self):
        """
        Gets the export_scope of this ExportDataAssetDetails.
        Array of objects and their child types to be selected for export.


        :return: The export_scope of this ExportDataAssetDetails.
        :rtype: list[oci.data_catalog.models.DataAssetExportScope]
        """
        return self._export_scope

    @export_scope.setter
    def export_scope(self, export_scope):
        """
        Sets the export_scope of this ExportDataAssetDetails.
        Array of objects and their child types to be selected for export.


        :param export_scope: The export_scope of this ExportDataAssetDetails.
        :type: list[oci.data_catalog.models.DataAssetExportScope]
        """
        self._export_scope = export_scope

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
