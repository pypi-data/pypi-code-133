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
from ubika_waap_api_client.models.add_reverse_proxy_profile_success import AddReverseProxyProfileSuccess  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestAddReverseProxyProfileSuccess(unittest.TestCase):
    """AddReverseProxyProfileSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddReverseProxyProfileSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.add_reverse_proxy_profile_success.AddReverseProxyProfileSuccess()  # noqa: E501
        if include_optional :
            return AddReverseProxyProfileSuccess(
                data = ubika_waap_api_client.models.add_reverse_proxy_profile_success_data.AddReverseProxyProfileSuccess_data(
                    uid = '0', 
                    name = '0', 
                    start_server = 56, 
                    server_limit = 56, 
                    max_clients = 56, 
                    max_spare_threads = 56, 
                    min_spare_threads = 56, 
                    thread_per_child = 56, 
                    max_requests_per_child = 56, 
                    limit_request_field_size = 56, 
                    timeout = 56, 
                    proxy_timeout = 56, 
                    keep_alive = True, 
                    keep_alive_timeout = 56, 
                    max_keep_alive_requests = 56, 
                    ssl_session_cache_size = 56, 
                    ssl_session_cache_timeout = 56, 
                    is_default = True, )
            )
        else :
            return AddReverseProxyProfileSuccess(
        )

    def testAddReverseProxyProfileSuccess(self):
        """Test AddReverseProxyProfileSuccess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
