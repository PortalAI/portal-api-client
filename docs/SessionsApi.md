# portal_client.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_async_session**](SessionsApi.md#create_async_session) | **POST** /sessions/async | Create Async Session
[**create_session**](SessionsApi.md#create_session) | **POST** /sessions | Create Session
[**create_session_from_replay**](SessionsApi.md#create_session_from_replay) | **POST** /sessions/replay | Create Session From Replay
[**get_grouped_sessions**](SessionsApi.md#get_grouped_sessions) | **GET** /sessions/grouped | Get Grouped Sessions
[**get_session**](SessionsApi.md#get_session) | **GET** /sessions/{session_id} | Get Session
[**get_sessions**](SessionsApi.md#get_sessions) | **GET** /sessions | Get Sessions
[**subscribe_to_session**](SessionsApi.md#subscribe_to_session) | **GET** /sessions/{session_id}/subscribe | Subscribe To Session
[**update_async_session**](SessionsApi.md#update_async_session) | **PUT** /sessions/{session_id}/async | Update Async Session
[**update_session**](SessionsApi.md#update_session) | **PUT** /sessions/{session_id} | Update Session


# **create_async_session**
> AsyncSessionResponse create_async_session(agent_id, text_prompt, files=files)

Create Async Session

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.async_session_response import AsyncSessionResponse
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
    api_instance = portal_client.SessionsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    text_prompt = 'text_prompt_example' # str | 
    files = None # List[bytearray] |  (optional)

    try:
        # Create Async Session
        api_response = api_instance.create_async_session(agent_id, text_prompt, files=files)
        print("The response of SessionsApi->create_async_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_async_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **text_prompt** | **str**|  | 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

[**AsyncSessionResponse**](AsyncSessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> Session create_session(agent_id, text_prompt, files=files)

Create Session

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.session import Session
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
    api_instance = portal_client.SessionsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    text_prompt = 'text_prompt_example' # str | 
    files = None # List[bytearray] |  (optional)

    try:
        # Create Session
        api_response = api_instance.create_session(agent_id, text_prompt, files=files)
        print("The response of SessionsApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **text_prompt** | **str**|  | 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session_from_replay**
> Session create_session_from_replay(session_id, last_message_index)

Create Session From Replay

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.session import Session
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
    api_instance = portal_client.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    last_message_index = 56 # int | 

    try:
        # Create Session From Replay
        api_response = api_instance.create_session_from_replay(session_id, last_message_index)
        print("The response of SessionsApi->create_session_from_replay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_session_from_replay: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **last_message_index** | **int**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grouped_sessions**
> GroupedSessionsResponse get_grouped_sessions()

Get Grouped Sessions

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.grouped_sessions_response import GroupedSessionsResponse
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
    api_instance = portal_client.SessionsApi(api_client)

    try:
        # Get Grouped Sessions
        api_response = api_instance.get_grouped_sessions()
        print("The response of SessionsApi->get_grouped_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_grouped_sessions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupedSessionsResponse**](GroupedSessionsResponse.md)

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

# **get_session**
> Session get_session(session_id)

Get Session

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.session import Session
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
    api_instance = portal_client.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Get Session
        api_response = api_instance.get_session(session_id)
        print("The response of SessionsApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> GetSessionsResponse get_sessions(agent_id)

Get Sessions

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.get_sessions_response import GetSessionsResponse
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
    api_instance = portal_client.SessionsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Sessions
        api_response = api_instance.get_sessions(agent_id)
        print("The response of SessionsApi->get_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_sessions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**GetSessionsResponse**](GetSessionsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_session**
> Session subscribe_to_session(session_id)

Subscribe To Session

### Example

```python
import time
import os
import portal_client
from portal_client.models.session import Session
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
    api_instance = portal_client.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Subscribe To Session
        api_response = api_instance.subscribe_to_session(session_id)
        print("The response of SessionsApi->subscribe_to_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->subscribe_to_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**Session**](Session.md)

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

# **update_async_session**
> AsyncSessionResponse update_async_session(session_id, text_prompt, files=files)

Update Async Session

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.async_session_response import AsyncSessionResponse
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
    api_instance = portal_client.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    text_prompt = 'text_prompt_example' # str | 
    files = None # List[bytearray] |  (optional)

    try:
        # Update Async Session
        api_response = api_instance.update_async_session(session_id, text_prompt, files=files)
        print("The response of SessionsApi->update_async_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->update_async_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **text_prompt** | **str**|  | 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

[**AsyncSessionResponse**](AsyncSessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_session**
> Session update_session(session_id, text_prompt, files=files)

Update Session

### Example

* Bearer Authentication (HTTPBearer):
```python
import time
import os
import portal_client
from portal_client.models.session import Session
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
    api_instance = portal_client.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    text_prompt = 'text_prompt_example' # str | 
    files = None # List[bytearray] |  (optional)

    try:
        # Update Session
        api_response = api_instance.update_session(session_id, text_prompt, files=files)
        print("The response of SessionsApi->update_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->update_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **text_prompt** | **str**|  | 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

