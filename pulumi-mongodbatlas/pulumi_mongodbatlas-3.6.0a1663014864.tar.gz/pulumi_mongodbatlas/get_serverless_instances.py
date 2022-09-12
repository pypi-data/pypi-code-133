# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetServerlessInstancesResult',
    'AwaitableGetServerlessInstancesResult',
    'get_serverless_instances',
    'get_serverless_instances_output',
]

@pulumi.output_type
class GetServerlessInstancesResult:
    """
    A collection of values returned by getServerlessInstances.
    """
    def __init__(__self__, id=None, project_id=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetServerlessInstancesResultResult']:
        """
        A list where each represents a search index.
        """
        return pulumi.get(self, "results")


class AwaitableGetServerlessInstancesResult(GetServerlessInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerlessInstancesResult(
            id=self.id,
            project_id=self.project_id,
            results=self.results)


def get_serverless_instances(project_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerlessInstancesResult:
    """
    `get_serverless_instances` describe all serverless instances. This represents serverless instances that have been created for the specified group id.

    > **NOTE:**  Serverless instances do not support some Atlas features at this time.
    For a full list of unsupported features, see [Serverless Instance Limitations](https://docs.atlas.mongodb.com/reference/serverless-instance-limitations/).

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    data_serverless = mongodbatlas.get_serverless_instances(project_id="<PROJECT_ID")
    ```


    :param str project_id: Unique identifier for the [project](https://docs.atlas.mongodb.com/organizations-projects/#std-label-projects) that contains the specified cluster.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getServerlessInstances:getServerlessInstances', __args__, opts=opts, typ=GetServerlessInstancesResult).value

    return AwaitableGetServerlessInstancesResult(
        id=__ret__.id,
        project_id=__ret__.project_id,
        results=__ret__.results)


@_utilities.lift_output_func(get_serverless_instances)
def get_serverless_instances_output(project_id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerlessInstancesResult]:
    """
    `get_serverless_instances` describe all serverless instances. This represents serverless instances that have been created for the specified group id.

    > **NOTE:**  Serverless instances do not support some Atlas features at this time.
    For a full list of unsupported features, see [Serverless Instance Limitations](https://docs.atlas.mongodb.com/reference/serverless-instance-limitations/).

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    data_serverless = mongodbatlas.get_serverless_instances(project_id="<PROJECT_ID")
    ```


    :param str project_id: Unique identifier for the [project](https://docs.atlas.mongodb.com/organizations-projects/#std-label-projects) that contains the specified cluster.
    """
    ...
