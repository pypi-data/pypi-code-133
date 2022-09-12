# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIdpGroupMappingDetails(object):
    """
    CreateIdpGroupMappingDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIdpGroupMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idp_group_name:
            The value to assign to the idp_group_name property of this CreateIdpGroupMappingDetails.
        :type idp_group_name: str

        :param group_id:
            The value to assign to the group_id property of this CreateIdpGroupMappingDetails.
        :type group_id: str

        """
        self.swagger_types = {
            'idp_group_name': 'str',
            'group_id': 'str'
        }

        self.attribute_map = {
            'idp_group_name': 'idpGroupName',
            'group_id': 'groupId'
        }

        self._idp_group_name = None
        self._group_id = None

    @property
    def idp_group_name(self):
        """
        **[Required]** Gets the idp_group_name of this CreateIdpGroupMappingDetails.
        The name of the IdP group you want to map.


        :return: The idp_group_name of this CreateIdpGroupMappingDetails.
        :rtype: str
        """
        return self._idp_group_name

    @idp_group_name.setter
    def idp_group_name(self, idp_group_name):
        """
        Sets the idp_group_name of this CreateIdpGroupMappingDetails.
        The name of the IdP group you want to map.


        :param idp_group_name: The idp_group_name of this CreateIdpGroupMappingDetails.
        :type: str
        """
        self._idp_group_name = idp_group_name

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this CreateIdpGroupMappingDetails.
        The OCID of the IAM Service :class:`Group`
        you want to map to the IdP group.


        :return: The group_id of this CreateIdpGroupMappingDetails.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this CreateIdpGroupMappingDetails.
        The OCID of the IAM Service :class:`Group`
        you want to map to the IdP group.


        :param group_id: The group_id of this CreateIdpGroupMappingDetails.
        :type: str
        """
        self._group_id = group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
