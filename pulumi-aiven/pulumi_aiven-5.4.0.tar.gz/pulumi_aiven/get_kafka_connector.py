# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetKafkaConnectorResult',
    'AwaitableGetKafkaConnectorResult',
    'get_kafka_connector',
    'get_kafka_connector_output',
]

@pulumi.output_type
class GetKafkaConnectorResult:
    """
    A collection of values returned by getKafkaConnector.
    """
    def __init__(__self__, config=None, connector_name=None, id=None, plugin_author=None, plugin_class=None, plugin_doc_url=None, plugin_title=None, plugin_type=None, plugin_version=None, project=None, service_name=None, tasks=None):
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if connector_name and not isinstance(connector_name, str):
            raise TypeError("Expected argument 'connector_name' to be a str")
        pulumi.set(__self__, "connector_name", connector_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if plugin_author and not isinstance(plugin_author, str):
            raise TypeError("Expected argument 'plugin_author' to be a str")
        pulumi.set(__self__, "plugin_author", plugin_author)
        if plugin_class and not isinstance(plugin_class, str):
            raise TypeError("Expected argument 'plugin_class' to be a str")
        pulumi.set(__self__, "plugin_class", plugin_class)
        if plugin_doc_url and not isinstance(plugin_doc_url, str):
            raise TypeError("Expected argument 'plugin_doc_url' to be a str")
        pulumi.set(__self__, "plugin_doc_url", plugin_doc_url)
        if plugin_title and not isinstance(plugin_title, str):
            raise TypeError("Expected argument 'plugin_title' to be a str")
        pulumi.set(__self__, "plugin_title", plugin_title)
        if plugin_type and not isinstance(plugin_type, str):
            raise TypeError("Expected argument 'plugin_type' to be a str")
        pulumi.set(__self__, "plugin_type", plugin_type)
        if plugin_version and not isinstance(plugin_version, str):
            raise TypeError("Expected argument 'plugin_version' to be a str")
        pulumi.set(__self__, "plugin_version", plugin_version)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if tasks and not isinstance(tasks, list):
            raise TypeError("Expected argument 'tasks' to be a list")
        pulumi.set(__self__, "tasks", tasks)

    @property
    @pulumi.getter
    def config(self) -> Mapping[str, str]:
        """
        The Kafka Connector configuration parameters.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> str:
        """
        The kafka connector name. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "connector_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="pluginAuthor")
    def plugin_author(self) -> str:
        """
        The Kafka connector author.
        """
        return pulumi.get(self, "plugin_author")

    @property
    @pulumi.getter(name="pluginClass")
    def plugin_class(self) -> str:
        """
        The Kafka connector Java class.
        """
        return pulumi.get(self, "plugin_class")

    @property
    @pulumi.getter(name="pluginDocUrl")
    def plugin_doc_url(self) -> str:
        """
        The Kafka connector documentation URL.
        """
        return pulumi.get(self, "plugin_doc_url")

    @property
    @pulumi.getter(name="pluginTitle")
    def plugin_title(self) -> str:
        """
        The Kafka connector title.
        """
        return pulumi.get(self, "plugin_title")

    @property
    @pulumi.getter(name="pluginType")
    def plugin_type(self) -> str:
        """
        The Kafka connector type.
        """
        return pulumi.get(self, "plugin_type")

    @property
    @pulumi.getter(name="pluginVersion")
    def plugin_version(self) -> str:
        """
        The version of the kafka connector.
        """
        return pulumi.get(self, "plugin_version")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def tasks(self) -> Sequence['outputs.GetKafkaConnectorTaskResult']:
        """
        List of tasks of a connector.
        """
        return pulumi.get(self, "tasks")


class AwaitableGetKafkaConnectorResult(GetKafkaConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaConnectorResult(
            config=self.config,
            connector_name=self.connector_name,
            id=self.id,
            plugin_author=self.plugin_author,
            plugin_class=self.plugin_class,
            plugin_doc_url=self.plugin_doc_url,
            plugin_title=self.plugin_title,
            plugin_type=self.plugin_type,
            plugin_version=self.plugin_version,
            project=self.project,
            service_name=self.service_name,
            tasks=self.tasks)


def get_kafka_connector(connector_name: Optional[str] = None,
                        project: Optional[str] = None,
                        service_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaConnectorResult:
    """
    The Kafka connector data source provides information about the existing Aiven Kafka connector.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    kafka_es_con1 = aiven.get_kafka_connector(project=aiven_project["kafka-con-project1"]["project"],
        service_name=aiven_service["kafka-service1"]["service_name"],
        connector_name="kafka-es-con1")
    ```


    :param str connector_name: The kafka connector name. This property cannot be changed, doing so forces recreation of the resource.
    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    __args__ = dict()
    __args__['connectorName'] = connector_name
    __args__['project'] = project
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getKafkaConnector:getKafkaConnector', __args__, opts=opts, typ=GetKafkaConnectorResult).value

    return AwaitableGetKafkaConnectorResult(
        config=__ret__.config,
        connector_name=__ret__.connector_name,
        id=__ret__.id,
        plugin_author=__ret__.plugin_author,
        plugin_class=__ret__.plugin_class,
        plugin_doc_url=__ret__.plugin_doc_url,
        plugin_title=__ret__.plugin_title,
        plugin_type=__ret__.plugin_type,
        plugin_version=__ret__.plugin_version,
        project=__ret__.project,
        service_name=__ret__.service_name,
        tasks=__ret__.tasks)


@_utilities.lift_output_func(get_kafka_connector)
def get_kafka_connector_output(connector_name: Optional[pulumi.Input[str]] = None,
                               project: Optional[pulumi.Input[str]] = None,
                               service_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaConnectorResult]:
    """
    The Kafka connector data source provides information about the existing Aiven Kafka connector.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    kafka_es_con1 = aiven.get_kafka_connector(project=aiven_project["kafka-con-project1"]["project"],
        service_name=aiven_service["kafka-service1"]["service_name"],
        connector_name="kafka-es-con1")
    ```


    :param str connector_name: The kafka connector name. This property cannot be changed, doing so forces recreation of the resource.
    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    ...
