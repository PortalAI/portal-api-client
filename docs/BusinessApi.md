# portal_client.BusinessApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_business**](BusinessApi.md#delete_business) | **DELETE** /business/{business_id} | Delete Business
[**get_business**](BusinessApi.md#get_business) | **GET** /business | Get Business
[**update_business**](BusinessApi.md#update_business) | **PUT** /business | Update Business


# **delete_business**
> DeleteBusinessResponse delete_business(business_id)

Delete Business

### Example

```python
import time
import os
import portal_client
from portal_client.models.delete_business_response import DeleteBusinessResponse
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
    api_instance = portal_client.BusinessApi(api_client)
    business_id = 'business_id_example' # str | 

    try:
        # Delete Business
        api_response = api_instance.delete_business(business_id)
        print("The response of BusinessApi->delete_business:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->delete_business: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 

### Return type

[**DeleteBusinessResponse**](DeleteBusinessResponse.md)

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

# **get_business**
> BusinessResponse get_business()

Get Business

### Example

```python
import time
import os
import portal_client
from portal_client.models.business_response import BusinessResponse
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
    api_instance = portal_client.BusinessApi(api_client)

    try:
        # Get Business
        api_response = api_instance.get_business()
        print("The response of BusinessApi->get_business:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->get_business: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**BusinessResponse**](BusinessResponse.md)

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

# **update_business**
> Business update_business(business)

Update Business

### Example

```python
import time
import os
import portal_client
from portal_client.models.business import Business
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
    api_instance = portal_client.BusinessApi(api_client)
    business = portal_client.Business() # Business | 

    try:
        # Update Business
        api_response = api_instance.update_business(business)
        print("The response of BusinessApi->update_business:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->update_business: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business** | [**Business**](Business.md)|  | 

### Return type

[**Business**](Business.md)

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

