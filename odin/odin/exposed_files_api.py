# coding: utf-8

"""
    Odin

    ODIN APIs to search across IP Services, CVEs, Certificates, Exposed Files/Buckets, Domains and more  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from odin.api_client import ApiClient


class ExposedFilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_exposed_files_count_post(self, body, **kwargs):  # noqa: E501
        """Get file count  # noqa: E501

        Returns overall count of exposed bucket files according to filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_exposed_files_count_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExposedCountRequest body: Count Request (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_exposed_files_count_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_exposed_files_count_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_exposed_files_count_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get file count  # noqa: E501

        Returns overall count of exposed bucket files according to filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_exposed_files_count_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExposedCountRequest body: Count Request (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_exposed_files_count_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_exposed_files_count_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/exposed/files/count', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_exposed_files_search_post(self, body, **kwargs):  # noqa: E501
        """Search exposed files  # noqa: E501

        Search exposed files using advanved filters Search across categories {img, aud, vid, font, txt, doc, src, db, march, arch, 3d, exec, key, cert} Search across labels {credential, financial, pii, legal, ip, medical, hr, report, confidential, backup, compromised, vulnerable} Search across providers {aws, gcp, do, linode}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_exposed_files_search_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExposedSearchRequest body: Search Query (required)
        :return: ExposedFileAPIResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_exposed_files_search_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_exposed_files_search_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_exposed_files_search_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search exposed files  # noqa: E501

        Search exposed files using advanved filters Search across categories {img, aud, vid, font, txt, doc, src, db, march, arch, 3d, exec, key, cert} Search across labels {credential, financial, pii, legal, ip, medical, hr, report, confidential, backup, compromised, vulnerable} Search across providers {aws, gcp, do, linode}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_exposed_files_search_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExposedSearchRequest body: Search Query (required)
        :return: ExposedFileAPIResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_exposed_files_search_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_exposed_files_search_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/exposed/files/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExposedFileAPIResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_exposed_files_summary_post(self, body, **kwargs):  # noqa: E501
        """Get file summary  # noqa: E501

        Returns a summary of exposed bucket files according to provided filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_exposed_files_summary_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExposedSummaryRequest body: Summary Request (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_exposed_files_summary_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_exposed_files_summary_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_exposed_files_summary_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get file summary  # noqa: E501

        Returns a summary of exposed bucket files according to provided filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_exposed_files_summary_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExposedSummaryRequest body: Summary Request (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_exposed_files_summary_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_exposed_files_summary_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/exposed/files/summary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
