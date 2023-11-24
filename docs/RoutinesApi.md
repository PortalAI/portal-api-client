# openapi_client.RoutinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_routine**](RoutinesApi.md#create_routine) | **POST** /routines | Create Routine
[**delete_routine**](RoutinesApi.md#delete_routine) | **DELETE** /routines/{routine_id} | Delete Routine
[**get_routines**](RoutinesApi.md#get_routines) | **GET** /routines | Get Routines
[**run_async_routine**](RoutinesApi.md#run_async_routine) | **PUT** /routines/{routine_id}/run/async | Run Async Routine
[**run_routine**](RoutinesApi.md#run_routine) | **PUT** /routines/{routine_id}/run | Run Routine


# **create_routine**
> Routine create_routine(create_routine_request)

Create Routine

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_routine_request import CreateRoutineRequest
from openapi_client.models.routine import Routine
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
    api_instance = openapi_client.RoutinesApi(api_client)
    create_routine_request = openapi_client.CreateRoutineRequest() # CreateRoutineRequest | 

    try:
        # Create Routine
        api_response = api_instance.create_routine(create_routine_request)
        print("The response of RoutinesApi->create_routine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutinesApi->create_routine: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_routine_request** | [**CreateRoutineRequest**](CreateRoutineRequest.md)|  | 

### Return type

[**Routine**](Routine.md)

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

# **delete_routine**
> RoutinesResponse delete_routine(routine_id)

Delete Routine

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.routines_response import RoutinesResponse
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
    api_instance = openapi_client.RoutinesApi(api_client)
    routine_id = 'routine_id_example' # str | 

    try:
        # Delete Routine
        api_response = api_instance.delete_routine(routine_id)
        print("The response of RoutinesApi->delete_routine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutinesApi->delete_routine: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routine_id** | **str**|  | 

### Return type

[**RoutinesResponse**](RoutinesResponse.md)

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

# **get_routines**
> RoutinesResponse get_routines(agent_id)

Get Routines

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.routines_response import RoutinesResponse
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
    api_instance = openapi_client.RoutinesApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Routines
        api_response = api_instance.get_routines(agent_id)
        print("The response of RoutinesApi->get_routines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutinesApi->get_routines: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**RoutinesResponse**](RoutinesResponse.md)

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

# **run_async_routine**
> RoutinesResponse run_async_routine(routine_id)

Run Async Routine

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.routines_response import RoutinesResponse
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
    api_instance = openapi_client.RoutinesApi(api_client)
    routine_id = 'routine_id_example' # str | 

    try:
        # Run Async Routine
        api_response = api_instance.run_async_routine(routine_id)
        print("The response of RoutinesApi->run_async_routine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutinesApi->run_async_routine: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routine_id** | **str**|  | 

### Return type

[**RoutinesResponse**](RoutinesResponse.md)

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

# **run_routine**
> RoutinesResponse run_routine(routine_id)

Run Routine

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.routines_response import RoutinesResponse
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
    api_instance = openapi_client.RoutinesApi(api_client)
    routine_id = 'routine_id_example' # str | 

    try:
        # Run Routine
        api_response = api_instance.run_routine(routine_id)
        print("The response of RoutinesApi->run_routine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutinesApi->run_routine: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routine_id** | **str**|  | 

### Return type

[**RoutinesResponse**](RoutinesResponse.md)

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

