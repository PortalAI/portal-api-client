# CreateBusinessRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from portal_client.models.create_business_request import CreateBusinessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBusinessRequest from a JSON string
create_business_request_instance = CreateBusinessRequest.from_json(json)
# print the JSON string representation of the object
print CreateBusinessRequest.to_json()

# convert the object into a dict
create_business_request_dict = create_business_request_instance.to_dict()
# create an instance of CreateBusinessRequest from a dict
create_business_request_form_dict = create_business_request.from_dict(create_business_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


