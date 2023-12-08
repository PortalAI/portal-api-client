# MessageAgent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**icon** | **str** |  | 

## Example

```python
from portal_client.models.message_agent import MessageAgent

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAgent from a JSON string
message_agent_instance = MessageAgent.from_json(json)
# print the JSON string representation of the object
print MessageAgent.to_json()

# convert the object into a dict
message_agent_dict = message_agent_instance.to_dict()
# create an instance of MessageAgent from a dict
message_agent_form_dict = message_agent.from_dict(message_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


