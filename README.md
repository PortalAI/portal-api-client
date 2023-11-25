# portal_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.6
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import portal_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import portal_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import portal_client
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
    except ApiException as e:
        print("Exception when calling AgentsApi->get_agent: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**get_agent**](docs/AgentsApi.md#get_agent) | **GET** /agents/{agent_id} | Get Agents
*AgentsApi* | [**get_agents**](docs/AgentsApi.md#get_agents) | **GET** /agents | Get Agents
*AlertsApi* | [**create_alert**](docs/AlertsApi.md#create_alert) | **POST** /alerts | Create Alert
*AlertsApi* | [**get_alerts**](docs/AlertsApi.md#get_alerts) | **GET** /alerts | Get Alerts
*AlertsApi* | [**update_alert**](docs/AlertsApi.md#update_alert) | **PUT** /alerts/{alert_id} | Update Alert
*BusinessApi* | [**create_business**](docs/BusinessApi.md#create_business) | **POST** /business | Create Business
*BusinessApi* | [**delete_business**](docs/BusinessApi.md#delete_business) | **DELETE** /business/{business_id} | Delete Business
*BusinessApi* | [**get_business**](docs/BusinessApi.md#get_business) | **GET** /business | Get Business
*BusinessApi* | [**update_business**](docs/BusinessApi.md#update_business) | **PUT** /business | Update Business
*DashboardApi* | [**get_dashboard**](docs/DashboardApi.md#get_dashboard) | **GET** /dashboard | Get Dashboard
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Root
*ReportsApi* | [**get_report**](docs/ReportsApi.md#get_report) | **GET** /reports/{agent_id} | Get Report
*RoutinesApi* | [**create_routine**](docs/RoutinesApi.md#create_routine) | **POST** /routines | Create Routine
*RoutinesApi* | [**delete_routine**](docs/RoutinesApi.md#delete_routine) | **DELETE** /routines/{routine_id} | Delete Routine
*RoutinesApi* | [**get_routines**](docs/RoutinesApi.md#get_routines) | **GET** /routines | Get Routines
*RoutinesApi* | [**run_async_routine**](docs/RoutinesApi.md#run_async_routine) | **PUT** /routines/{routine_id}/run/async | Run Async Routine
*RoutinesApi* | [**run_routine**](docs/RoutinesApi.md#run_routine) | **PUT** /routines/{routine_id}/run | Run Routine
*SessionsApi* | [**create_session_from_text**](docs/SessionsApi.md#create_session_from_text) | **POST** /sessions/text | Create Session From Text
*SessionsApi* | [**get_grouped_sessions**](docs/SessionsApi.md#get_grouped_sessions) | **GET** /sessions/grouped | Get Grouped Sessions
*SessionsApi* | [**get_session**](docs/SessionsApi.md#get_session) | **GET** /sessions/{session_id} | Get Session
*SessionsApi* | [**get_sessions**](docs/SessionsApi.md#get_sessions) | **GET** /sessions | Get Sessions
*SessionsApi* | [**update_session**](docs/SessionsApi.md#update_session) | **PUT** /sessions/{session_id} | Update Session
*TestApi* | [**get_agents_test_metrics_get**](docs/TestApi.md#get_agents_test_metrics_get) | **GET** /test/metrics | Get Agents


## Documentation For Models

 - [Agent](docs/Agent.md)
 - [AgentsResponse](docs/AgentsResponse.md)
 - [Alert](docs/Alert.md)
 - [AlertStatus](docs/AlertStatus.md)
 - [Business](docs/Business.md)
 - [BusinessResponse](docs/BusinessResponse.md)
 - [CreateBusinessRequest](docs/CreateBusinessRequest.md)
 - [CreateRoutineRequest](docs/CreateRoutineRequest.md)
 - [Dashboard](docs/Dashboard.md)
 - [DataSource](docs/DataSource.md)
 - [DeleteBusinessResponse](docs/DeleteBusinessResponse.md)
 - [EndpointDataSource](docs/EndpointDataSource.md)
 - [GetSessionsResponse](docs/GetSessionsResponse.md)
 - [GoogleTableDataSource](docs/GoogleTableDataSource.md)
 - [GroupedSessionsResponse](docs/GroupedSessionsResponse.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocalFileDataSource](docs/LocalFileDataSource.md)
 - [Message](docs/Message.md)
 - [MessageRole](docs/MessageRole.md)
 - [Notification](docs/Notification.md)
 - [Report](docs/Report.md)
 - [ReportRow](docs/ReportRow.md)
 - [ReportTable](docs/ReportTable.md)
 - [ReportValue](docs/ReportValue.md)
 - [Routine](docs/Routine.md)
 - [RoutineWithSessions](docs/RoutineWithSessions.md)
 - [RoutinesResponse](docs/RoutinesResponse.md)
 - [Session](docs/Session.md)
 - [SessionStatus](docs/SessionStatus.md)
 - [SessionSummary](docs/SessionSummary.md)
 - [SqlTablesDataSource](docs/SqlTablesDataSource.md)
 - [Trend](docs/Trend.md)
 - [TrendStatus](docs/TrendStatus.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [Widget](docs/Widget.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




