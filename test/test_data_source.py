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

from portal_client.models.data_source import DataSource

class TestDataSource(unittest.TestCase):
    """DataSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSource:
        """Test DataSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSource`
        """
        model = DataSource()
        if include_optional:
            return DataSource(
                endpoints = [
                    portal_client.models.endpoint_data_source.EndpointDataSource(
                        url = '', 
                        method = '', 
                        description = '', )
                    ],
                sql_tables = [
                    portal_client.models.sql_tables_data_source.SqlTablesDataSource(
                        connection_string = '', 
                        table_name = '', )
                    ],
                google_tables = [
                    portal_client.models.google_table_data_source.GoogleTableDataSource(
                        spreadsheet_id = '', 
                        sheet_name = '', )
                    ],
                local_files = [
                    portal_client.models.local_file_data_source.LocalFileDataSource(
                        path = '', )
                    ]
            )
        else:
            return DataSource(
        )
        """

    def testDataSource(self):
        """Test DataSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
