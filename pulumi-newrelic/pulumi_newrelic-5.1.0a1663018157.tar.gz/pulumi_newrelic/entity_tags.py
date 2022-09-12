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
from ._inputs import *

__all__ = ['EntityTagsArgs', 'EntityTags']

@pulumi.input_type
class EntityTagsArgs:
    def __init__(__self__, *,
                 guid: pulumi.Input[str],
                 tags: pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]]):
        """
        The set of arguments for constructing a EntityTags resource.
        :param pulumi.Input[str] guid: The guid of the entity to tag.
        :param pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]] tags: A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        pulumi.set(__self__, "guid", guid)
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def guid(self) -> pulumi.Input[str]:
        """
        The guid of the entity to tag.
        """
        return pulumi.get(self, "guid")

    @guid.setter
    def guid(self, value: pulumi.Input[str]):
        pulumi.set(self, "guid", value)

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]]:
        """
        A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _EntityTagsState:
    def __init__(__self__, *,
                 guid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]]] = None):
        """
        Input properties used for looking up and filtering EntityTags resources.
        :param pulumi.Input[str] guid: The guid of the entity to tag.
        :param pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]] tags: A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        if guid is not None:
            pulumi.set(__self__, "guid", guid)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def guid(self) -> Optional[pulumi.Input[str]]:
        """
        The guid of the entity to tag.
        """
        return pulumi.get(self, "guid")

    @guid.setter
    def guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guid", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]]]:
        """
        A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EntityTagsTagArgs']]]]):
        pulumi.set(self, "tags", value)


class EntityTags(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 guid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityTagsTagArgs']]]]] = None,
                 __props__=None):
        """
        Use this resource to create, update, and delete tags for a New Relic One entity.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo_entity = newrelic.get_entity(name="Example application",
            type="APPLICATION",
            domain="APM")
        foo_entity_tags = newrelic.EntityTags("fooEntityTags",
            guid=foo_entity.guid,
            tags=[
                newrelic.EntityTagsTagArgs(
                    key="my-key",
                    values=[
                        "my-value",
                        "my-other-value",
                    ],
                ),
                newrelic.EntityTagsTagArgs(
                    key="my-key-2",
                    values=["my-value-2"],
                ),
            ])
        ```

        ## Import

        New Relic One entity tags can be imported using a concatenated string of the format

        `<guid>`, e.g. bash

        ```sh
         $ pulumi import newrelic:index/entityTags:EntityTags foo MjUyMDUyOHxBUE18QVBRTElDQVRJT058MjE1MDM3Nzk1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] guid: The guid of the entity to tag.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityTagsTagArgs']]]] tags: A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EntityTagsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to create, update, and delete tags for a New Relic One entity.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo_entity = newrelic.get_entity(name="Example application",
            type="APPLICATION",
            domain="APM")
        foo_entity_tags = newrelic.EntityTags("fooEntityTags",
            guid=foo_entity.guid,
            tags=[
                newrelic.EntityTagsTagArgs(
                    key="my-key",
                    values=[
                        "my-value",
                        "my-other-value",
                    ],
                ),
                newrelic.EntityTagsTagArgs(
                    key="my-key-2",
                    values=["my-value-2"],
                ),
            ])
        ```

        ## Import

        New Relic One entity tags can be imported using a concatenated string of the format

        `<guid>`, e.g. bash

        ```sh
         $ pulumi import newrelic:index/entityTags:EntityTags foo MjUyMDUyOHxBUE18QVBRTElDQVRJT058MjE1MDM3Nzk1
        ```

        :param str resource_name: The name of the resource.
        :param EntityTagsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EntityTagsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 guid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityTagsTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EntityTagsArgs.__new__(EntityTagsArgs)

            if guid is None and not opts.urn:
                raise TypeError("Missing required property 'guid'")
            __props__.__dict__["guid"] = guid
            if tags is None and not opts.urn:
                raise TypeError("Missing required property 'tags'")
            __props__.__dict__["tags"] = tags
        super(EntityTags, __self__).__init__(
            'newrelic:index/entityTags:EntityTags',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            guid: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityTagsTagArgs']]]]] = None) -> 'EntityTags':
        """
        Get an existing EntityTags resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] guid: The guid of the entity to tag.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityTagsTagArgs']]]] tags: A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EntityTagsState.__new__(_EntityTagsState)

        __props__.__dict__["guid"] = guid
        __props__.__dict__["tags"] = tags
        return EntityTags(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def guid(self) -> pulumi.Output[str]:
        """
        The guid of the entity to tag.
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence['outputs.EntityTagsTag']]:
        """
        A nested block that describes an entity tag. See Nested tag blocks below for details.
        """
        return pulumi.get(self, "tags")

