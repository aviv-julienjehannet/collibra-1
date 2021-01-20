# collibra_core.ActivitiesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activities**](ActivitiesApi.md#get_activities) | **GET** /activities | Returns activities matching the given search criteria.


# **get_activities**
> ActivityPagedResponse get_activities()

Returns activities matching the given search criteria.

Returns activities matching the given search criteria.Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.All other parameters are ignored.The returned activities satisfy all constraints that are specified in this search criteria.By default a result containing 100 activities is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import activities_api
from collibra_core.model.activity_paged_response import ActivityPagedResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activities_api.ActivitiesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    task_id = "taskId_example" # str | The ID of the task which contains the basic find activities request. (optional)
    context_id = "contextId_example" # str | The ID of the context which the activities should be searched for. (optional)
    involved_people_ids = [
        "involvedPeopleIds_example",
    ] # [str] | The list of IDs of the people that should be involved in searched activities. (optional)
    involved_role_ids = [
        "involvedRoleIds_example",
    ] # [str] | The list of IDs of the roles that should be involved in searched activities. (optional)
    performed_by_user_id = "performedByUserId_example" # str | The ID of the user who performed searched activities. (optional)
    performed_by_role_ids = [
        "performedByRoleIds_example",
    ] # [str] | The list of IDs of the roles assigned to users who performed searched activities. (optional)
    activity_type = "ADD" # str | The type of the activity. (optional)
    call_id = "callId_example" # str | The ID of the call. (optional)
    categories = [
        "ATTRIBUTE",
    ] # [str] | The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT,<br/>STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS]. (optional)
    resource_types = [
        "View",
    ] # [str] | The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute,<br/>Relation, WorkflowInstance]. (optional)
    start_date = 1 # int | TThe start date of the searched activities. It is the timestamp (in UTC time standard). (optional)
    end_date = 1 # int | The end date of the searched activities. It is the timestamp (in UTC time standard). (optional)
    call_count_enabled = False # bool | Flag to indicate if the number of calls standing behind the activity should be returned or not.<br/>Note that by default that count will be not calculated as it brings an important performance penalty. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns activities matching the given search criteria.
        api_response = api_instance.get_activities(offset=offset, limit=limit, task_id=task_id, context_id=context_id, involved_people_ids=involved_people_ids, involved_role_ids=involved_role_ids, performed_by_user_id=performed_by_user_id, performed_by_role_ids=performed_by_role_ids, activity_type=activity_type, call_id=call_id, categories=categories, resource_types=resource_types, start_date=start_date, end_date=end_date, call_count_enabled=call_count_enabled)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling ActivitiesApi->get_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **task_id** | **str**| The ID of the task which contains the basic find activities request. | [optional]
 **context_id** | **str**| The ID of the context which the activities should be searched for. | [optional]
 **involved_people_ids** | **[str]**| The list of IDs of the people that should be involved in searched activities. | [optional]
 **involved_role_ids** | **[str]**| The list of IDs of the roles that should be involved in searched activities. | [optional]
 **performed_by_user_id** | **str**| The ID of the user who performed searched activities. | [optional]
 **performed_by_role_ids** | **[str]**| The list of IDs of the roles assigned to users who performed searched activities. | [optional]
 **activity_type** | **str**| The type of the activity. | [optional]
 **call_id** | **str**| The ID of the call. | [optional]
 **categories** | **[str]**| The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT,&lt;br/&gt;STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS]. | [optional]
 **resource_types** | **[str]**| The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute,&lt;br/&gt;Relation, WorkflowInstance]. | [optional]
 **start_date** | **int**| TThe start date of the searched activities. It is the timestamp (in UTC time standard). | [optional]
 **end_date** | **int**| The end date of the searched activities. It is the timestamp (in UTC time standard). | [optional]
 **call_count_enabled** | **bool**| Flag to indicate if the number of calls standing behind the activity should be returned or not.&lt;br/&gt;Note that by default that count will be not calculated as it brings an important performance penalty. | [optional] if omitted the server will use the default value of False

### Return type

[**ActivityPagedResponse**](ActivityPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found Activity information. The total number of results is not calculated and should be ignored |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

