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

from portal_client.models.agent import Agent

class TestAgent(unittest.TestCase):
    """Agent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Agent:
        """Test Agent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Agent`
        """
        model = Agent()
        if include_optional:
            return Agent(
                id = '',
                name = '',
                assistant_id = '',
                assistant_nickname = '',
                welcome_message = '',
                user_initial_message = '',
                icon = '',
                visibility_requirements = [
                    ''
                    ]
            )
        else:
            return Agent(
                id = '',
                name = '',
                assistant_id = '',
                assistant_nickname = '',
                welcome_message = '',
                user_initial_message = '',
                icon = '',
                visibility_requirements = [
                    ''
                    ],
        )
        """

    def testAgent(self):
        """Test Agent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
