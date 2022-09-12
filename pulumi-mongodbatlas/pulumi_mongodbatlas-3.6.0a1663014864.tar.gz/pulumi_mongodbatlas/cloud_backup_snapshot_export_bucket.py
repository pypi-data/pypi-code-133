# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CloudBackupSnapshotExportBucketArgs', 'CloudBackupSnapshotExportBucket']

@pulumi.input_type
class CloudBackupSnapshotExportBucketArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str],
                 cloud_provider: pulumi.Input[str],
                 iam_role_id: pulumi.Input[str],
                 project_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a CloudBackupSnapshotExportBucket resource.
        :param pulumi.Input[str] bucket_name: Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        :param pulumi.Input[str] cloud_provider: Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        :param pulumi.Input[str] iam_role_id: Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        :param pulumi.Input[str] project_id: The unique identifier of the project for the Atlas cluster.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "iam_role_id", iam_role_id)
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Input[str]:
        """
        Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        """
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> pulumi.Input[str]:
        """
        Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        """
        return pulumi.get(self, "iam_role_id")

    @iam_role_id.setter
    def iam_role_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "iam_role_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The unique identifier of the project for the Atlas cluster.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)


@pulumi.input_type
class _CloudBackupSnapshotExportBucketState:
    def __init__(__self__, *,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 export_bucket_id: Optional[pulumi.Input[str]] = None,
                 iam_role_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudBackupSnapshotExportBucket resources.
        :param pulumi.Input[str] bucket_name: Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        :param pulumi.Input[str] cloud_provider: Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        :param pulumi.Input[str] export_bucket_id: Unique identifier of the snapshot export bucket.
        :param pulumi.Input[str] iam_role_id: Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        :param pulumi.Input[str] project_id: The unique identifier of the project for the Atlas cluster.
        """
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if cloud_provider is not None:
            pulumi.set(__self__, "cloud_provider", cloud_provider)
        if export_bucket_id is not None:
            pulumi.set(__self__, "export_bucket_id", export_bucket_id)
        if iam_role_id is not None:
            pulumi.set(__self__, "iam_role_id", iam_role_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        """
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter(name="exportBucketId")
    def export_bucket_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the snapshot export bucket.
        """
        return pulumi.get(self, "export_bucket_id")

    @export_bucket_id.setter
    def export_bucket_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_bucket_id", value)

    @property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        """
        return pulumi.get(self, "iam_role_id")

    @iam_role_id.setter
    def iam_role_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_role_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the project for the Atlas cluster.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


class CloudBackupSnapshotExportBucket(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 iam_role_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `CloudBackupSnapshotExportBucket` resource allows you to create an export snapshot bucket for the specified project.

        > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.CloudBackupSnapshotExportBucket("test",
            bucket_name="example-bucket",
            cloud_provider="AWS",
            iam_role_id="{IAM_ROLE_ID}",
            project_id="{PROJECT_ID}")
        ```

        ## Import

        Cloud Backup Snapshot Export Backup entries can be imported using project project_id, and bucket_id (Unique identifier of the snapshot export bucket), in the format `PROJECTID-BUCKETID`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/cloudBackupSnapshotExportBucket:CloudBackupSnapshotExportBucket test 5d0f1f73cf09a29120e173cf-5d116d82014b764445b2f9b5
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/cloud-backup/export/create-one-export-bucket/)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        :param pulumi.Input[str] cloud_provider: Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        :param pulumi.Input[str] iam_role_id: Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        :param pulumi.Input[str] project_id: The unique identifier of the project for the Atlas cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudBackupSnapshotExportBucketArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `CloudBackupSnapshotExportBucket` resource allows you to create an export snapshot bucket for the specified project.

        > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.CloudBackupSnapshotExportBucket("test",
            bucket_name="example-bucket",
            cloud_provider="AWS",
            iam_role_id="{IAM_ROLE_ID}",
            project_id="{PROJECT_ID}")
        ```

        ## Import

        Cloud Backup Snapshot Export Backup entries can be imported using project project_id, and bucket_id (Unique identifier of the snapshot export bucket), in the format `PROJECTID-BUCKETID`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/cloudBackupSnapshotExportBucket:CloudBackupSnapshotExportBucket test 5d0f1f73cf09a29120e173cf-5d116d82014b764445b2f9b5
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/cloud-backup/export/create-one-export-bucket/)

        :param str resource_name: The name of the resource.
        :param CloudBackupSnapshotExportBucketArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudBackupSnapshotExportBucketArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 iam_role_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudBackupSnapshotExportBucketArgs.__new__(CloudBackupSnapshotExportBucketArgs)

            if bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 'bucket_name'")
            __props__.__dict__["bucket_name"] = bucket_name
            if cloud_provider is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_provider'")
            __props__.__dict__["cloud_provider"] = cloud_provider
            if iam_role_id is None and not opts.urn:
                raise TypeError("Missing required property 'iam_role_id'")
            __props__.__dict__["iam_role_id"] = iam_role_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["export_bucket_id"] = None
        super(CloudBackupSnapshotExportBucket, __self__).__init__(
            'mongodbatlas:index/cloudBackupSnapshotExportBucket:CloudBackupSnapshotExportBucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket_name: Optional[pulumi.Input[str]] = None,
            cloud_provider: Optional[pulumi.Input[str]] = None,
            export_bucket_id: Optional[pulumi.Input[str]] = None,
            iam_role_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None) -> 'CloudBackupSnapshotExportBucket':
        """
        Get an existing CloudBackupSnapshotExportBucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        :param pulumi.Input[str] cloud_provider: Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        :param pulumi.Input[str] export_bucket_id: Unique identifier of the snapshot export bucket.
        :param pulumi.Input[str] iam_role_id: Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        :param pulumi.Input[str] project_id: The unique identifier of the project for the Atlas cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudBackupSnapshotExportBucketState.__new__(_CloudBackupSnapshotExportBucketState)

        __props__.__dict__["bucket_name"] = bucket_name
        __props__.__dict__["cloud_provider"] = cloud_provider
        __props__.__dict__["export_bucket_id"] = export_bucket_id
        __props__.__dict__["iam_role_id"] = iam_role_id
        __props__.__dict__["project_id"] = project_id
        return CloudBackupSnapshotExportBucket(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[str]:
        """
        Name of the bucket that the provided role ID is authorized to access. You must also specify the `iam_role_id`.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Output[str]:
        """
        Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas only supports `AWS`.
        """
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="exportBucketId")
    def export_bucket_id(self) -> pulumi.Output[str]:
        """
        Unique identifier of the snapshot export bucket.
        """
        return pulumi.get(self, "export_bucket_id")

    @property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> pulumi.Output[str]:
        """
        Unique identifier of the role that Atlas can use to access the bucket. You must also specify the `bucket_name`.
        """
        return pulumi.get(self, "iam_role_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The unique identifier of the project for the Atlas cluster.
        """
        return pulumi.get(self, "project_id")

