# GroupedSessionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_to_sessions** | **Dict[str, object]** |  | 

## Example

```python
from portal_client.models.grouped_sessions_response import GroupedSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedSessionsResponse from a JSON string
grouped_sessions_response_instance = GroupedSessionsResponse.from_json(json)
# print the JSON string representation of the object
print GroupedSessionsResponse.to_json()

# convert the object into a dict
grouped_sessions_response_dict = grouped_sessions_response_instance.to_dict()
# create an instance of GroupedSessionsResponse from a dict
grouped_sessions_response_form_dict = grouped_sessions_response.from_dict(grouped_sessions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


