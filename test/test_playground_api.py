# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from portal_client.api.playground_api import PlaygroundApi


class TestPlaygroundApi(unittest.TestCase):
    """PlaygroundApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlaygroundApi()

    def tearDown(self) -> None:
        pass

    def test_get_playground_agents(self) -> None:
        """Test case for get_playground_agents

        Get Agents
        """
        pass

    def test_update_playground_agents(self) -> None:
        """Test case for update_playground_agents

        Update Agents
        """
        pass


if __name__ == '__main__':
    unittest.main()
