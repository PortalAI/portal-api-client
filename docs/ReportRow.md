# ReportRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ReportValue]**](ReportValue.md) |  | 

## Example

```python
from portal_client.models.report_row import ReportRow

# TODO update the JSON string below
json = "{}"
# create an instance of ReportRow from a JSON string
report_row_instance = ReportRow.from_json(json)
# print the JSON string representation of the object
print ReportRow.to_json()

# convert the object into a dict
report_row_dict = report_row_instance.to_dict()
# create an instance of ReportRow from a dict
report_row_form_dict = report_row.from_dict(report_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


