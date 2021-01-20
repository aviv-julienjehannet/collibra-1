# collibra_core.AttachmentsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attachment**](AttachmentsApi.md#add_attachment) | **POST** /attachments | Add attachment
[**find_attachments**](AttachmentsApi.md#find_attachments) | **GET** /attachments | Find attachments
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachmentId} | Get attachment
[**get_attachment_content**](AttachmentsApi.md#get_attachment_content) | **GET** /attachments/{attachmentId}/file | Get attachment content
[**remove_attachment**](AttachmentsApi.md#remove_attachment) | **DELETE** /attachments/{attachmentId} | Remove attachment


# **add_attachment**
> AttachmentImpl add_attachment()

Add attachment

Adds new attachment.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attachments_api
from collibra_core.model.attachment_impl import AttachmentImpl
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | the file - attachment content (optional)
    file_name = "file_name_example" # str | the display name of the file of this attachment (optional)
    resource_type = "View" # str | the type of the resource the attachment should refer to. An attachment can be added on those resource types: User, Community, Domain, Asset, Role, ValidationRule, Workflow. (optional)
    resource_id = "resource_id_example" # str | the id of the resource the attachment should refer to (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add attachment
        api_response = api_instance.add_attachment(file=file, file_name=file_name, resource_type=resource_type, resource_id=resource_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttachmentsApi->add_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| the file - attachment content | [optional]
 **file_name** | **str**| the display name of the file of this attachment | [optional]
 **resource_type** | **str**| the type of the resource the attachment should refer to. An attachment can be added on those resource types: User, Community, Domain, Asset, Role, ValidationRule, Workflow. | [optional]
 **resource_id** | **str**| the id of the resource the attachment should refer to | [optional]

### Return type

[**AttachmentImpl**](AttachmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_attachments**
> AttachmentPagedResponse find_attachments()

Find attachments

Returns attachments matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attachments satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attachments is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attachments_api
from collibra_core.model.attachment_paged_response import AttachmentPagedResponse
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    file_name = "fileName_example" # str | The name of the file representing searched attachment. (optional)
    file_content_type = "fileContentType_example" # str | The type of the content of the file representing searched attachment. (optional)
    upload_date = 1 # int | The date of attachment upload. It is the timestamp (in UTC time standard). (optional)
    user_id = "userId_example" # str | The ID of the user who uploaded the attachment. (optional)
    base_resource_id = "baseResourceId_example" # str | The ID of the resource the attachment refers to. (optional)
    sort_field = "LAST_MODIFIED" # str | The field that should be used as reference for sorting. (optional) if omitted the server will use the default value of "LAST_MODIFIED"
    sort_order = "DESC" # str | The order of sorting. (optional) if omitted the server will use the default value of "DESC"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find attachments
        api_response = api_instance.find_attachments(offset=offset, limit=limit, file_name=file_name, file_content_type=file_content_type, upload_date=upload_date, user_id=user_id, base_resource_id=base_resource_id, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttachmentsApi->find_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **file_name** | **str**| The name of the file representing searched attachment. | [optional]
 **file_content_type** | **str**| The type of the content of the file representing searched attachment. | [optional]
 **upload_date** | **int**| The date of attachment upload. It is the timestamp (in UTC time standard). | [optional]
 **user_id** | **str**| The ID of the user who uploaded the attachment. | [optional]
 **base_resource_id** | **str**| The ID of the resource the attachment refers to. | [optional]
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] if omitted the server will use the default value of "LAST_MODIFIED"
 **sort_order** | **str**| The order of sorting. | [optional] if omitted the server will use the default value of "DESC"

### Return type

[**AttachmentPagedResponse**](AttachmentPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentImpl get_attachment(attachment_id)

Get attachment

Returns information about the attachment identified by id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attachments_api
from collibra_core.model.attachment_impl import AttachmentImpl
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = "attachmentId_example" # str | the id of the attachment

    # example passing only required values which don't have defaults set
    try:
        # Get attachment
        api_response = api_instance.get_attachment(attachment_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| the id of the attachment |

### Return type

[**AttachmentImpl**](AttachmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_content**
> file_type get_attachment_content(attachment_id)

Get attachment content

Returns content of the attachment identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = "attachmentId_example" # str | the id of the attachment

    # example passing only required values which don't have defaults set
    try:
        # Get attachment content
        api_response = api_instance.get_attachment_content(attachment_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| the id of the attachment |

### Return type

**file_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The attachment has been downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attachment**
> remove_attachment(attachment_id)

Remove attachment

Removes attachment identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = "attachmentId_example" # str | the id of the attachment

    # example passing only required values which don't have defaults set
    try:
        # Remove attachment
        api_instance.remove_attachment(attachment_id)
    except collibra_core.ApiException as e:
        print("Exception when calling AttachmentsApi->remove_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| the id of the attachment |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The attachment has been successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

