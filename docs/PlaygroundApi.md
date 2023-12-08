# portal_client.PlaygroundApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_playground_agents**](PlaygroundApi.md#get_playground_agents) | **GET** /playground/agents | Get Agents
[**update_playground_agents**](PlaygroundApi.md#update_playground_agents) | **PUT** /playground/agents | Update Agents


# **get_playground_agents**
> PlaygroundAgentsResponse get_playground_agents()

Get Agents

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.playground_agents_response import PlaygroundAgentsResponse
from portal_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = portal_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = portal_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with portal_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = portal_client.PlaygroundApi(api_client)

    try:
        # Get Agents
        api_response = api_instance.get_playground_agents()
        print("The response of PlaygroundApi->get_playground_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->get_playground_agents: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PlaygroundAgentsResponse**](PlaygroundAgentsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_playground_agents**
> PlaygroundAgentsResponse update_playground_agents(playground_update_agents_request)

Update Agents

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.playground_agents_response import PlaygroundAgentsResponse
from portal_client.models.playground_update_agents_request import PlaygroundUpdateAgentsRequest
from portal_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = portal_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = portal_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with portal_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = portal_client.PlaygroundApi(api_client)
    playground_update_agents_request = portal_client.PlaygroundUpdateAgentsRequest() # PlaygroundUpdateAgentsRequest | 

    try:
        # Update Agents
        api_response = api_instance.update_playground_agents(playground_update_agents_request)
        print("The response of PlaygroundApi->update_playground_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->update_playground_agents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playground_update_agents_request** | [**PlaygroundUpdateAgentsRequest**](PlaygroundUpdateAgentsRequest.md)|  | 

### Return type

[**PlaygroundAgentsResponse**](PlaygroundAgentsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

