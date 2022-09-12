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
from ubika_waap_api_client.models.update_certificates_bundle_ca_success_array import UpdateCertificatesBundleCaSuccessArray  # noqa: E501
from ubika_waap_api_client.rest import ApiException

class TestUpdateCertificatesBundleCaSuccessArray(unittest.TestCase):
    """UpdateCertificatesBundleCaSuccessArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateCertificatesBundleCaSuccessArray
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ubika_waap_api_client.models.update_certificates_bundle_ca_success_array.UpdateCertificatesBundleCaSuccessArray()  # noqa: E501
        if include_optional :
            return UpdateCertificatesBundleCaSuccessArray(
                uid = '0', 
                name = '0', 
                date = '0', 
                dn = '0'
            )
        else :
            return UpdateCertificatesBundleCaSuccessArray(
        )

    def testUpdateCertificatesBundleCaSuccessArray(self):
        """Test UpdateCertificatesBundleCaSuccessArray"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
