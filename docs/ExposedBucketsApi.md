# odin.ExposedBucketsApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_exposed_buckets_count_post**](ExposedBucketsApi.md#v1_exposed_buckets_count_post) | **POST** /v1/exposed/buckets/count | Get exposed bucket count
[**v1_exposed_buckets_search_post**](ExposedBucketsApi.md#v1_exposed_buckets_search_post) | **POST** /v1/exposed/buckets/search | Search exposed buckets
[**v1_exposed_buckets_summary_post**](ExposedBucketsApi.md#v1_exposed_buckets_summary_post) | **POST** /v1/exposed/buckets/summary | Get Exposed buckets summary

# **v1_exposed_buckets_count_post**
> InlineResponse2009 v1_exposed_buckets_count_post(body)

Get exposed bucket count

Get exposed bucket count according to provided filters

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
api_instance = odin.ExposedBucketsApi(odin.ApiClient(configuration))
body = odin.ExposedCountRequest() # ExposedCountRequest | Count Request

try:
    # Get exposed bucket count
    api_response = api_instance.v1_exposed_buckets_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExposedBucketsApi->v1_exposed_buckets_count_post: %s\n" % e)
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

# **v1_exposed_buckets_search_post**
> ExposedBucketAPIResponse v1_exposed_buckets_search_post(body)

Search exposed buckets

Search exposed buckets according to provided filters Search across categories {img, aud, vid, font, doc, src, web, bkup, dbdump} Search across labels {credential, financial, pii, legal, ip, medical, hr, report, confidential, backup, compromised, vulnerable} Search across providers {aws, gcp, do, linode}

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
api_instance = odin.ExposedBucketsApi(odin.ApiClient(configuration))
body = odin.ExposedSearchRequest() # ExposedSearchRequest | Search Query

try:
    # Search exposed buckets
    api_response = api_instance.v1_exposed_buckets_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExposedBucketsApi->v1_exposed_buckets_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExposedSearchRequest**](ExposedSearchRequest.md)| Search Query |

### Return type

[**ExposedBucketAPIResponse**](ExposedBucketAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_exposed_buckets_summary_post**
> InlineResponse20010 v1_exposed_buckets_summary_post(body)

Get Exposed buckets summary

Get Returns exposed buckets aggregated count according to filters

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
api_instance = odin.ExposedBucketsApi(odin.ApiClient(configuration))
body = odin.ExposedSummaryRequest() # ExposedSummaryRequest | Summary Request

try:
    # Get Exposed buckets summary
    api_response = api_instance.v1_exposed_buckets_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExposedBucketsApi->v1_exposed_buckets_summary_post: %s\n" % e)
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

