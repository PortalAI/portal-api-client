# PlaygroundAgent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**icon** | **str** |  | 
**assistant_id** | **str** |  | 
**instructions** | **str** |  | 

## Example

```python
from portal_client.models.playground_agent import PlaygroundAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundAgent from a JSON string
playground_agent_instance = PlaygroundAgent.from_json(json)
# print the JSON string representation of the object
print PlaygroundAgent.to_json()

# convert the object into a dict
playground_agent_dict = playground_agent_instance.to_dict()
# create an instance of PlaygroundAgent from a dict
playground_agent_form_dict = playground_agent.from_dict(playground_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


