# coding: utf-8

"""
    Ring-Moon Systems OpenAPI

    This is a simple API wrapping the OPUS API of the PDS Ring-Moon Systems node.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: kmichael.aye@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def metadata_v2_opus_id_json_get(self, opus_id, **kwargs):  # noqa: E501
        """metadata_v2_opus_id_json_get  # noqa: E501

        Get all available, or particular, metadata for a single observation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metadata_v2_opus_id_json_get(opus_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str opus_id: valid opus_id (or old ring_obs_id) (required)
        :param list[str] cols: one or more column names
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.metadata_v2_opus_id_json_get_with_http_info(opus_id, **kwargs)  # noqa: E501
        else:
            (data) = self.metadata_v2_opus_id_json_get_with_http_info(opus_id, **kwargs)  # noqa: E501
            return data

    def metadata_v2_opus_id_json_get_with_http_info(self, opus_id, **kwargs):  # noqa: E501
        """metadata_v2_opus_id_json_get  # noqa: E501

        Get all available, or particular, metadata for a single observation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metadata_v2_opus_id_json_get_with_http_info(opus_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str opus_id: valid opus_id (or old ring_obs_id) (required)
        :param list[str] cols: one or more column names
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['opus_id', 'cols']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method metadata_v2_opus_id_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'opus_id' is set
        if ('opus_id' not in params or
                params['opus_id'] is None):
            raise ValueError("Missing the required parameter `opus_id` when calling `metadata_v2_opus_id_json_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'opus_id' in params:
            path_params['opus_id'] = params['opus_id']  # noqa: E501

        query_params = []
        if 'cols' in params:
            query_params.append(('cols', params['cols']))  # noqa: E501
            collection_formats['cols'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/metadata_v2/{opus_id}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)