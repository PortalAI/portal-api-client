# PlaygroundAgentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[PlaygroundAgent]**](PlaygroundAgent.md) |  | 

## Example

```python
from portal_client.models.playground_agents_response import PlaygroundAgentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundAgentsResponse from a JSON string
playground_agents_response_instance = PlaygroundAgentsResponse.from_json(json)
# print the JSON string representation of the object
print PlaygroundAgentsResponse.to_json()

# convert the object into a dict
playground_agents_response_dict = playground_agents_response_instance.to_dict()
# create an instance of PlaygroundAgentsResponse from a dict
playground_agents_response_form_dict = playground_agents_response.from_dict(playground_agents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


