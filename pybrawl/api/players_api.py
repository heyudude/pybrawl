# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pybrawl.api_client import ApiClient
from pybrawl.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlayersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_player(self, player_tag, **kwargs):  # noqa: E501
        """Get player information  # noqa: E501

        Get information about a single player by player tag. Player tags can befound either in game or by from club member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player(player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str player_tag: Tag of the player to retrieve.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PlayerDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_player_with_http_info(player_tag, **kwargs)  # noqa: E501

    def get_player_with_http_info(self, player_tag, **kwargs):  # noqa: E501
        """Get player information  # noqa: E501

        Get information about a single player by player tag. Player tags can befound either in game or by from club member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_with_http_info(player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str player_tag: Tag of the player to retrieve.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PlayerDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'player_tag'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'player_tag' is set
        #if self.api_client.client_side_validation and ('player_tag' not in local_var_params or  # noqa: E501
        #                                                local_var_params['player_tag'] is None):  # noqa: E501
        #    raise ApiValueError("Missing the required parameter `player_tag` when calling `get_player`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'player_tag' in local_var_params:
            path_params['playerTag'] = local_var_params['player_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/players/{playerTag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_battles(self, player_tag, **kwargs):  # noqa: E501
        """Get log of recent battles for a player  # noqa: E501

        Get list of recent battle results for a player.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_battles(player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str player_tag: Tag of the player whose information to retrieve.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BattleLogEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_player_battles_with_http_info(player_tag, **kwargs)  # noqa: E501

    def get_player_battles_with_http_info(self, player_tag, **kwargs):  # noqa: E501
        """Get log of recent battles for a player  # noqa: E501

        Get list of recent battle results for a player.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_battles_with_http_info(player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str player_tag: Tag of the player whose information to retrieve.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BattleLogEntry], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'player_tag'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_battles" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'player_tag' is set
        if self.api_client.client_side_validation and ('player_tag' not in local_var_params or  # noqa: E501
                                                        local_var_params['player_tag'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `player_tag` when calling `get_player_battles`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'player_tag' in local_var_params:
            path_params['playerTag'] = local_var_params['player_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/players/{playerTag}/battlelog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BattleLogEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
