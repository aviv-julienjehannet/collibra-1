# JdbcDriver

The list of results.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the represented object (entity). | 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]. | 
**created_by** | **str** | The id of the user that created this resource. | [optional] 
**created_on** | **int** | The timestamp (in UTC time standard) of the creation of this resource. | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time. | [optional] 
**last_modified_on** | **int** | The timestamp (in UTC time standard) of the last modification of this resource. | [optional] 
**system** | **bool** | Whether this is a system resource or not. | [optional] 
**database_name** | **str** |  | [optional] 
**database_version** | **str** |  | [optional] 
**driver** | **str** |  | [optional] 
**connection_string** | **str** |  | [optional] 
**jdbc_driver_files** | [**[JdbcDriverFile]**](JdbcDriverFile.md) |  | [optional] 
**connection_string_parameters** | [**[ConnectionStringParameter]**](ConnectionStringParameter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


