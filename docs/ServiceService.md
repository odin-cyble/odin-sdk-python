# ServiceService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ServiceIPServiceMeta**](ServiceIPServiceMeta.md) |  | [optional] 
**asn** | [**ServiceIPASN**](ServiceIPASN.md) |  | [optional] 
**asn_updated_at** | **str** |  | [optional] 
**banners** | **list[str]** |  | [optional] 
**cve** | [**list[ServiceFullCveData]**](ServiceFullCveData.md) |  | [optional] 
**domains** | [**list[ServiceIPDomain]**](ServiceIPDomain.md) |  | [optional] 
**extra_info** | **str** |  | [optional] 
**hostnames** | [**list[ServiceIPHostname]**](ServiceIPHostname.md) |  | [optional] 
**ip** | **str** |  | [optional] 
**is_ipv4** | **bool** |  | [optional] 
**is_ipv6** | **bool** |  | [optional] 
**is_vuln** | **bool** |  | [optional] 
**last_updated_at** | **str** |  | [optional] 
**location** | [**ServiceIPLocation**](ServiceIPLocation.md) |  | [optional] 
**location_updated_at** | **str** |  | [optional] 
**modules** | **dict(str, object)** | services.tls -&gt; services.modules.tls key names - if you mess up the key names | [optional] 
**name** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**product** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**scan_id** | **int** |  | [optional] 
**softwares** | [**list[ServiceIPServiceSoftware]**](ServiceIPServiceSoftware.md) |  | [optional] 
**tags** | [**list[ServiceIPTag]**](ServiceIPTag.md) |  | [optional] 
**tunnel** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**whois** | [**ServiceIPWhois**](ServiceIPWhois.md) |  | [optional] 
**whois_updated_at** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

