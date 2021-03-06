# coding: utf-8

"""
    Brawl_Stars_API

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


class ClubsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_club(self, club_tag, **kwargs):  # noqa: E501
        """Get club information  # noqa: E501

        Get information about a single club by club tag. Club tags can be found either in game or by from club member lists. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_club(club_tag, async_req=True)
        >>> result = thread.get()

        :param club_tag: Tag of the club to retrieve.  (required)
        :type club_tag: str
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
        :rtype: Club
        """
        kwargs['_return_http_data_only'] = True
        return self.get_club_with_http_info(club_tag, **kwargs)  # noqa: E501

    def get_club_with_http_info(self, club_tag, **kwargs):  # noqa: E501
        """Get club information  # noqa: E501

        Get information about a single club by club tag. Club tags can be found either in game or by from club member lists. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_club_with_http_info(club_tag, async_req=True)
        >>> result = thread.get()

        :param club_tag: Tag of the club to retrieve.  (required)
        :type club_tag: str
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
        :rtype: tuple(Club, status_code(int), headers(HTTPHeaderDict))
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
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_club" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'club_tag' is set
        if self.api_client.client_side_validation and ('club_tag' not in local_var_params or  # noqa: E501
                                                        local_var_params['club_tag'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `club_tag` when calling `get_club`")  # noqa: E501

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
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_club_members(self, club_tag, **kwargs):  # noqa: E501
        """Get members of a club  # noqa: E501

        Get information about the mmebers in a single club by club tag. Club tags can be found either in game or by from club member lists. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_club_members(club_tag, async_req=True)
        >>> result = thread.get()

        :param club_tag: Tag of the club to retrieve.  (required)
        :type club_tag: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: ClubMemberList
        """
        kwargs['_return_http_data_only'] = True
        return self.get_club_members_with_http_info(club_tag, **kwargs)  # noqa: E501

    def get_club_members_with_http_info(self, club_tag, **kwargs):  # noqa: E501
        """Get members of a club  # noqa: E501

        Get information about the mmebers in a single club by club tag. Club tags can be found either in game or by from club member lists. Note that club tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_club_members_with_http_info(club_tag, async_req=True)
        >>> result = thread.get()

        :param club_tag: Tag of the club to retrieve.  (required)
        :type club_tag: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: tuple(ClubMemberList, status_code(int), headers(HTTPHeaderDict))
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
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_club_members" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'club_tag' is set
        if self.api_client.client_side_validation and ('club_tag' not in local_var_params or  # noqa: E501
                                                        local_var_params['club_tag'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `club_tag` when calling `get_club_members`")  # noqa: E501

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
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_ranking_brawlers(self, country_code, brawler_id, **kwargs):  # noqa: E501
        """Get brawler ranking for a country  # noqa: E501

        Get information about the ranking of brawlers in a single country.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ranking_brawlers(country_code, brawler_id, async_req=True)
        >>> result = thread.get()

        :param country_code: Country code of the country club list to retrieve.  (required)
        :type country_code: str
        :param brawler_id: Brawler ID of the brawler rank to retrieve.  (required)
        :type brawler_id: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: RankingBrawlerList
        """
        kwargs['_return_http_data_only'] = True
        return self.get_ranking_brawlers_with_http_info(country_code, brawler_id, **kwargs)  # noqa: E501

    def get_ranking_brawlers_with_http_info(self, country_code, brawler_id, **kwargs):  # noqa: E501
        """Get brawler ranking for a country  # noqa: E501

        Get information about the ranking of brawlers in a single country.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ranking_brawlers_with_http_info(country_code, brawler_id, async_req=True)
        >>> result = thread.get()

        :param country_code: Country code of the country club list to retrieve.  (required)
        :type country_code: str
        :param brawler_id: Brawler ID of the brawler rank to retrieve.  (required)
        :type brawler_id: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: tuple(RankingBrawlerList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'country_code',
            'brawler_id',
            'limit',
            'after',
            'before'
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
                    " to method get_ranking_brawlers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'country_code' is set
        if self.api_client.client_side_validation and ('country_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['country_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `country_code` when calling `get_ranking_brawlers`")  # noqa: E501
        # verify the required parameter 'brawler_id' is set
        if self.api_client.client_side_validation and ('brawler_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['brawler_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `brawler_id` when calling `get_ranking_brawlers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in local_var_params:
            path_params['countryCode'] = local_var_params['country_code']  # noqa: E501
        if 'brawler_id' in local_var_params:
            path_params['brawlerId'] = local_var_params['brawler_id']  # noqa: E501

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
            '/clubs/{countryCode}/brawlers/{brawlerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RankingBrawlerList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_ranking_clubs(self, country_code, **kwargs):  # noqa: E501
        """Get club ranking for a country  # noqa: E501

        Get information about the ranking of clubs in a single country.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ranking_clubs(country_code, async_req=True)
        >>> result = thread.get()

        :param country_code: Country code of the country club list to retrieve.  (required)
        :type country_code: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: RankingClubList
        """
        kwargs['_return_http_data_only'] = True
        return self.get_ranking_clubs_with_http_info(country_code, **kwargs)  # noqa: E501

    def get_ranking_clubs_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """Get club ranking for a country  # noqa: E501

        Get information about the ranking of clubs in a single country.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ranking_clubs_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param country_code: Country code of the country club list to retrieve.  (required)
        :type country_code: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: tuple(RankingClubList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'country_code',
            'limit',
            'after',
            'before'
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
                    " to method get_ranking_clubs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'country_code' is set
        if self.api_client.client_side_validation and ('country_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['country_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `country_code` when calling `get_ranking_clubs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in local_var_params:
            path_params['countryCode'] = local_var_params['country_code']  # noqa: E501

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
            '/clubs/{countryCode}/clubs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RankingClubList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_ranking_players(self, country_code, **kwargs):  # noqa: E501
        """Get player ranking for a country  # noqa: E501

        Get information about the ranking of players in a single country.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ranking_players(country_code, async_req=True)
        >>> result = thread.get()

        :param country_code: Country code of the country player list to retrieve.  (required)
        :type country_code: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: RankingPlayerList
        """
        kwargs['_return_http_data_only'] = True
        return self.get_ranking_players_with_http_info(country_code, **kwargs)  # noqa: E501

    def get_ranking_players_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """Get player ranking for a country  # noqa: E501

        Get information about the ranking of players in a single country.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ranking_players_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param country_code: Country code of the country player list to retrieve.  (required)
        :type country_code: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param after: Return only items that occur after this marker. After marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: int
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: int
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
        :rtype: tuple(RankingPlayerList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'country_code',
            'limit',
            'after',
            'before'
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
                    " to method get_ranking_players" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'country_code' is set
        if self.api_client.client_side_validation and ('country_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['country_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `country_code` when calling `get_ranking_players`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in local_var_params:
            path_params['countryCode'] = local_var_params['country_code']  # noqa: E501

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
            '/clubs/{countryCode}/players', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RankingPlayerList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
