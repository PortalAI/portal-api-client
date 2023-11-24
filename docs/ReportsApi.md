# portal_client.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report**](ReportsApi.md#get_report) | **GET** /reports/{agent_id} | Get Report


# **get_report**
> Report get_report(agent_id)

Get Report

### Example

```python
import time
import os
import portal_client
from portal_client.models.report import Report
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
    api_instance = portal_client.ReportsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Report
        api_response = api_instance.get_report(agent_id)
        print("The response of ReportsApi->get_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

