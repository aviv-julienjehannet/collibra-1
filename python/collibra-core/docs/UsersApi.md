# collibra_core.UsersApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /users | Adds a new user
[**add_user_groups_for_user**](UsersApi.md#add_user_groups_for_user) | **POST** /users/{userId}/userGroups | Add a user to multiple user groups
[**add_users**](UsersApi.md#add_users) | **POST** /users/bulk | Adds multiple new users
[**change_user**](UsersApi.md#change_user) | **PATCH** /users/{userId} | Changes the user with the information that is present in the request
[**change_user_avatar**](UsersApi.md#change_user_avatar) | **PATCH** /users/{userId}/avatar | Changes the avatar for the user identified by the given ID
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{userId} | Deletes the user with the given ID
[**delete_user_avatar**](UsersApi.md#delete_user_avatar) | **DELETE** /users/{userId}/avatar | Deletes the avatar for the user identified by the given ID
[**find_users**](UsersApi.md#find_users) | **GET** /users | Returns users matching the given search criteria
[**get_avatar_file**](UsersApi.md#get_avatar_file) | **GET** /users/{userId}/avatar | Get the avatar image for the user with the given ID
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/current | Returns the current user, if logged in
[**get_current_user_permissions**](UsersApi.md#get_current_user_permissions) | **GET** /users/current/permissions | Returns the current user permissions, if logged in
[**get_user**](UsersApi.md#get_user) | **GET** /users/{userId} | Gets the user with the given ID
[**get_user_by_email_address**](UsersApi.md#get_user_by_email_address) | **GET** /users/email/{emailAddress} | Gets the user identified by given e-mail address
[**get_user_required_license_type**](UsersApi.md#get_user_required_license_type) | **GET** /users/{userId}/licenseType | Gets the required LicenseType for the given user
[**remove_user_from_user_groups**](UsersApi.md#remove_user_from_user_groups) | **DELETE** /users/{userId}/userGroups | Removes user from multiple user groups
[**set_user_groups_for_user**](UsersApi.md#set_user_groups_for_user) | **PUT** /users/{userId}/userGroups | Sets user groups for the indicated user


# **add_user**
> User add_user()

Adds a new user

Adds a new user

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user import User
from collibra_core.model.add_user_request import AddUserRequest
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
    api_instance = users_api.UsersApi(api_client)
    add_user_request = AddUserRequest(
        user_name="user_name_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email_address="email_address_example",
        gender="MALE",
        language="language_example",
        user_group_ids=[
            "user_group_ids_example",
        ],
        license_type="CONSUMER",
        addresses=[
            Address(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                city="city_example",
                street="street_example",
                number="number_example",
                state="state_example",
                country="country_example",
                postal_code="postal_code_example",
                type="HOME",
            ),
        ],
        phones=[
            PhoneNumber(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                type="FAX",
                phone_number="phone_number_example",
            ),
        ],
        additional_email_addresses=[
            Email(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                email_address="email_address_example",
            ),
        ],
        instant_messaging_accounts=[
            InstantMessagingAccount(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                account="account_example",
                type="AOL",
            ),
        ],
        websites=[
            Website(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                url="url_example",
                type="FACEBOOK",
            ),
        ],
    ) # AddUserRequest | The properties of the user to be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds a new user
        api_response = api_instance.add_user(add_user_request=add_user_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_request** | [**AddUserRequest**](AddUserRequest.md)| The properties of the user to be added | [optional]

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_groups_for_user**
> [UserGroupImpl] add_user_groups_for_user(user_id)

Add a user to multiple user groups

Add a user to multiple user groups

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.add_user_to_user_groups_request import AddUserToUserGroupsRequest
from collibra_core.model.user_group_impl import UserGroupImpl
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user
    add_user_to_user_groups_request = AddUserToUserGroupsRequest(
        user_id="user_id_example",
        user_group_ids=[
            "user_group_ids_example",
        ],
    ) # AddUserToUserGroupsRequest | the properties needed to add the user to the user groups (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a user to multiple user groups
        api_response = api_instance.add_user_groups_for_user(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->add_user_groups_for_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a user to multiple user groups
        api_response = api_instance.add_user_groups_for_user(user_id, add_user_to_user_groups_request=add_user_to_user_groups_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->add_user_groups_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user |
 **add_user_to_user_groups_request** | [**AddUserToUserGroupsRequest**](AddUserToUserGroupsRequest.md)| the properties needed to add the user to the user groups | [optional]

### Return type

[**[UserGroupImpl]**](UserGroupImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully added to the indicated groups. |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users**
> [User] add_users()

Adds multiple new users

Adds multiple new users

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user import User
from collibra_core.model.add_user_request import AddUserRequest
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
    api_instance = users_api.UsersApi(api_client)
    add_user_request = [
        AddUserRequest(
            user_name="user_name_example",
            first_name="first_name_example",
            last_name="last_name_example",
            email_address="email_address_example",
            gender="MALE",
            language="language_example",
            user_group_ids=[
                "user_group_ids_example",
            ],
            license_type="CONSUMER",
            addresses=[
                Address(
                    id="id_example",
                    created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                    created_on=1475503010320,
                    last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                    last_modified_on=1476703764163,
                    system=True,
                    resource_type="Job",
                    city="city_example",
                    street="street_example",
                    number="number_example",
                    state="state_example",
                    country="country_example",
                    postal_code="postal_code_example",
                    type="HOME",
                ),
            ],
            phones=[
                PhoneNumber(
                    id="id_example",
                    created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                    created_on=1475503010320,
                    last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                    last_modified_on=1476703764163,
                    system=True,
                    resource_type="Job",
                    type="FAX",
                    phone_number="phone_number_example",
                ),
            ],
            additional_email_addresses=[
                Email(
                    id="id_example",
                    created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                    created_on=1475503010320,
                    last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                    last_modified_on=1476703764163,
                    system=True,
                    resource_type="Job",
                    email_address="email_address_example",
                ),
            ],
            instant_messaging_accounts=[
                InstantMessagingAccount(
                    id="id_example",
                    created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                    created_on=1475503010320,
                    last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                    last_modified_on=1476703764163,
                    system=True,
                    resource_type="Job",
                    account="account_example",
                    type="AOL",
                ),
            ],
            websites=[
                Website(
                    id="id_example",
                    created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                    created_on=1475503010320,
                    last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                    last_modified_on=1476703764163,
                    system=True,
                    resource_type="Job",
                    url="url_example",
                    type="FACEBOOK",
                ),
            ],
        ),
    ] # [AddUserRequest] | The properties of the users to be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds multiple new users
        api_response = api_instance.add_users(add_user_request=add_user_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->add_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_request** | [**[AddUserRequest]**](AddUserRequest.md)| The properties of the users to be added | [optional]

### Return type

[**[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Users successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user**
> User change_user(user_id)

Changes the user with the information that is present in the request

Only properties that are specified in this request and have non-<code>null</code> values are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.change_user_request import ChangeUserRequest
from collibra_core.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user to be changed
    change_user_request = ChangeUserRequest(
        enabled=True,
        username="username_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        gender="MALE",
        language="language_example",
        license_type="CONSUMER",
        addresses=[
            Address(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                city="city_example",
                street="street_example",
                number="number_example",
                state="state_example",
                country="country_example",
                postal_code="postal_code_example",
                type="HOME",
            ),
        ],
        phones=[
            PhoneNumber(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                type="FAX",
                phone_number="phone_number_example",
            ),
        ],
        additional_email_addresses=[
            Email(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                email_address="email_address_example",
            ),
        ],
        instant_messaging_accounts=[
            InstantMessagingAccount(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                account="account_example",
                type="AOL",
            ),
        ],
        websites=[
            Website(
                id="id_example",
                created_by="4d250cc5-e583-4640-9874-b93d82c7a6cb",
                created_on=1475503010320,
                last_modified_by="a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                last_modified_on=1476703764163,
                system=True,
                resource_type="Job",
                url="url_example",
                type="FACEBOOK",
            ),
        ],
    ) # ChangeUserRequest | the properties of the user to be changed (optional)

    # example passing only required values which don't have defaults set
    try:
        # Changes the user with the information that is present in the request
        api_response = api_instance.change_user(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->change_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Changes the user with the information that is present in the request
        api_response = api_instance.change_user(user_id, change_user_request=change_user_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->change_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user to be changed |
 **change_user_request** | [**ChangeUserRequest**](ChangeUserRequest.md)| the properties of the user to be changed | [optional]

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully changed |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_avatar**
> User change_user_avatar(user_id)

Changes the avatar for the user identified by the given ID

Changes the avatar for the user identified by the given ID

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user import User
from collibra_core.model.change_user_avatar_request import ChangeUserAvatarRequest
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user to change the avatar for
    change_user_avatar_request = ChangeUserAvatarRequest(
        file_id="file_id_example",
    ) # ChangeUserAvatarRequest | the properties needed to change to avatar for the user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Changes the avatar for the user identified by the given ID
        api_response = api_instance.change_user_avatar(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->change_user_avatar: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Changes the avatar for the user identified by the given ID
        api_response = api_instance.change_user_avatar(user_id, change_user_avatar_request=change_user_avatar_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->change_user_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user to change the avatar for |
 **change_user_avatar_request** | [**ChangeUserAvatarRequest**](ChangeUserAvatarRequest.md)| the properties needed to change to avatar for the user | [optional]

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User avatar successfully changed |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Deletes the user with the given ID

Deletes the user with the given ID

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Deletes the user with the given ID
        api_instance.delete_user(user_id)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user to be deleted |

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
**204** | User successfully deleted |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_avatar**
> delete_user_avatar(user_id)

Deletes the avatar for the user identified by the given ID

Deletes the avatar for the user identified by the given ID

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user to delete the avatar for

    # example passing only required values which don't have defaults set
    try:
        # Deletes the avatar for the user identified by the given ID
        api_instance.delete_user_avatar(user_id)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->delete_user_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user to delete the avatar for |

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
**204** | User avatar successfully deleted |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_users**
> UserPagedResponse find_users()

Returns users matching the given search criteria

Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.<p>The returned users satisfy all constraints that are specified in this search criteria.</p><p>By default a result containing 1000 users is returned.</p>

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user_paged_response import UserPagedResponse
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
    api_instance = users_api.UsersApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    user_id = [
        "userId_example",
    ] # [str] | Comma-separated list of user IDs to look for. Alternatively, you can pass this query parameter multiple times. (optional)
    name = "name_example" # str | The name of the user. The search will occur in the username, first name, last name, and a combination of those. (optional)
    group_id = "groupId_example" # str | The ID of the group the searched users should belong to. (optional)
    only_logged_in = True # bool | Whether only currently logged in users should be returned. (optional)
    include_disabled = True # bool | Whether disabled users should be included in the search results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns users matching the given search criteria
        api_response = api_instance.find_users(offset=offset, limit=limit, user_id=user_id, name=name, group_id=group_id, only_logged_in=only_logged_in, include_disabled=include_disabled)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->find_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **user_id** | **[str]**| Comma-separated list of user IDs to look for. Alternatively, you can pass this query parameter multiple times. | [optional]
 **name** | **str**| The name of the user. The search will occur in the username, first name, last name, and a combination of those. | [optional]
 **group_id** | **str**| The ID of the group the searched users should belong to. | [optional]
 **only_logged_in** | **bool**| Whether only currently logged in users should be returned. | [optional]
 **include_disabled** | **bool**| Whether disabled users should be included in the search results. | [optional]

### Return type

[**UserPagedResponse**](UserPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar_file**
> file_type get_avatar_file(user_id)

Get the avatar image for the user with the given ID

Get the avatar image for the user with the given ID

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The ID of the user to get the avatar for
    width = 1 # int | The width of the returned avatar (optional)
    height = 1 # int | The height of the returned avatar (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the avatar image for the user with the given ID
        api_response = api_instance.get_avatar_file(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_avatar_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the avatar image for the user with the given ID
        api_response = api_instance.get_avatar_file(user_id, width=width, height=height)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_avatar_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to get the avatar for |
 **width** | **int**| The width of the returned avatar | [optional]
 **height** | **int**| The height of the returned avatar | [optional]

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
**200** | Avatar image successfully retrieved |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user()

Returns the current user, if logged in

If the user is not logged in, <code>null</code> is returned

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user import User
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the current user, if logged in
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User succesfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_permissions**
> UserPermissions get_current_user_permissions()

Returns the current user permissions, if logged in

If the user is not logged in, Permissions of the Guest user are returned

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user_permissions import UserPermissions
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the current user permissions, if logged in
        api_response = api_instance.get_current_user_permissions()
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_current_user_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserPermissions**](UserPermissions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Gets the user with the given ID

Gets the user with the given ID

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The ID of the user

    # example passing only required values which don't have defaults set
    try:
        # Gets the user with the given ID
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user |

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully retrieved |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_email_address**
> User get_user_by_email_address(email_address)

Gets the user identified by given e-mail address

Gets the user identified by given e-mail address

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    email_address = "emailAddress_example" # str | The e-mail address of the user

    # example passing only required values which don't have defaults set
    try:
        # Gets the user identified by given e-mail address
        api_response = api_instance.get_user_by_email_address(email_address)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| The e-mail address of the user |

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully retrieved |  -  |
**404** | User with given e-mail not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_required_license_type**
> str get_user_required_license_type(user_id)

Gets the required LicenseType for the given user

This endpoint will be removed in the future.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user

    # example passing only required values which don't have defaults set
    try:
        # Gets the required LicenseType for the given user
        api_response = api_instance.get_user_required_license_type(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->get_user_required_license_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user |

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LicenseType successfully retrieved |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_user_groups**
> remove_user_from_user_groups(user_id)

Removes user from multiple user groups

Removes user from multiple user groups

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.remove_user_from_user_groups_request import RemoveUserFromUserGroupsRequest
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The ID of the user
    remove_user_from_user_groups_request = RemoveUserFromUserGroupsRequest(
        user_id="user_id_example",
        user_group_ids=[
            "user_group_ids_example",
        ],
    ) # RemoveUserFromUserGroupsRequest | The properties needed to remove the user from user groups (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes user from multiple user groups
        api_instance.remove_user_from_user_groups(user_id)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->remove_user_from_user_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes user from multiple user groups
        api_instance.remove_user_from_user_groups(user_id, remove_user_from_user_groups_request=remove_user_from_user_groups_request)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->remove_user_from_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user |
 **remove_user_from_user_groups_request** | [**RemoveUserFromUserGroupsRequest**](RemoveUserFromUserGroupsRequest.md)| The properties needed to remove the user from user groups | [optional]

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
**204** | User successfully removed from user groups |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_groups_for_user**
> User set_user_groups_for_user(user_id)

Sets user groups for the indicated user

Sets user groups for the indicated user

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import users_api
from collibra_core.model.set_user_groups_for_user_request import SetUserGroupsForUserRequest
from collibra_core.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | the ID of the user
    set_user_groups_for_user_request = SetUserGroupsForUserRequest(
        user_group_ids=[
            "user_group_ids_example",
        ],
    ) # SetUserGroupsForUserRequest | the properties needed to add the user to user groups (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sets user groups for the indicated user
        api_response = api_instance.set_user_groups_for_user(user_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->set_user_groups_for_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sets user groups for the indicated user
        api_response = api_instance.set_user_groups_for_user(user_id, set_user_groups_for_user_request=set_user_groups_for_user_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling UsersApi->set_user_groups_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the ID of the user |
 **set_user_groups_for_user_request** | [**SetUserGroupsForUserRequest**](SetUserGroupsForUserRequest.md)| the properties needed to add the user to user groups | [optional]

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User groups set successfully |  -  |
**404** | User with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

