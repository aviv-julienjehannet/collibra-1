# collibra_core.AssetsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset**](AssetsApi.md#add_asset) | **POST** /assets | Add asset
[**add_assets**](AssetsApi.md#add_assets) | **POST** /assets/bulk | Add multiple assets
[**add_tags_to_asset**](AssetsApi.md#add_tags_to_asset) | **POST** /assets/{assetId}/tags | Add tags
[**change_asset**](AssetsApi.md#change_asset) | **PATCH** /assets/{assetId} | Change asset
[**change_assets**](AssetsApi.md#change_assets) | **PATCH** /assets/bulk | Change multiple assets
[**find_assets**](AssetsApi.md#find_assets) | **GET** /assets | Find assets
[**get_asset**](AssetsApi.md#get_asset) | **GET** /assets/{assetId} | Get asset
[**get_asset_breadcrumb**](AssetsApi.md#get_asset_breadcrumb) | **GET** /assets/{assetId}/breadcrumb | Get asset breadcrumb
[**get_asset_tags**](AssetsApi.md#get_asset_tags) | **GET** /assets/{assetId}/tags | Get asset tags
[**remove_asset**](AssetsApi.md#remove_asset) | **DELETE** /assets/{assetId} | Remove asset
[**remove_assets**](AssetsApi.md#remove_assets) | **DELETE** /assets/bulk | Remove assets
[**remove_tags_from_asset**](AssetsApi.md#remove_tags_from_asset) | **DELETE** /assets/{assetId}/tags | Remove tags
[**set_asset_attributes**](AssetsApi.md#set_asset_attributes) | **PUT** /assets/{assetId}/attributes | Set asset attributes
[**set_asset_relations**](AssetsApi.md#set_asset_relations) | **PUT** /assets/{assetId}/relations | Set asset relations
[**set_asset_responsibilities**](AssetsApi.md#set_asset_responsibilities) | **PUT** /assets/{assetId}/responsibilities | Set asset responsibilities
[**set_tags_for_asset**](AssetsApi.md#set_tags_for_asset) | **PUT** /assets/{assetId}/tags | Set asset tags


# **add_asset**
> AssetImpl add_asset()

Add asset

Adds a new asset to a domain

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.asset_impl import AssetImpl
from collibra_core.model.add_asset_request import AddAssetRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    add_asset_request = AddAssetRequest(
        name="name_example",
        display_name="display_name_example",
        domain_id="domain_id_example",
        type_id="type_id_example",
        id="id_example",
        status_id="status_id_example",
        excluded_from_auto_hyperlinking=True,
    ) # AddAssetRequest | The properties of the asset to be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add asset
        api_response = api_instance.add_asset(add_asset_request=add_asset_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->add_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_asset_request** | [**AddAssetRequest**](AddAssetRequest.md)| The properties of the asset to be added | [optional]

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset successfully added. |  -  |
**400** | An asset with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_assets**
> [AssetImpl] add_assets()

Add multiple assets

Adds multiple assets in one go

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.asset_impl import AssetImpl
from collibra_core.model.add_asset_request import AddAssetRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    add_asset_request = [
        AddAssetRequest(
            name="name_example",
            display_name="display_name_example",
            domain_id="domain_id_example",
            type_id="type_id_example",
            id="id_example",
            status_id="status_id_example",
            excluded_from_auto_hyperlinking=True,
        ),
    ] # [AddAssetRequest] | The properties of the assets to be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add multiple assets
        api_response = api_instance.add_assets(add_asset_request=add_asset_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->add_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_asset_request** | [**[AddAssetRequest]**](AddAssetRequest.md)| The properties of the assets to be added | [optional]

### Return type

[**[AssetImpl]**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assets successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tags_to_asset**
> [Tag] add_tags_to_asset(asset_id)

Add tags

Adds tags to the asset with the given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.add_asset_tags_request import AddAssetTagsRequest
from collibra_core.model.tag import Tag
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset
    add_asset_tags_request = AddAssetTagsRequest(
        tag_names=[
            "tag_names_example",
        ],
    ) # AddAssetTagsRequest | The tags to be added to a given asset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add tags
        api_response = api_instance.add_tags_to_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->add_tags_to_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add tags
        api_response = api_instance.add_tags_to_asset(asset_id, add_asset_tags_request=add_asset_tags_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->add_tags_to_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |
 **add_asset_tags_request** | [**AddAssetTagsRequest**](AddAssetTagsRequest.md)| The tags to be added to a given asset | [optional]

### Return type

[**[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tags added |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset**
> AssetImpl change_asset(asset_id)

Change asset

Changes the asset with the given ID as specified by the given request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.asset_impl import AssetImpl
from collibra_core.model.change_asset_request import ChangeAssetRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset to be changed
    change_asset_request = ChangeAssetRequest(
        id="id_example",
        name="name_example",
        display_name="display_name_example",
        type_id="type_id_example",
        status_id="status_id_example",
        domain_id="domain_id_example",
        excluded_from_auto_hyperlinking=True,
    ) # ChangeAssetRequest | The properties of the assets to be changed (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change asset
        api_response = api_instance.change_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->change_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change asset
        api_response = api_instance.change_asset(asset_id, change_asset_request=change_asset_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->change_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset to be changed |
 **change_asset_request** | [**ChangeAssetRequest**](ChangeAssetRequest.md)| The properties of the assets to be changed | [optional]

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed asset |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_assets**
> [AssetImpl] change_assets()

Change multiple assets

Changes multiple assets in one go

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.asset_impl import AssetImpl
from collibra_core.model.change_asset_request import ChangeAssetRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    change_asset_request = [
        ChangeAssetRequest(
            id="id_example",
            name="name_example",
            display_name="display_name_example",
            type_id="type_id_example",
            status_id="status_id_example",
            domain_id="domain_id_example",
            excluded_from_auto_hyperlinking=True,
        ),
    ] # [ChangeAssetRequest] | The properties of the assets to be changed (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change multiple assets
        api_response = api_instance.change_assets(change_asset_request=change_asset_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->change_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_asset_request** | [**[ChangeAssetRequest]**](ChangeAssetRequest.md)| The properties of the assets to be changed | [optional]

### Return type

[**[AssetImpl]**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assets changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_assets**
> AssetPagedResponse find_assets()

Find assets

Returns assets matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 assets is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.asset_paged_response import AssetPagedResponse
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
    api_instance = assets_api.AssetsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    name = "name_example" # str | The name of the asset to search for (either display name or full name). (optional)
    name_match_mode = "ANYWHERE" # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) if omitted the server will use the default value of "ANYWHERE"
    domain_id = "domainId_example" # str | The ID of the domain to find the assets in. (optional)
    community_id = "communityId_example" # str | The ID of the community to find the assets in. (optional)
    type_id = [
        "typeId_example",
    ] # [str] | The list of IDs of the asset types. The returned assets are of one of types specified by this parameter. (optional)
    status_id = [
        "statusId_example",
    ] # [str] | The list of IDs of the statuses. The returned assets have one of statuses specified by this parameter. (optional)
    tag_names = [
        "tagNames_example",
    ] # [str] | The list of names of tags. The returned assets have one of tags with names specified by this parameter. (optional)
    type_inheritance = True # bool | Whether the type inheritance for the asset type filtering should be applied or not. (optional) if omitted the server will use the default value of True
    exclude_meta = True # bool | The exclude meta flag. If this is set to true then the assets from meta domains will not be returned<br/>(meta domains are the domains which were not created by the user manually). (optional) if omitted the server will use the default value of True
    sort_field = "NAME" # str | The field that should be used as reference for sorting. (optional) if omitted the server will use the default value of "NAME"
    sort_order = "ASC" # str | The order of sorting. (optional) if omitted the server will use the default value of "ASC"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find assets
        api_response = api_instance.find_assets(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, domain_id=domain_id, community_id=community_id, type_id=type_id, status_id=status_id, tag_names=tag_names, type_inheritance=type_inheritance, exclude_meta=exclude_meta, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->find_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **name** | **str**| The name of the asset to search for (either display name or full name). | [optional]
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] if omitted the server will use the default value of "ANYWHERE"
 **domain_id** | **str**| The ID of the domain to find the assets in. | [optional]
 **community_id** | **str**| The ID of the community to find the assets in. | [optional]
 **type_id** | **[str]**| The list of IDs of the asset types. The returned assets are of one of types specified by this parameter. | [optional]
 **status_id** | **[str]**| The list of IDs of the statuses. The returned assets have one of statuses specified by this parameter. | [optional]
 **tag_names** | **[str]**| The list of names of tags. The returned assets have one of tags with names specified by this parameter. | [optional]
 **type_inheritance** | **bool**| Whether the type inheritance for the asset type filtering should be applied or not. | [optional] if omitted the server will use the default value of True
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the assets from meta domains will not be returned&lt;br/&gt;(meta domains are the domains which were not created by the user manually). | [optional] if omitted the server will use the default value of True
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] if omitted the server will use the default value of "NAME"
 **sort_order** | **str**| The order of sorting. | [optional] if omitted the server will use the default value of "ASC"

### Return type

[**AssetPagedResponse**](AssetPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search ran successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetImpl get_asset(asset_id)

Get asset

Returns the asset having the given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.asset_impl import AssetImpl
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset

    # example passing only required values which don't have defaults set
    try:
        # Get asset
        api_response = api_instance.get_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset found |  -  |
**401** | User lacks view permission |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_breadcrumb**
> [NamedResourceReferenceImpl] get_asset_breadcrumb(asset_id)

Get asset breadcrumb

Returns the list of resources that lead to the asset identified by the given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.named_resource_reference_impl import NamedResourceReferenceImpl
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset

    # example passing only required values which don't have defaults set
    try:
        # Get asset breadcrumb
        api_response = api_instance.get_asset_breadcrumb(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_breadcrumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |

### Return type

[**[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asset breadcrumb |  -  |
**401** | User lacks view permission |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_tags**
> [Tag] get_asset_tags(asset_id)

Get asset tags

Returns all tags of the asset with the given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.tag import Tag
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset

    # example passing only required values which don't have defaults set
    try:
        # Get asset tags
        api_response = api_instance.get_asset_tags(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |

### Return type

[**[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asset tags |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset**
> remove_asset(asset_id)

Remove asset

Removes an asset identified by given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset

    # example passing only required values which don't have defaults set
    try:
        # Remove asset
        api_instance.remove_asset(asset_id)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->remove_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |

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
**204** | Asset removed |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assets**
> remove_assets()

Remove assets

Removes multiple assets.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
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
    api_instance = assets_api.AssetsApi(api_client)
    request_body = [
        "request_body_example",
    ] # [str] | The IDs of the assets to be removed (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove assets
        api_instance.remove_assets(request_body=request_body)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->remove_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**| The IDs of the assets to be removed | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Assets successfully removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tags_from_asset**
> remove_tags_from_asset(asset_id)

Remove tags

Removes tags from the asset with the given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.remove_asset_tags_request import RemoveAssetTagsRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset
    remove_asset_tags_request = RemoveAssetTagsRequest(
        tag_names=[
            "tag_names_example",
        ],
    ) # RemoveAssetTagsRequest | The tags to be removed from given asset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove tags
        api_instance.remove_tags_from_asset(asset_id)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->remove_tags_from_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove tags
        api_instance.remove_tags_from_asset(asset_id, remove_asset_tags_request=remove_asset_tags_request)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->remove_tags_from_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |
 **remove_asset_tags_request** | [**RemoveAssetTagsRequest**](RemoveAssetTagsRequest.md)| The tags to be removed from given asset | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Tags removed |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_attributes**
> [Attribute] set_asset_attributes(asset_id)

Set asset attributes

Replaces all attributes of the asset with the given ID (of given attribute type) with the attributes from the request, except matching attributes, which are retained.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.attribute import Attribute
from collibra_core.model.set_asset_attributes_request import SetAssetAttributesRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset
    set_asset_attributes_request = SetAssetAttributesRequest(
        type_id="type_id_example",
        values=[
            {},
        ],
    ) # SetAssetAttributesRequest | The attributes to be set on the given asset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set asset attributes
        api_response = api_instance.set_asset_attributes(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_asset_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set asset attributes
        api_response = api_instance.set_asset_attributes(asset_id, set_asset_attributes_request=set_asset_attributes_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_asset_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |
 **set_asset_attributes_request** | [**SetAssetAttributesRequest**](SetAssetAttributesRequest.md)| The attributes to be set on the given asset | [optional]

### Return type

[**[Attribute]**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attributes changed |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_relations**
> [RelationImpl] set_asset_relations(asset_id)

Set asset relations

Sets relations for the asset with the given ID. All the relations described by this request will replace the existing ones (identified with asset as one end, relation type and direction of the relation).

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.relation_impl import RelationImpl
from collibra_core.model.set_asset_relations_request import SetAssetRelationsRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset
    set_asset_relations_request = SetAssetRelationsRequest(
        type_id="type_id_example",
        related_asset_ids=[
            "related_asset_ids_example",
        ],
        relation_direction="TO_TARGET",
    ) # SetAssetRelationsRequest | The relations to be set on given asset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set asset relations
        api_response = api_instance.set_asset_relations(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_asset_relations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set asset relations
        api_response = api_instance.set_asset_relations(asset_id, set_asset_relations_request=set_asset_relations_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_asset_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |
 **set_asset_relations_request** | [**SetAssetRelationsRequest**](SetAssetRelationsRequest.md)| The relations to be set on given asset | [optional]

### Return type

[**[RelationImpl]**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed relations |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_responsibilities**
> [ResponsibilityImpl] set_asset_responsibilities(asset_id)

Set asset responsibilities

Sets responsibilities for the asset with the given ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.responsibility_impl import ResponsibilityImpl
from collibra_core.model.set_asset_responsibilities_request import SetAssetResponsibilitiesRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset
    set_asset_responsibilities_request = SetAssetResponsibilitiesRequest(
        role_id="role_id_example",
        owner_ids=[
            "owner_ids_example",
        ],
    ) # SetAssetResponsibilitiesRequest | The responsibilities to be set on given asset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set asset responsibilities
        api_response = api_instance.set_asset_responsibilities(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_asset_responsibilities: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set asset responsibilities
        api_response = api_instance.set_asset_responsibilities(asset_id, set_asset_responsibilities_request=set_asset_responsibilities_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_asset_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |
 **set_asset_responsibilities_request** | [**SetAssetResponsibilitiesRequest**](SetAssetResponsibilitiesRequest.md)| The responsibilities to be set on given asset | [optional]

### Return type

[**[ResponsibilityImpl]**](ResponsibilityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed responsibilities |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tags_for_asset**
> [Tag] set_tags_for_asset(asset_id)

Set asset tags

Sets tags for the asset with the given ID. The asset will contain only those tags specified in the request.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import assets_api
from collibra_core.model.tag import Tag
from collibra_core.model.set_asset_tags_request import SetAssetTagsRequest
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
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "assetId_example" # str | The ID of the asset
    set_asset_tags_request = SetAssetTagsRequest(
        tag_names=[
            "tag_names_example",
        ],
    ) # SetAssetTagsRequest | The tags to be set on given asset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set asset tags
        api_response = api_instance.set_tags_for_asset(asset_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_tags_for_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set asset tags
        api_response = api_instance.set_tags_for_asset(asset_id, set_asset_tags_request=set_asset_tags_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AssetsApi->set_tags_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset |
 **set_asset_tags_request** | [**SetAssetTagsRequest**](SetAssetTagsRequest.md)| The tags to be set on given asset | [optional]

### Return type

[**[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed tags |  -  |
**400** | No asset with the given ID exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

