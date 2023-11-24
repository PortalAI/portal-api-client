# Business


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from portal_client.models.business import Business

# TODO update the JSON string below
json = "{}"
# create an instance of Business from a JSON string
business_instance = Business.from_json(json)
# print the JSON string representation of the object
print Business.to_json()

# convert the object into a dict
business_dict = business_instance.to_dict()
# create an instance of Business from a dict
business_form_dict = business.from_dict(business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


