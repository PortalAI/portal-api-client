# Trend


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**status** | [**TrendStatus**](TrendStatus.md) |  | 

## Example

```python
from portal_client.models.trend import Trend

# TODO update the JSON string below
json = "{}"
# create an instance of Trend from a JSON string
trend_instance = Trend.from_json(json)
# print the JSON string representation of the object
print Trend.to_json()

# convert the object into a dict
trend_dict = trend_instance.to_dict()
# create an instance of Trend from a dict
trend_form_dict = trend.from_dict(trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


