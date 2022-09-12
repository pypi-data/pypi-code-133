# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_context_attribute import AccessContextAttribute
from .access_context_attribute_collection import AccessContextAttributeCollection
from .access_materials import AccessMaterials
from .access_request import AccessRequest
from .access_request_collection import AccessRequestCollection
from .access_request_summary import AccessRequestSummary
from .activity_log import ActivityLog
from .approval_template import ApprovalTemplate
from .approval_template_collection import ApprovalTemplateCollection
from .approval_template_summary import ApprovalTemplateSummary
from .approver_info import ApproverInfo
from .approver_levels import ApproverLevels
from .change_approval_template_compartment_details import ChangeApprovalTemplateCompartmentDetails
from .change_lockbox_compartment_details import ChangeLockboxCompartmentDetails
from .create_access_request_details import CreateAccessRequestDetails
from .create_approval_template_details import CreateApprovalTemplateDetails
from .create_lockbox_details import CreateLockboxDetails
from .handle_access_request_details import HandleAccessRequestDetails
from .lockbox import Lockbox
from .lockbox_collection import LockboxCollection
from .lockbox_summary import LockboxSummary
from .update_approval_template_details import UpdateApprovalTemplateDetails
from .update_lockbox_details import UpdateLockboxDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for lockbox services.
lockbox_type_mapping = {
    "AccessContextAttribute": AccessContextAttribute,
    "AccessContextAttributeCollection": AccessContextAttributeCollection,
    "AccessMaterials": AccessMaterials,
    "AccessRequest": AccessRequest,
    "AccessRequestCollection": AccessRequestCollection,
    "AccessRequestSummary": AccessRequestSummary,
    "ActivityLog": ActivityLog,
    "ApprovalTemplate": ApprovalTemplate,
    "ApprovalTemplateCollection": ApprovalTemplateCollection,
    "ApprovalTemplateSummary": ApprovalTemplateSummary,
    "ApproverInfo": ApproverInfo,
    "ApproverLevels": ApproverLevels,
    "ChangeApprovalTemplateCompartmentDetails": ChangeApprovalTemplateCompartmentDetails,
    "ChangeLockboxCompartmentDetails": ChangeLockboxCompartmentDetails,
    "CreateAccessRequestDetails": CreateAccessRequestDetails,
    "CreateApprovalTemplateDetails": CreateApprovalTemplateDetails,
    "CreateLockboxDetails": CreateLockboxDetails,
    "HandleAccessRequestDetails": HandleAccessRequestDetails,
    "Lockbox": Lockbox,
    "LockboxCollection": LockboxCollection,
    "LockboxSummary": LockboxSummary,
    "UpdateApprovalTemplateDetails": UpdateApprovalTemplateDetails,
    "UpdateLockboxDetails": UpdateLockboxDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
