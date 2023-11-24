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

from openapi_client.models.routine_with_sessions import RoutineWithSessions

class TestRoutineWithSessions(unittest.TestCase):
    """RoutineWithSessions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutineWithSessions:
        """Test RoutineWithSessions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutineWithSessions`
        """
        model = RoutineWithSessions()
        if include_optional:
            return RoutineWithSessions(
                id = '',
                agent_id = '',
                name = '',
                requirements = '',
                interval = '',
                trend = openapi_client.models.trend.Trend(
                    description = '', 
                    status = 'POSITIVE', ),
                data_source = openapi_client.models.data_source.DataSource(
                    endpoints = [
                        openapi_client.models.endpoint_data_source.EndpointDataSource(
                            url = '', 
                            method = '', 
                            description = '', )
                        ], 
                    sql_tables = [
                        openapi_client.models.sql_tables_data_source.SqlTablesDataSource(
                            connection_string = '', 
                            table_name = '', )
                        ], 
                    google_tables = [
                        openapi_client.models.google_table_data_source.GoogleTableDataSource(
                            spreadsheet_id = '', 
                            sheet_name = '', )
                        ], 
                    local_files = [
                        openapi_client.models.local_file_data_source.LocalFileDataSource(
                            path = '', )
                        ], ),
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
                latest_answer = ''
            )
        else:
            return RoutineWithSessions(
                id = '',
                agent_id = '',
                name = '',
                requirements = '',
                interval = '',
                trend = openapi_client.models.trend.Trend(
                    description = '', 
                    status = 'POSITIVE', ),
                data_source = openapi_client.models.data_source.DataSource(
                    endpoints = [
                        openapi_client.models.endpoint_data_source.EndpointDataSource(
                            url = '', 
                            method = '', 
                            description = '', )
                        ], 
                    sql_tables = [
                        openapi_client.models.sql_tables_data_source.SqlTablesDataSource(
                            connection_string = '', 
                            table_name = '', )
                        ], 
                    google_tables = [
                        openapi_client.models.google_table_data_source.GoogleTableDataSource(
                            spreadsheet_id = '', 
                            sheet_name = '', )
                        ], 
                    local_files = [
                        openapi_client.models.local_file_data_source.LocalFileDataSource(
                            path = '', )
                        ], ),
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
                latest_answer = '',
        )
        """

    def testRoutineWithSessions(self):
        """Test RoutineWithSessions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
