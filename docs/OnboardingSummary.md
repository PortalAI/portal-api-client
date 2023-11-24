# OnboardingSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business** | [**Business**](Business.md) |  | 
**routines** | [**List[Routine]**](Routine.md) |  | 

## Example

```python
from portal_client.models.onboarding_summary import OnboardingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingSummary from a JSON string
onboarding_summary_instance = OnboardingSummary.from_json(json)
# print the JSON string representation of the object
print OnboardingSummary.to_json()

# convert the object into a dict
onboarding_summary_dict = onboarding_summary_instance.to_dict()
# create an instance of OnboardingSummary from a dict
onboarding_summary_form_dict = onboarding_summary.from_dict(onboarding_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


