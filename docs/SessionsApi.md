# portal_client.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session_from_text**](SessionsApi.md#create_session_from_text) | **POST** /sessions/text | Create Session From Text
[**get_grouped_sessions**](SessionsApi.md#get_grouped_sessions) | **GET** /sessions/grouped | Get Grouped Sessions
[**get_session**](SessionsApi.md#get_session) | **GET** /sessions/{session_id} | Get Session
[**get_sessions**](SessionsApi.md#get_sessions) | **GET** /sessions | Get Sessions
[**update_session**](SessionsApi.md#update_session) | **PUT** /sessions/{session_id} | Update Session


# **create_session_from_text**
> Session create_session_from_text(agent_id, text_prompt, files=files)

Create Session From Text

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
    agent_id = 'agent_id_example' # str | 
    text_prompt = 'text_prompt_example' # str | 
    files = None # List[bytearray] |  (optional)

    try:
        # Create Session From Text
        api_response = api_instance.create_session_from_text(agent_id, text_prompt, files=files)
        print("The response of SessionsApi->create_session_from_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_session_from_text: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

No authorization required

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

# **get_sessions**
> GetSessionsResponse get_sessions(agent_id)

Get Sessions

### Example

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

# **update_session**
> Session update_session(session_id, text_prompt, files=files)

Update Session

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

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

