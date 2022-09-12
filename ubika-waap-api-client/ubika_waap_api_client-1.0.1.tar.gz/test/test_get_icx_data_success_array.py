# coding: utf-8

"""
    UBIKA WAAP Gateway and Cloud API

    The UBIKA's WAAP management API provides a REST/JSON programming interface. It allows automation and scripting of WAAP administration tasks, such as management of reverse proxies and tunnels. The API documentation is shipped with the product itself. Once the product installed, you can access the documentation on the following URL https://ManagementWAAP:3001/api/v1/doc/  # noqa: E501

    The version of the OpenAPI document: 1.0.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ubika_waap_api_client
from ubika_waap_api_client.models.get_icx_data_success_array import GetIcxDataSuccessArray  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestGetIcxDataSuccessArray(unittest.TestCase):
    """GetIcxDataSuccessArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetIcxDataSuccessArray
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.get_icx_data_success_array.GetIcxDataSuccessArray()  # noqa: E501
        if include_optional :
            return GetIcxDataSuccessArray(
                uid = '0', 
                name = '0', 
                description = '0', 
                editable = True, 
                legacy_resolve = True, 
                categories = [
                    ubika_waap_api_client.models.get_icx_categories_success_array.GetIcxCategoriesSuccessArray(
                        uid = '0', 
                        name = '0', 
                        description = '0', 
                        icx_uid = '0', 
                        rules = [
                            ubika_waap_api_client.models.get_icx_rules_success_array.GetIcxRulesSuccessArray(
                                name = '0', 
                                uid = '0', 
                                match = '0', 
                                action = '0', 
                                enable = True, 
                                description = '0', 
                                scope = '0', 
                                filters = [
                                    ubika_waap_api_client.models.get_icx_filters_success_array.GetIcxFiltersSuccessArray(
                                        name = '0', 
                                        key = '0', 
                                        value = '0', 
                                        key_type = '0', 
                                        value_type = '0', 
                                        key_condition = '0', 
                                        value_condition = '0', )
                                    ], )
                            ], )
                    ]
            )
        else :
            return GetIcxDataSuccessArray(
        )

    def testGetIcxDataSuccessArray(self):
        """Test GetIcxDataSuccessArray"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
