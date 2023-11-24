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

from openapi_client.models.get_sessions_response import GetSessionsResponse

class TestGetSessionsResponse(unittest.TestCase):
    """GetSessionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSessionsResponse:
        """Test GetSessionsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSessionsResponse`
        """
        model = GetSessionsResponse()
        if include_optional:
            return GetSessionsResponse(
                sessions = [
                    openapi_client.models.session.Session(
                        id = '', 
                        agent_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        messages = [
                            openapi_client.models.message.Message(
                                text = '', 
                                role = 'user', )
                            ], 
                        status = 'Ready', 
                        routine_id = '', )
                    ]
            )
        else:
            return GetSessionsResponse(
                sessions = [
                    openapi_client.models.session.Session(
                        id = '', 
                        agent_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        messages = [
                            openapi_client.models.message.Message(
                                text = '', 
                                role = 'user', )
                            ], 
                        status = 'Ready', 
                        routine_id = '', )
                    ],
        )
        """

    def testGetSessionsResponse(self):
        """Test GetSessionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
