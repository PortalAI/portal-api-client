# RoutineWithSessions


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
**sessions** | [**List[Session]**](Session.md) |  | 
**latest_answer** | **str** |  | 

## Example

```python
from portal_client.models.routine_with_sessions import RoutineWithSessions

# TODO update the JSON string below
json = "{}"
# create an instance of RoutineWithSessions from a JSON string
routine_with_sessions_instance = RoutineWithSessions.from_json(json)
# print the JSON string representation of the object
print RoutineWithSessions.to_json()

# convert the object into a dict
routine_with_sessions_dict = routine_with_sessions_instance.to_dict()
# create an instance of RoutineWithSessions from a dict
routine_with_sessions_form_dict = routine_with_sessions.from_dict(routine_with_sessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


