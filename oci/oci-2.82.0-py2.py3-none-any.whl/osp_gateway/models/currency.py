# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Currency(object):
    """
    Currency details model
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Currency object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param currency_code:
            The value to assign to the currency_code property of this Currency.
        :type currency_code: str

        :param currency_symbol:
            The value to assign to the currency_symbol property of this Currency.
        :type currency_symbol: str

        :param name:
            The value to assign to the name property of this Currency.
        :type name: str

        :param usd_conversion:
            The value to assign to the usd_conversion property of this Currency.
        :type usd_conversion: float

        :param round_decimal_point:
            The value to assign to the round_decimal_point property of this Currency.
        :type round_decimal_point: float

        """
        self.swagger_types = {
            'currency_code': 'str',
            'currency_symbol': 'str',
            'name': 'str',
            'usd_conversion': 'float',
            'round_decimal_point': 'float'
        }

        self.attribute_map = {
            'currency_code': 'currencyCode',
            'currency_symbol': 'currencySymbol',
            'name': 'name',
            'usd_conversion': 'usdConversion',
            'round_decimal_point': 'roundDecimalPoint'
        }

        self._currency_code = None
        self._currency_symbol = None
        self._name = None
        self._usd_conversion = None
        self._round_decimal_point = None

    @property
    def currency_code(self):
        """
        Gets the currency_code of this Currency.
        Currency code


        :return: The currency_code of this Currency.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this Currency.
        Currency code


        :param currency_code: The currency_code of this Currency.
        :type: str
        """
        self._currency_code = currency_code

    @property
    def currency_symbol(self):
        """
        Gets the currency_symbol of this Currency.
        Currency symbol


        :return: The currency_symbol of this Currency.
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """
        Sets the currency_symbol of this Currency.
        Currency symbol


        :param currency_symbol: The currency_symbol of this Currency.
        :type: str
        """
        self._currency_symbol = currency_symbol

    @property
    def name(self):
        """
        Gets the name of this Currency.
        Name of the currency


        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Currency.
        Name of the currency


        :param name: The name of this Currency.
        :type: str
        """
        self._name = name

    @property
    def usd_conversion(self):
        """
        Gets the usd_conversion of this Currency.
        USD conversion rate of the currency


        :return: The usd_conversion of this Currency.
        :rtype: float
        """
        return self._usd_conversion

    @usd_conversion.setter
    def usd_conversion(self, usd_conversion):
        """
        Sets the usd_conversion of this Currency.
        USD conversion rate of the currency


        :param usd_conversion: The usd_conversion of this Currency.
        :type: float
        """
        self._usd_conversion = usd_conversion

    @property
    def round_decimal_point(self):
        """
        Gets the round_decimal_point of this Currency.
        Round decimal point


        :return: The round_decimal_point of this Currency.
        :rtype: float
        """
        return self._round_decimal_point

    @round_decimal_point.setter
    def round_decimal_point(self, round_decimal_point):
        """
        Sets the round_decimal_point of this Currency.
        Round decimal point


        :param round_decimal_point: The round_decimal_point of this Currency.
        :type: float
        """
        self._round_decimal_point = round_decimal_point

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
