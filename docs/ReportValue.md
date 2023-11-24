# ReportValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**text** | **str** |  | 
**link** | **str** |  | [optional] [default to '']

## Example

```python
from portal_client.models.report_value import ReportValue

# TODO update the JSON string below
json = "{}"
# create an instance of ReportValue from a JSON string
report_value_instance = ReportValue.from_json(json)
# print the JSON string representation of the object
print ReportValue.to_json()

# convert the object into a dict
report_value_dict = report_value_instance.to_dict()
# create an instance of ReportValue from a dict
report_value_form_dict = report_value.from_dict(report_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


