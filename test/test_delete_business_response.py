# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from portal_client.models.delete_business_response import DeleteBusinessResponse

class TestDeleteBusinessResponse(unittest.TestCase):
    """DeleteBusinessResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteBusinessResponse:
        """Test DeleteBusinessResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteBusinessResponse`
        """
        model = DeleteBusinessResponse()
        if include_optional:
            return DeleteBusinessResponse(
                success = True
            )
        else:
            return DeleteBusinessResponse(
                success = True,
        )
        """

    def testDeleteBusinessResponse(self):
        """Test DeleteBusinessResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
