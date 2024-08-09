# odin.ExposedFilesApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_exposed_files_count_post**](ExposedFilesApi.md#v1_exposed_files_count_post) | **POST** /v1/exposed/files/count | Get file count
[**v1_exposed_files_search_post**](ExposedFilesApi.md#v1_exposed_files_search_post) | **POST** /v1/exposed/files/search | Search exposed files
[**v1_exposed_files_summary_post**](ExposedFilesApi.md#v1_exposed_files_summary_post) | **POST** /v1/exposed/files/summary | Get file summary

# **v1_exposed_files_count_post**
> InlineResponse2009 v1_exposed_files_count_post(body)

Get file count

Returns overall count of exposed bucket files according to filters

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = odin.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = odin.ExposedFilesApi(odin.ApiClient(configuration))
body = odin.ExposedCountRequest() # ExposedCountRequest | Count Request

try:
    # Get file count
    api_response = api_instance.v1_exposed_files_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExposedFilesApi->v1_exposed_files_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExposedCountRequest**](ExposedCountRequest.md)| Count Request |

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_exposed_files_search_post**
> ExposedFileAPIResponse v1_exposed_files_search_post(body)

Search exposed files

Search exposed files using advanved filters Search across categories {img, aud, vid, font, txt, doc, src, db, march, arch, 3d, exec, key, cert} Search across labels {credential, financial, pii, legal, ip, medical, hr, report, confidential, backup, compromised, vulnerable} Search across providers {aws, gcp, do, linode}

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = odin.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = odin.ExposedFilesApi(odin.ApiClient(configuration))
body = odin.ExposedSearchRequest() # ExposedSearchRequest | Search Query

try:
    # Search exposed files
    api_response = api_instance.v1_exposed_files_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExposedFilesApi->v1_exposed_files_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExposedSearchRequest**](ExposedSearchRequest.md)| Search Query |

### Return type

[**ExposedFileAPIResponse**](ExposedFileAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_exposed_files_summary_post**
> InlineResponse20010 v1_exposed_files_summary_post(body)

Get file summary

Returns a summary of exposed bucket files according to provided filters

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = odin.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = odin.ExposedFilesApi(odin.ApiClient(configuration))
body = odin.ExposedSummaryRequest() # ExposedSummaryRequest | Summary Request

try:
    # Get file summary
    api_response = api_instance.v1_exposed_files_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExposedFilesApi->v1_exposed_files_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExposedSummaryRequest**](ExposedSummaryRequest.md)| Summary Request |

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

