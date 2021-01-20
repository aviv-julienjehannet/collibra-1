# collibra_core.FilesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_files**](FilesApi.md#add_files) | **POST** /files | Upload files
[**get_file**](FilesApi.md#get_file) | **GET** /files/{fileId} | Download file
[**get_file_info**](FilesApi.md#get_file_info) | **GET** /files/{fileId}/info | Get file information


# **add_files**
> [FileInfoImpl] add_files()

Upload files

Upload files

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import files_api
from collibra_core.model.file_info_impl import FileInfoImpl
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
    api_instance = files_api.FilesApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | File to upload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload files
        api_response = api_instance.add_files(file=file)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling FilesApi->add_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| File to upload | [optional]

### Return type

[**[FileInfoImpl]**](FileInfoImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Files successfully uploaded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> file_type get_file(file_id)

Download file

Downloads file identified by given id.  Keep in mind to use GET /attachments/{attachmentId}/file instead of this endpoint when you want to get the file of an attachment.  A File and its id can be temporary so it's possible this endpoint will not get you the desired file.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import files_api
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
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | the id of the file

    # example passing only required values which don't have defaults set
    try:
        # Download file
        api_response = api_instance.get_file(file_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| the id of the file |

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
**200** | The file has been downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> ScopeImpl get_file_info(file_id)

Get file information

Returns information about the file identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import files_api
from collibra_core.model.scope_impl import ScopeImpl
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
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | the id of the file

    # example passing only required values which don't have defaults set
    try:
        # Get file information
        api_response = api_instance.get_file_info(file_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling FilesApi->get_file_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| the id of the file |

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

