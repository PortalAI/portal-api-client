# AsyncSessionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 

## Example

```python
from portal_client.models.async_session_response import AsyncSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncSessionResponse from a JSON string
async_session_response_instance = AsyncSessionResponse.from_json(json)
# print the JSON string representation of the object
print AsyncSessionResponse.to_json()

# convert the object into a dict
async_session_response_dict = async_session_response_instance.to_dict()
# create an instance of AsyncSessionResponse from a dict
async_session_response_form_dict = async_session_response.from_dict(async_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


