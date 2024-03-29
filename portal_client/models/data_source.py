# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from portal_client.models.endpoint_data_source import EndpointDataSource
from portal_client.models.google_table_data_source import GoogleTableDataSource
from portal_client.models.local_file_data_source import LocalFileDataSource
from portal_client.models.sql_tables_data_source import SqlTablesDataSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DataSource(BaseModel):
    """
    DataSource
    """ # noqa: E501
    endpoints: Optional[List[EndpointDataSource]] = None
    sql_tables: Optional[List[SqlTablesDataSource]] = None
    google_tables: Optional[List[GoogleTableDataSource]] = None
    local_files: Optional[List[LocalFileDataSource]] = None
    file_ids: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["endpoints", "sql_tables", "google_tables", "local_files", "file_ids"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item in self.endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sql_tables (list)
        _items = []
        if self.sql_tables:
            for _item in self.sql_tables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sql_tables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in google_tables (list)
        _items = []
        if self.google_tables:
            for _item in self.google_tables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['google_tables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in local_files (list)
        _items = []
        if self.local_files:
            for _item in self.local_files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['local_files'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DataSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endpoints": [EndpointDataSource.from_dict(_item) for _item in obj.get("endpoints")] if obj.get("endpoints") is not None else None,
            "sql_tables": [SqlTablesDataSource.from_dict(_item) for _item in obj.get("sql_tables")] if obj.get("sql_tables") is not None else None,
            "google_tables": [GoogleTableDataSource.from_dict(_item) for _item in obj.get("google_tables")] if obj.get("google_tables") is not None else None,
            "local_files": [LocalFileDataSource.from_dict(_item) for _item in obj.get("local_files")] if obj.get("local_files") is not None else None,
            "file_ids": obj.get("file_ids")
        })
        return _obj


