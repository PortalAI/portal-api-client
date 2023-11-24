# RoutinesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routines** | [**List[RoutineWithSessions]**](RoutineWithSessions.md) |  | 

## Example

```python
from openapi_client.models.routines_response import RoutinesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutinesResponse from a JSON string
routines_response_instance = RoutinesResponse.from_json(json)
# print the JSON string representation of the object
print RoutinesResponse.to_json()

# convert the object into a dict
routines_response_dict = routines_response_instance.to_dict()
# create an instance of RoutinesResponse from a dict
routines_response_form_dict = routines_response.from_dict(routines_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


