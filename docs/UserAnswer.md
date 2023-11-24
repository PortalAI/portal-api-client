# UserAnswer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from portal_client.portal_client.user_answer import UserAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of UserAnswer from a JSON string
user_answer_instance = UserAnswer.from_json(json)
# print the JSON string representation of the object
print UserAnswer.to_json()

# convert the object into a dict
user_answer_dict = user_answer_instance.to_dict()
# create an instance of UserAnswer from a dict
user_answer_form_dict = user_answer.from_dict(user_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


