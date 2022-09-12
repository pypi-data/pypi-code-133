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
from ubika_waap_api_client.models.patch_certificates_bundle_success_data import PatchCertificatesBundleSuccessData  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestPatchCertificatesBundleSuccessData(unittest.TestCase):
    """PatchCertificatesBundleSuccessData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchCertificatesBundleSuccessData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.patch_certificates_bundle_success_data.PatchCertificatesBundleSuccessData()  # noqa: E501
        if include_optional :
            return PatchCertificatesBundleSuccessData(
                uid = '0', 
                name = '0', 
                ca = [
                    ubika_waap_api_client.models.patch_certificates_bundle_ca_success_array.PatchCertificatesBundleCaSuccessArray(
                        uid = '0', 
                        name = '0', 
                        date = '0', 
                        dn = '0', )
                    ], 
                ca_ocsp = [
                    ubika_waap_api_client.models.patch_certificates_bundle_ca_ocsp_success_array.PatchCertificatesBundleCaOCSPSuccessArray(
                        uid = '0', 
                        name = '0', 
                        expiration = '0', 
                        dn = '0', )
                    ], 
                crl = [
                    ubika_waap_api_client.models.patch_certificates_bundle_crl_success_array.PatchCertificatesBundleCrlSuccessArray(
                        uid = '0', 
                        name = '0', 
                        expiration = '0', 
                        issuer = '0', 
                        next_update = '0', 
                        enable_auto_update = True, 
                        download_url = '0', 
                        download_method = '0', 
                        refresh_cron_time = '0', 
                        enable = True, 
                        enable_proxy = True, 
                        enable_proxy_authentication = True, 
                        proxy_profile_uid = '0', 
                        header_host = '0', )
                    ], 
                t_update = 1.337
            )
        else :
            return PatchCertificatesBundleSuccessData(
        )

    def testPatchCertificatesBundleSuccessData(self):
        """Test PatchCertificatesBundleSuccessData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
