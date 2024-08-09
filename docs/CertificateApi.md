# odin.CertificateApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_certificates_count_post**](CertificateApi.md#v1_certificates_count_post) | **POST** /v1/certificates/count | Get records count
[**v1_certificates_hash_get**](CertificateApi.md#v1_certificates_hash_get) | **GET** /v1/certificates/{hash} | Get the complete certificate
[**v1_certificates_scroll_next_post**](CertificateApi.md#v1_certificates_scroll_next_post) | **POST** /v1/certificates/scroll/next | Get the next batch of record
[**v1_certificates_scroll_post**](CertificateApi.md#v1_certificates_scroll_post) | **POST** /v1/certificates/scroll | Get the record based on query
[**v1_certificates_search_post**](CertificateApi.md#v1_certificates_search_post) | **POST** /v1/certificates/search | Search records
[**v1_certificates_summary_post**](CertificateApi.md#v1_certificates_summary_post) | **POST** /v1/certificates/summary | Get summary

# **v1_certificates_count_post**
> InlineResponse200 v1_certificates_count_post(body)

Get records count

Get total no of records based on query

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
api_instance = odin.CertificateApi(odin.ApiClient(configuration))
body = odin.CertificateCertCountRequest() # CertificateCertCountRequest | Count Query

try:
    # Get records count
    api_response = api_instance.v1_certificates_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->v1_certificates_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateCertCountRequest**](CertificateCertCountRequest.md)| Count Query |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_certificates_hash_get**
> CertificateCertificateHashResponse v1_certificates_hash_get(hash)

Get the complete certificate

Get the complete certificate based on provided hash

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
api_instance = odin.CertificateApi(odin.ApiClient(configuration))
hash = 'hash_example' # str | get the complete cert by hash

try:
    # Get the complete certificate
    api_response = api_instance.v1_certificates_hash_get(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->v1_certificates_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| get the complete cert by hash |

### Return type

[**CertificateCertificateHashResponse**](CertificateCertificateHashResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_certificates_scroll_next_post**
> InlineResponse2002 v1_certificates_scroll_next_post(body)

Get the next batch of record

Get the next batch of record based on query. It uses es scroll api for the pagination.

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
api_instance = odin.CertificateApi(odin.ApiClient(configuration))
body = odin.CertificateNextBatchRequest() # CertificateNextBatchRequest | Search Query

try:
    # Get the next batch of record
    api_response = api_instance.v1_certificates_scroll_next_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->v1_certificates_scroll_next_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateNextBatchRequest**](CertificateNextBatchRequest.md)| Search Query |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_certificates_scroll_post**
> InlineResponse2001 v1_certificates_scroll_post(body)

Get the record based on query

Get the record based on query. It uses es scroll api for the pagination.

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
api_instance = odin.CertificateApi(odin.ApiClient(configuration))
body = odin.CertificateCertScrollRequest() # CertificateCertScrollRequest | Search Query

try:
    # Get the record based on query
    api_response = api_instance.v1_certificates_scroll_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->v1_certificates_scroll_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateCertScrollRequest**](CertificateCertScrollRequest.md)| Search Query |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_certificates_search_post**
> CertificateCertificateSearchResponse v1_certificates_search_post(body)

Search records

Search record baseds based on the query

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
api_instance = odin.CertificateApi(odin.ApiClient(configuration))
body = odin.CertificateCertSearchRequest() # CertificateCertSearchRequest | Search Query

try:
    # Search records
    api_response = api_instance.v1_certificates_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->v1_certificates_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateCertSearchRequest**](CertificateCertSearchRequest.md)| Search Query |

### Return type

[**CertificateCertificateSearchResponse**](CertificateCertificateSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_certificates_summary_post**
> CertificateCertificateSummaryResponse v1_certificates_summary_post(body)

Get summary

Get summary of records based on the query

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
api_instance = odin.CertificateApi(odin.ApiClient(configuration))
body = odin.CertificateCertSummaryRequest() # CertificateCertSummaryRequest | Summary

try:
    # Get summary
    api_response = api_instance.v1_certificates_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->v1_certificates_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateCertSummaryRequest**](CertificateCertSummaryRequest.md)| Summary |

### Return type

[**CertificateCertificateSummaryResponse**](CertificateCertificateSummaryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

