# ChangeAssignmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_ids** | **[str]** | The list of IDs of the statuses | [optional] 
**characteristic_types** | [**[CharacteristicTypeAssignmentReference]**](CharacteristicTypeAssignmentReference.md) | List of references to characteristic types corresponding to the assignment | [optional] 
**articulation_rules** | [**[ArticulationRuleRequest]**](ArticulationRuleRequest.md) | The articulation rule definitions | [optional] 
**validation_rule_ids** | **[str]** | The list of IDs of the validation rules | [optional] 
**data_quality_rule_ids** | **[str]** | The list of IDs of the data quality rules | [optional] 
**domain_type_ids** | **[str]** | The list of IDs of the domain types | [optional] 
**default_status_id** | **str** | The ID of the default status for the asset type | [optional] 
**scope_id** | **str** | The ID of the scope the assignment corresponds to. The scopeId will be removed in the future. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


