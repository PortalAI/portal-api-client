# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.test_api import TestApi


class TestTestApi(unittest.TestCase):
    """TestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TestApi()

    def tearDown(self) -> None:
        pass

    def test_get_agents_test_metrics_get(self) -> None:
        """Test case for get_agents_test_metrics_get

        Get Agents
        """
        pass


if __name__ == '__main__':
    unittest.main()