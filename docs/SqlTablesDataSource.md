# SqlTablesDataSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** |  | 
**table_name** | **str** |  | 

## Example

```python
from portal_client.models.sql_tables_data_source import SqlTablesDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTablesDataSource from a JSON string
sql_tables_data_source_instance = SqlTablesDataSource.from_json(json)
# print the JSON string representation of the object
print SqlTablesDataSource.to_json()

# convert the object into a dict
sql_tables_data_source_dict = sql_tables_data_source_instance.to_dict()
# create an instance of SqlTablesDataSource from a dict
sql_tables_data_source_form_dict = sql_tables_data_source.from_dict(sql_tables_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


