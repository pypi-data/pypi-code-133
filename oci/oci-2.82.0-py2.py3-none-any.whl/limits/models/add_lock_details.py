# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddLockDetails(object):
    """
    Request payload to add lock to the resource. The FULL lock type allows no modifications (delete, create, update).
    The DELETE lock type allows all modifications, but delete is not allowed.
    """

    #: A constant which can be used with the type property of a AddLockDetails.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a AddLockDetails.
    #: This constant has a value of "DELETE"
    TYPE_DELETE = "DELETE"

    def __init__(self, **kwargs):
        """
        Initializes a new AddLockDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AddLockDetails.
            Allowed values for this property are: "FULL", "DELETE"
        :type type: str

        :param related_resource_id:
            The value to assign to the related_resource_id property of this AddLockDetails.
        :type related_resource_id: str

        :param message:
            The value to assign to the message property of this AddLockDetails.
        :type message: str

        """
        self.swagger_types = {
            'type': 'str',
            'related_resource_id': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'related_resource_id': 'relatedResourceId',
            'message': 'message'
        }

        self._type = None
        self._related_resource_id = None
        self._message = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AddLockDetails.
        Lock type.

        Allowed values for this property are: "FULL", "DELETE"


        :return: The type of this AddLockDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AddLockDetails.
        Lock type.


        :param type: The type of this AddLockDetails.
        :type: str
        """
        allowed_values = ["FULL", "DELETE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def related_resource_id(self):
        """
        Gets the related_resource_id of this AddLockDetails.
        The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.


        :return: The related_resource_id of this AddLockDetails.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this AddLockDetails.
        The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.


        :param related_resource_id: The related_resource_id of this AddLockDetails.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def message(self):
        """
        Gets the message of this AddLockDetails.
        A message added by the lock creator. The message typically gives an
        indication of why the resource is locked.


        :return: The message of this AddLockDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AddLockDetails.
        A message added by the lock creator. The message typically gives an
        indication of why the resource is locked.


        :param message: The message of this AddLockDetails.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
