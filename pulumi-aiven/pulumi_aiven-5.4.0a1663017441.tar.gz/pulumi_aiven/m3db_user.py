# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['M3dbUserArgs', 'M3dbUser']

@pulumi.input_type
class M3dbUserArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 username: pulumi.Input[str],
                 password: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a M3dbUser resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] username: The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] password: The password of the M3DB User.
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "username", username)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the M3DB User.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class _M3dbUserState:
    def __init__(__self__, *,
                 password: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering M3dbUser resources.
        :param pulumi.Input[str] password: The password of the M3DB User.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] type: Type of the user account. Tells whether the user is the primary account or a regular account.
        :param pulumi.Input[str] username: The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        if password is not None:
            pulumi.set(__self__, "password", password)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the M3DB User.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the user account. Tells whether the user is the primary account or a regular account.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class M3dbUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The M3DB User resource allows the creation and management of Aiven M3DB Users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        foo = aiven.M3dbUser("foo",
            service_name=aiven_m3db["bar"]["service_name"],
            project="my-project",
            username="user-1",
            password="Test$1234")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] password: The password of the M3DB User.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] username: The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: M3dbUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The M3DB User resource allows the creation and management of Aiven M3DB Users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        foo = aiven.M3dbUser("foo",
            service_name=aiven_m3db["bar"]["service_name"],
            project="my-project",
            username="user-1",
            password="Test$1234")
        ```

        :param str resource_name: The name of the resource.
        :param M3dbUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(M3dbUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = M3dbUserArgs.__new__(M3dbUserArgs)

            __props__.__dict__["password"] = password
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["type"] = None
        super(M3dbUser, __self__).__init__(
            'aiven:index/m3dbUser:M3dbUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            password: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'M3dbUser':
        """
        Get an existing M3dbUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] password: The password of the M3DB User.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] type: Type of the user account. Tells whether the user is the primary account or a regular account.
        :param pulumi.Input[str] username: The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _M3dbUserState.__new__(_M3dbUserState)

        __props__.__dict__["password"] = password
        __props__.__dict__["project"] = project
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["type"] = type
        __props__.__dict__["username"] = username
        return M3dbUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password of the M3DB User.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the user account. Tells whether the user is the primary account or a regular account.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The actual name of the M3DB User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")

