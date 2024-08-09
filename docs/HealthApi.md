# odin.HealthApi

All URIs are relative to *https://api.odin.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ping_get**](HealthApi.md#v1_ping_get) | **GET** /v1/ping | Health Check

# **v1_ping_get**
> str v1_ping_get()

Health Check

Returns the pong as response

### Example
```python
from __future__ import print_function
import time
import odin
from odin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = odin.HealthApi()

try:
    # Health Check
    api_response = api_instance.v1_ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->v1_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

