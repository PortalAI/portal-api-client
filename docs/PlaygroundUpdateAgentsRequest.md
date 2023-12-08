# PlaygroundUpdateAgentsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[PlaygroundAgent]**](PlaygroundAgent.md) |  | 

## Example

```python
from portal_client.models.playground_update_agents_request import PlaygroundUpdateAgentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundUpdateAgentsRequest from a JSON string
playground_update_agents_request_instance = PlaygroundUpdateAgentsRequest.from_json(json)
# print the JSON string representation of the object
print PlaygroundUpdateAgentsRequest.to_json()

# convert the object into a dict
playground_update_agents_request_dict = playground_update_agents_request_instance.to_dict()
# create an instance of PlaygroundUpdateAgentsRequest from a dict
playground_update_agents_request_form_dict = playground_update_agents_request.from_dict(playground_update_agents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


