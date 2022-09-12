# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetKafkaSchemaRegistryAclResult',
    'AwaitableGetKafkaSchemaRegistryAclResult',
    'get_kafka_schema_registry_acl',
    'get_kafka_schema_registry_acl_output',
]

@pulumi.output_type
class GetKafkaSchemaRegistryAclResult:
    """
    A collection of values returned by getKafkaSchemaRegistryAcl.
    """
    def __init__(__self__, acl_id=None, id=None, permission=None, project=None, resource=None, service_name=None, username=None):
        if acl_id and not isinstance(acl_id, str):
            raise TypeError("Expected argument 'acl_id' to be a str")
        pulumi.set(__self__, "acl_id", acl_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if permission and not isinstance(permission, str):
            raise TypeError("Expected argument 'permission' to be a str")
        pulumi.set(__self__, "permission", permission)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if resource and not isinstance(resource, str):
            raise TypeError("Expected argument 'resource' to be a str")
        pulumi.set(__self__, "resource", resource)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> str:
        """
        Kafka Schema Registry ACL ID
        """
        return pulumi.get(self, "acl_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def permission(self) -> str:
        """
        Kafka Schema Registry permission to grant. The possible values are `schema_registry_read` and `schema_registry_write`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        Resource name pattern for the Schema Registry ACL entry. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Username pattern for the ACL entry. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")


class AwaitableGetKafkaSchemaRegistryAclResult(GetKafkaSchemaRegistryAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaSchemaRegistryAclResult(
            acl_id=self.acl_id,
            id=self.id,
            permission=self.permission,
            project=self.project,
            resource=self.resource,
            service_name=self.service_name,
            username=self.username)


def get_kafka_schema_registry_acl(permission: Optional[str] = None,
                                  project: Optional[str] = None,
                                  resource: Optional[str] = None,
                                  service_name: Optional[str] = None,
                                  username: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaSchemaRegistryAclResult:
    """
    The Data Source Kafka Schema Registry ACL data source provides information about the existing Aiven Kafka Schema Registry ACL for a Kafka service.


    :param str permission: Kafka Schema Registry permission to grant. The possible values are `schema_registry_read` and `schema_registry_write`. This property cannot be changed, doing so forces recreation of the resource.
    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str resource: Resource name pattern for the Schema Registry ACL entry. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str username: Username pattern for the ACL entry. This property cannot be changed, doing so forces recreation of the resource.
    """
    __args__ = dict()
    __args__['permission'] = permission
    __args__['project'] = project
    __args__['resource'] = resource
    __args__['serviceName'] = service_name
    __args__['username'] = username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getKafkaSchemaRegistryAcl:getKafkaSchemaRegistryAcl', __args__, opts=opts, typ=GetKafkaSchemaRegistryAclResult).value

    return AwaitableGetKafkaSchemaRegistryAclResult(
        acl_id=__ret__.acl_id,
        id=__ret__.id,
        permission=__ret__.permission,
        project=__ret__.project,
        resource=__ret__.resource,
        service_name=__ret__.service_name,
        username=__ret__.username)


@_utilities.lift_output_func(get_kafka_schema_registry_acl)
def get_kafka_schema_registry_acl_output(permission: Optional[pulumi.Input[str]] = None,
                                         project: Optional[pulumi.Input[str]] = None,
                                         resource: Optional[pulumi.Input[str]] = None,
                                         service_name: Optional[pulumi.Input[str]] = None,
                                         username: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaSchemaRegistryAclResult]:
    """
    The Data Source Kafka Schema Registry ACL data source provides information about the existing Aiven Kafka Schema Registry ACL for a Kafka service.


    :param str permission: Kafka Schema Registry permission to grant. The possible values are `schema_registry_read` and `schema_registry_write`. This property cannot be changed, doing so forces recreation of the resource.
    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str resource: Resource name pattern for the Schema Registry ACL entry. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str username: Username pattern for the ACL entry. This property cannot be changed, doing so forces recreation of the resource.
    """
    ...
