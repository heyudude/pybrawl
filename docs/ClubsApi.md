# pybrawl.ClubsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getclub**](ClubsApi.md#getclub) | **GET** /clubs/{clubTag} | Get club information
[**getclub_members**](ClubsApi.md#getclub_members) | **GET** /clubs/{clubTag}/members | List club members


# **getclub**
> Club getclub(club_tag)

Get club information

Get information about a single club by club tag. club tags can be found using club search operation. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example club tag '#2ABC' would become '%232ABC' in the URL. 

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
        api_response = api_instance.getclub(club_tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->getclub: %s\n" % e)
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

# **getclub_members**
> ClubMemberList getclub_members(club_tag, limit=limit, after=after, before=before)

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
        api_response = api_instance.getclub_members(club_tag, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->getclub_members: %s\n" % e)
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

