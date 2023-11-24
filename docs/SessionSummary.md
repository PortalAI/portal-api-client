# SessionSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**agent** | [**Agent**](Agent.md) |  | 
**updated_at** | **datetime** |  | 
**name** | **str** |  | 

## Example

```python
from portal_client.portal_client.session_summary import SessionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSummary from a JSON string
session_summary_instance = SessionSummary.from_json(json)
# print the JSON string representation of the object
print SessionSummary.to_json()

# convert the object into a dict
session_summary_dict = session_summary_instance.to_dict()
# create an instance of SessionSummary from a dict
session_summary_form_dict = session_summary.from_dict(session_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


