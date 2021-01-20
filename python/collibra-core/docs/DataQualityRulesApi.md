# collibra_core.DataQualityRulesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_quality_rule**](DataQualityRulesApi.md#add_data_quality_rule) | **POST** /dataQualityRules | Adds a new data quality rule.
[**change_data_quality_rule**](DataQualityRulesApi.md#change_data_quality_rule) | **PATCH** /dataQualityRules/{dataQualityRuleId} | Changes the data quality rule with the information that is present in the request.
[**find_data_quality_rules**](DataQualityRulesApi.md#find_data_quality_rules) | **GET** /dataQualityRules | Returns data quality rules matching the given search criteria.
[**get_data_quality_rule**](DataQualityRulesApi.md#get_data_quality_rule) | **GET** /dataQualityRules/{dataQualityRuleId} | Returns the DataQualityRule identified by given id.
[**remove_data_quality_rule**](DataQualityRulesApi.md#remove_data_quality_rule) | **DELETE** /dataQualityRules/{dataQualityRuleId} | Removes the DataQualityRule identified by the given id.


# **add_data_quality_rule**
> DataQualityRuleImpl add_data_quality_rule()

Adds a new data quality rule.

Adds a new data quality rule.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import data_quality_rules_api
from collibra_core.model.data_quality_rule_impl import DataQualityRuleImpl
from collibra_core.model.add_data_quality_rule_request import AddDataQualityRuleRequest
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
    api_instance = data_quality_rules_api.DataQualityRulesApi(api_client)
    add_data_quality_rule_request = AddDataQualityRuleRequest(
        id="id_example",
        name="name_example",
        description="description_example",
        categorization_relation_type_id="categorization_relation_type_id_example",
        data_quality_metrics=[
            DataQualityMetricRequest(
                count_operation="Sum",
                attribute_type_id="attribute_type_id_example",
            ),
        ],
        relation_trace_entries=[
            RelationTraceEntryRequest(
                role_direction=True,
                relation_type_id="relation_type_id_example",
            ),
        ],
    ) # AddDataQualityRuleRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds a new data quality rule.
        api_response = api_instance.add_data_quality_rule(add_data_quality_rule_request=add_data_quality_rule_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling DataQualityRulesApi->add_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_data_quality_rule_request** | [**AddDataQualityRuleRequest**](AddDataQualityRuleRequest.md)|  | [optional]

### Return type

[**DataQualityRuleImpl**](DataQualityRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Data quality rule successfully added. |  -  |
**400** | A data quality rule with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_data_quality_rule**
> DataQualityRuleImpl change_data_quality_rule(data_quality_rule_id)

Changes the data quality rule with the information that is present in the request.

Changes the data quality rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import data_quality_rules_api
from collibra_core.model.data_quality_rule_impl import DataQualityRuleImpl
from collibra_core.model.change_data_quality_rule_request import ChangeDataQualityRuleRequest
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
    api_instance = data_quality_rules_api.DataQualityRulesApi(api_client)
    data_quality_rule_id = "dataQualityRuleId_example" # str | the unique identifier of the data quality rule
    change_data_quality_rule_request = ChangeDataQualityRuleRequest(
        name="name_example",
        description="description_example",
        categorization_relation_type_id="categorization_relation_type_id_example",
        data_quality_metrics=[
            DataQualityMetricRequest(
                count_operation="Sum",
                attribute_type_id="attribute_type_id_example",
            ),
        ],
        relation_trace_entries=[
            RelationTraceEntryRequest(
                role_direction=True,
                relation_type_id="relation_type_id_example",
            ),
        ],
    ) # ChangeDataQualityRuleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Changes the data quality rule with the information that is present in the request.
        api_response = api_instance.change_data_quality_rule(data_quality_rule_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling DataQualityRulesApi->change_data_quality_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Changes the data quality rule with the information that is present in the request.
        api_response = api_instance.change_data_quality_rule(data_quality_rule_id, change_data_quality_rule_request=change_data_quality_rule_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling DataQualityRulesApi->change_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | **str**| the unique identifier of the data quality rule |
 **change_data_quality_rule_request** | [**ChangeDataQualityRuleRequest**](ChangeDataQualityRuleRequest.md)|  | [optional]

### Return type

[**DataQualityRuleImpl**](DataQualityRuleImpl.md)

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

# **find_data_quality_rules**
> DataQualityRulePagedResponse find_data_quality_rules()

Returns data quality rules matching the given search criteria.

Returns data quality rules matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned data quality rules satisfy all constraints that are specified in this search criteria. By default a result containing 1000 data quality rules is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import data_quality_rules_api
from collibra_core.model.data_quality_rule_paged_response import DataQualityRulePagedResponse
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
    api_instance = data_quality_rules_api.DataQualityRulesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    name = "name_example" # str | The name of the dataquality rule to search for. (optional)
    name_match_mode = "ANYWHERE" # str | The match mode used to compare <code>name</code>. (optional) if omitted the server will use the default value of "ANYWHERE"
    sort_field = "NAME" # str | The field that should be used as reference for sorting. (optional) if omitted the server will use the default value of "NAME"
    sort_order = "ASC" # str | The order of sorting. (optional) if omitted the server will use the default value of "ASC"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns data quality rules matching the given search criteria.
        api_response = api_instance.find_data_quality_rules(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling DataQualityRulesApi->find_data_quality_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **name** | **str**| The name of the dataquality rule to search for. | [optional]
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] if omitted the server will use the default value of "ANYWHERE"
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] if omitted the server will use the default value of "NAME"
 **sort_order** | **str**| The order of sorting. | [optional] if omitted the server will use the default value of "ASC"

### Return type

[**DataQualityRulePagedResponse**](DataQualityRulePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found DataQualityRule information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_quality_rule**
> DataQualityRuleImpl get_data_quality_rule(data_quality_rule_id)

Returns the DataQualityRule identified by given id.

Returns the DataQualityRule identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import data_quality_rules_api
from collibra_core.model.data_quality_rule_impl import DataQualityRuleImpl
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
    api_instance = data_quality_rules_api.DataQualityRulesApi(api_client)
    data_quality_rule_id = "dataQualityRuleId_example" # str | the unique identifier of the data quality rule

    # example passing only required values which don't have defaults set
    try:
        # Returns the DataQualityRule identified by given id.
        api_response = api_instance.get_data_quality_rule(data_quality_rule_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling DataQualityRulesApi->get_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | **str**| the unique identifier of the data quality rule |

### Return type

[**DataQualityRuleImpl**](DataQualityRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DataQualityRule found. |  -  |
**404** | DataQualityRule not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_data_quality_rule**
> remove_data_quality_rule(data_quality_rule_id)

Removes the DataQualityRule identified by the given id.

Removes the DataQualityRule identified by the given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import data_quality_rules_api
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
    api_instance = data_quality_rules_api.DataQualityRulesApi(api_client)
    data_quality_rule_id = "dataQualityRuleId_example" # str | the unique identifier of the data quality rule

    # example passing only required values which don't have defaults set
    try:
        # Removes the DataQualityRule identified by the given id.
        api_instance.remove_data_quality_rule(data_quality_rule_id)
    except collibra_core.ApiException as e:
        print("Exception when calling DataQualityRulesApi->remove_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | **str**| the unique identifier of the data quality rule |

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
**200** | DataQualityRule removed. |  -  |
**404** | DataQualityRule not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

