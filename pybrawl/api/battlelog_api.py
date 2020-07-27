# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/heyudude/brawlstars-swagger
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


class BattlelogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_battlelog(self, player_tag, **kwargs):  # noqa: E501
        """Get player's battlelog  # noqa: E501

        Get information about a single player's battlelog  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_battlelog(player_tag, async_req=True)
        >>> result = thread.get()

        :param player_tag: Tag of the player's battle log to retrieve.  (required)
        :type player_tag: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PlayerBattleLog
        """
        kwargs['_return_http_data_only'] = True
        return self.get_battlelog_with_http_info(player_tag, **kwargs)  # noqa: E501

    def get_battlelog_with_http_info(self, player_tag, **kwargs):  # noqa: E501
        """Get player's battlelog  # noqa: E501

        Get information about a single player's battlelog  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_battlelog_with_http_info(player_tag, async_req=True)
        >>> result = thread.get()

        :param player_tag: Tag of the player's battle log to retrieve.  (required)
        :type player_tag: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PlayerBattleLog, status_code(int), headers(HTTPHeaderDict))
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
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_battlelog" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'player_tag' is set
        if self.api_client.client_side_validation and ('player_tag' not in local_var_params or  # noqa: E501
                                                        local_var_params['player_tag'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `player_tag` when calling `get_battlelog`")  # noqa: E501

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
        auth_settings = ['JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/players/{playerTag}/battlelog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerBattleLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
