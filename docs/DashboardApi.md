# portal_client.DashboardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /dashboard | Get Dashboard


# **get_dashboard**
> Dashboard get_dashboard()

Get Dashboard

### Example

```python
import time
import os
import portal_client
from portal_client.models.dashboard import Dashboard
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
    api_instance = portal_client.DashboardApi(api_client)

    try:
        # Get Dashboard
        api_response = api_instance.get_dashboard()
        print("The response of DashboardApi->get_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->get_dashboard: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Dashboard**](Dashboard.md)

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

