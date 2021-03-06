# pybrawl.ClubsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club**](ClubsApi.md#get_club) | **GET** /clubs/{clubTag} | Get club information
[**get_club_members**](ClubsApi.md#get_club_members) | **GET** /clubs/{clubTag}/members | Get members of a club
[**get_ranking_brawlers**](ClubsApi.md#get_ranking_brawlers) | **GET** /clubs/{countryCode}/brawlers/{brawlerId} | Get brawler ranking for a country
[**get_ranking_clubs**](ClubsApi.md#get_ranking_clubs) | **GET** /clubs/{countryCode}/clubs | Get club ranking for a country
[**get_ranking_players**](ClubsApi.md#get_ranking_players) | **GET** /clubs/{countryCode}/players | Get player ranking for a country


# **get_club**
> Club get_club(club_tag)

Get club information

Get information about a single club by club tag. Club tags can be found either in game or by from club member lists. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL. 

### Example

* Bearer (JWT) Authentication (JWT):
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

# Configure Bearer authorization (JWT): JWT
configuration = pybrawl.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
 **club_tag** | **str**| Tag of the club to retrieve.  | 

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
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temporarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_members**
> ClubMemberList get_club_members(club_tag, limit=limit, after=after, before=before)

Get members of a club

Get information about the mmebers in a single club by club tag. Club tags can be found either in game or by from club member lists. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL. 

### Example

* Bearer (JWT) Authentication (JWT):
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

# Configure Bearer authorization (JWT): JWT
configuration = pybrawl.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.ClubsApi(api_client)
    club_tag = 'club_tag_example' # str | Tag of the club to retrieve. 
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get members of a club
        api_response = api_instance.get_club_members(club_tag, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->get_club_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_tag** | **str**| Tag of the club to retrieve.  | 
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
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temporarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ranking_brawlers**
> RankingBrawlerList get_ranking_brawlers(country_code, brawler_id, limit=limit, after=after, before=before)

Get brawler ranking for a country

Get information about the ranking of brawlers in a single country. 

### Example

* Bearer (JWT) Authentication (JWT):
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

# Configure Bearer authorization (JWT): JWT
configuration = pybrawl.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.ClubsApi(api_client)
    country_code = 'country_code_example' # str | Country code of the country club list to retrieve. 
brawler_id = 'brawler_id_example' # str | Brawler ID of the brawler rank to retrieve. 
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get brawler ranking for a country
        api_response = api_instance.get_ranking_brawlers(country_code, brawler_id, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->get_ranking_brawlers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Country code of the country club list to retrieve.  | 
 **brawler_id** | **str**| Brawler ID of the brawler rank to retrieve.  | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**RankingBrawlerList**](RankingBrawlerList.md)

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
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temporarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ranking_clubs**
> RankingClubList get_ranking_clubs(country_code, limit=limit, after=after, before=before)

Get club ranking for a country

Get information about the ranking of clubs in a single country. 

### Example

* Bearer (JWT) Authentication (JWT):
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

# Configure Bearer authorization (JWT): JWT
configuration = pybrawl.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.ClubsApi(api_client)
    country_code = 'country_code_example' # str | Country code of the country club list to retrieve. 
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get club ranking for a country
        api_response = api_instance.get_ranking_clubs(country_code, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->get_ranking_clubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Country code of the country club list to retrieve.  | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**RankingClubList**](RankingClubList.md)

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
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temporarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ranking_players**
> RankingPlayerList get_ranking_players(country_code, limit=limit, after=after, before=before)

Get player ranking for a country

Get information about the ranking of players in a single country. 

### Example

* Bearer (JWT) Authentication (JWT):
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

# Configure Bearer authorization (JWT): JWT
configuration = pybrawl.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.ClubsApi(api_client)
    country_code = 'country_code_example' # str | Country code of the country player list to retrieve. 
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 56 # int | Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 56 # int | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get player ranking for a country
        api_response = api_instance.get_ranking_players(country_code, limit=limit, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClubsApi->get_ranking_players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Country code of the country player list to retrieve.  | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **int**| Return only items that occur after this marker. After marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **int**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**RankingPlayerList**](RankingPlayerList.md)

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
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temporarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

