# CreateOnboardingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_message** | **str** |  | 

## Example

```python
from portal_client.models.create_onboarding_request import CreateOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOnboardingRequest from a JSON string
create_onboarding_request_instance = CreateOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print CreateOnboardingRequest.to_json()

# convert the object into a dict
create_onboarding_request_dict = create_onboarding_request_instance.to_dict()
# create an instance of CreateOnboardingRequest from a dict
create_onboarding_request_form_dict = create_onboarding_request.from_dict(create_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


