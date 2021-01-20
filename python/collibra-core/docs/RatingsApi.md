# collibra_core.RatingsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rating**](RatingsApi.md#add_rating) | **POST** /ratings | Add rating.
[**change_rating**](RatingsApi.md#change_rating) | **PATCH** /ratings/{ratingId} | Change rating.
[**find_ratings**](RatingsApi.md#find_ratings) | **GET** /ratings | Find ratings.
[**get_rating**](RatingsApi.md#get_rating) | **GET** /ratings/{ratingId} | Get rating.
[**remove_rating**](RatingsApi.md#remove_rating) | **DELETE** /ratings/{ratingId} | Remove rating.


# **add_rating**
> Rating add_rating()

Add rating.

Adds a new rating.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import ratings_api
from collibra_core.model.add_rating_request import AddRatingRequest
from collibra_core.model.rating import Rating
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
    api_instance = ratings_api.RatingsApi(api_client)
    add_rating_request = AddRatingRequest(
        rating=0.2,
        review="This is a review",
        asset_id="asset_id_example",
    ) # AddRatingRequest | The properties of the rating to be added. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add rating.
        api_response = api_instance.add_rating(add_rating_request=add_rating_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling RatingsApi->add_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_rating_request** | [**AddRatingRequest**](AddRatingRequest.md)| The properties of the rating to be added. | [optional]

### Return type

[**Rating**](Rating.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Rating successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_rating**
> Rating change_rating(rating_id)

Change rating.

Modifies the rating with the specified ID.<p>Only properties that are specified in these requests and have not <code>null</code> values are updated. All other properties are ignored.</p>

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import ratings_api
from collibra_core.model.change_rating_request import ChangeRatingRequest
from collibra_core.model.rating import Rating
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
    api_instance = ratings_api.RatingsApi(api_client)
    rating_id = "ratingId_example" # str | The ID of the rating to be changed.
    change_rating_request = ChangeRatingRequest(
        rating=0.2,
        review="review_example",
    ) # ChangeRatingRequest | The properties of the rating to be changed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change rating.
        api_response = api_instance.change_rating(rating_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling RatingsApi->change_rating: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change rating.
        api_response = api_instance.change_rating(rating_id, change_rating_request=change_rating_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling RatingsApi->change_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| The ID of the rating to be changed. |
 **change_rating_request** | [**ChangeRatingRequest**](ChangeRatingRequest.md)| The properties of the rating to be changed. | [optional]

### Return type

[**Rating**](Rating.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating successfully changed. |  -  |
**404** | Rating with given ID could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ratings**
> RatingsPagedResponse find_ratings()

Find ratings.

Returns ratings matching the given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p><p>The returned ratings satisfy all constraints that are specified in this search criteria. By default, the result contains up to 1000 ratings.</p>

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import ratings_api
from collibra_core.model.ratings_paged_response import RatingsPagedResponse
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
    api_instance = ratings_api.RatingsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    sort_order = "DESC" # str | The order of sorting (on creation date) the found ratings. (optional) if omitted the server will use the default value of "DESC"
    asset_id = "assetId_example" # str | The ID of the asset the rating belongs to. (optional)
    user_id = "userId_example" # str | The ID of the rating author. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find ratings.
        api_response = api_instance.find_ratings(offset=offset, limit=limit, sort_order=sort_order, asset_id=asset_id, user_id=user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling RatingsApi->find_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **sort_order** | **str**| The order of sorting (on creation date) the found ratings. | [optional] if omitted the server will use the default value of "DESC"
 **asset_id** | **str**| The ID of the asset the rating belongs to. | [optional]
 **user_id** | **str**| The ID of the rating author. | [optional]

### Return type

[**RatingsPagedResponse**](RatingsPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found ratings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rating**
> Rating get_rating(rating_id)

Get rating.

Returns the rating with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import ratings_api
from collibra_core.model.rating import Rating
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
    api_instance = ratings_api.RatingsApi(api_client)
    rating_id = "ratingId_example" # str | The ID of the rating.

    # example passing only required values which don't have defaults set
    try:
        # Get rating.
        api_response = api_instance.get_rating(rating_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling RatingsApi->get_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| The ID of the rating. |

### Return type

[**Rating**](Rating.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating found. |  -  |
**404** | Rating with given ID could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rating**
> remove_rating(rating_id)

Remove rating.

Removes the rating with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import ratings_api
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
    api_instance = ratings_api.RatingsApi(api_client)
    rating_id = "ratingId_example" # str | The ID of the rating to be removed.

    # example passing only required values which don't have defaults set
    try:
        # Remove rating.
        api_instance.remove_rating(rating_id)
    except collibra_core.ApiException as e:
        print("Exception when calling RatingsApi->remove_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| The ID of the rating to be removed. |

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
**204** | Rating successfully removed. |  -  |
**404** | Rating with given ID could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

