# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccountTeamProjectArgs', 'AccountTeamProject']

@pulumi.input_type
class AccountTeamProjectArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 team_id: pulumi.Input[str],
                 project_name: Optional[pulumi.Input[str]] = None,
                 team_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccountTeamProject resource.
        :param pulumi.Input[str] account_id: The unique account id
        :param pulumi.Input[str] team_id: An account team id
        :param pulumi.Input[str] project_name: The name of an already existing project
        :param pulumi.Input[str] team_type: The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "team_id", team_id)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if team_type is not None:
            pulumi.set(__self__, "team_type", team_type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The unique account id
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        An account team id
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an already existing project
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="teamType")
    def team_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        return pulumi.get(self, "team_type")

    @team_type.setter
    def team_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_type", value)


@pulumi.input_type
class _AccountTeamProjectState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 team_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccountTeamProject resources.
        :param pulumi.Input[str] account_id: The unique account id
        :param pulumi.Input[str] project_name: The name of an already existing project
        :param pulumi.Input[str] team_id: An account team id
        :param pulumi.Input[str] team_type: The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if team_type is not None:
            pulumi.set(__self__, "team_type", team_type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique account id
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an already existing project
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        An account team id
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="teamType")
    def team_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        return pulumi.get(self, "team_type")

    @team_type.setter
    def team_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_type", value)


class AccountTeamProject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 team_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Account Team Project resource allows the creation and management of an Account Team Project.

        It is intended to link an existing project to the existing account team.
        It is important to note that the project should have an `account_id` property set equal to the
        account team you are trying to link to this project.

        ## Import

        ```sh
         $ pulumi import aiven:index/accountTeamProject:AccountTeamProject account_team_project1 account_id/team_id/project_name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The unique account id
        :param pulumi.Input[str] project_name: The name of an already existing project
        :param pulumi.Input[str] team_id: An account team id
        :param pulumi.Input[str] team_type: The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountTeamProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Account Team Project resource allows the creation and management of an Account Team Project.

        It is intended to link an existing project to the existing account team.
        It is important to note that the project should have an `account_id` property set equal to the
        account team you are trying to link to this project.

        ## Import

        ```sh
         $ pulumi import aiven:index/accountTeamProject:AccountTeamProject account_team_project1 account_id/team_id/project_name
        ```

        :param str resource_name: The name of the resource.
        :param AccountTeamProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountTeamProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 team_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountTeamProjectArgs.__new__(AccountTeamProjectArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["project_name"] = project_name
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["team_type"] = team_type
        super(AccountTeamProject, __self__).__init__(
            'aiven:index/accountTeamProject:AccountTeamProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            project_name: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            team_type: Optional[pulumi.Input[str]] = None) -> 'AccountTeamProject':
        """
        Get an existing AccountTeamProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The unique account id
        :param pulumi.Input[str] project_name: The name of an already existing project
        :param pulumi.Input[str] team_id: An account team id
        :param pulumi.Input[str] team_type: The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountTeamProjectState.__new__(_AccountTeamProjectState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["project_name"] = project_name
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["team_type"] = team_type
        return AccountTeamProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The unique account id
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an already existing project
        """
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        An account team id
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="teamType")
    def team_type(self) -> pulumi.Output[Optional[str]]:
        """
        The Account team project type The possible values are `admin`, `developer`, `operator` and `read_only`.
        """
        return pulumi.get(self, "team_type")

