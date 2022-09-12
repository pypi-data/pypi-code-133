# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AuditingArgs', 'Auditing']

@pulumi.input_type
class AuditingArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 audit_authorization_success: Optional[pulumi.Input[bool]] = None,
                 audit_filter: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Auditing resource.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        :param pulumi.Input[bool] audit_authorization_success: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        :param pulumi.Input[str] audit_filter: JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        """
        pulumi.set(__self__, "project_id", project_id)
        if audit_authorization_success is not None:
            pulumi.set(__self__, "audit_authorization_success", audit_authorization_success)
        if audit_filter is not None:
            pulumi.set(__self__, "audit_filter", audit_filter)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The unique ID for the project to configure auditing.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="auditAuthorizationSuccess")
    def audit_authorization_success(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        """
        return pulumi.get(self, "audit_authorization_success")

    @audit_authorization_success.setter
    def audit_authorization_success(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "audit_authorization_success", value)

    @property
    @pulumi.getter(name="auditFilter")
    def audit_filter(self) -> Optional[pulumi.Input[str]]:
        """
        JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        """
        return pulumi.get(self, "audit_filter")

    @audit_filter.setter
    def audit_filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_filter", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class _AuditingState:
    def __init__(__self__, *,
                 audit_authorization_success: Optional[pulumi.Input[bool]] = None,
                 audit_filter: Optional[pulumi.Input[str]] = None,
                 configuration_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Auditing resources.
        :param pulumi.Input[bool] audit_authorization_success: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        :param pulumi.Input[str] audit_filter: JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        :param pulumi.Input[str] configuration_type: Denotes the configuration method for the audit filter. Possible values are: 
               * NONE - auditing not configured for the project.
               * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
               * FILTER_JSON - auditing configured via Atlas custom filter or API.
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        """
        if audit_authorization_success is not None:
            pulumi.set(__self__, "audit_authorization_success", audit_authorization_success)
        if audit_filter is not None:
            pulumi.set(__self__, "audit_filter", audit_filter)
        if configuration_type is not None:
            pulumi.set(__self__, "configuration_type", configuration_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="auditAuthorizationSuccess")
    def audit_authorization_success(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        """
        return pulumi.get(self, "audit_authorization_success")

    @audit_authorization_success.setter
    def audit_authorization_success(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "audit_authorization_success", value)

    @property
    @pulumi.getter(name="auditFilter")
    def audit_filter(self) -> Optional[pulumi.Input[str]]:
        """
        JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        """
        return pulumi.get(self, "audit_filter")

    @audit_filter.setter
    def audit_filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_filter", value)

    @property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> Optional[pulumi.Input[str]]:
        """
        Denotes the configuration method for the audit filter. Possible values are: 
        * NONE - auditing not configured for the project.
        * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
        * FILTER_JSON - auditing configured via Atlas custom filter or API.
        """
        return pulumi.get(self, "configuration_type")

    @configuration_type.setter
    def configuration_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID for the project to configure auditing.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


class Auditing(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_authorization_success: Optional[pulumi.Input[bool]] = None,
                 audit_filter: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `Auditing` provides an Auditing resource. This allows auditing to be created.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.Auditing("test",
            audit_authorization_success=False,
            audit_filter="{ 'atype': 'authenticate', 'param': {   'user': 'auditAdmin',   'db': 'admin',   'mechanism': 'SCRAM-SHA-1' }}",
            enabled=True,
            project_id="<project-id>")
        ```

        ## Import

        Auditing must be imported using auditing ID, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/auditing:Auditing my_auditing 5d09d6a59ccf6445652a444a
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/auditing/)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_authorization_success: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        :param pulumi.Input[str] audit_filter: JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuditingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `Auditing` provides an Auditing resource. This allows auditing to be created.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.Auditing("test",
            audit_authorization_success=False,
            audit_filter="{ 'atype': 'authenticate', 'param': {   'user': 'auditAdmin',   'db': 'admin',   'mechanism': 'SCRAM-SHA-1' }}",
            enabled=True,
            project_id="<project-id>")
        ```

        ## Import

        Auditing must be imported using auditing ID, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/auditing:Auditing my_auditing 5d09d6a59ccf6445652a444a
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/auditing/)

        :param str resource_name: The name of the resource.
        :param AuditingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuditingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_authorization_success: Optional[pulumi.Input[bool]] = None,
                 audit_filter: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuditingArgs.__new__(AuditingArgs)

            __props__.__dict__["audit_authorization_success"] = audit_authorization_success
            __props__.__dict__["audit_filter"] = audit_filter
            __props__.__dict__["enabled"] = enabled
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["configuration_type"] = None
        super(Auditing, __self__).__init__(
            'mongodbatlas:index/auditing:Auditing',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audit_authorization_success: Optional[pulumi.Input[bool]] = None,
            audit_filter: Optional[pulumi.Input[str]] = None,
            configuration_type: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            project_id: Optional[pulumi.Input[str]] = None) -> 'Auditing':
        """
        Get an existing Auditing resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_authorization_success: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        :param pulumi.Input[str] audit_filter: JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        :param pulumi.Input[str] configuration_type: Denotes the configuration method for the audit filter. Possible values are: 
               * NONE - auditing not configured for the project.
               * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
               * FILTER_JSON - auditing configured via Atlas custom filter or API.
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuditingState.__new__(_AuditingState)

        __props__.__dict__["audit_authorization_success"] = audit_authorization_success
        __props__.__dict__["audit_filter"] = audit_filter
        __props__.__dict__["configuration_type"] = configuration_type
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["project_id"] = project_id
        return Auditing(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="auditAuthorizationSuccess")
    def audit_authorization_success(self) -> pulumi.Output[bool]:
        """
        Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see [auditAuthorizationSuccess](https://docs.mongodb.com/manual/reference/parameters/#param.auditAuthorizationSuccess).  **Warning! Enabling Audit authorization successes can severely impact cluster performance. Enable this option with caution.**
        """
        return pulumi.get(self, "audit_authorization_success")

    @property
    @pulumi.getter(name="auditFilter")
    def audit_filter(self) -> pulumi.Output[str]:
        """
        JSON-formatted audit filter. For complete documentation on custom auditing filters, see [Configure Audit Filters](https://docs.mongodb.com/manual/tutorial/configure-audit-filters/).
        """
        return pulumi.get(self, "audit_filter")

    @property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Output[str]:
        """
        Denotes the configuration method for the audit filter. Possible values are: 
        * NONE - auditing not configured for the project.
        * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
        * FILTER_JSON - auditing configured via Atlas custom filter or API.
        """
        return pulumi.get(self, "configuration_type")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Denotes whether or not the project associated with the {project_id} has database auditing enabled.  Defaults to false.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The unique ID for the project to configure auditing.
        """
        return pulumi.get(self, "project_id")

