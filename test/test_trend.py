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

from openapi_client.models.trend import Trend

class TestTrend(unittest.TestCase):
    """Trend unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Trend:
        """Test Trend
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Trend`
        """
        model = Trend()
        if include_optional:
            return Trend(
                description = '',
                status = 'POSITIVE'
            )
        else:
            return Trend(
                description = '',
                status = 'POSITIVE',
        )
        """

    def testTrend(self):
        """Test Trend"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()