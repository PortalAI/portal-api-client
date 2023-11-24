# CreateRoutineRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | 
**name** | **str** |  | 
**requirements** | **str** |  | 
**interval** | **str** |  | 
**data_source** | [**DataSource**](DataSource.md) |  | 

## Example

```python
from portal_client.models.create_routine_request import CreateRoutineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoutineRequest from a JSON string
create_routine_request_instance = CreateRoutineRequest.from_json(json)
# print the JSON string representation of the object
print CreateRoutineRequest.to_json()

# convert the object into a dict
create_routine_request_dict = create_routine_request_instance.to_dict()
# create an instance of CreateRoutineRequest from a dict
create_routine_request_form_dict = create_routine_request.from_dict(create_routine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


