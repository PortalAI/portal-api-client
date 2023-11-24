# GetSessionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[Session]**](Session.md) |  | 

## Example

```python
from portal_client.models.get_sessions_response import GetSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSessionsResponse from a JSON string
get_sessions_response_instance = GetSessionsResponse.from_json(json)
# print the JSON string representation of the object
print GetSessionsResponse.to_json()

# convert the object into a dict
get_sessions_response_dict = get_sessions_response_instance.to_dict()
# create an instance of GetSessionsResponse from a dict
get_sessions_response_form_dict = get_sessions_response.from_dict(get_sessions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


