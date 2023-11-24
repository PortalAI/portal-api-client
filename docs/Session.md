# Session


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**agent_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**messages** | [**List[Message]**](Message.md) |  | 
**status** | [**SessionStatus**](SessionStatus.md) |  | 
**routine_id** | **str** |  | [optional] 

## Example

```python
from portal_client.portal_client.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print Session.to_json()

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_form_dict = session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


