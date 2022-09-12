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
    'GetTeamResult',
    'AwaitableGetTeamResult',
    'get_team',
    'get_team_output',
]

@pulumi.output_type
class GetTeamResult:
    """
    A collection of values returned by getTeam.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Grafana team.
        """
        return pulumi.get(self, "name")


class AwaitableGetTeamResult(GetTeamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTeamResult(
            id=self.id,
            name=self.name)


def get_team(name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTeamResult:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/administration/manage-users-and-permissions/manage-teams/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/team/)

    ## Example Usage

    ```python
    import pulumi
    import lbrlabs_pulumi_grafana as grafana
    import pulumi_grafana as grafana

    test = grafana.Team("test", email="test-team-email@test.com")
    from_name = grafana.get_team_output(name=test.name)
    ```


    :param str name: The name of the Grafana team.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getTeam:getTeam', __args__, opts=opts, typ=GetTeamResult).value

    return AwaitableGetTeamResult(
        id=__ret__.id,
        name=__ret__.name)


@_utilities.lift_output_func(get_team)
def get_team_output(name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTeamResult]:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/administration/manage-users-and-permissions/manage-teams/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/team/)

    ## Example Usage

    ```python
    import pulumi
    import lbrlabs_pulumi_grafana as grafana
    import pulumi_grafana as grafana

    test = grafana.Team("test", email="test-team-email@test.com")
    from_name = grafana.get_team_output(name=test.name)
    ```


    :param str name: The name of the Grafana team.
    """
    ...
