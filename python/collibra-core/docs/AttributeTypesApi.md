# collibra_core.AttributeTypesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attribute_type**](AttributeTypesApi.md#add_attribute_type) | **POST** /attributeTypes | Adds a new Attribute Type.
[**add_attribute_types**](AttributeTypesApi.md#add_attribute_types) | **POST** /attributeTypes/bulk | Adds multiple Attribute Types.
[**change_attribute_type**](AttributeTypesApi.md#change_attribute_type) | **PATCH** /attributeTypes/{attributeTypeId} | Changes the attribute types.
[**change_attribute_types**](AttributeTypesApi.md#change_attribute_types) | **PATCH** /attributeTypes/bulk | Changes multiple attribute types.
[**find_attribute_types**](AttributeTypesApi.md#find_attribute_types) | **GET** /attributeTypes | Returns attribute types matching the given search criteria.
[**get_attribute_type**](AttributeTypesApi.md#get_attribute_type) | **GET** /attributeTypes/{attributeTypeId} | Returns the attribute type identified by given UUID.
[**get_attribute_type_by_name**](AttributeTypesApi.md#get_attribute_type_by_name) | **GET** /attributeTypes/name/{attributeTypeName} | Returns the attribute type identified by given name.
[**remove_attribute_type**](AttributeTypesApi.md#remove_attribute_type) | **DELETE** /attributeTypes/{attributeTypeId} | Removes attribute type identified by given UUID.
[**remove_attribute_types**](AttributeTypesApi.md#remove_attribute_types) | **DELETE** /attributeTypes/bulk | Removes multiple attribute types.


# **add_attribute_type**
> AttributeType add_attribute_type()

Adds a new Attribute Type.

Adds a new Attribute Type.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type import AttributeType
from collibra_core.model.add_attribute_type_request import AddAttributeTypeRequest
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    add_attribute_type_request = AddAttributeTypeRequest(
        id="id_example",
        name="name_example",
        description="description_example",
        kind="BOOLEAN",
        language="language_example",
        statistics_enabled=True,
        allowed_values=[
            "allowed_values_example",
        ],
        string_type="RICH_TEXT",
        id_string="id_string_example",
        is_integer=True,
    ) # AddAttributeTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds a new Attribute Type.
        api_response = api_instance.add_attribute_type(add_attribute_type_request=add_attribute_type_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->add_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_attribute_type_request** | [**AddAttributeTypeRequest**](AddAttributeTypeRequest.md)|  | [optional]

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attribute Type successfully added. |  -  |
**400** | An attribute type with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_attribute_types**
> AttributeType add_attribute_types()

Adds multiple Attribute Types.

Adds multiple Attribute Types.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type import AttributeType
from collibra_core.model.add_attribute_type_request import AddAttributeTypeRequest
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    add_attribute_type_request = [
        AddAttributeTypeRequest(
            id="id_example",
            name="name_example",
            description="description_example",
            kind="BOOLEAN",
            language="language_example",
            statistics_enabled=True,
            allowed_values=[
                "allowed_values_example",
            ],
            string_type="RICH_TEXT",
            id_string="id_string_example",
            is_integer=True,
        ),
    ] # [AddAttributeTypeRequest] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds multiple Attribute Types.
        api_response = api_instance.add_attribute_types(add_attribute_type_request=add_attribute_type_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->add_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_attribute_type_request** | [**[AddAttributeTypeRequest]**](AddAttributeTypeRequest.md)|  | [optional]

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attribute Types successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attribute_type**
> AttributeType change_attribute_type(attribute_type_id)

Changes the attribute types.

Changes the attribute types with the information present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type import AttributeType
from collibra_core.model.change_attribute_type_request import ChangeAttributeTypeRequest
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    attribute_type_id = "attributeTypeId_example" # str | the unique identifier of the attribute type
    change_attribute_type_request = ChangeAttributeTypeRequest(
        id="id_example",
        name="name_example",
        description="description_example",
        language="language_example",
        statistics_enabled=True,
        is_integer=True,
        allowed_values=[
            "allowed_values_example",
        ],
    ) # ChangeAttributeTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Changes the attribute types.
        api_response = api_instance.change_attribute_type(attribute_type_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->change_attribute_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Changes the attribute types.
        api_response = api_instance.change_attribute_type(attribute_type_id, change_attribute_type_request=change_attribute_type_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->change_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | **str**| the unique identifier of the attribute type |
 **change_attribute_type_request** | [**ChangeAttributeTypeRequest**](ChangeAttributeTypeRequest.md)|  | [optional]

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute Type successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attribute_types**
> [AttributeType] change_attribute_types()

Changes multiple attribute types.

Changes multiple attribute types with the information present in the request.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type import AttributeType
from collibra_core.model.change_attribute_type_request import ChangeAttributeTypeRequest
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    change_attribute_type_request = [
        ChangeAttributeTypeRequest(
            id="id_example",
            name="name_example",
            description="description_example",
            language="language_example",
            statistics_enabled=True,
            is_integer=True,
            allowed_values=[
                "allowed_values_example",
            ],
        ),
    ] # [ChangeAttributeTypeRequest] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Changes multiple attribute types.
        api_response = api_instance.change_attribute_types(change_attribute_type_request=change_attribute_type_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->change_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_attribute_type_request** | [**[ChangeAttributeTypeRequest]**](ChangeAttributeTypeRequest.md)|  | [optional]

### Return type

[**[AttributeType]**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute Types successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_attribute_types**
> AttributeTypePagedResponse find_attribute_types()

Returns attribute types matching the given search criteria.

Returns attribute types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attribute types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attribute types is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type_paged_response import AttributeTypePagedResponse
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    name = "name_example" # str | The name of the attribute type to search for. (optional)
    name_match_mode = "ANYWHERE" # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) if omitted the server will use the default value of "ANYWHERE"
    kind = "BOOLEAN" # str | The kind of the attribute type to search for. (optional)
    language = "language_example" # str | The language of the attribute type to search for. (optional)
    statistics_enabled = True # bool | Whether the attribute types should be searched with statistics enabled or not. (optional)
    is_integer = True # bool | Whether only integer-type attribute types should be searched or not. (optional)
    sort_field = "NAME" # str | The field that should be used as reference for sorting. (optional) if omitted the server will use the default value of "NAME"
    sort_order = "ASC" # str | The order of sorting. (optional) if omitted the server will use the default value of "ASC"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns attribute types matching the given search criteria.
        api_response = api_instance.find_attribute_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, kind=kind, language=language, statistics_enabled=statistics_enabled, is_integer=is_integer, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->find_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **name** | **str**| The name of the attribute type to search for. | [optional]
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] if omitted the server will use the default value of "ANYWHERE"
 **kind** | **str**| The kind of the attribute type to search for. | [optional]
 **language** | **str**| The language of the attribute type to search for. | [optional]
 **statistics_enabled** | **bool**| Whether the attribute types should be searched with statistics enabled or not. | [optional]
 **is_integer** | **bool**| Whether only integer-type attribute types should be searched or not. | [optional]
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] if omitted the server will use the default value of "NAME"
 **sort_order** | **str**| The order of sorting. | [optional] if omitted the server will use the default value of "ASC"

### Return type

[**AttributeTypePagedResponse**](AttributeTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response of found Attribute Types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type**
> AttributeType get_attribute_type(attribute_type_id)

Returns the attribute type identified by given UUID.

Returns the attribute type identified by given UUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type import AttributeType
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    attribute_type_id = "attributeTypeId_example" # str | the unique identifier of the attribute type

    # example passing only required values which don't have defaults set
    try:
        # Returns the attribute type identified by given UUID.
        api_response = api_instance.get_attribute_type(attribute_type_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->get_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | **str**| the unique identifier of the attribute type |

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute Type found. |  -  |
**404** | Attribute Type not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type_by_name**
> AttributeType get_attribute_type_by_name(attribute_type_name)

Returns the attribute type identified by given name.

Returns the attribute type identified by given name.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
from collibra_core.model.attribute_type import AttributeType
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    attribute_type_name = "attributeTypeName_example" # str | the unique identifier of the attribute type

    # example passing only required values which don't have defaults set
    try:
        # Returns the attribute type identified by given name.
        api_response = api_instance.get_attribute_type_by_name(attribute_type_name)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->get_attribute_type_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_name** | **str**| the unique identifier of the attribute type |

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute Type found. |  -  |
**404** | Attribute Type not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attribute_type**
> remove_attribute_type(attribute_type_id)

Removes attribute type identified by given UUID.

Removes attribute type identified by given UUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    attribute_type_id = "attributeTypeId_example" # str | the unique identifier of the attribute type

    # example passing only required values which don't have defaults set
    try:
        # Removes attribute type identified by given UUID.
        api_instance.remove_attribute_type(attribute_type_id)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->remove_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | **str**| the unique identifier of the attribute type |

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

# **remove_attribute_types**
> remove_attribute_types()

Removes multiple attribute types.

Removes multiple attribute types identified by the UUIDs passed as parameter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attribute_types_api
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
    api_instance = attribute_types_api.AttributeTypesApi(api_client)
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes multiple attribute types.
        api_instance.remove_attribute_types(request_body=request_body)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributeTypesApi->remove_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

