# portal_client.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent**](AgentsApi.md#get_agent) | **GET** /agents/{agent_id} | Get Agents
[**get_agents**](AgentsApi.md#get_agents) | **GET** /agents | Get Agents


# **get_agent**
> Agent get_agent(agent_id)

Get Agents

### Example

```python
import time
import os
import portal_client
from portal_client.models.agent import Agent
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
    api_instance = portal_client.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agents
        api_response = api_instance.get_agent(agent_id)
        print("The response of AgentsApi->get_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**Agent**](Agent.md)

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

# **get_agents**
> AgentsResponse get_agents()

Get Agents

### Example

```python
import time
import os
import portal_client
from portal_client.models.agents_response import AgentsResponse
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
    api_instance = portal_client.AgentsApi(api_client)

    try:
        # Get Agents
        api_response = api_instance.get_agents()
        print("The response of AgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AgentsResponse**](AgentsResponse.md)

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

