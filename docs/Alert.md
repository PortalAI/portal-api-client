# Alert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**insight** | **str** |  | 
**notifications** | [**List[Notification]**](Notification.md) |  | 
**status** | [**AlertStatus**](AlertStatus.md) |  | 
**is_active** | **bool** |  | 
**routine_id** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from openapi_client.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print Alert.to_json()

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_form_dict = alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


