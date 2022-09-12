# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .aggregated_computed_usage_summary import AggregatedComputedUsageSummary
from .billing_schedule_product import BillingScheduleProduct
from .billing_schedule_summary import BillingScheduleSummary
from .commitment import Commitment
from .commitment_service import CommitmentService
from .commitment_summary import CommitmentSummary
from .computed_usage import ComputedUsage
from .computed_usage_aggregation import ComputedUsageAggregation
from .computed_usage_product import ComputedUsageProduct
from .computed_usage_summary import ComputedUsageSummary
from .invoice_line_summary import InvoiceLineSummary
from .invoice_summary import InvoiceSummary
from .invoiceline_computed_usage_summary import InvoicelineComputedUsageSummary
from .invoicing_address import InvoicingAddress
from .invoicing_business_partner import InvoicingBusinessPartner
from .invoicing_currency import InvoicingCurrency
from .invoicing_location import InvoicingLocation
from .invoicing_organization import InvoicingOrganization
from .invoicing_payment_term import InvoicingPaymentTerm
from .invoicing_product import InvoicingProduct
from .invoicing_user import InvoicingUser
from .organization_subscription_summary import OrganizationSubscriptionSummary
from .orgnization_subs_currency import OrgnizationSubsCurrency
from .rate_card_product import RateCardProduct
from .rate_card_summary import RateCardSummary
from .rate_card_tier import RateCardTier
from .subscribed_service import SubscribedService
from .subscribed_service_address import SubscribedServiceAddress
from .subscribed_service_business_partner import SubscribedServiceBusinessPartner
from .subscribed_service_location import SubscribedServiceLocation
from .subscribed_service_payment_term import SubscribedServicePaymentTerm
from .subscribed_service_summary import SubscribedServiceSummary
from .subscribed_service_user import SubscribedServiceUser
from .subscription_currency import SubscriptionCurrency
from .subscription_product import SubscriptionProduct
from .subscription_subscribed_service import SubscriptionSubscribedService
from .subscription_summary import SubscriptionSummary

# Maps type names to classes for onesubscription services.
onesubscription_type_mapping = {
    "AggregatedComputedUsageSummary": AggregatedComputedUsageSummary,
    "BillingScheduleProduct": BillingScheduleProduct,
    "BillingScheduleSummary": BillingScheduleSummary,
    "Commitment": Commitment,
    "CommitmentService": CommitmentService,
    "CommitmentSummary": CommitmentSummary,
    "ComputedUsage": ComputedUsage,
    "ComputedUsageAggregation": ComputedUsageAggregation,
    "ComputedUsageProduct": ComputedUsageProduct,
    "ComputedUsageSummary": ComputedUsageSummary,
    "InvoiceLineSummary": InvoiceLineSummary,
    "InvoiceSummary": InvoiceSummary,
    "InvoicelineComputedUsageSummary": InvoicelineComputedUsageSummary,
    "InvoicingAddress": InvoicingAddress,
    "InvoicingBusinessPartner": InvoicingBusinessPartner,
    "InvoicingCurrency": InvoicingCurrency,
    "InvoicingLocation": InvoicingLocation,
    "InvoicingOrganization": InvoicingOrganization,
    "InvoicingPaymentTerm": InvoicingPaymentTerm,
    "InvoicingProduct": InvoicingProduct,
    "InvoicingUser": InvoicingUser,
    "OrganizationSubscriptionSummary": OrganizationSubscriptionSummary,
    "OrgnizationSubsCurrency": OrgnizationSubsCurrency,
    "RateCardProduct": RateCardProduct,
    "RateCardSummary": RateCardSummary,
    "RateCardTier": RateCardTier,
    "SubscribedService": SubscribedService,
    "SubscribedServiceAddress": SubscribedServiceAddress,
    "SubscribedServiceBusinessPartner": SubscribedServiceBusinessPartner,
    "SubscribedServiceLocation": SubscribedServiceLocation,
    "SubscribedServicePaymentTerm": SubscribedServicePaymentTerm,
    "SubscribedServiceSummary": SubscribedServiceSummary,
    "SubscribedServiceUser": SubscribedServiceUser,
    "SubscriptionCurrency": SubscriptionCurrency,
    "SubscriptionProduct": SubscriptionProduct,
    "SubscriptionSubscribedService": SubscriptionSubscribedService,
    "SubscriptionSummary": SubscriptionSummary
}
