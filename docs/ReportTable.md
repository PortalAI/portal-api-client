# ReportTable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**columns** | **List[str]** |  | 
**rows** | [**List[ReportRow]**](ReportRow.md) |  | 

## Example

```python
from portal_client.portal_client.report_table import ReportTable

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTable from a JSON string
report_table_instance = ReportTable.from_json(json)
# print the JSON string representation of the object
print ReportTable.to_json()

# convert the object into a dict
report_table_dict = report_table_instance.to_dict()
# create an instance of ReportTable from a dict
report_table_form_dict = report_table.from_dict(report_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


