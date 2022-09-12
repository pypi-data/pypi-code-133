# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 project: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 lc_collate: Optional[pulumi.Input[str]] = None,
                 lc_ctype: Optional[pulumi.Input[str]] = None,
                 termination_protection: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] database_name: The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_collate: Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_ctype: Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[bool] termination_protection: It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
               recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "service_name", service_name)
        if lc_collate is not None:
            pulumi.set(__self__, "lc_collate", lc_collate)
        if lc_ctype is not None:
            pulumi.set(__self__, "lc_ctype", lc_ctype)
        if termination_protection is not None:
            pulumi.set(__self__, "termination_protection", termination_protection)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

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
    @pulumi.getter(name="lcCollate")
    def lc_collate(self) -> Optional[pulumi.Input[str]]:
        """
        Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "lc_collate")

    @lc_collate.setter
    def lc_collate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lc_collate", value)

    @property
    @pulumi.getter(name="lcCtype")
    def lc_ctype(self) -> Optional[pulumi.Input[str]]:
        """
        Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "lc_ctype")

    @lc_ctype.setter
    def lc_ctype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lc_ctype", value)

    @property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
        recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        return pulumi.get(self, "termination_protection")

    @termination_protection.setter
    def termination_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "termination_protection", value)


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *,
                 database_name: Optional[pulumi.Input[str]] = None,
                 lc_collate: Optional[pulumi.Input[str]] = None,
                 lc_ctype: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 termination_protection: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Database resources.
        :param pulumi.Input[str] database_name: The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_collate: Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_ctype: Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[bool] termination_protection: It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
               recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if lc_collate is not None:
            pulumi.set(__self__, "lc_collate", lc_collate)
        if lc_ctype is not None:
            pulumi.set(__self__, "lc_ctype", lc_ctype)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if termination_protection is not None:
            pulumi.set(__self__, "termination_protection", termination_protection)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="lcCollate")
    def lc_collate(self) -> Optional[pulumi.Input[str]]:
        """
        Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "lc_collate")

    @lc_collate.setter
    def lc_collate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lc_collate", value)

    @property
    @pulumi.getter(name="lcCtype")
    def lc_ctype(self) -> Optional[pulumi.Input[str]]:
        """
        Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "lc_ctype")

    @lc_ctype.setter
    def lc_ctype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lc_ctype", value)

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
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
        recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        return pulumi.get(self, "termination_protection")

    @termination_protection.setter
    def termination_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "termination_protection", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 lc_collate: Optional[pulumi.Input[str]] = None,
                 lc_ctype: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 termination_protection: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The Database resource allows the creation and management of Aiven Databases.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        mydatabase = aiven.Database("mydatabase",
            project=aiven_project["myproject"]["project"],
            service_name=aiven_service["myservice"]["service_name"],
            database_name="<DATABASE_NAME>")
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/database:Database mydatabase project/service_name/database_name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_collate: Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_ctype: Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[bool] termination_protection: It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
               recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Database resource allows the creation and management of Aiven Databases.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        mydatabase = aiven.Database("mydatabase",
            project=aiven_project["myproject"]["project"],
            service_name=aiven_service["myservice"]["service_name"],
            database_name="<DATABASE_NAME>")
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/database:Database mydatabase project/service_name/database_name
        ```

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 lc_collate: Optional[pulumi.Input[str]] = None,
                 lc_ctype: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 termination_protection: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["lc_collate"] = lc_collate
            __props__.__dict__["lc_ctype"] = lc_ctype
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["termination_protection"] = termination_protection
        super(Database, __self__).__init__(
            'aiven:index/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            lc_collate: Optional[pulumi.Input[str]] = None,
            lc_ctype: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            termination_protection: Optional[pulumi.Input[bool]] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_collate: Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] lc_ctype: Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[bool] termination_protection: It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
               recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatabaseState.__new__(_DatabaseState)

        __props__.__dict__["database_name"] = database_name
        __props__.__dict__["lc_collate"] = lc_collate
        __props__.__dict__["lc_ctype"] = lc_ctype
        __props__.__dict__["project"] = project
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["termination_protection"] = termination_protection
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        The name of the service database. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="lcCollate")
    def lc_collate(self) -> pulumi.Output[Optional[str]]:
        """
        Default string sort order (`LC_COLLATE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "lc_collate")

    @property
    @pulumi.getter(name="lcCtype")
    def lc_ctype(self) -> pulumi.Output[Optional[str]]:
        """
        Default character classification (`LC_CTYPE`) of the database. The default value is `en_US.UTF-8`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "lc_ctype")

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
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
        recommended to enable this for any production databases containing critical data. The default value is `false`.
        """
        return pulumi.get(self, "termination_protection")

