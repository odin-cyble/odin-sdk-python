# odin.FieldsApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_fields_certificates_category_get**](FieldsApi.md#v1_fields_certificates_category_get) | **GET** /v1/fields/certificates/{category}/ | Get the fields for certificates
[**v1_fields_exposed_buckets_get**](FieldsApi.md#v1_fields_exposed_buckets_get) | **GET** /v1/fields/exposed/buckets/ | Get the fields for exposed
[**v1_fields_exposed_files_get**](FieldsApi.md#v1_fields_exposed_files_get) | **GET** /v1/fields/exposed/files/ | Get the fields data
[**v1_fields_hosts_category_get**](FieldsApi.md#v1_fields_hosts_category_get) | **GET** /v1/fields/hosts/{category}/ | Get the fields for hosts
[**v2_fields_hosts_category_get**](FieldsApi.md#v2_fields_hosts_category_get) | **GET** /v2/fields/hosts/{category}/ | Get the fields for hosts v2

# **v1_fields_certificates_category_get**
> InlineResponse20011 v1_fields_certificates_category_get(category)

Get the fields for certificates

Get the list of fields to query upon certificates

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.FieldsApi()
category = 'category_example' # str | get the category

try:
    # Get the fields for certificates
    api_response = api_instance.v1_fields_certificates_category_get(category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->v1_fields_certificates_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| get the category |

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_fields_exposed_buckets_get**
> InlineResponse20012 v1_fields_exposed_buckets_get()

Get the fields for exposed

Get the list of fields that can be used to query on exposed buckets and files

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.FieldsApi()

try:
    # Get the fields for exposed
    api_response = api_instance.v1_fields_exposed_buckets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->v1_fields_exposed_buckets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_fields_exposed_files_get**
> InlineResponse20012 v1_fields_exposed_files_get()

Get the fields data

Returns the fields data

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.FieldsApi()

try:
    # Get the fields data
    api_response = api_instance.v1_fields_exposed_files_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->v1_fields_exposed_files_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_fields_hosts_category_get**
> InlineResponse20011 v1_fields_hosts_category_get(category)

Get the fields for hosts

Get the list of fields to query on host

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.FieldsApi()
category = 'category_example' # str | get the category

try:
    # Get the fields for hosts
    api_response = api_instance.v1_fields_hosts_category_get(category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->v1_fields_hosts_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| get the category |

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_fields_hosts_category_get**
> InlineResponse20011 v2_fields_hosts_category_get(category)

Get the fields for hosts v2

Get the list of fields to query on hosts v2

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.FieldsApi()
category = 'category_example' # str | get the category

try:
    # Get the fields for hosts v2
    api_response = api_instance.v2_fields_hosts_category_get(category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->v2_fields_hosts_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| get the category |

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

