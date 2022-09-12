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
from ubika_waap_api_client.models.update_accesslogprofile_success import UpdateAccesslogprofileSuccess  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestUpdateAccesslogprofileSuccess(unittest.TestCase):
    """UpdateAccesslogprofileSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateAccesslogprofileSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.update_accesslogprofile_success.UpdateAccesslogprofileSuccess()  # noqa: E501
        if include_optional :
            return UpdateAccesslogprofileSuccess(
                data = ubika_waap_api_client.models.update_accesslogprofile_success_data.UpdateAccesslogprofileSuccess_data(
                    uid = '0', 
                    name = '0', 
                    type = '0', 
                    format = '0', 
                    used_by = [
                        ubika_waap_api_client.models.update_accesslogprofile_used_by_success_array.UpdateAccesslogprofileUsedBySuccessArray(
                            tunnel_uid = '0', 
                            tunnel_name = '0', )
                        ], 
                    t_update = 1.337, 
                    t_create = 1.337, ), 
                data_used_by = [
                    ubika_waap_api_client.models.update_accesslogprofile_used_by_success_array.UpdateAccesslogprofileUsedBySuccessArray(
                        tunnel_uid = '0', 
                        tunnel_name = '0', )
                    ]
            )
        else :
            return UpdateAccesslogprofileSuccess(
        )

    def testUpdateAccesslogprofileSuccess(self):
        """Test UpdateAccesslogprofileSuccess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
