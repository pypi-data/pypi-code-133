# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ServiceUserArgs', 'ServiceUser']

@pulumi.input_type
class ServiceUserArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 username: pulumi.Input[str],
                 authentication: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pg_allow_replication: Optional[pulumi.Input[bool]] = None,
                 redis_acl_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_commands: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServiceUser resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] username: The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] authentication: Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        :param pulumi.Input[str] password: The password of the service user ( not applicable for all services ).
        :param pulumi.Input[bool] pg_allow_replication: Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_categories: Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_channels: Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_commands: Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_keys: Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "username", username)
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if pg_allow_replication is not None:
            pulumi.set(__self__, "pg_allow_replication", pg_allow_replication)
        if redis_acl_categories is not None:
            pulumi.set(__self__, "redis_acl_categories", redis_acl_categories)
        if redis_acl_channels is not None:
            pulumi.set(__self__, "redis_acl_channels", redis_acl_channels)
        if redis_acl_commands is not None:
            pulumi.set(__self__, "redis_acl_commands", redis_acl_commands)
        if redis_acl_keys is not None:
            pulumi.set(__self__, "redis_acl_keys", redis_acl_keys)

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
        The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[str]]:
        """
        Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the service user ( not applicable for all services ).
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="pgAllowReplication")
    def pg_allow_replication(self) -> Optional[pulumi.Input[bool]]:
        """
        Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "pg_allow_replication")

    @pg_allow_replication.setter
    def pg_allow_replication(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "pg_allow_replication", value)

    @property
    @pulumi.getter(name="redisAclCategories")
    def redis_acl_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_categories")

    @redis_acl_categories.setter
    def redis_acl_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_categories", value)

    @property
    @pulumi.getter(name="redisAclChannels")
    def redis_acl_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_channels")

    @redis_acl_channels.setter
    def redis_acl_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_channels", value)

    @property
    @pulumi.getter(name="redisAclCommands")
    def redis_acl_commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_commands")

    @redis_acl_commands.setter
    def redis_acl_commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_commands", value)

    @property
    @pulumi.getter(name="redisAclKeys")
    def redis_acl_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_keys")

    @redis_acl_keys.setter
    def redis_acl_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_keys", value)


