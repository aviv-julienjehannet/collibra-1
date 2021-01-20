# collibra_core.JDBCDriverApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_jdbc_drivers**](JDBCDriverApi.md#find_jdbc_drivers) | **GET** /jdbc | Find JDBC Drivers


# **find_jdbc_drivers**
> JdbcDriverPagedResponse find_jdbc_drivers()

Find JDBC Drivers

Finds JDBC drivers that match the given search criteria. By default a result containing 1000 JDBC drivers are returned.<br />This operation is deprecated and it will be removed in the future.

### Example

```python
import time
import collibra_core
from collibra_core.api import jdbc_driver_api
from collibra_core.model.jdbc_driver_paged_response import JdbcDriverPagedResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)


# Enter a context with an instance of the API client
with collibra_core.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jdbc_driver_api.JDBCDriverApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    database_name = "databaseName_example" # str |  (optional)
    database_version = "databaseVersion_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find JDBC Drivers
        api_response = api_instance.find_jdbc_drivers(offset=offset, limit=limit, database_name=database_name, database_version=database_version)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling JDBCDriverApi->find_jdbc_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **database_name** | **str**|  | [optional]
 **database_version** | **str**|  | [optional]

### Return type

[**JdbcDriverPagedResponse**](JdbcDriverPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JDBC drivers searched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

