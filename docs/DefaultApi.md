# swagger_client.DefaultApi

All URIs are relative to *https://tools.pds-rings.seti.org/opus/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_v2_opus_id_json_get**](DefaultApi.md#metadata_v2_opus_id_json_get) | **GET** /metadata_v2/{opus_id}.json | 

# **metadata_v2_opus_id_json_get**
> object metadata_v2_opus_id_json_get(opus_id, cols=cols)



Get all available, or particular, metadata for a single observation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
opus_id = 'opus_id_example' # str | valid opus_id (or old ring_obs_id)
cols = ['cols_example'] # list[str] | one or more column names (optional)

try:
    api_response = api_instance.metadata_v2_opus_id_json_get(opus_id, cols=cols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->metadata_v2_opus_id_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opus_id** | **str**| valid opus_id (or old ring_obs_id) | 
 **cols** | [**list[str]**](str.md)| one or more column names | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

