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
    'GetProjectUserResult',
    'AwaitableGetProjectUserResult',
    'get_project_user',
    'get_project_user_output',
]

@pulumi.output_type
class GetProjectUserResult:
    """
    A collection of values returned by getProjectUser.
    """
    def __init__(__self__, accepted=None, email=None, id=None, member_type=None, project=None):
        if accepted and not isinstance(accepted, bool):
            raise TypeError("Expected argument 'accepted' to be a bool")
        pulumi.set(__self__, "accepted", accepted)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_type and not isinstance(member_type, str):
            raise TypeError("Expected argument 'member_type' to be a str")
        pulumi.set(__self__, "member_type", member_type)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def accepted(self) -> bool:
        """
        Whether the user has accepted the request to join the project; adding user to a project sends an invitation to the target user and the actual membership is only created once the user accepts the invitation.
        """
        return pulumi.get(self, "accepted")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email address of the user. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> str:
        """
        Project membership type. The possible values are `admin`, `developer` and `operator`.
        """
        return pulumi.get(self, "member_type")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")


class AwaitableGetProjectUserResult(GetProjectUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectUserResult(
            accepted=self.accepted,
            email=self.email,
            id=self.id,
            member_type=self.member_type,
            project=self.project)


def get_project_user(email: Optional[str] = None,
                     project: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectUserResult:
    """
    The Project User data source provides information about the existing Aiven Project User.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mytestuser = aiven.get_project_user(project=aiven_project["myproject"]["project"],
        email="john.doe@example.com")
    ```


    :param str email: Email address of the user. This property cannot be changed, doing so forces recreation of the resource.
    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    __args__ = dict()
    __args__['email'] = email
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getProjectUser:getProjectUser', __args__, opts=opts, typ=GetProjectUserResult).value

    return AwaitableGetProjectUserResult(
        accepted=__ret__.accepted,
        email=__ret__.email,
        id=__ret__.id,
        member_type=__ret__.member_type,
        project=__ret__.project)


@_utilities.lift_output_func(get_project_user)
def get_project_user_output(email: Optional[pulumi.Input[str]] = None,
                            project: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectUserResult]:
    """
    The Project User data source provides information about the existing Aiven Project User.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mytestuser = aiven.get_project_user(project=aiven_project["myproject"]["project"],
        email="john.doe@example.com")
    ```


    :param str email: Email address of the user. This property cannot be changed, doing so forces recreation of the resource.
    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    ...
