# Agent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**assistant_id** | **str** |  | 
**assistant_nickname** | **str** |  | 
**welcome_message** | **str** |  | 
**user_initial_message** | **str** |  | 
**icon** | **str** |  | 
**visibility_requirements** | **List[str]** |  | 

## Example

```python
from portal_client.portal_client.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print Agent.to_json()

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


