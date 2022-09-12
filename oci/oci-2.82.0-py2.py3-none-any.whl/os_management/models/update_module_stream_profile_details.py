# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateModuleStreamProfileDetails(object):
    """
    Information detailing the state of a module stream profile
    """

    #: A constant which can be used with the status property of a UpdateModuleStreamProfileDetails.
    #: This constant has a value of "INSTALLED"
    STATUS_INSTALLED = "INSTALLED"

    #: A constant which can be used with the status property of a UpdateModuleStreamProfileDetails.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateModuleStreamProfileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param profile_name:
            The value to assign to the profile_name property of this UpdateModuleStreamProfileDetails.
        :type profile_name: str

        :param status:
            The value to assign to the status property of this UpdateModuleStreamProfileDetails.
            Allowed values for this property are: "INSTALLED", "AVAILABLE"
        :type status: str

        :param is_default:
            The value to assign to the is_default property of this UpdateModuleStreamProfileDetails.
        :type is_default: bool

        :param time_modified:
            The value to assign to the time_modified property of this UpdateModuleStreamProfileDetails.
        :type time_modified: datetime

        """
        self.swagger_types = {
            'profile_name': 'str',
            'status': 'str',
            'is_default': 'bool',
            'time_modified': 'datetime'
        }

        self.attribute_map = {
            'profile_name': 'profileName',
            'status': 'status',
            'is_default': 'isDefault',
            'time_modified': 'timeModified'
        }

        self._profile_name = None
        self._status = None
        self._is_default = None
        self._time_modified = None

    @property
    def profile_name(self):
        """
        **[Required]** Gets the profile_name of this UpdateModuleStreamProfileDetails.
        The name of the profile of the parent stream


        :return: The profile_name of this UpdateModuleStreamProfileDetails.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this UpdateModuleStreamProfileDetails.
        The name of the profile of the parent stream


        :param profile_name: The profile_name of this UpdateModuleStreamProfileDetails.
        :type: str
        """
        self._profile_name = profile_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateModuleStreamProfileDetails.
        The status of the profile.

        A profile with the \"INSTALLED\" status indicates that the
        profile has been installed.

        A profile with the \"AVAILABLE\" status indicates that the
        profile is not installed, but can be.

        Allowed values for this property are: "INSTALLED", "AVAILABLE"


        :return: The status of this UpdateModuleStreamProfileDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateModuleStreamProfileDetails.
        The status of the profile.

        A profile with the \"INSTALLED\" status indicates that the
        profile has been installed.

        A profile with the \"AVAILABLE\" status indicates that the
        profile is not installed, but can be.


        :param status: The status of this UpdateModuleStreamProfileDetails.
        :type: str
        """
        allowed_values = ["INSTALLED", "AVAILABLE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def is_default(self):
        """
        Gets the is_default of this UpdateModuleStreamProfileDetails.
        Indicates if the module stream profile is the default


        :return: The is_default of this UpdateModuleStreamProfileDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this UpdateModuleStreamProfileDetails.
        Indicates if the module stream profile is the default


        :param is_default: The is_default of this UpdateModuleStreamProfileDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def time_modified(self):
        """
        **[Required]** Gets the time_modified of this UpdateModuleStreamProfileDetails.
        The date and time of the last status change for this object, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_modified of this UpdateModuleStreamProfileDetails.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this UpdateModuleStreamProfileDetails.
        The date and time of the last status change for this object, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_modified: The time_modified of this UpdateModuleStreamProfileDetails.
        :type: datetime
        """
        self._time_modified = time_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