@pulumi.input_type
class _ServiceUserState:
    def __init__(__self__, *,
                 access_cert: Optional[pulumi.Input[str]] = None,
                 access_key: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pg_allow_replication: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 redis_acl_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_commands: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServiceUser resources.
        :param pulumi.Input[str] access_cert: Access certificate for the user if applicable for the service in question
        :param pulumi.Input[str] access_key: Access certificate key for the user if applicable for the service in question
        :param pulumi.Input[str] authentication: Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        :param pulumi.Input[str] password: The password of the service user ( not applicable for all services ).
        :param pulumi.Input[bool] pg_allow_replication: Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_categories: Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_channels: Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_commands: Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_keys: Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] type: Type of the user account. Tells wether the user is the primary account or a regular account.
        :param pulumi.Input[str] username: The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        if access_cert is not None:
            pulumi.set(__self__, "access_cert", access_cert)
        if access_key is not None:
            pulumi.set(__self__, "access_key", access_key)
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if pg_allow_replication is not None:
            pulumi.set(__self__, "pg_allow_replication", pg_allow_replication)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if redis_acl_categories is not None:
            pulumi.set(__self__, "redis_acl_categories", redis_acl_categories)
        if redis_acl_channels is not None:
            pulumi.set(__self__, "redis_acl_channels", redis_acl_channels)
        if redis_acl_commands is not None:
            pulumi.set(__self__, "redis_acl_commands", redis_acl_commands)
        if redis_acl_keys is not None:
            pulumi.set(__self__, "redis_acl_keys", redis_acl_keys)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="accessCert")
    def access_cert(self) -> Optional[pulumi.Input[str]]:
        """
        Access certificate for the user if applicable for the service in question
        """
        return pulumi.get(self, "access_cert")

    @access_cert.setter
    def access_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_cert", value)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[str]]:
        """
        Access certificate key for the user if applicable for the service in question
        """
        return pulumi.get(self, "access_key")

    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key", value)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[str]]:
        """
        Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the service user ( not applicable for all services ).
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="pgAllowReplication")
    def pg_allow_replication(self) -> Optional[pulumi.Input[bool]]:
        """
        Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "pg_allow_replication")

    @pg_allow_replication.setter
    def pg_allow_replication(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "pg_allow_replication", value)

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
    @pulumi.getter(name="redisAclCategories")
    def redis_acl_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_categories")

    @redis_acl_categories.setter
    def redis_acl_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_categories", value)

    @property
    @pulumi.getter(name="redisAclChannels")
    def redis_acl_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_channels")

    @redis_acl_channels.setter
    def redis_acl_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_channels", value)

    @property
    @pulumi.getter(name="redisAclCommands")
    def redis_acl_commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_commands")

    @redis_acl_commands.setter
    def redis_acl_commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_commands", value)

    @property
    @pulumi.getter(name="redisAclKeys")
    def redis_acl_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_keys")

    @redis_acl_keys.setter
    def redis_acl_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "redis_acl_keys", value)

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
        Type of the user account. Tells wether the user is the primary account or a regular account.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class ServiceUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pg_allow_replication: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 redis_acl_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_commands: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Service User resource allows the creation and management of Aiven Service Users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        myserviceuser = aiven.ServiceUser("myserviceuser",
            project=aiven_project["myproject"]["project"],
            service_name=aiven_service["myservice"]["service_name"],
            username="<USERNAME>")
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/serviceUser:ServiceUser myserviceuser project/service_name/username
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication: Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        :param pulumi.Input[str] password: The password of the service user ( not applicable for all services ).
        :param pulumi.Input[bool] pg_allow_replication: Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_categories: Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_channels: Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_commands: Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_keys: Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] username: The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Service User resource allows the creation and management of Aiven Service Users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        myserviceuser = aiven.ServiceUser("myserviceuser",
            project=aiven_project["myproject"]["project"],
            service_name=aiven_service["myservice"]["service_name"],
            username="<USERNAME>")
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/serviceUser:ServiceUser myserviceuser project/service_name/username
        ```

        :param str resource_name: The name of the resource.
        :param ServiceUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pg_allow_replication: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 redis_acl_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_commands: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 redis_acl_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceUserArgs.__new__(ServiceUserArgs)

            __props__.__dict__["authentication"] = authentication
            __props__.__dict__["password"] = password
            __props__.__dict__["pg_allow_replication"] = pg_allow_replication
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["redis_acl_categories"] = redis_acl_categories
            __props__.__dict__["redis_acl_channels"] = redis_acl_channels
            __props__.__dict__["redis_acl_commands"] = redis_acl_commands
            __props__.__dict__["redis_acl_keys"] = redis_acl_keys
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["access_cert"] = None
            __props__.__dict__["access_key"] = None
            __props__.__dict__["type"] = None
        super(ServiceUser, __self__).__init__(
            'aiven:index/serviceUser:ServiceUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_cert: Optional[pulumi.Input[str]] = None,
            access_key: Optional[pulumi.Input[str]] = None,
            authentication: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            pg_allow_replication: Optional[pulumi.Input[bool]] = None,
            project: Optional[pulumi.Input[str]] = None,
            redis_acl_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            redis_acl_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            redis_acl_commands: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            redis_acl_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'ServiceUser':
        """
        Get an existing ServiceUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_cert: Access certificate for the user if applicable for the service in question
        :param pulumi.Input[str] access_key: Access certificate key for the user if applicable for the service in question
        :param pulumi.Input[str] authentication: Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        :param pulumi.Input[str] password: The password of the service user ( not applicable for all services ).
        :param pulumi.Input[bool] pg_allow_replication: Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_categories: Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_channels: Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_commands: Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] redis_acl_keys: Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] type: Type of the user account. Tells wether the user is the primary account or a regular account.
        :param pulumi.Input[str] username: The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceUserState.__new__(_ServiceUserState)

        __props__.__dict__["access_cert"] = access_cert
        __props__.__dict__["access_key"] = access_key
        __props__.__dict__["authentication"] = authentication
        __props__.__dict__["password"] = password
        __props__.__dict__["pg_allow_replication"] = pg_allow_replication
        __props__.__dict__["project"] = project
        __props__.__dict__["redis_acl_categories"] = redis_acl_categories
        __props__.__dict__["redis_acl_channels"] = redis_acl_channels
        __props__.__dict__["redis_acl_commands"] = redis_acl_commands
        __props__.__dict__["redis_acl_keys"] = redis_acl_keys
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["type"] = type
        __props__.__dict__["username"] = username
        return ServiceUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessCert")
    def access_cert(self) -> pulumi.Output[str]:
        """
        Access certificate for the user if applicable for the service in question
        """
        return pulumi.get(self, "access_cert")

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[str]:
        """
        Access certificate key for the user if applicable for the service in question
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional[str]]:
        """
        Authentication details. The possible values are `caching_sha2_password` and `mysql_native_password`.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password of the service user ( not applicable for all services ).
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="pgAllowReplication")
    def pg_allow_replication(self) -> pulumi.Output[Optional[bool]]:
        """
        Postgres specific field, defines whether replication is allowed. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "pg_allow_replication")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="redisAclCategories")
    def redis_acl_categories(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Redis specific field, defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_categories")

    @property
    @pulumi.getter(name="redisAclChannels")
    def redis_acl_channels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Redis specific field, defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_channels")

    @property
    @pulumi.getter(name="redisAclCommands")
    def redis_acl_commands(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Redis specific field, defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_commands")

    @property
    @pulumi.getter(name="redisAclKeys")
    def redis_acl_keys(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Redis specific field, defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_keys")

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
        Type of the user account. Tells wether the user is the primary account or a regular account.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The actual name of the service user. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")

