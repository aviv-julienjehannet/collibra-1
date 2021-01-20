# AddComplexRelationTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new complex relation type. Should be unique within all complex relation types. | 
**symbol_type** | **str** | The symbol type. | 
**attribute_types** | [**[ComplexRelationAttributeTypeRequest]**](ComplexRelationAttributeTypeRequest.md) | The list of attribute types for the new complex relation type. | 
**leg_types** | [**[ComplexRelationLegTypeRequest]**](ComplexRelationLegTypeRequest.md) | The list of leg types for the new complex relation type. | 
**id** | **str** | The ID of the new complex relation type. Should be unique within all complex relation types.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**description** | **str** | The description of the new complex relation type. | [optional] 
**color** | **str** | The color of the symbol, in a hex format e.g. &#39;#000000&#39;.  This format always includes the &#39;#&#39; and has a size of 7. | [optional] 
**icon_code** | **str** | The icon code of the new complex relation type. | [optional] 
**acronym_code** | **str** | The acronym code of the new complex relation type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


