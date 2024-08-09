# odin.DomainApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_domain_count_post**](DomainApi.md#v1_domain_count_post) | **POST** /v1/domain/count | Get domains count
[**v1_domain_search_post**](DomainApi.md#v1_domain_search_post) | **POST** /v1/domain/search | Search domains
[**v1_domain_subdomain_count_post**](DomainApi.md#v1_domain_subdomain_count_post) | **POST** /v1/domain/subdomain/count | Fetch the total no. of subdomain records
[**v1_domain_subdomain_search_post**](DomainApi.md#v1_domain_subdomain_search_post) | **POST** /v1/domain/subdomain/search | Fetch the subdomain record
[**v1_domain_whois_domain_name_get**](DomainApi.md#v1_domain_whois_domain_name_get) | **GET** /v1/domain/whois/{domain-name} | Fetch the domain whois record details
[**v1_domain_whois_domain_name_historical_get**](DomainApi.md#v1_domain_whois_domain_name_historical_get) | **GET** /v1/domain/whois/{domain-name}/historical | Fetch all the domain whois historical records
[**v1_domain_whois_domain_name_is_expired_get**](DomainApi.md#v1_domain_whois_domain_name_is_expired_get) | **GET** /v1/domain/whois/{domain-name}/is-expired | Get the expiry for a particular domain
[**v1_domain_whois_domain_name_is_registered_get**](DomainApi.md#v1_domain_whois_domain_name_is_registered_get) | **GET** /v1/domain/whois/{domain-name}/is-registered | Fetch all the domain whois historical records

# **v1_domain_count_post**
> InlineResponse2003 v1_domain_count_post(body)

Get domains count

Get count of domain records based on query

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.DomainApi()
body = odin.DnsDNSCountRequest() # DnsDNSCountRequest | Query

try:
    # Get domains count
    api_response = api_instance.v1_domain_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsDNSCountRequest**](DnsDNSCountRequest.md)| Query |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_search_post**
> InlineResponse2004 v1_domain_search_post(body)

Search domains

Search domains based on the query

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.DomainApi()
body = odin.DnsDomainRequest() # DnsDomainRequest | Query

try:
    # Search domains
    api_response = api_instance.v1_domain_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsDomainRequest**](DnsDomainRequest.md)| Query |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_subdomain_count_post**
> InlineResponse2003 v1_domain_subdomain_count_post(body)

Fetch the total no. of subdomain records

Returns the count of subdomain records based on domain

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
api_instance = odin.DomainApi(odin.ApiClient(configuration))
body = odin.DnsDNSCountRequest() # DnsDNSCountRequest | Query

try:
    # Fetch the total no. of subdomain records
    api_response = api_instance.v1_domain_subdomain_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_subdomain_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsDNSCountRequest**](DnsDNSCountRequest.md)| Query |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_subdomain_search_post**
> InlineResponse2005 v1_domain_subdomain_search_post(body)

Fetch the subdomain record

Returns the subdomain records based on query

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
api_instance = odin.DomainApi(odin.ApiClient(configuration))
body = odin.DnsDomainRequest() # DnsDomainRequest | Query

try:
    # Fetch the subdomain record
    api_response = api_instance.v1_domain_subdomain_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_subdomain_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsDomainRequest**](DnsDomainRequest.md)| Query |

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_whois_domain_name_get**
> InlineResponse2006 v1_domain_whois_domain_name_get(domain_name)

Fetch the domain whois record details

Provides extensive details about the domain whois record like name servers, domain status, registrar, etc.

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
api_instance = odin.DomainApi(odin.ApiClient(configuration))
domain_name = 'domain_name_example' # str | domain

try:
    # Fetch the domain whois record details
    api_response = api_instance.v1_domain_whois_domain_name_get(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_whois_domain_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_whois_domain_name_historical_get**
> InlineResponse2007 v1_domain_whois_domain_name_historical_get(domain_name)

Fetch all the domain whois historical records

Provides historical details about the domain whois record like name servers, domain status, registrar, etc

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
api_instance = odin.DomainApi(odin.ApiClient(configuration))
domain_name = 'domain_name_example' # str | domain

try:
    # Fetch all the domain whois historical records
    api_response = api_instance.v1_domain_whois_domain_name_historical_get(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_whois_domain_name_historical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_whois_domain_name_is_expired_get**
> InlineResponse2008 v1_domain_whois_domain_name_is_expired_get(domain_name)

Get the expiry for a particular domain

Provides historical details about the domain whois record like name servers, domain status, registrar, etc

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
api_instance = odin.DomainApi(odin.ApiClient(configuration))
domain_name = 'domain_name_example' # str | domain

try:
    # Get the expiry for a particular domain
    api_response = api_instance.v1_domain_whois_domain_name_is_expired_get(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_whois_domain_name_is_expired_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain |

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domain_whois_domain_name_is_registered_get**
> InlineResponse2008 v1_domain_whois_domain_name_is_registered_get(domain_name)

Fetch all the domain whois historical records

Provides historical details about the domain whois record like name servers, domain status, registrar, etc

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
api_instance = odin.DomainApi(odin.ApiClient(configuration))
domain_name = 'domain_name_example' # str | domain

try:
    # Fetch all the domain whois historical records
    api_response = api_instance.v1_domain_whois_domain_name_is_registered_get(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_domain_whois_domain_name_is_registered_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain |

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

