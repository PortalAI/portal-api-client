# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class MessageRole(str, Enum):
    """
    MessageRole
    """

    """
    allowed enum values
    """
    USER = 'user'
    ASSISTANT = 'assistant'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageRole from a JSON string"""
        return cls(json.loads(json_str))


