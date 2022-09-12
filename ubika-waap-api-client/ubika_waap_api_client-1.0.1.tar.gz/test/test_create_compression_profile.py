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
from ubika_waap_api_client.models.create_compression_profile import CreateCompressionProfile  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestCreateCompressionProfile(unittest.TestCase):
    """CreateCompressionProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCompressionProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.create_compression_profile.CreateCompressionProfile()  # noqa: E501
        if include_optional :
            return CreateCompressionProfile(
                name = '0', 
                content_types = '0', 
                exclude_browser = '0', 
                buffer_size = 56, 
                compression_level = 56, 
                memory_level = 56, 
                window_size = 56
            )
        else :
            return CreateCompressionProfile(
        )

    def testCreateCompressionProfile(self):
        """Test CreateCompressionProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
