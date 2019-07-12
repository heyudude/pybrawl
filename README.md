# pyroyale
Unofficial Swagger definition for the official Clash Royale API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pyroyale 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pyroyale
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyroyale.CardsApi(pyroyale.ApiClient(configuration))

try:
    # Get list of available cards
    api_response = api_instance.get_cards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->get_cards: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.clashroyale.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CardsApi* | [**get_cards**](docs/CardsApi.md#get_cards) | **GET** /cards | Get list of available cards
*ClansApi* | [**get_clan**](docs/ClansApi.md#get_clan) | **GET** /clans/{clanTag} | Get clan information
*ClansApi* | [**get_clan_members**](docs/ClansApi.md#get_clan_members) | **GET** /clans/{clanTag}/members | List clan members
*ClansApi* | [**get_clan_war_log**](docs/ClansApi.md#get_clan_war_log) | **GET** /clans/{clanTag}/warlog | Retrieve clan&#x27;s clan war log
*ClansApi* | [**get_current_war**](docs/ClansApi.md#get_current_war) | **GET** /clans/{clanTag}/currentwar | Information about clan&#x27;s current clan war
*ClansApi* | [**search_clans**](docs/ClansApi.md#search_clans) | **GET** /clans | Search clans
*LocationsApi* | [**get_clan_ranking**](docs/LocationsApi.md#get_clan_ranking) | **GET** /locations/{locationId}/rankings/clans | Get clan rankings for a specific location
*LocationsApi* | [**get_clan_wars_ranking**](docs/LocationsApi.md#get_clan_wars_ranking) | **GET** /locations/{locationId}/rankings/clanwars | Get clan war rankings for a specific location
*LocationsApi* | [**get_location**](docs/LocationsApi.md#get_location) | **GET** /locations/{locationId} | Get location information
*LocationsApi* | [**get_locations**](docs/LocationsApi.md#get_locations) | **GET** /locations | List locations
*LocationsApi* | [**get_player_ranking**](docs/LocationsApi.md#get_player_ranking) | **GET** /locations/{locationId}/rankings/players | Get player rankings for a specific location
*PlayersApi* | [**get_player**](docs/PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information
*PlayersApi* | [**get_player_battles**](docs/PlayersApi.md#get_player_battles) | **GET** /players/{playerTag}/battlelog | Get log of recent battles for a player
*PlayersApi* | [**get_player_upcoming_chests**](docs/PlayersApi.md#get_player_upcoming_chests) | **GET** /players/{playerTag}/upcomingchests | Get information about player&#x27;s upcoming chests
*TournamentsApi* | [**get_global_tournaments**](docs/TournamentsApi.md#get_global_tournaments) | **GET** /globaltournaments | List global tournaments
*TournamentsApi* | [**get_tournament**](docs/TournamentsApi.md#get_tournament) | **GET** /tournaments/{tournamentTag} | Get tournament information
*TournamentsApi* | [**search_tournaments**](docs/TournamentsApi.md#search_tournaments) | **GET** /tournaments | Search tournaments

## Documentation For Models

 - [Arena](docs/Arena.md)
 - [BattleLog](docs/BattleLog.md)
 - [BattleLogEntry](docs/BattleLogEntry.md)
 - [BattleLogGameMode](docs/BattleLogGameMode.md)
 - [BattleLogTeam](docs/BattleLogTeam.md)
 - [BattleLogTeamList](docs/BattleLogTeamList.md)
 - [Card](docs/Card.md)
 - [CardIconUrls](docs/CardIconUrls.md)
 - [CardList](docs/CardList.md)
 - [Chest](docs/Chest.md)
 - [ChestList](docs/ChestList.md)
 - [Clan](docs/Clan.md)
 - [ClanBase](docs/ClanBase.md)
 - [ClanMember](docs/ClanMember.md)
 - [ClanMemberList](docs/ClanMemberList.md)
 - [ClanRanked](docs/ClanRanked.md)
 - [ClanRankingList](docs/ClanRankingList.md)
 - [ClanSearchResult](docs/ClanSearchResult.md)
 - [ClanSearchResultClan](docs/ClanSearchResultClan.md)
 - [ClanWarRanked](docs/ClanWarRanked.md)
 - [ClanWarsRankingList](docs/ClanWarsRankingList.md)
 - [Error](docs/Error.md)
 - [Location](docs/Location.md)
 - [LocationList](docs/LocationList.md)
 - [PlayerAchievement](docs/PlayerAchievement.md)
 - [PlayerBadge](docs/PlayerBadge.md)
 - [PlayerBase](docs/PlayerBase.md)
 - [PlayerDetail](docs/PlayerDetail.md)
 - [PlayerLeagueStatistics](docs/PlayerLeagueStatistics.md)
 - [PlayerRanked](docs/PlayerRanked.md)
 - [PlayerRankingList](docs/PlayerRankingList.md)
 - [SeasonStatistics](docs/SeasonStatistics.md)
 - [Tournament](docs/Tournament.md)
 - [TournamentDetail](docs/TournamentDetail.md)
 - [TournamentList](docs/TournamentList.md)
 - [TournamentPlayer](docs/TournamentPlayer.md)
 - [TournamentSearchResult](docs/TournamentSearchResult.md)
 - [War](docs/War.md)
 - [WarClan](docs/WarClan.md)
 - [WarCurrent](docs/WarCurrent.md)
 - [WarLog](docs/WarLog.md)
 - [WarParticipant](docs/WarParticipant.md)
 - [WarStanding](docs/WarStanding.md)
 - [WarStandingClan](docs/WarStandingClan.md)

## Documentation For Authorization


## JWT

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author


