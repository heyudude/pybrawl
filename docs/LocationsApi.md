# pybrawl.LocationsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club_ranking**](LocationsApi.md#get_club_ranking) | **GET** /locations/{locationId}/rankings/clubs | Get club rankings for a specific location
[**get_location**](LocationsApi.md#get_location) | **GET** /locations/{locationId} | Get location information
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | List locations
[**get_player_ranking**](LocationsApi.md#get_player_ranking) | **GET** /locations/{locationId}/rankings/players | Get player rankings for a specific location


# **get_club_ranking**
> ClubRankingList get_club_ranking(location_id, limit=limit, after=after, before=before)

Get club rankings for a specific location

Get club rankings for a specific location

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pybrawl
from pybrawl.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get club rankings for a specific location
        api_response = api_instance.get_club_ranking(location_id, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationsApi->get_club_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClubRankingList**](ClubRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location**
> Location get_location(location_id)

Get location information

Get information about specific location

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pybrawl
from pybrawl.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.

    try:
        # Get location information
        api_response = api_instance.get_location(location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationsApi->get_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 

### Return type

[**Location**](Location.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations**
> LocationList get_locations(limit=limit, after=after, before=before)

List locations

List all available locations

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pybrawl
from pybrawl.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.LocationsApi(api_client)
    limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # List locations
        api_response = api_instance.get_locations(limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**LocationList**](LocationList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_ranking**
> PlayerRankingList get_player_ranking(location_id, limit=limit, after=after, before=before)

Get player rankings for a specific location

Get player rankings for a specific location

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pybrawl
from pybrawl.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get player rankings for a specific location
        api_response = api_instance.get_player_ranking(location_id, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationsApi->get_player_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**PlayerRankingList**](PlayerRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

