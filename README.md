# pybrawl
Unofficial Swagger definition for the official Brawl Stars API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pybrawl
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pybrawl
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = pybrawl.BattlelogApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player's battle log to retrieve. 

    try:
        # Get player's battlelog
        api_response = api_instance.get_battlelog(player_tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BattlelogApi->get_battlelog: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.brawlstars.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BattlelogApi* | [**get_battlelog**](docs/BattlelogApi.md#get_battlelog) | **GET** /players/{playerTag}/battlelog | Get player&#39;s battlelog
*PlayersApi* | [**get_player**](docs/PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information


## Documentation For Models

 - [Battle](docs/Battle.md)
 - [BattleBrawler](docs/BattleBrawler.md)
 - [Battles](docs/Battles.md)
 - [Brawler](docs/Brawler.md)
 - [BrawlerList](docs/BrawlerList.md)
 - [ClubBase](docs/ClubBase.md)
 - [Error](docs/Error.md)
 - [Event](docs/Event.md)
 - [Gadgets](docs/Gadgets.md)
 - [PlayerBattleLog](docs/PlayerBattleLog.md)
 - [PlayerDetail](docs/PlayerDetail.md)
 - [StarBrawler](docs/StarBrawler.md)
 - [StarPlayer](docs/StarPlayer.md)
 - [StarPowers](docs/StarPowers.md)
 - [Teams](docs/Teams.md)


## Documentation For Authorization


## JWT

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author




- Aaron Traas <aaron@traas.org>

## Development links

This project uses SonarQube for static analysis. The results of analysis are at
[SonarCloud](https://sonarcloud.io/dashboard?id=AaronTraas_Clash-Royale-Club-Tools).
The code quality and test coverage are a work in progress.

## Support
If you need help getting this up and running, feel free to hop on the
[pybrawl discord](https://discord.gg/K2UDCXU).

