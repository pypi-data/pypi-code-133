# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VrackIpLoadbalancingArgs', 'VrackIpLoadbalancing']

@pulumi.input_type
class VrackIpLoadbalancingArgs:
    def __init__(__self__, *,
                 ip_loadbalancing: pulumi.Input[str],
                 service_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a VrackIpLoadbalancing resource.
        :param pulumi.Input[str] ip_loadbalancing: The id of the ip loadbalancing.
        :param pulumi.Input[str] service_name: The id of the vrack.
        """
        pulumi.set(__self__, "ip_loadbalancing", ip_loadbalancing)
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="ipLoadbalancing")
    def ip_loadbalancing(self) -> pulumi.Input[str]:
        """
        The id of the ip loadbalancing.
        """
        return pulumi.get(self, "ip_loadbalancing")

    @ip_loadbalancing.setter
    def ip_loadbalancing(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_loadbalancing", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The id of the vrack.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)


@pulumi.input_type
class _VrackIpLoadbalancingState:
    def __init__(__self__, *,
                 ip_loadbalancing: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VrackIpLoadbalancing resources.
        :param pulumi.Input[str] ip_loadbalancing: The id of the ip loadbalancing.
        :param pulumi.Input[str] service_name: The id of the vrack.
        """
        if ip_loadbalancing is not None:
            pulumi.set(__self__, "ip_loadbalancing", ip_loadbalancing)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="ipLoadbalancing")
    def ip_loadbalancing(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the ip loadbalancing.
        """
        return pulumi.get(self, "ip_loadbalancing")

    @ip_loadbalancing.setter
    def ip_loadbalancing(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_loadbalancing", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the vrack.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)


class VrackIpLoadbalancing(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_loadbalancing: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Attach a ip loadbalancing to a VRack.

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_ovh as ovh

        viplb = ovh.VrackIpLoadbalancing("viplb",
            ip_loadbalancing="yyy",
            service_name="xxx")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_loadbalancing: The id of the ip loadbalancing.
        :param pulumi.Input[str] service_name: The id of the vrack.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VrackIpLoadbalancingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Attach a ip loadbalancing to a VRack.

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_ovh as ovh

        viplb = ovh.VrackIpLoadbalancing("viplb",
            ip_loadbalancing="yyy",
            service_name="xxx")
        ```

        :param str resource_name: The name of the resource.
        :param VrackIpLoadbalancingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VrackIpLoadbalancingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_loadbalancing: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VrackIpLoadbalancingArgs.__new__(VrackIpLoadbalancingArgs)

            if ip_loadbalancing is None and not opts.urn:
                raise TypeError("Missing required property 'ip_loadbalancing'")
            __props__.__dict__["ip_loadbalancing"] = ip_loadbalancing
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
        super(VrackIpLoadbalancing, __self__).__init__(
            'ovh:index/vrackIpLoadbalancing:VrackIpLoadbalancing',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_loadbalancing: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None) -> 'VrackIpLoadbalancing':
        """
        Get an existing VrackIpLoadbalancing resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_loadbalancing: The id of the ip loadbalancing.
        :param pulumi.Input[str] service_name: The id of the vrack.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VrackIpLoadbalancingState.__new__(_VrackIpLoadbalancingState)

        __props__.__dict__["ip_loadbalancing"] = ip_loadbalancing
        __props__.__dict__["service_name"] = service_name
        return VrackIpLoadbalancing(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipLoadbalancing")
    def ip_loadbalancing(self) -> pulumi.Output[str]:
        """
        The id of the ip loadbalancing.
        """
        return pulumi.get(self, "ip_loadbalancing")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The id of the vrack.
        """
        return pulumi.get(self, "service_name")

