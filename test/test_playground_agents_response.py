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

from portal_client.models.playground_agents_response import PlaygroundAgentsResponse

class TestPlaygroundAgentsResponse(unittest.TestCase):
    """PlaygroundAgentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaygroundAgentsResponse:
        """Test PlaygroundAgentsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaygroundAgentsResponse`
        """
        model = PlaygroundAgentsResponse()
        if include_optional:
            return PlaygroundAgentsResponse(
                agents = [
                    portal_client.models.playground_agent.PlaygroundAgent(
                        id = '', 
                        name = '', 
                        icon = '', 
                        assistant_id = '', 
                        instructions = '', )
                    ]
            )
        else:
            return PlaygroundAgentsResponse(
                agents = [
                    portal_client.models.playground_agent.PlaygroundAgent(
                        id = '', 
                        name = '', 
                        icon = '', 
                        assistant_id = '', 
                        instructions = '', )
                    ],
        )
        """

    def testPlaygroundAgentsResponse(self):
        """Test PlaygroundAgentsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()