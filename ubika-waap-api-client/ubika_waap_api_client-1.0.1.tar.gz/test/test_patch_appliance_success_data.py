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
from ubika_waap_api_client.models.patch_appliance_success_data import PatchApplianceSuccessData  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestPatchApplianceSuccessData(unittest.TestCase):
    """PatchApplianceSuccessData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchApplianceSuccessData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.patch_appliance_success_data.PatchApplianceSuccessData()  # noqa: E501
        if include_optional :
            return PatchApplianceSuccessData(
                uid = '0', 
                name = '0', 
                role = '0', 
                autoscale = True, 
                admin_ip = '0', 
                admin_port = 56, 
                location = '0', 
                contact = '0', 
                os_version = '0', 
                ssh = ubika_waap_api_client.models.patch_appliance_success_data_ssh.PatchApplianceSuccess_data_ssh(
                    enable = True, 
                    interfaces = [
                        ubika_waap_api_client.models.patch_appliance_interfaces_success_array.PatchApplianceInterfacesSuccessArray(
                            uid = '0', 
                            name = '0', 
                            ip = '0', )
                        ], 
                    port = 56, ), 
                dns = ubika_waap_api_client.models.create_appliance_success_data_dns.CreateApplianceSuccess_data_dns(
                    enable = True, 
                    dns1 = '0', 
                    dns2 = '0', 
                    dns_ttl_min = '0', 
                    dns_ttl_max = '0', ), 
                snmp = ubika_waap_api_client.models.patch_appliance_success_data_snmp.PatchApplianceSuccess_data_snmp(
                    enable = True, 
                    interfaces = [
                        ubika_waap_api_client.models.patch_appliance_interfaces_success_array.PatchApplianceInterfacesSuccessArray(
                            uid = '0', 
                            name = '0', 
                            ip = '0', )
                        ], 
                    port = '0', 
                    sys_location = '0', 
                    sys_contact = '0', 
                    community = '0', 
                    network_filter = '0', ), 
                hosts = ubika_waap_api_client.models.create_appliance_success_data_hosts.CreateApplianceSuccess_data_hosts(
                    ip = '0', 
                    hostname = '0', ), 
                network_devices = [
                    ubika_waap_api_client.models.patch_appliance_network_devices_success_array.PatchApplianceNetworkDevicesSuccessArray(
                        uid = '0', 
                        name = '0', )
                    ], 
                sysctl_profile = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                    uid = '0', 
                    name = '0', ), 
                t_update = 1.337
            )
        else :
            return PatchApplianceSuccessData(
        )

    def testPatchApplianceSuccessData(self):
        """Test PatchApplianceSuccessData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
