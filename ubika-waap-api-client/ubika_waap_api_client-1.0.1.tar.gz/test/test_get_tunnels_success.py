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
from ubika_waap_api_client.models.get_tunnels_success import GetTunnelsSuccess  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestGetTunnelsSuccess(unittest.TestCase):
    """GetTunnelsSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTunnelsSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.get_tunnels_success.GetTunnelsSuccess()  # noqa: E501
        if include_optional :
            return GetTunnelsSuccess(
                data = [
                    ubika_waap_api_client.models.get_tunnels_data_success_array.GetTunnelsDataSuccessArray(
                        uid = '0', 
                        name = '0', 
                        type = '0', 
                        reverse_proxy = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                            uid = '0', 
                            name = '0', ), 
                        workflow = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                            uid = '0', 
                            name = '0', ), 
                        workflow_parameters = [
                            ubika_waap_api_client.models.get_tunnels_workflow_parameters_success_array.GetTunnelsWorkflowParametersSuccessArray(
                                name = '0', 
                                value = '0', )
                            ], 
                        enabled = '0', 
                        labels = [
                            ubika_waap_api_client.models.get_tunnels_labels_success_array.GetTunnelsLabelsSuccessArray(
                                uid = '0', 
                                name = '0', )
                            ], 
                        network = ubika_waap_api_client.models.get_tunnels_data_success_array_network.GetTunnelsDataSuccessArray_network(
                            incoming = ubika_waap_api_client.models.get_tunnels_data_success_array_network_incoming.GetTunnelsDataSuccessArray_network_incoming(
                                incoming_type = '0', 
                                ip = '0', 
                                port = 56, 
                                vip = ubika_waap_api_client.models.create_tunnel_success_data_network_incoming_interface.CreateTunnelSuccess_data_network_incoming_interface(
                                    uid = '0', 
                                    name = '0', 
                                    ip = '0', ), 
                                interface = ubika_waap_api_client.models.create_tunnel_success_data_network_incoming_interface.CreateTunnelSuccess_data_network_incoming_interface(
                                    uid = '0', 
                                    name = '0', 
                                    ip = '0', ), 
                                pooler_tunnel = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                    uid = '0', 
                                    name = '0', ), 
                                server_name = '0', 
                                server_alias = [
                                    ubika_waap_api_client.models.get_tunnels_server_alias_success_array.GetTunnelsServerAliasSuccessArray()
                                    ], 
                                ssl = ubika_waap_api_client.models.create_tunnel_network_incoming_ssl.CreateTunnel_network_incoming_ssl(
                                    profile = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                        uid = '0', 
                                        name = '0', ), 
                                    certificate = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                        uid = '0', 
                                        name = '0', ), 
                                    sni_vhost_check = True, 
                                    sslhsts_enable = True, 
                                    verify_client_certificate = ubika_waap_api_client.models.create_tunnel_network_incoming_ssl_verify_client_certificate.CreateTunnel_network_incoming_ssl_verifyClientCertificate(
                                        bundle = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                            uid = '0', 
                                            name = '0', ), 
                                        ca = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                            uid = '0', 
                                            name = '0', ), 
                                        type = '0', 
                                        depth = 56, 
                                        ocsp = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                            uid = '0', 
                                            name = '0', ), 
                                        catch_errors = True, 
                                        legacy_dn_string_format = True, 
                                        ssl_redirect_enable = True, 
                                        ssl_redirect_port_in = 56, ), ), 
                                http2_enabled = True, ), 
                            outgoing = ubika_waap_api_client.models.get_tunnels_data_success_array_network_outgoing.GetTunnelsDataSuccessArray_network_outgoing(
                                address = '0', 
                                port = 56, 
                                load_balancer = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                    uid = '0', 
                                    name = '0', ), 
                                pooling_interface = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                                    uid = '0', 
                                    name = '0', ), 
                                pooling_port = 56, 
                                ajp_enable = True, ), ), 
                        secondary_tunnels = [
                            ubika_waap_api_client.models.get_tunnels_secondary_tunnels_success_array.GetTunnelsSecondaryTunnelsSuccessArray(
                                uid = '0', 
                                name = '0', )
                            ], 
                        appliance = ubika_waap_api_client.models.create_appliance_sysctl_profile.CreateAppliance_sysctlProfile(
                            uid = '0', 
                            name = '0', ), 
                        advanced = ubika_waap_api_client.models.create_tunnel_advanced.CreateTunnel_advanced(
                            advanced_parameters = ubika_waap_api_client.models.apply_ssl_key_uid.Apply_SSLKeyUid(
                                uid = '0', ), 
                            workflow_body = True, 
                            workflow_url_decode_body_plus_as_space = True, 
                            geo_ip_enabled = True, 
                            limit_request_body = 56, 
                            priority = 56, ), 
                        t_update = 1.337, )
                    ], 
                data_workflow_parameters = [
                    ubika_waap_api_client.models.get_tunnels_workflow_parameters_success_array.GetTunnelsWorkflowParametersSuccessArray(
                        name = '0', 
                        value = '0', )
                    ], 
                data_labels = [
                    ubika_waap_api_client.models.get_tunnels_labels_success_array.GetTunnelsLabelsSuccessArray(
                        uid = '0', 
                        name = '0', )
                    ], 
                data_network_incoming_server_alias = [
                    ubika_waap_api_client.models.get_tunnels_server_alias_success_array.GetTunnelsServerAliasSuccessArray()
                    ], 
                data_secondary_tunnels = [
                    ubika_waap_api_client.models.get_tunnels_secondary_tunnels_success_array.GetTunnelsSecondaryTunnelsSuccessArray(
                        uid = '0', 
                        name = '0', )
                    ]
            )
        else :
            return GetTunnelsSuccess(
        )

    def testGetTunnelsSuccess(self):
        """Test GetTunnelsSuccess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
