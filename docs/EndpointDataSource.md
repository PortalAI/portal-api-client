# EndpointDataSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**method** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from openapi_client.models.endpoint_data_source import EndpointDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDataSource from a JSON string
endpoint_data_source_instance = EndpointDataSource.from_json(json)
# print the JSON string representation of the object
print EndpointDataSource.to_json()

# convert the object into a dict
endpoint_data_source_dict = endpoint_data_source_instance.to_dict()
# create an instance of EndpointDataSource from a dict
endpoint_data_source_form_dict = endpoint_data_source.from_dict(endpoint_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


