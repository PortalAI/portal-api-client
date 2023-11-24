# BusinessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business** | [**Business**](Business.md) |  | 

## Example

```python
from portal_client.portal_client.business_response import BusinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessResponse from a JSON string
business_response_instance = BusinessResponse.from_json(json)
# print the JSON string representation of the object
print BusinessResponse.to_json()

# convert the object into a dict
business_response_dict = business_response_instance.to_dict()
# create an instance of BusinessResponse from a dict
business_response_form_dict = business_response.from_dict(business_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


