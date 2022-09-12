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
    'GetDomainZoneResult',
    'AwaitableGetDomainZoneResult',
    'get_domain_zone',
    'get_domain_zone_output',
]

@pulumi.output_type
class GetDomainZoneResult:
    """
    A collection of values returned by getDomainZone.
    """
    def __init__(__self__, domain=None, id=None, message=None, ns=None, ns_defaults=None, ns_masters=None, project_id=None, status=None, subdomain=None, updated_at=None):
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if message and not isinstance(message, str):
            raise TypeError("Expected argument 'message' to be a str")
        pulumi.set(__self__, "message", message)
        if ns and not isinstance(ns, list):
            raise TypeError("Expected argument 'ns' to be a list")
        pulumi.set(__self__, "ns", ns)
        if ns_defaults and not isinstance(ns_defaults, list):
            raise TypeError("Expected argument 'ns_defaults' to be a list")
        pulumi.set(__self__, "ns_defaults", ns_defaults)
        if ns_masters and not isinstance(ns_masters, list):
            raise TypeError("Expected argument 'ns_masters' to be a list")
        pulumi.set(__self__, "ns_masters", ns_masters)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subdomain and not isinstance(subdomain, str):
            raise TypeError("Expected argument 'subdomain' to be a str")
        pulumi.set(__self__, "subdomain", subdomain)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        Message
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def ns(self) -> Sequence[str]:
        """
        NameServer list for zone.
        """
        return pulumi.get(self, "ns")

    @property
    @pulumi.getter(name="nsDefaults")
    def ns_defaults(self) -> Sequence[str]:
        """
        NameServer default list for zone.
        """
        return pulumi.get(self, "ns_defaults")

    @property
    @pulumi.getter(name="nsMasters")
    def ns_masters(self) -> Sequence[str]:
        """
        NameServer master list for zone.
        """
        return pulumi.get(self, "ns_masters")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The domain zone status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[str]:
        return pulumi.get(self, "subdomain")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The date and time of the last update of the DNS zone.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetDomainZoneResult(GetDomainZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainZoneResult(
            domain=self.domain,
            id=self.id,
            message=self.message,
            ns=self.ns,
            ns_defaults=self.ns_defaults,
            ns_masters=self.ns_masters,
            project_id=self.project_id,
            status=self.status,
            subdomain=self.subdomain,
            updated_at=self.updated_at)


def get_domain_zone(domain: Optional[str] = None,
                    subdomain: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainZoneResult:
    """
    Gets information about a domain zone.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    main = scaleway.get_domain_zone(domain="scaleway-terraform.com",
        subdomain="test")
    ```


    :param str domain: The domain where the DNS zone will be created.
    :param str subdomain: The subdomain(zone name) to create in the domain.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['subdomain'] = subdomain
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scaleway:index/getDomainZone:getDomainZone', __args__, opts=opts, typ=GetDomainZoneResult).value

    return AwaitableGetDomainZoneResult(
        domain=__ret__.domain,
        id=__ret__.id,
        message=__ret__.message,
        ns=__ret__.ns,
        ns_defaults=__ret__.ns_defaults,
        ns_masters=__ret__.ns_masters,
        project_id=__ret__.project_id,
        status=__ret__.status,
        subdomain=__ret__.subdomain,
        updated_at=__ret__.updated_at)


@_utilities.lift_output_func(get_domain_zone)
def get_domain_zone_output(domain: Optional[pulumi.Input[Optional[str]]] = None,
                           subdomain: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainZoneResult]:
    """
    Gets information about a domain zone.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    main = scaleway.get_domain_zone(domain="scaleway-terraform.com",
        subdomain="test")
    ```


    :param str domain: The domain where the DNS zone will be created.
    :param str subdomain: The subdomain(zone name) to create in the domain.
    """
    ...
