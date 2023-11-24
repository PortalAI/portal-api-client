# Dashboard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widgets** | [**List[Widget]**](Widget.md) |  | 

## Example

```python
from portal_client.portal_client.dashboard import Dashboard

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboard from a JSON string
dashboard_instance = Dashboard.from_json(json)
# print the JSON string representation of the object
print Dashboard.to_json()

# convert the object into a dict
dashboard_dict = dashboard_instance.to_dict()
# create an instance of Dashboard from a dict
dashboard_form_dict = dashboard.from_dict(dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


