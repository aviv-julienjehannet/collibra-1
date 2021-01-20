# collibra_core.AssignmentsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_assignment**](AssignmentsApi.md#add_assignment) | **POST** /assignments | Adds a new Assignment.
[**change_assignment**](AssignmentsApi.md#change_assignment) | **PATCH** /assignments/{assignmentId} | Changes the assignment with the information that is provided in the request.
[**find_assignments_for_resource**](AssignmentsApi.md#find_assignments_for_resource) | **GET** /assignments/forResource | Find the assignments where a given resource is assigned.
[**get_assignments_for_asset**](AssignmentsApi.md#get_assignments_for_asset) | **GET** /assignments/asset/{assetId} | Returns the Assignment identified by the given Asset.
[**get_assignments_for_asset_type**](AssignmentsApi.md#get_assignments_for_asset_type) | **GET** /assignments/assetType/{assetTypeId} | Returns Assignments for given asset type id.
[**get_available_asset_types_for_domain**](AssignmentsApi.md#get_available_asset_types_for_domain) | **GET** /assignments/domain/{domainId}/assetTypes | Returns available asset types for domain identified by given id.
[**get_available_attribute_types_for_asset**](AssignmentsApi.md#get_available_attribute_types_for_asset) | **GET** /assignments/asset/{assetId}/attributeTypes | Returns available attribute types for asset identified by given id.
[**get_available_complex_relation_types_for_asset**](AssignmentsApi.md#get_available_complex_relation_types_for_asset) | **GET** /assignments/asset/{assetId}/complexRelationTypes | Returns the available ComplexRelationTypes for the Asset identified by the given id.
[**get_available_relation_types_for_asset**](AssignmentsApi.md#get_available_relation_types_for_asset) | **GET** /assignments/asset/{assetId}/relationTypes | Returns the available RelationTypes for the Asset identified by the given id.
[**remove_assignment**](AssignmentsApi.md#remove_assignment) | **DELETE** /assignments/{assignmentId} | Removes the Assignment identified by the given id.


# **add_assignment**
> AssignmentImpl add_assignment()

Adds a new Assignment.

Adds a new Assignment.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.add_assignment_request import AddAssignmentRequest
from collibra_core.model.assignment_impl import AssignmentImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    add_assignment_request = AddAssignmentRequest(
        id="id_example",
        asset_type_id="asset_type_id_example",
        status_ids=[
            "status_ids_example",
        ],
        characteristic_types=[
            CharacteristicTypeAssignmentReference(
                id="id_example",
                min=0,
                max=1,
                type="View",
            ),
        ],
        articulation_rules=[
            ArticulationRuleRequest(
                id="id_example",
                operation="ADD",
                score=0,
                status_id="status_id_example",
                attribute_type_id="attribute_type_id_example",
            ),
        ],
        validation_rule_ids=[
            "validation_rule_ids_example",
        ],
        data_quality_rule_ids=[
            "data_quality_rule_ids_example",
        ],
        domain_type_ids=[
            "domain_type_ids_example",
        ],
        default_status_id="default_status_id_example",
        scope_id="scope_id_example",
    ) # AddAssignmentRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds a new Assignment.
        api_response = api_instance.add_assignment(add_assignment_request=add_assignment_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->add_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_assignment_request** | [**AddAssignmentRequest**](AddAssignmentRequest.md)|  | [optional]

### Return type

[**AssignmentImpl**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assignment successfully added. |  -  |
**400** | An assignment with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_assignment**
> AssignmentImpl change_assignment(assignment_id)

Changes the assignment with the information that is provided in the request.

Changes the assignment with the information that is provided in the request. Only properties that are specified in the request and are not NULL are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.assignment_impl import AssignmentImpl
from collibra_core.model.change_assignment_request import ChangeAssignmentRequest
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    assignment_id = "assignmentId_example" # str | The unique identifier of the Assignment.
    change_assignment_request = ChangeAssignmentRequest(
        status_ids=[
            "status_ids_example",
        ],
        characteristic_types=[
            CharacteristicTypeAssignmentReference(
                id="id_example",
                min=0,
                max=1,
                type="View",
            ),
        ],
        articulation_rules=[
            ArticulationRuleRequest(
                id="id_example",
                operation="ADD",
                score=0,
                status_id="status_id_example",
                attribute_type_id="attribute_type_id_example",
            ),
        ],
        validation_rule_ids=[
            "validation_rule_ids_example",
        ],
        data_quality_rule_ids=[
            "data_quality_rule_ids_example",
        ],
        domain_type_ids=[
            "domain_type_ids_example",
        ],
        default_status_id="default_status_id_example",
        scope_id="scope_id_example",
    ) # ChangeAssignmentRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Changes the assignment with the information that is provided in the request.
        api_response = api_instance.change_assignment(assignment_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->change_assignment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Changes the assignment with the information that is provided in the request.
        api_response = api_instance.change_assignment(assignment_id, change_assignment_request=change_assignment_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->change_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| The unique identifier of the Assignment. |
 **change_assignment_request** | [**ChangeAssignmentRequest**](ChangeAssignmentRequest.md)|  | [optional]

### Return type

[**AssignmentImpl**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignment successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_assignments_for_resource**
> [AssignmentImpl] find_assignments_for_resource()

Find the assignments where a given resource is assigned.

Find the assignments where a given resource is assigned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.assignment_impl import AssignmentImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    resource_id = "resourceId_example" # str | The ID of the resource on which the assignment applies. (optional)
    resource_type = "View" # str | The type of resource that is assigned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find the assignments where a given resource is assigned.
        api_response = api_instance.find_assignments_for_resource(resource_id=resource_id, resource_type=resource_type)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->find_assignments_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource on which the assignment applies. | [optional]
 **resource_type** | **str**| The type of resource that is assigned. | [optional]

### Return type

[**[AssignmentImpl]**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignments found |  -  |
**400** | The parameter is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignments_for_asset**
> AssignmentImpl get_assignments_for_asset(asset_id)

Returns the Assignment identified by the given Asset.

Returns the Assignment identified by the given Asset.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.assignment_impl import AssignmentImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    asset_id = "assetId_example" # str | The unique identifier of the Asset.

    # example passing only required values which don't have defaults set
    try:
        # Returns the Assignment identified by the given Asset.
        api_response = api_instance.get_assignments_for_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->get_assignments_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The unique identifier of the Asset. |

### Return type

[**AssignmentImpl**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignment found. |  -  |
**404** | Assignment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignments_for_asset_type**
> [AssignmentImpl] get_assignments_for_asset_type(asset_type_id)

Returns Assignments for given asset type id.

Returns Assignments for given asset type id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.assignment_impl import AssignmentImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    asset_type_id = "assetTypeId_example" # str | The unique identifier of the AssetType.

    # example passing only required values which don't have defaults set
    try:
        # Returns Assignments for given asset type id.
        api_response = api_instance.get_assignments_for_asset_type(asset_type_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->get_assignments_for_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**| The unique identifier of the AssetType. |

### Return type

[**[AssignmentImpl]**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignments found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_asset_types_for_domain**
> [AssetTypeImpl] get_available_asset_types_for_domain(domain_id)

Returns available asset types for domain identified by given id.

Returns available asset types for domain identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.asset_type_impl import AssetTypeImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    domain_id = "domainId_example" # str | The unique identifier of the Domain.

    # example passing only required values which don't have defaults set
    try:
        # Returns available asset types for domain identified by given id.
        api_response = api_instance.get_available_asset_types_for_domain(domain_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->get_available_asset_types_for_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| The unique identifier of the Domain. |

### Return type

[**[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AssetTypes found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_attribute_types_for_asset**
> [AttributeType] get_available_attribute_types_for_asset(asset_id)

Returns available attribute types for asset identified by given id.

Returns available attribute types for asset identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    asset_id = "assetId_example" # str | The unique identifier of the Asset.

    # example passing only required values which don't have defaults set
    try:
        # Returns available attribute types for asset identified by given id.
        api_response = api_instance.get_available_attribute_types_for_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->get_available_attribute_types_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The unique identifier of the Asset. |

### Return type

[**[AttributeType]**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AttributeTypes found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_complex_relation_types_for_asset**
> [ComplexRelationTypeImpl] get_available_complex_relation_types_for_asset(asset_id)

Returns the available ComplexRelationTypes for the Asset identified by the given id.

Returns the available ComplexRelationTypes for the Asset identified by the given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.complex_relation_type_impl import ComplexRelationTypeImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    asset_id = "assetId_example" # str | The unique identifier of the Asset.

    # example passing only required values which don't have defaults set
    try:
        # Returns the available ComplexRelationTypes for the Asset identified by the given id.
        api_response = api_instance.get_available_complex_relation_types_for_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->get_available_complex_relation_types_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The unique identifier of the Asset. |

### Return type

[**[ComplexRelationTypeImpl]**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ComplexRelationTypes found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_relation_types_for_asset**
> [RelationTypeImpl] get_available_relation_types_for_asset(asset_id)

Returns the available RelationTypes for the Asset identified by the given id.

Returns the available RelationTypes for the Asset identified by the given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
from collibra_core.model.relation_type_impl import RelationTypeImpl
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    asset_id = "assetId_example" # str | The unique identifier of the Asset.

    # example passing only required values which don't have defaults set
    try:
        # Returns the available RelationTypes for the Asset identified by the given id.
        api_response = api_instance.get_available_relation_types_for_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->get_available_relation_types_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The unique identifier of the Asset. |

### Return type

[**[RelationTypeImpl]**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RelationTypes found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignment**
> remove_assignment(assignment_id)

Removes the Assignment identified by the given id.

Removes the Assignment identified by the given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assignments_api
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    assignment_id = "assignmentId_example" # str | The unique identifier of the Assignment.

    # example passing only required values which don't have defaults set
    try:
        # Removes the Assignment identified by the given id.
        api_instance.remove_assignment(assignment_id)
    except collibra_core.ApiException as e:
        print("Exception when calling AssignmentsApi->remove_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| The unique identifier of the Assignment. |

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
**200** | Assignment removed. |  -  |
**404** | Assignment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

