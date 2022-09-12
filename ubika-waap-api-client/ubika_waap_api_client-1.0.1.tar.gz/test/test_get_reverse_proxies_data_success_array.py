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
from ubika_waap_api_client.models.get_reverse_proxies_data_success_array import GetReverseProxiesDataSuccessArray  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestGetReverseProxiesDataSuccessArray(unittest.TestCase):
    """GetReverseProxiesDataSuccessArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetReverseProxiesDataSuccessArray
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.get_reverse_proxies_data_success_array.GetReverseProxiesDataSuccessArray()  # noqa: E501
        if include_optional :
            return GetReverseProxiesDataSuccessArray(
                appliance = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                    uid = '0', 
                    name = '0', ), 
                uid = '0', 
                name = '0', 
                enabled = True, 
                healthcheck_uri = '0', 
                access_log = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                    uid = '0', 
                    name = '0', ), 
                advanced_parameters = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                    uid = '0', 
                    name = '0', ), 
                block_default_tunnel = ubika_waap_api_client.models.add_reverse_proxy_block_default_tunnel.AddReverseProxy_blockDefaultTunnel(
                    block = True, 
                    log = True, ), 
                request_timeout = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                    uid = '0', 
                    name = '0', ), 
                no_log_on = ubika_waap_api_client.models.add_reverse_proxy_no_log_on.AddReverseProxy_noLogOn(
                    enabled = True, 
                    type = '0', 
                    value = '0', ), 
                labels = [
                    ubika_waap_api_client.models.get_reverse_proxies_labels_success_array.GetReverseProxiesLabelsSuccessArray(
                        uid = '0', 
                        name = '0', )
                    ], 
                syslog_destinations = ubika_waap_api_client.models.add_reverse_proxy_syslog_destinations.AddReverseProxy_syslogDestinations(
                    enabled = True, 
                    uids = '0', ), 
                logs = ubika_waap_api_client.models.add_reverse_proxy_success_data_logs.AddReverseProxySuccess_data_logs(
                    debug = True, 
                    filter = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                        uid = '0', 
                        name = '0', ), ), 
                monitor = ubika_waap_api_client.models.add_reverse_proxy_monitor.AddReverseProxy_monitor(
                    enabled = True, ), 
                t_update = 1.337
            )
        else :
            return GetReverseProxiesDataSuccessArray(
        )

    def testGetReverseProxiesDataSuccessArray(self):
        """Test GetReverseProxiesDataSuccessArray"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
