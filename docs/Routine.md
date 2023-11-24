# Routine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**agent_id** | **str** |  | 
**name** | **str** |  | 
**requirements** | **str** |  | 
**interval** | **str** |  | 
**trend** | [**Trend**](Trend.md) |  | 
**data_source** | [**DataSource**](DataSource.md) |  | 

## Example

```python
from portal_client.models.routine import Routine

# TODO update the JSON string below
json = "{}"
# create an instance of Routine from a JSON string
routine_instance = Routine.from_json(json)
# print the JSON string representation of the object
print Routine.to_json()

# convert the object into a dict
routine_dict = routine_instance.to_dict()
# create an instance of Routine from a dict
routine_form_dict = routine.from_dict(routine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


