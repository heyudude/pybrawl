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


class ClubsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def getclub(self, club_tag, **kwargs):  # noqa: E501
        """Get club information  # noqa: E501

        Get information about a single club by club tag. club tags can be found using club search operation. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example club tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getclub(club_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str club_tag: Tag of the club to retrieve. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Club
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.getclub_with_http_info(club_tag, **kwargs)  # noqa: E501

    def getclub_with_http_info(self, club_tag, **kwargs):  # noqa: E501
        """Get club information  # noqa: E501

        Get information about a single club by club tag. club tags can be found using club search operation. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example club tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getclub_with_http_info(club_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str club_tag: Tag of the club to retrieve. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Club, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'club_tag'
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
                    " to method getclub" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'club_tag' is set
        if self.api_client.client_side_validation and ('club_tag' not in local_var_params or  # noqa: E501
                                                        local_var_params['club_tag'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `club_tag` when calling `getclub`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'club_tag' in local_var_params:
            path_params['clubTag'] = local_var_params['club_tag']  # noqa: E501

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
            '/clubs/{clubTag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Club',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getclub_members(self, club_tag, **kwargs):  # noqa: E501
        """List club members  # noqa: E501

        List club members  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getclub_members(club_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str club_tag: Tag of the club whose members to retrieve. (required)
        :param int limit: Limit the number of items returned in the response.
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ClubMemberList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.getclub_members_with_http_info(club_tag, **kwargs)  # noqa: E501

    def getclub_members_with_http_info(self, club_tag, **kwargs):  # noqa: E501
        """List club members  # noqa: E501

        List club members  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getclub_members_with_http_info(club_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str club_tag: Tag of the club whose members to retrieve. (required)
        :param int limit: Limit the number of items returned in the response.
        :param int after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ClubMemberList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'club_tag',
            'limit',
            'after',
            'before'
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
                    " to method getclub_members" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'club_tag' is set
        if self.api_client.client_side_validation and ('club_tag' not in local_var_params or  # noqa: E501
                                                        local_var_params['club_tag'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `club_tag` when calling `getclub_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'club_tag' in local_var_params:
            path_params['clubTag'] = local_var_params['club_tag']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'after' in local_var_params and local_var_params['after'] is not None:  # noqa: E501
            query_params.append(('after', local_var_params['after']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501

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
            '/clubs/{clubTag}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClubMemberList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
