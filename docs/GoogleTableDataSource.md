# GoogleTableDataSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spreadsheet_id** | **str** |  | 
**sheet_name** | **str** |  | 

## Example

```python
from portal_client.models.google_table_data_source import GoogleTableDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTableDataSource from a JSON string
google_table_data_source_instance = GoogleTableDataSource.from_json(json)
# print the JSON string representation of the object
print GoogleTableDataSource.to_json()

# convert the object into a dict
google_table_data_source_dict = google_table_data_source_instance.to_dict()
# create an instance of GoogleTableDataSource from a dict
google_table_data_source_form_dict = google_table_data_source.from_dict(google_table_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


