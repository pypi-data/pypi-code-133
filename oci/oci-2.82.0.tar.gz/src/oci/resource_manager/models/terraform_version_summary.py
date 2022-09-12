# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TerraformVersionSummary(object):
    """
    A Terraform version supported for use with stacks.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TerraformVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this TerraformVersionSummary.
        :type name: str

        :param is_default:
            The value to assign to the is_default property of this TerraformVersionSummary.
        :type is_default: bool

        """
        self.swagger_types = {
            'name': 'str',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'is_default': 'isDefault'
        }

        self._name = None
        self._is_default = None

    @property
    def name(self):
        """
        Gets the name of this TerraformVersionSummary.
        A supported Terraform version. Example: `0.12.x`


        :return: The name of this TerraformVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TerraformVersionSummary.
        A supported Terraform version. Example: `0.12.x`


        :param name: The name of this TerraformVersionSummary.
        :type: str
        """
        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this TerraformVersionSummary.
        Indicates whether this Terraform version is used by default in :func:`create_stack`.


        :return: The is_default of this TerraformVersionSummary.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this TerraformVersionSummary.
        Indicates whether this Terraform version is used by default in :func:`create_stack`.


        :param is_default: The is_default of this TerraformVersionSummary.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
