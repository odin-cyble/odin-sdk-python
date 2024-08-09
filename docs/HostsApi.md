# odin.HostsApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cves_all_ip_page_get**](HostsApi.md#v1_cves_all_ip_page_get) | **GET** /v1/cves/all/{ip}/{page} | Get cve details
[**v1_hosts_count_post**](HostsApi.md#v1_hosts_count_post) | **POST** /v1/hosts/count | Get the record count
[**v1_hosts_cve_ip_get**](HostsApi.md#v1_hosts_cve_ip_get) | **GET** /v1/hosts/cve/{ip}/ | Get ip cve details
[**v1_hosts_cves_ip_cve_get**](HostsApi.md#v1_hosts_cves_ip_cve_get) | **GET** /v1/hosts/cves/{ip}/{cve} | Get cve
[**v1_hosts_exploits_ip_cve_get**](HostsApi.md#v1_hosts_exploits_ip_cve_get) | **GET** /v1/hosts/exploits/{ip}/{cve} | Get exploits for ip and cve
[**v1_hosts_exploits_ip_get**](HostsApi.md#v1_hosts_exploits_ip_get) | **GET** /v1/hosts/exploits/{ip}/ | Get exploits for ip
[**v1_hosts_ip_get**](HostsApi.md#v1_hosts_ip_get) | **GET** /v1/hosts/{ip}/ | Get the latest ip details
[**v1_hosts_search_post**](HostsApi.md#v1_hosts_search_post) | **POST** /v1/hosts/search | Search hosts
[**v1_hosts_summary_post**](HostsApi.md#v1_hosts_summary_post) | **POST** /v1/hosts/summary | Get summary
[**v2_hosts_count_post**](HostsApi.md#v2_hosts_count_post) | **POST** /v2/hosts/count | Fetch the record count
[**v2_hosts_ip_post**](HostsApi.md#v2_hosts_ip_post) | **POST** /v2/hosts/{ip} | Fetch the latest ip details
[**v2_hosts_search_post**](HostsApi.md#v2_hosts_search_post) | **POST** /v2/hosts/search | Fetch the record based on query
[**v2_hosts_summary_post**](HostsApi.md#v2_hosts_summary_post) | **POST** /v2/hosts/summary | Create the summary of the field based on query

# **v1_cves_all_ip_page_get**
> IpservicesIpCveResponse v1_cves_all_ip_page_get(ip, page)

Get cve details

Get the detailed cve details for ip based on page

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | get the ip
page = 'page_example' # str | get the page

try:
    # Get cve details
    api_response = api_instance.v1_cves_all_ip_page_get(ip, page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_cves_all_ip_page_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| get the ip |
 **page** | **str**| get the page |

### Return type

[**IpservicesIpCveResponse**](IpservicesIpCveResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_count_post**
> InlineResponse20013 v1_hosts_count_post(body)

Get the record count

Returns the total no of records based on query

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
body = odin.CountRequest() # CountRequest | Count Query

try:
    # Get the record count
    api_response = api_instance.v1_hosts_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CountRequest**](CountRequest.md)| Count Query |

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_cve_ip_get**
> IpservicesIpCveResponse v1_hosts_cve_ip_get(ip)

Get ip cve details

Get detailed lost of cve ips

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | get the ip

try:
    # Get ip cve details
    api_response = api_instance.v1_hosts_cve_ip_get(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_cve_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| get the ip |

### Return type

[**IpservicesIpCveResponse**](IpservicesIpCveResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_cves_ip_cve_get**
> IpservicesIpCveResponse v1_hosts_cves_ip_cve_get(ip, cve)

Get cve

Get the detailed cve based on ip and cve

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | host ip ip
cve = 'cve_example' # str | cve id

try:
    # Get cve
    api_response = api_instance.v1_hosts_cves_ip_cve_get(ip, cve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_cves_ip_cve_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| host ip ip |
 **cve** | **str**| cve id |

### Return type

[**IpservicesIpCveResponse**](IpservicesIpCveResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_exploits_ip_cve_get**
> InlineResponse20014 v1_hosts_exploits_ip_cve_get(ip, cve)

Get exploits for ip and cve

Get the detailed exploit details for ip and cve

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | ip address of the host
cve = 'cve_example' # str | cve id

try:
    # Get exploits for ip and cve
    api_response = api_instance.v1_hosts_exploits_ip_cve_get(ip, cve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_exploits_ip_cve_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| ip address of the host |
 **cve** | **str**| cve id |

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_exploits_ip_get**
> IpservicesIpCveResponse v1_hosts_exploits_ip_get(ip)

Get exploits for ip

Get the detailed list of exploits for the ip

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | get the ip

try:
    # Get exploits for ip
    api_response = api_instance.v1_hosts_exploits_ip_get(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_exploits_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| get the ip |

### Return type

[**IpservicesIpCveResponse**](IpservicesIpCveResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_ip_get**
> InlineResponse20016 v1_hosts_ip_get(ip)

Get the latest ip details

Get the complete and latest ip details

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | get the ip

try:
    # Get the latest ip details
    api_response = api_instance.v1_hosts_ip_get(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| get the ip |

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_search_post**
> InlineResponse20015 v1_hosts_search_post(body)

Search hosts

Get the detailed list of hosts based on query

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
body = odin.SearchRequest() # SearchRequest | Search Query

try:
    # Search hosts
    api_response = api_instance.v1_hosts_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| Search Query |

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hosts_summary_post**
> IpservicesHostsSummaryResponse v1_hosts_summary_post(body)

Get summary

Get the summary of hosts based on the field

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
body = odin.SummaryRequest() # SummaryRequest | Summary

try:
    # Get summary
    api_response = api_instance.v1_hosts_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v1_hosts_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SummaryRequest**](SummaryRequest.md)| Summary |

### Return type

[**IpservicesHostsSummaryResponse**](IpservicesHostsSummaryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_hosts_count_post**
> InlineResponse20017 v2_hosts_count_post(body)

Fetch the record count

Returns the total no of records based on query

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
body = odin.CybleComOdinApiControllersV2IpservicesCountRequest() # CybleComOdinApiControllersV2IpservicesCountRequest | Count Query

try:
    # Fetch the record count
    api_response = api_instance.v2_hosts_count_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v2_hosts_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CybleComOdinApiControllersV2IpservicesCountRequest**](CybleComOdinApiControllersV2IpservicesCountRequest.md)| Count Query |

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_hosts_ip_post**
> CybleComOdinApiControllersV2IpservicesAPIResponse v2_hosts_ip_post(ip)

Fetch the latest ip details

Returns the complete ip details

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
ip = 'ip_example' # str | get the ip

try:
    # Fetch the latest ip details
    api_response = api_instance.v2_hosts_ip_post(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v2_hosts_ip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| get the ip |

### Return type

[**CybleComOdinApiControllersV2IpservicesAPIResponse**](CybleComOdinApiControllersV2IpservicesAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_hosts_search_post**
> InlineResponse20018 v2_hosts_search_post(body)

Fetch the record based on query

Returns the record based on query and blank query will return all records. It uses es searchafter for the pagination.

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
body = odin.CybleComOdinApiControllersV2IpservicesSearchRequest() # CybleComOdinApiControllersV2IpservicesSearchRequest | Search Query

try:
    # Fetch the record based on query
    api_response = api_instance.v2_hosts_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v2_hosts_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CybleComOdinApiControllersV2IpservicesSearchRequest**](CybleComOdinApiControllersV2IpservicesSearchRequest.md)| Search Query |

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_hosts_summary_post**
> InlineResponse20019 v2_hosts_summary_post(body)

Create the summary of the field based on query

Returns the summary of the field based on query

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
api_instance = odin.HostsApi(odin.ApiClient(configuration))
body = odin.CybleComOdinApiControllersV2IpservicesSummaryRequest() # CybleComOdinApiControllersV2IpservicesSummaryRequest | Summary

try:
    # Create the summary of the field based on query
    api_response = api_instance.v2_hosts_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->v2_hosts_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CybleComOdinApiControllersV2IpservicesSummaryRequest**](CybleComOdinApiControllersV2IpservicesSummaryRequest.md)| Summary |

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

