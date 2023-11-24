# OnboardingProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**answer** | [**Message**](Message.md) |  | 
**is_completed** | **bool** |  | 

## Example

```python
from openapi_client.models.onboarding_process import OnboardingProcess

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingProcess from a JSON string
onboarding_process_instance = OnboardingProcess.from_json(json)
# print the JSON string representation of the object
print OnboardingProcess.to_json()

# convert the object into a dict
onboarding_process_dict = onboarding_process_instance.to_dict()
# create an instance of OnboardingProcess from a dict
onboarding_process_form_dict = onboarding_process.from_dict(onboarding_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


