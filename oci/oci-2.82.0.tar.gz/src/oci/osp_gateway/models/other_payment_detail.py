# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .payment_detail import PaymentDetail
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OtherPaymentDetail(PaymentDetail):
    """
    Other Payment related details
    """

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "VISA"
    CREDIT_CARD_TYPE_VISA = "VISA"

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "AMEX"
    CREDIT_CARD_TYPE_AMEX = "AMEX"

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "MASTERCARD"
    CREDIT_CARD_TYPE_MASTERCARD = "MASTERCARD"

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "DISCOVER"
    CREDIT_CARD_TYPE_DISCOVER = "DISCOVER"

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "JCB"
    CREDIT_CARD_TYPE_JCB = "JCB"

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "DINER"
    CREDIT_CARD_TYPE_DINER = "DINER"

    #: A constant which can be used with the credit_card_type property of a OtherPaymentDetail.
    #: This constant has a value of "ELO"
    CREDIT_CARD_TYPE_ELO = "ELO"

    def __init__(self, **kwargs):
        """
        Initializes a new OtherPaymentDetail object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.OtherPaymentDetail.payment_method` attribute
        of this class is ``OTHER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_paid_on:
            The value to assign to the time_paid_on property of this OtherPaymentDetail.
        :type time_paid_on: datetime

        :param paid_by:
            The value to assign to the paid_by property of this OtherPaymentDetail.
        :type paid_by: str

        :param payment_method:
            The value to assign to the payment_method property of this OtherPaymentDetail.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type payment_method: str

        :param amount_paid:
            The value to assign to the amount_paid property of this OtherPaymentDetail.
        :type amount_paid: float

        :param echeck_routing:
            The value to assign to the echeck_routing property of this OtherPaymentDetail.
        :type echeck_routing: str

        :param name_on_card:
            The value to assign to the name_on_card property of this OtherPaymentDetail.
        :type name_on_card: str

        :param credit_card_type:
            The value to assign to the credit_card_type property of this OtherPaymentDetail.
            Allowed values for this property are: "VISA", "AMEX", "MASTERCARD", "DISCOVER", "JCB", "DINER", "ELO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credit_card_type: str

        :param last_digits:
            The value to assign to the last_digits property of this OtherPaymentDetail.
        :type last_digits: str

        :param time_expiration:
            The value to assign to the time_expiration property of this OtherPaymentDetail.
        :type time_expiration: datetime

        """
        self.swagger_types = {
            'time_paid_on': 'datetime',
            'paid_by': 'str',
            'payment_method': 'str',
            'amount_paid': 'float',
            'echeck_routing': 'str',
            'name_on_card': 'str',
            'credit_card_type': 'str',
            'last_digits': 'str',
            'time_expiration': 'datetime'
        }

        self.attribute_map = {
            'time_paid_on': 'timePaidOn',
            'paid_by': 'paidBy',
            'payment_method': 'paymentMethod',
            'amount_paid': 'amountPaid',
            'echeck_routing': 'echeckRouting',
            'name_on_card': 'nameOnCard',
            'credit_card_type': 'creditCardType',
            'last_digits': 'lastDigits',
            'time_expiration': 'timeExpiration'
        }

        self._time_paid_on = None
        self._paid_by = None
        self._payment_method = None
        self._amount_paid = None
        self._echeck_routing = None
        self._name_on_card = None
        self._credit_card_type = None
        self._last_digits = None
        self._time_expiration = None
        self._payment_method = 'OTHER'

    @property
    def echeck_routing(self):
        """
        Gets the echeck_routing of this OtherPaymentDetail.
        Last four routing digits of the card


        :return: The echeck_routing of this OtherPaymentDetail.
        :rtype: str
        """
        return self._echeck_routing

    @echeck_routing.setter
    def echeck_routing(self, echeck_routing):
        """
        Sets the echeck_routing of this OtherPaymentDetail.
        Last four routing digits of the card


        :param echeck_routing: The echeck_routing of this OtherPaymentDetail.
        :type: str
        """
        self._echeck_routing = echeck_routing

    @property
    def name_on_card(self):
        """
        Gets the name_on_card of this OtherPaymentDetail.
        Name on the echeck card


        :return: The name_on_card of this OtherPaymentDetail.
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """
        Sets the name_on_card of this OtherPaymentDetail.
        Name on the echeck card


        :param name_on_card: The name_on_card of this OtherPaymentDetail.
        :type: str
        """
        self._name_on_card = name_on_card

    @property
    def credit_card_type(self):
        """
        Gets the credit_card_type of this OtherPaymentDetail.
        Echeck card type

        Allowed values for this property are: "VISA", "AMEX", "MASTERCARD", "DISCOVER", "JCB", "DINER", "ELO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credit_card_type of this OtherPaymentDetail.
        :rtype: str
        """
        return self._credit_card_type

    @credit_card_type.setter
    def credit_card_type(self, credit_card_type):
        """
        Sets the credit_card_type of this OtherPaymentDetail.
        Echeck card type


        :param credit_card_type: The credit_card_type of this OtherPaymentDetail.
        :type: str
        """
        allowed_values = ["VISA", "AMEX", "MASTERCARD", "DISCOVER", "JCB", "DINER", "ELO"]
        if not value_allowed_none_or_none_sentinel(credit_card_type, allowed_values):
            credit_card_type = 'UNKNOWN_ENUM_VALUE'
        self._credit_card_type = credit_card_type

    @property
    def last_digits(self):
        """
        Gets the last_digits of this OtherPaymentDetail.
        Last four digits of the card


        :return: The last_digits of this OtherPaymentDetail.
        :rtype: str
        """
        return self._last_digits

    @last_digits.setter
    def last_digits(self, last_digits):
        """
        Sets the last_digits of this OtherPaymentDetail.
        Last four digits of the card


        :param last_digits: The last_digits of this OtherPaymentDetail.
        :type: str
        """
        self._last_digits = last_digits

    @property
    def time_expiration(self):
        """
        Gets the time_expiration of this OtherPaymentDetail.
        Expired date of the echeck card


        :return: The time_expiration of this OtherPaymentDetail.
        :rtype: datetime
        """
        return self._time_expiration

    @time_expiration.setter
    def time_expiration(self, time_expiration):
        """
        Sets the time_expiration of this OtherPaymentDetail.
        Expired date of the echeck card


        :param time_expiration: The time_expiration of this OtherPaymentDetail.
        :type: datetime
        """
        self._time_expiration = time_expiration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
