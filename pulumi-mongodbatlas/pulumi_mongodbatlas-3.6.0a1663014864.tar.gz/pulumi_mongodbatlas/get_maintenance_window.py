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
    'GetMaintenanceWindowResult',
    'AwaitableGetMaintenanceWindowResult',
    'get_maintenance_window',
    'get_maintenance_window_output',
]

@pulumi.output_type
class GetMaintenanceWindowResult:
    """
    A collection of values returned by getMaintenanceWindow.
    """
    def __init__(__self__, auto_defer_once_enabled=None, day_of_week=None, hour_of_day=None, id=None, number_of_deferrals=None, project_id=None, start_asap=None):
        if auto_defer_once_enabled and not isinstance(auto_defer_once_enabled, bool):
            raise TypeError("Expected argument 'auto_defer_once_enabled' to be a bool")
        pulumi.set(__self__, "auto_defer_once_enabled", auto_defer_once_enabled)
        if day_of_week and not isinstance(day_of_week, int):
            raise TypeError("Expected argument 'day_of_week' to be a int")
        pulumi.set(__self__, "day_of_week", day_of_week)
        if hour_of_day and not isinstance(hour_of_day, int):
            raise TypeError("Expected argument 'hour_of_day' to be a int")
        pulumi.set(__self__, "hour_of_day", hour_of_day)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if number_of_deferrals and not isinstance(number_of_deferrals, int):
            raise TypeError("Expected argument 'number_of_deferrals' to be a int")
        pulumi.set(__self__, "number_of_deferrals", number_of_deferrals)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if start_asap and not isinstance(start_asap, bool):
            raise TypeError("Expected argument 'start_asap' to be a bool")
        pulumi.set(__self__, "start_asap", start_asap)

    @property
    @pulumi.getter(name="autoDeferOnceEnabled")
    def auto_defer_once_enabled(self) -> bool:
        """
        Flag that indicates whether you want to defer all maintenance windows one week they would be triggered.
        For more information see: [MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/maintenance-windows/)
        """
        return pulumi.get(self, "auto_defer_once_enabled")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> int:
        """
        Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> int:
        """
        Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12  (Time zone is UTC).
        """
        return pulumi.get(self, "hour_of_day")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="numberOfDeferrals")
    def number_of_deferrals(self) -> int:
        """
        Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.
        """
        return pulumi.get(self, "number_of_deferrals")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="startAsap")
    def start_asap(self) -> bool:
        """
        Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.
        """
        return pulumi.get(self, "start_asap")


class AwaitableGetMaintenanceWindowResult(GetMaintenanceWindowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMaintenanceWindowResult(
            auto_defer_once_enabled=self.auto_defer_once_enabled,
            day_of_week=self.day_of_week,
            hour_of_day=self.hour_of_day,
            id=self.id,
            number_of_deferrals=self.number_of_deferrals,
            project_id=self.project_id,
            start_asap=self.start_asap)


def get_maintenance_window(project_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMaintenanceWindowResult:
    """
    `MaintenanceWindow` provides a Maintenance Window entry datasource. Gets information regarding the configured maintenance window for a MongoDB Atlas project.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.


    :param str project_id: The unique identifier of the project for the Maintenance Window.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getMaintenanceWindow:getMaintenanceWindow', __args__, opts=opts, typ=GetMaintenanceWindowResult).value

    return AwaitableGetMaintenanceWindowResult(
        auto_defer_once_enabled=__ret__.auto_defer_once_enabled,
        day_of_week=__ret__.day_of_week,
        hour_of_day=__ret__.hour_of_day,
        id=__ret__.id,
        number_of_deferrals=__ret__.number_of_deferrals,
        project_id=__ret__.project_id,
        start_asap=__ret__.start_asap)


@_utilities.lift_output_func(get_maintenance_window)
def get_maintenance_window_output(project_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMaintenanceWindowResult]:
    """
    `MaintenanceWindow` provides a Maintenance Window entry datasource. Gets information regarding the configured maintenance window for a MongoDB Atlas project.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.


    :param str project_id: The unique identifier of the project for the Maintenance Window.
    """
    ...
