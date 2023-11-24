# portal_client.AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert**](AlertsApi.md#create_alert) | **POST** /alerts | Create Alert
[**get_alerts**](AlertsApi.md#get_alerts) | **GET** /alerts | Get Alerts
[**update_alert**](AlertsApi.md#update_alert) | **PUT** /alerts/{alert_id} | Update Alert


# **create_alert**
> Alert create_alert(alert)

Create Alert

### Example

```python
import time
import os
import portal_client
from portal_client.models.alert import Alert
from portal_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = portal_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with portal_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = portal_client.AlertsApi(api_client)
    alert = portal_client.Alert() # Alert | 

    try:
        # Create Alert
        api_response = api_instance.create_alert(alert)
        print("The response of AlertsApi->create_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**Alert**](Alert.md)|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> List[Alert] get_alerts()

Get Alerts

### Example

```python
import time
import os
import portal_client
from portal_client.models.alert import Alert
from portal_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = portal_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with portal_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = portal_client.AlertsApi(api_client)

    try:
        # Get Alerts
        api_response = api_instance.get_alerts()
        print("The response of AlertsApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Alert]**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> Alert update_alert(alert_id, alert)

Update Alert

### Example

```python
import time
import os
import portal_client
from portal_client.models.alert import Alert
from portal_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = portal_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with portal_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = portal_client.AlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 
    alert = portal_client.Alert() # Alert | 

    try:
        # Update Alert
        api_response = api_instance.update_alert(alert_id, alert)
        print("The response of AlertsApi->update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_alert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 
 **alert** | [**Alert**](Alert.md)|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

