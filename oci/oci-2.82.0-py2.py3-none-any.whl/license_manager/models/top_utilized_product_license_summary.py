# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopUtilizedProductLicenseSummary(object):
    """
    A summary of the top utilized product licenses.
    """

    #: A constant which can be used with the unit_type property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "OCPU"
    UNIT_TYPE_OCPU = "OCPU"

    #: A constant which can be used with the unit_type property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "NAMED_USER_PLUS"
    UNIT_TYPE_NAMED_USER_PLUS = "NAMED_USER_PLUS"

    #: A constant which can be used with the unit_type property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "PROCESSORS"
    UNIT_TYPE_PROCESSORS = "PROCESSORS"

    #: A constant which can be used with the status property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "INCOMPLETE"
    STATUS_INCOMPLETE = "INCOMPLETE"

    #: A constant which can be used with the status property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "ISSUES_FOUND"
    STATUS_ISSUES_FOUND = "ISSUES_FOUND"

    #: A constant which can be used with the status property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a TopUtilizedProductLicenseSummary.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    def __init__(self, **kwargs):
        """
        Initializes a new TopUtilizedProductLicenseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param product_license_id:
            The value to assign to the product_license_id property of this TopUtilizedProductLicenseSummary.
        :type product_license_id: str

        :param product_type:
            The value to assign to the product_type property of this TopUtilizedProductLicenseSummary.
        :type product_type: str

        :param unit_type:
            The value to assign to the unit_type property of this TopUtilizedProductLicenseSummary.
            Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit_type: str

        :param total_units_consumed:
            The value to assign to the total_units_consumed property of this TopUtilizedProductLicenseSummary.
        :type total_units_consumed: float

        :param total_license_unit_count:
            The value to assign to the total_license_unit_count property of this TopUtilizedProductLicenseSummary.
        :type total_license_unit_count: int

        :param is_unlimited:
            The value to assign to the is_unlimited property of this TopUtilizedProductLicenseSummary.
        :type is_unlimited: bool

        :param status:
            The value to assign to the status property of this TopUtilizedProductLicenseSummary.
            Allowed values for this property are: "INCOMPLETE", "ISSUES_FOUND", "WARNING", "OK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'product_license_id': 'str',
            'product_type': 'str',
            'unit_type': 'str',
            'total_units_consumed': 'float',
            'total_license_unit_count': 'int',
            'is_unlimited': 'bool',
            'status': 'str'
        }

        self.attribute_map = {
            'product_license_id': 'productLicenseId',
            'product_type': 'productType',
            'unit_type': 'unitType',
            'total_units_consumed': 'totalUnitsConsumed',
            'total_license_unit_count': 'totalLicenseUnitCount',
            'is_unlimited': 'isUnlimited',
            'status': 'status'
        }

        self._product_license_id = None
        self._product_type = None
        self._unit_type = None
        self._total_units_consumed = None
        self._total_license_unit_count = None
        self._is_unlimited = None
        self._status = None

    @property
    def product_license_id(self):
        """
        **[Required]** Gets the product_license_id of this TopUtilizedProductLicenseSummary.
        The product license `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The product_license_id of this TopUtilizedProductLicenseSummary.
        :rtype: str
        """
        return self._product_license_id

    @product_license_id.setter
    def product_license_id(self, product_license_id):
        """
        Sets the product_license_id of this TopUtilizedProductLicenseSummary.
        The product license `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param product_license_id: The product_license_id of this TopUtilizedProductLicenseSummary.
        :type: str
        """
        self._product_license_id = product_license_id

    @property
    def product_type(self):
        """
        **[Required]** Gets the product_type of this TopUtilizedProductLicenseSummary.
        The product type.


        :return: The product_type of this TopUtilizedProductLicenseSummary.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this TopUtilizedProductLicenseSummary.
        The product type.


        :param product_type: The product_type of this TopUtilizedProductLicenseSummary.
        :type: str
        """
        self._product_type = product_type

    @property
    def unit_type(self):
        """
        **[Required]** Gets the unit_type of this TopUtilizedProductLicenseSummary.
        The product license unit.

        Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit_type of this TopUtilizedProductLicenseSummary.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this TopUtilizedProductLicenseSummary.
        The product license unit.


        :param unit_type: The unit_type of this TopUtilizedProductLicenseSummary.
        :type: str
        """
        allowed_values = ["OCPU", "NAMED_USER_PLUS", "PROCESSORS"]
        if not value_allowed_none_or_none_sentinel(unit_type, allowed_values):
            unit_type = 'UNKNOWN_ENUM_VALUE'
        self._unit_type = unit_type

    @property
    def total_units_consumed(self):
        """
        **[Required]** Gets the total_units_consumed of this TopUtilizedProductLicenseSummary.
        Number of license units consumed.


        :return: The total_units_consumed of this TopUtilizedProductLicenseSummary.
        :rtype: float
        """
        return self._total_units_consumed

    @total_units_consumed.setter
    def total_units_consumed(self, total_units_consumed):
        """
        Sets the total_units_consumed of this TopUtilizedProductLicenseSummary.
        Number of license units consumed.


        :param total_units_consumed: The total_units_consumed of this TopUtilizedProductLicenseSummary.
        :type: float
        """
        self._total_units_consumed = total_units_consumed

    @property
    def total_license_unit_count(self):
        """
        **[Required]** Gets the total_license_unit_count of this TopUtilizedProductLicenseSummary.
        Total number of license units in the product license provided by the user.


        :return: The total_license_unit_count of this TopUtilizedProductLicenseSummary.
        :rtype: int
        """
        return self._total_license_unit_count

    @total_license_unit_count.setter
    def total_license_unit_count(self, total_license_unit_count):
        """
        Sets the total_license_unit_count of this TopUtilizedProductLicenseSummary.
        Total number of license units in the product license provided by the user.


        :param total_license_unit_count: The total_license_unit_count of this TopUtilizedProductLicenseSummary.
        :type: int
        """
        self._total_license_unit_count = total_license_unit_count

    @property
    def is_unlimited(self):
        """
        **[Required]** Gets the is_unlimited of this TopUtilizedProductLicenseSummary.
        Specifies if the license unit count is unlimited.


        :return: The is_unlimited of this TopUtilizedProductLicenseSummary.
        :rtype: bool
        """
        return self._is_unlimited

    @is_unlimited.setter
    def is_unlimited(self, is_unlimited):
        """
        Sets the is_unlimited of this TopUtilizedProductLicenseSummary.
        Specifies if the license unit count is unlimited.


        :param is_unlimited: The is_unlimited of this TopUtilizedProductLicenseSummary.
        :type: bool
        """
        self._is_unlimited = is_unlimited

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TopUtilizedProductLicenseSummary.
        The current product license status.

        Allowed values for this property are: "INCOMPLETE", "ISSUES_FOUND", "WARNING", "OK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TopUtilizedProductLicenseSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TopUtilizedProductLicenseSummary.
        The current product license status.


        :param status: The status of this TopUtilizedProductLicenseSummary.
        :type: str
        """
        allowed_values = ["INCOMPLETE", "ISSUES_FOUND", "WARNING", "OK"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
