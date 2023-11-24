# openapi_client.OnboardingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_onboarding**](OnboardingApi.md#create_onboarding) | **POST** /onboarding | Create Onboarding
[**summarize_onboarding**](OnboardingApi.md#summarize_onboarding) | **PUT** /onboarding/{onboarding_id}/summarize | Summarize
[**update_onboarding**](OnboardingApi.md#update_onboarding) | **PUT** /onboarding/{onboarding_id} | Update Onboarding


# **create_onboarding**
> OnboardingProcess create_onboarding(create_onboarding_request)

Create Onboarding

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_onboarding_request import CreateOnboardingRequest
from openapi_client.models.onboarding_process import OnboardingProcess
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OnboardingApi(api_client)
    create_onboarding_request = openapi_client.CreateOnboardingRequest() # CreateOnboardingRequest | 

    try:
        # Create Onboarding
        api_response = api_instance.create_onboarding(create_onboarding_request)
        print("The response of OnboardingApi->create_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->create_onboarding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_onboarding_request** | [**CreateOnboardingRequest**](CreateOnboardingRequest.md)|  | 

### Return type

[**OnboardingProcess**](OnboardingProcess.md)

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

# **summarize_onboarding**
> OnboardingSummary summarize_onboarding(onboarding_id)

Summarize

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.onboarding_summary import OnboardingSummary
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OnboardingApi(api_client)
    onboarding_id = 'onboarding_id_example' # str | 

    try:
        # Summarize
        api_response = api_instance.summarize_onboarding(onboarding_id)
        print("The response of OnboardingApi->summarize_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->summarize_onboarding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboarding_id** | **str**|  | 

### Return type

[**OnboardingSummary**](OnboardingSummary.md)

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

# **update_onboarding**
> OnboardingProcess update_onboarding(onboarding_id, user_answer)

Update Onboarding

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.onboarding_process import OnboardingProcess
from openapi_client.models.user_answer import UserAnswer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OnboardingApi(api_client)
    onboarding_id = 'onboarding_id_example' # str | 
    user_answer = openapi_client.UserAnswer() # UserAnswer | 

    try:
        # Update Onboarding
        api_response = api_instance.update_onboarding(onboarding_id, user_answer)
        print("The response of OnboardingApi->update_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->update_onboarding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboarding_id** | **str**|  | 
 **user_answer** | [**UserAnswer**](UserAnswer.md)|  | 

### Return type

[**OnboardingProcess**](OnboardingProcess.md)

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

