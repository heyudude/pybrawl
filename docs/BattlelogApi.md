# pybrawl.BattlelogApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_battlelog**](BattlelogApi.md#get_battlelog) | **GET** /players/{playerTag}/battlelog | Get player&#39;s battlelog


# **get_battlelog**
> PlayerBattleLog get_battlelog(player_tag)

Get player's battlelog

Get information about a single player's battlelog

### Example

* Api Key Authentication (bearerAuth):
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

# Configure API key authorization: bearerAuth
configuration = pybrawl.Configuration(
    host = "https://api.brawlstars.com/v1",
    api_key = {
        'bearerAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pybrawl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybrawl.BattlelogApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player's battle log to retrieve. 

    try:
        # Get player's battlelog
        api_response = api_instance.get_battlelog(player_tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BattlelogApi->get_battlelog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player&#39;s battle log to retrieve.  | 

### Return type

[**PlayerBattleLog**](PlayerBattleLog.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

