# collibra_core.ViewPermissionsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_view_permission**](ViewPermissionsApi.md#add_view_permission) | **POST** /viewPermissions | Adds a view permission.
[**find_view_permissions**](ViewPermissionsApi.md#find_view_permissions) | **GET** /viewPermissions | Finds view permissions with given criteria.
[**get_view_permission**](ViewPermissionsApi.md#get_view_permission) | **GET** /viewPermissions/{viewPermissionId} | Retrieves a view permission.
[**remove_view_permission**](ViewPermissionsApi.md#remove_view_permission) | **DELETE** /viewPermissions/{viewPermissionId} | Removes a view permission.


# **add_view_permission**
> ViewPermissionImpl add_view_permission()

Adds a view permission.

Adds a view permission.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import view_permissions_api
from collibra_core.model.view_permission_impl import ViewPermissionImpl
from collibra_core.model.add_view_permission_request import AddViewPermissionRequest
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
    api_instance = view_permissions_api.ViewPermissionsApi(api_client)
    add_view_permission_request = AddViewPermissionRequest(
        user_id="user_id_example",
        user_group_id="user_group_id_example",
        base_resource=ResourceReference(
            id="2b7f3a1a-4e50-4077-96f0-a58a395c860d",
            resource_type="Asset",
        ),
    ) # AddViewPermissionRequest | Properties of the new view permission. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds a view permission.
        api_response = api_instance.add_view_permission(add_view_permission_request=add_view_permission_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling ViewPermissionsApi->add_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_view_permission_request** | [**AddViewPermissionRequest**](AddViewPermissionRequest.md)| Properties of the new view permission. | [optional]

### Return type

[**ViewPermissionImpl**](ViewPermissionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | View permission successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_view_permissions**
> PagedResponseViewPermission find_view_permissions()

Finds view permissions with given criteria.

Finds view permissions with given criteria.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import view_permissions_api
from collibra_core.model.paged_response_view_permission import PagedResponseViewPermission
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
    api_instance = view_permissions_api.ViewPermissionsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    user_id = "userId_example" # str | The ID of the user for whom the view permission applies. (optional)
    user_group_id = "userGroupId_example" # str | The ID of the user group for whose members the view permission applies. (optional)
    resource_id = "resourceId_example" # str | The ID of the resource to which the view permission applies. (optional)
    resource_type = "View" # str | The type of resource addressed by the view permission. (optional)
    include_inherited = True # bool | Whether to include inherited permissions in search results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Finds view permissions with given criteria.
        api_response = api_instance.find_view_permissions(offset=offset, limit=limit, user_id=user_id, user_group_id=user_group_id, resource_id=resource_id, resource_type=resource_type, include_inherited=include_inherited)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling ViewPermissionsApi->find_view_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **user_id** | **str**| The ID of the user for whom the view permission applies. | [optional]
 **user_group_id** | **str**| The ID of the user group for whose members the view permission applies. | [optional]
 **resource_id** | **str**| The ID of the resource to which the view permission applies. | [optional]
 **resource_type** | **str**| The type of resource addressed by the view permission. | [optional]
 **include_inherited** | **bool**| Whether to include inherited permissions in search results. | [optional]

### Return type

[**PagedResponseViewPermission**](PagedResponseViewPermission.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_permission**
> ViewPermissionImpl get_view_permission(view_permission_id)

Retrieves a view permission.

Retrieves a view permission.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import view_permissions_api
from collibra_core.model.view_permission_impl import ViewPermissionImpl
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
    api_instance = view_permissions_api.ViewPermissionsApi(api_client)
    view_permission_id = "viewPermissionId_example" # str | Identifier of the view permission to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a view permission.
        api_response = api_instance.get_view_permission(view_permission_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling ViewPermissionsApi->get_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_permission_id** | **str**| Identifier of the view permission to retrieve. |

### Return type

[**ViewPermissionImpl**](ViewPermissionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_view_permission**
> remove_view_permission(view_permission_id)

Removes a view permission.

Removes a view permission.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import view_permissions_api
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
    api_instance = view_permissions_api.ViewPermissionsApi(api_client)
    view_permission_id = "viewPermissionId_example" # str | Identifier of the view permission to remove.

    # example passing only required values which don't have defaults set
    try:
        # Removes a view permission.
        api_instance.remove_view_permission(view_permission_id)
    except collibra_core.ApiException as e:
        print("Exception when calling ViewPermissionsApi->remove_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_permission_id** | **str**| Identifier of the view permission to remove. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

