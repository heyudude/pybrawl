# pybrawl.ClubsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club**](ClubsApi.md#get_club) | **GET** /clubs/{clubTag} | Get club information
[**get_club_members**](ClubsApi.md#get_club_members) | **GET** /clubs/{clubTag}/members | List club members
[**search_clubs**](ClubsApi.md#search_clubs) | **GET** /clubs | Search clubs


# **get_club**
> Club get_club(club_tag)

Get club information

Get information about a single club by club tag. Club tags can be found using club search operation. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example club tag '#2ABC' would become '%232ABC' in the URL. 

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
    api_instance = pybrawl.ClubsApi(api_client)
    club_tag = 'club_tag_example' # str | Tag of the club to retrieve.

    try:
        # Get club information
        api_response = api_instance.get_club(club_tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->get_club: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_tag** | **str**| Tag of the club to retrieve. | 

### Return type

[**Club**](Club.md)

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

# **get_club_members**
> ClubMemberList get_club_members(club_tag, limit=limit, after=after, before=before)

List club members

List club members

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
    api_instance = pybrawl.ClubsApi(api_client)
    club_tag = 'club_tag_example' # str | Tag of the club whose members to retrieve.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # List club members
        api_response = api_instance.get_club_members(club_tag, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->get_club_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_tag** | **str**| Tag of the club whose members to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClubMemberList**](ClubMemberList.md)

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

# **search_clubs**
> ClubSearchResult search_clubs(name=name, location_id=location_id, min_members=min_members, max_members=max_members, min_score=min_score, limit=limit, after=after, before=before)

Search clubs

Search all clubs by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is used as part of search, it is required to be at least three characters long. It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API. 

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
    api_instance = pybrawl.ClubsApi(api_client)
    name = 'name_example' # str | Search clubs by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild brawler search, so it may appear anywhere in the club name.  (optional)
location_id = 56 # int | Filter by club location identifier. For list of available locations, refer to getLocations operation.  (optional)
min_members = 56 # int | Filter by minimum amount of club members.  (optional)
max_members = 56 # int | Filter by maximum amount of club members.  (optional)
min_score = 56 # int | Filter by minimum amount of club score.  (optional)
limit = 56 # int | Limit the number of items returned in the response.  (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from theresponse, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Search clubs
        api_response = api_instance.search_clubs(name=name, location_id=location_id, min_members=min_members, max_members=max_members, min_score=min_score, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->search_clubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search clubs by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild brawler search, so it may appear anywhere in the club name.  | [optional] 
 **location_id** | **int**| Filter by club location identifier. For list of available locations, refer to getLocations operation.  | [optional] 
 **min_members** | **int**| Filter by minimum amount of club members.  | [optional] 
 **max_members** | **int**| Filter by maximum amount of club members.  | [optional] 
 **min_score** | **int**| Filter by minimum amount of club score.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response.  | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from theresponse, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClubSearchResult**](ClubSearchResult.md)

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

