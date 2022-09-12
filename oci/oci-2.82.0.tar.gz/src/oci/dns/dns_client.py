# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import dns_type_mapping
missing = Sentinel("Missing")


class DnsClient(object):
    """
    API for the DNS service. Use this API to manage DNS zones, records, and other DNS resources.
    For more information, see [Overview of the DNS Service](/iaas/Content/DNS/Concepts/dnszonemanagement.htm).
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        :param obj circuit_breaker_strategy: (optional)
            A circuit breaker strategy to apply to all calls made by this service client (i.e. at the client level).
            This client uses :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` as default if no circuit breaker strategy is provided.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.

        :param allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this client should allow control characters in the response object. By default, the client will not
            allow control characters to be in the response object.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20180115',
            'service_endpoint_template': 'https://dns.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("dns", config, signer, dns_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def change_resolver_compartment(self, resolver_id, change_resolver_compartment_details, **kwargs):
        """
        Moves a resolver into a different compartment along with its protected default view and any endpoints.

        Zones in the default view are not moved. VCN-dedicated resolvers are initially created in the same compartment
        as their corresponding VCN, but can then be moved to a different compartment.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param oci.dns.models.ChangeResolverCompartmentDetails change_resolver_compartment_details: (required)
            Details for moving a resolver, along with its protected default view and endpoints, into a
            different compartment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/change_resolver_compartment.py.html>`__ to see an example of how to use change_resolver_compartment API.
        """
        resource_path = "/resolvers/{resolverId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_resolver_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Resolver/ChangeResolverCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_resolver_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_resolver_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_resolver_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_steering_policy_compartment(self, steering_policy_id, change_steering_policy_compartment_details, **kwargs):
        """
        Moves a steering policy into a different compartment.


        :param str steering_policy_id: (required)
            The OCID of the target steering policy.

        :param oci.dns.models.ChangeSteeringPolicyCompartmentDetails change_steering_policy_compartment_details: (required)
            Details for moving a steering policy into a different compartment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/change_steering_policy_compartment.py.html>`__ to see an example of how to use change_steering_policy_compartment API.
        """
        resource_path = "/steeringPolicies/{steeringPolicyId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_steering_policy_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicy/ChangeSteeringPolicyCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_steering_policy_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyId": steering_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_steering_policy_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_steering_policy_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_tsig_key_compartment(self, tsig_key_id, change_tsig_key_compartment_details, **kwargs):
        """
        Moves a TSIG key into a different compartment.


        :param str tsig_key_id: (required)
            The OCID of the target TSIG key.

        :param oci.dns.models.ChangeTsigKeyCompartmentDetails change_tsig_key_compartment_details: (required)
            Details for moving a TSIG key into a different compartment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/change_tsig_key_compartment.py.html>`__ to see an example of how to use change_tsig_key_compartment API.
        """
        resource_path = "/tsigKeys/{tsigKeyId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_tsig_key_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/TsigKey/ChangeTsigKeyCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_tsig_key_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tsigKeyId": tsig_key_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_tsig_key_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_tsig_key_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_view_compartment(self, view_id, change_view_compartment_details, **kwargs):
        """
        Moves a view into a different compartment.

        To change the compartment of a protected view, change the compartment of its corresponding resolver.


        :param str view_id: (required)
            The OCID of the target view.

        :param oci.dns.models.ChangeViewCompartmentDetails change_view_compartment_details: (required)
            Details for moving a view into a different compartment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/change_view_compartment.py.html>`__ to see an example of how to use change_view_compartment API.
        """
        resource_path = "/views/{viewId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_view_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/View/ChangeViewCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_view_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "viewId": view_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_view_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_view_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_zone_compartment(self, zone_id, change_zone_compartment_details, **kwargs):
        """
        Moves a zone into a different compartment.

        Protected zones cannot have their compartment changed. When the zone name is provided as a path
        parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is
        required.

        **Note:** All SteeringPolicyAttachment objects associated with this zone will also be moved into
        the provided compartment.


        :param str zone_id: (required)
            The OCID of the target zone.

        :param oci.dns.models.ChangeZoneCompartmentDetails change_zone_compartment_details: (required)
            Details for moving a zone into a different compartment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/change_zone_compartment.py.html>`__ to see an example of how to use change_zone_compartment API.
        """
        resource_path = "/zones/{zoneId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_zone_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Zone/ChangeZoneCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_zone_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneId": zone_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_zone_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=change_zone_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_resolver_endpoint(self, resolver_id, create_resolver_endpoint_details, **kwargs):
        """
        Creates a new resolver endpoint in the same compartment as the resolver.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param oci.dns.models.CreateResolverEndpointDetails create_resolver_endpoint_details: (required)
            Details for creating a new resolver endpoint.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.ResolverEndpoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/create_resolver_endpoint.py.html>`__ to see an example of how to use create_resolver_endpoint API.
        """
        resource_path = "/resolvers/{resolverId}/endpoints"
        method = "POST"
        operation_name = "create_resolver_endpoint"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_resolver_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=create_resolver_endpoint_details,
                response_type="ResolverEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=create_resolver_endpoint_details,
                response_type="ResolverEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_steering_policy(self, create_steering_policy_details, **kwargs):
        """
        Creates a new steering policy in the specified compartment. For more information on
        creating policies with templates, see `Traffic Management API Guide`__.

        __ https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm


        :param oci.dns.models.CreateSteeringPolicyDetails create_steering_policy_details: (required)
            Details for creating a new steering policy.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.SteeringPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/create_steering_policy.py.html>`__ to see an example of how to use create_steering_policy API.
        """
        resource_path = "/steeringPolicies"
        method = "POST"
        operation_name = "create_steering_policy"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_steering_policy got unknown kwargs: {!r}".format(extra_kwargs))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_steering_policy_details,
                response_type="SteeringPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_steering_policy_details,
                response_type="SteeringPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_steering_policy_attachment(self, create_steering_policy_attachment_details, **kwargs):
        """
        Creates a new attachment between a steering policy and a domain, giving the
        policy permission to answer queries for the specified domain. A steering policy must
        be attached to a domain for the policy to answer DNS queries for that domain.

        For the purposes of access control, the attachment is automatically placed
        into the same compartment as the domain's zone.


        :param oci.dns.models.CreateSteeringPolicyAttachmentDetails create_steering_policy_attachment_details: (required)
            Details for creating a new steering policy attachment.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.SteeringPolicyAttachment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/create_steering_policy_attachment.py.html>`__ to see an example of how to use create_steering_policy_attachment API.
        """
        resource_path = "/steeringPolicyAttachments"
        method = "POST"
        operation_name = "create_steering_policy_attachment"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_steering_policy_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_steering_policy_attachment_details,
                response_type="SteeringPolicyAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_steering_policy_attachment_details,
                response_type="SteeringPolicyAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_tsig_key(self, create_tsig_key_details, **kwargs):
        """
        Creates a new TSIG key in the specified compartment. There is no
        `opc-retry-token` header since TSIG key names must be globally unique.


        :param oci.dns.models.CreateTsigKeyDetails create_tsig_key_details: (required)
            Details for creating a new TSIG key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.TsigKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/create_tsig_key.py.html>`__ to see an example of how to use create_tsig_key API.
        """
        resource_path = "/tsigKeys"
        method = "POST"
        operation_name = "create_tsig_key"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_tsig_key got unknown kwargs: {!r}".format(extra_kwargs))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_tsig_key_details,
                response_type="TsigKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_tsig_key_details,
                response_type="TsigKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_view(self, create_view_details, **kwargs):
        """
        Creates a new view in the specified compartment.


        :param oci.dns.models.CreateViewDetails create_view_details: (required)
            Details for creating a new view.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original creation
            request may be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.View`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/create_view.py.html>`__ to see an example of how to use create_view API.
        """
        resource_path = "/views"
        method = "POST"
        operation_name = "create_view"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_view got unknown kwargs: {!r}".format(extra_kwargs))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_view_details,
                response_type="View",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_view_details,
                response_type="View",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_zone(self, create_zone_details, **kwargs):
        """
        Creates a new zone in the specified compartment.

        Private zones must have a zone type of `PRIMARY`. Creating a private zone at or under `oraclevcn.com`
        within the default protected view of a VCN-dedicated resolver is not permitted.


        :param oci.dns.models.CreateZoneBaseDetails create_zone_details: (required)
            Details for creating a new zone.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Zone`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/create_zone.py.html>`__ to see an example of how to use create_zone API.
        """
        resource_path = "/zones"
        method = "POST"
        operation_name = "create_zone"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "scope",
            "view_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_zone got unknown kwargs: {!r}".format(extra_kwargs))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_zone_details,
                response_type="Zone",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_zone_details,
                response_type="Zone",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_domain_records(self, zone_name_or_id, domain, **kwargs):
        """
        Deletes all records at the specified zone and domain.

        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter
        then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_domain_records.py.html>`__ to see an example of how to use delete_domain_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "DELETE"
        operation_name = "delete_domain_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/DeleteDomainRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_resolver_endpoint(self, resolver_id, resolver_endpoint_name, **kwargs):
        """
        Deletes the specified resolver endpoint.

        Note that attempting to delete a resolver endpoint in the DELETED lifecycle state will result in
        a `404` response to be consistent with other operations of the API. Resolver endpoints may not
        be deleted if they are referenced by a resolver rule.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param str resolver_endpoint_name: (required)
            The name of the target resolver endpoint.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_resolver_endpoint.py.html>`__ to see an example of how to use delete_resolver_endpoint API.
        """
        resource_path = "/resolvers/{resolverId}/endpoints/{resolverEndpointName}"
        method = "DELETE"
        operation_name = "delete_resolver_endpoint"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/ResolverEndpoint/DeleteResolverEndpoint"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_resolver_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id,
            "resolverEndpointName": resolver_endpoint_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_rr_set(self, zone_name_or_id, domain, rtype, **kwargs):
        """
        Deletes all records in the specified RRSet.

        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope
        query parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_rr_set.py.html>`__ to see an example of how to use delete_rr_set API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "DELETE"
        operation_name = "delete_rr_set"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "compartment_id",
            "scope",
            "view_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_steering_policy(self, steering_policy_id, **kwargs):
        """
        Deletes the specified steering policy.

        A `204` response indicates that the delete has been successful.
        Deletion will fail if the policy is attached to any zones. To detach a
        policy from a zone, see `DeleteSteeringPolicyAttachment`.


        :param str steering_policy_id: (required)
            The OCID of the target steering policy.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_steering_policy.py.html>`__ to see an example of how to use delete_steering_policy API.
        """
        resource_path = "/steeringPolicies/{steeringPolicyId}"
        method = "DELETE"
        operation_name = "delete_steering_policy"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_steering_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyId": steering_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_steering_policy_attachment(self, steering_policy_attachment_id, **kwargs):
        """
        Deletes the specified steering policy attachment.
        A `204` response indicates that the delete has been successful.


        :param str steering_policy_attachment_id: (required)
            The OCID of the target steering policy attachment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_steering_policy_attachment.py.html>`__ to see an example of how to use delete_steering_policy_attachment API.
        """
        resource_path = "/steeringPolicyAttachments/{steeringPolicyAttachmentId}"
        method = "DELETE"
        operation_name = "delete_steering_policy_attachment"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_steering_policy_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyAttachmentId": steering_policy_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_tsig_key(self, tsig_key_id, **kwargs):
        """
        Deletes the specified TSIG key.


        :param str tsig_key_id: (required)
            The OCID of the target TSIG key.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_tsig_key.py.html>`__ to see an example of how to use delete_tsig_key API.
        """
        resource_path = "/tsigKeys/{tsigKeyId}"
        method = "DELETE"
        operation_name = "delete_tsig_key"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_tsig_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tsigKeyId": tsig_key_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_view(self, view_id, **kwargs):
        """
        Deletes the specified view.

        Note that attempting to delete a view in the DELETED lifecycleState will result in a `404`
        response to be consistent with other operations of the API. Views cannot be
        deleted if they are referenced by non-deleted zones or resolvers.
        Protected views cannot be deleted.


        :param str view_id: (required)
            The OCID of the target view.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_view.py.html>`__ to see an example of how to use delete_view API.
        """
        resource_path = "/views/{viewId}"
        method = "DELETE"
        operation_name = "delete_view"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/View/DeleteView"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_view got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "viewId": view_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_zone(self, zone_name_or_id, **kwargs):
        """
        Deletes the specified zone and all its steering policy attachments.

        A `204` response indicates that the zone has been successfully deleted. Protected zones cannot be deleted.
        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter
        then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/delete_zone.py.html>`__ to see an example of how to use delete_zone API.
        """
        resource_path = "/zones/{zoneNameOrId}"
        method = "DELETE"
        operation_name = "delete_zone"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_zone got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_domain_records(self, zone_name_or_id, domain, **kwargs):
        """
        Gets a list of all records at the specified zone and domain.

        The results are sorted by `rtype` in alphabetical order by default. You can optionally filter and/or sort
        the results using the listed parameters. When the zone name is provided as a path parameter and `PRIVATE`
        is used for the scope query parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str zone_version: (optional)
            The version of the zone for which data is requested.

        :param str rtype: (optional)
            Search by record type.
            Will match any record whose `type`__ (case-insensitive) equals the provided value.

            __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str sort_by: (optional)
            The field by which to sort records.

            Allowed values are: "rtype", "ttl"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_domain_records.py.html>`__ to see an example of how to use get_domain_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "GET"
        operation_name = "get_domain_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/GetDomainRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "limit",
            "page",
            "zone_version",
            "rtype",
            "scope",
            "view_id",
            "sort_by",
            "sort_order",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["rtype", "ttl"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "zoneVersion": kwargs.get("zone_version", missing),
            "rtype": kwargs.get("rtype", missing),
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_resolver(self, resolver_id, **kwargs):
        """
        Gets information about a specific resolver.

        Note that attempting to get a resolver in the DELETED lifecycleState will result in a `404`
        response to be consistent with other operations of the API.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Resolver`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_resolver.py.html>`__ to see an example of how to use get_resolver API.
        """
        resource_path = "/resolvers/{resolverId}"
        method = "GET"
        operation_name = "get_resolver"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Resolver/GetResolver"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_modified_since",
            "if_none_match",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_resolver got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "If-None-Match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Resolver",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Resolver",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_resolver_endpoint(self, resolver_id, resolver_endpoint_name, **kwargs):
        """
        Gets information about a specific resolver endpoint.

        Note that attempting to get a resolver endpoint in the DELETED lifecycle state will result
        in a `404` response to be consistent with other operations of the API.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param str resolver_endpoint_name: (required)
            The name of the target resolver endpoint.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.ResolverEndpoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_resolver_endpoint.py.html>`__ to see an example of how to use get_resolver_endpoint API.
        """
        resource_path = "/resolvers/{resolverId}/endpoints/{resolverEndpointName}"
        method = "GET"
        operation_name = "get_resolver_endpoint"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/ResolverEndpoint/GetResolverEndpoint"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_modified_since",
            "if_none_match",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_resolver_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id,
            "resolverEndpointName": resolver_endpoint_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "If-None-Match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ResolverEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ResolverEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_rr_set(self, zone_name_or_id, domain, rtype, **kwargs):
        """
        Gets a list of all records in the specified RRSet.

        The results are sorted by `recordHash` by default. When the zone name is provided as a path parameter
        and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str zone_version: (optional)
            The version of the zone for which data is requested.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RRSet`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_rr_set.py.html>`__ to see an example of how to use get_rr_set API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "GET"
        operation_name = "get_rr_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/RRSet/GetRrSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "limit",
            "page",
            "zone_version",
            "compartment_id",
            "scope",
            "view_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "zoneVersion": kwargs.get("zone_version", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RRSet",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RRSet",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_steering_policy(self, steering_policy_id, **kwargs):
        """
        Gets information about the specified steering policy.


        :param str steering_policy_id: (required)
            The OCID of the target steering policy.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.SteeringPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_steering_policy.py.html>`__ to see an example of how to use get_steering_policy API.
        """
        resource_path = "/steeringPolicies/{steeringPolicyId}"
        method = "GET"
        operation_name = "get_steering_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicy/GetSteeringPolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_steering_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyId": steering_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SteeringPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SteeringPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_steering_policy_attachment(self, steering_policy_attachment_id, **kwargs):
        """
        Gets information about the specified steering policy attachment.


        :param str steering_policy_attachment_id: (required)
            The OCID of the target steering policy attachment.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.SteeringPolicyAttachment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_steering_policy_attachment.py.html>`__ to see an example of how to use get_steering_policy_attachment API.
        """
        resource_path = "/steeringPolicyAttachments/{steeringPolicyAttachmentId}"
        method = "GET"
        operation_name = "get_steering_policy_attachment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicyAttachment/GetSteeringPolicyAttachment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_steering_policy_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyAttachmentId": steering_policy_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SteeringPolicyAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SteeringPolicyAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_tsig_key(self, tsig_key_id, **kwargs):
        """
        Gets information about the specified TSIG key.


        :param str tsig_key_id: (required)
            The OCID of the target TSIG key.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.TsigKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_tsig_key.py.html>`__ to see an example of how to use get_tsig_key API.
        """
        resource_path = "/tsigKeys/{tsigKeyId}"
        method = "GET"
        operation_name = "get_tsig_key"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/TsigKey/GetTsigKey"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_tsig_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tsigKeyId": tsig_key_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TsigKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TsigKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_view(self, view_id, **kwargs):
        """
        Gets information about a specific view.

        Note that attempting to get a
        view in the DELETED lifecycleState will result in a `404` response to be
        consistent with other operations of the API.


        :param str view_id: (required)
            The OCID of the target view.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.View`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_view.py.html>`__ to see an example of how to use get_view API.
        """
        resource_path = "/views/{viewId}"
        method = "GET"
        operation_name = "get_view"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/View/GetView"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_modified_since",
            "if_none_match",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_view got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "viewId": view_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "If-None-Match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="View",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="View",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_zone(self, zone_name_or_id, **kwargs):
        """
        Gets information about the specified zone, including its creation date, zone type, and serial.

        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query
        parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Zone`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_zone.py.html>`__ to see an example of how to use get_zone API.
        """
        resource_path = "/zones/{zoneNameOrId}"
        method = "GET"
        operation_name = "get_zone"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Zone/GetZone"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_zone got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Zone",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Zone",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_zone_content(self, zone_name_or_id, **kwargs):
        """
        Gets the requested zone's zone file.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_zone_content.py.html>`__ to see an example of how to use get_zone_content API.
        """
        resource_path = "/zones/{zoneNameOrId}/content"
        method = "GET"
        operation_name = "get_zone_content"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Zone/GetZoneContent"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "scope",
            "view_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_zone_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "text/dns",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_zone_records(self, zone_name_or_id, **kwargs):
        """
        Gets all records in the specified zone.

        The results are sorted by `domain` in alphabetical order by default. For more information about records,
        see `Resource Record (RR) TYPEs`__.
        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter
        then the viewId query parameter is required.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str zone_version: (optional)
            The version of the zone for which data is requested.

        :param str domain: (optional)
            Search by domain.
            Will match any record whose domain (case-insensitive) equals the provided value.

        :param str domain_contains: (optional)
            Search by domain.
            Will match any record whose domain (case-insensitive) contains the provided value.

        :param str rtype: (optional)
            Search by record type.
            Will match any record whose `type`__ (case-insensitive) equals the provided value.

            __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4

        :param str sort_by: (optional)
            The field by which to sort records.

            Allowed values are: "domain", "rtype", "ttl"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/get_zone_records.py.html>`__ to see an example of how to use get_zone_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records"
        method = "GET"
        operation_name = "get_zone_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/GetZoneRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "opc_request_id",
            "limit",
            "page",
            "zone_version",
            "domain",
            "domain_contains",
            "rtype",
            "sort_by",
            "sort_order",
            "compartment_id",
            "scope",
            "view_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_zone_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["domain", "rtype", "ttl"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "zoneVersion": kwargs.get("zone_version", missing),
            "domain": kwargs.get("domain", missing),
            "domainContains": kwargs.get("domain_contains", missing),
            "rtype": kwargs.get("rtype", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_resolver_endpoints(self, resolver_id, **kwargs):
        """
        Gets a list of all endpoints within a resolver. The collection can be filtered by name or lifecycle state.
        It can be sorted on creation time or name both in ASC or DESC order. Note that when no lifecycleState
        query parameter is provided, the collection does not include resolver endpoints in the DELETED
        lifecycle state to be consistent with other operations of the API.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str name: (optional)
            The name of a resource.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field by which to sort resolver endpoints.

            Allowed values are: "name", "timeCreated"

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.ResolverEndpointSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_resolver_endpoints.py.html>`__ to see an example of how to use list_resolver_endpoints API.
        """
        resource_path = "/resolvers/{resolverId}/endpoints"
        method = "GET"
        operation_name = "list_resolver_endpoints"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/ResolverEndpoint/ListResolverEndpoints"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "name",
            "page",
            "limit",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_resolver_endpoints got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "timeCreated"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ResolverEndpointSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ResolverEndpointSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_resolvers(self, compartment_id, **kwargs):
        """
        Gets a list of all resolvers within a compartment.

        The collection can be filtered by display name, id, or lifecycle state. It can be sorted
        on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState
        query parameter is provided, the collection does not include resolvers in the DELETED
        lifecycleState to be consistent with other operations of the API.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str display_name: (optional)
            The displayName of a resource.

        :param str id: (optional)
            The OCID of a resource.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field by which to sort resolvers.

            Allowed values are: "displayName", "timeCreated"

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.ResolverSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_resolvers.py.html>`__ to see an example of how to use list_resolvers API.
        """
        resource_path = "/resolvers"
        method = "GET"
        operation_name = "list_resolvers"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Resolver/ListResolvers"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "display_name",
            "id",
            "page",
            "limit",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_resolvers got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "timeCreated"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ResolverSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ResolverSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_steering_policies(self, compartment_id, **kwargs):
        """
        Gets a list of all steering policies in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str id: (optional)
            The OCID of a resource.

        :param str display_name: (optional)
            The displayName of a resource.

        :param str display_name_contains: (optional)
            The partial displayName of a resource. Will match any resource whose name
            (case-insensitive) contains the provided value.

        :param str health_check_monitor_id: (optional)
            Search by health check monitor OCID.
            Will match any resource whose health check monitor ID matches the provided value.

        :param datetime time_created_greater_than_or_equal_to: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created on or after the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param datetime time_created_less_than: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created before the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param str template: (optional)
            Search by steering template type.
            Will match any resource whose template type matches the provided value.

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING"

        :param str sort_by: (optional)
            The field by which to sort steering policies. If unspecified, defaults to `timeCreated`.

            Allowed values are: "displayName", "timeCreated", "template"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.SteeringPolicySummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_steering_policies.py.html>`__ to see an example of how to use list_steering_policies API.
        """
        resource_path = "/steeringPolicies"
        method = "GET"
        operation_name = "list_steering_policies"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicy/ListSteeringPolicies"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "id",
            "display_name",
            "display_name_contains",
            "health_check_monitor_id",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "template",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_steering_policies got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "timeCreated", "template"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "displayName": kwargs.get("display_name", missing),
            "displayNameContains": kwargs.get("display_name_contains", missing),
            "healthCheckMonitorId": kwargs.get("health_check_monitor_id", missing),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing),
            "template": kwargs.get("template", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SteeringPolicySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SteeringPolicySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_steering_policy_attachments(self, compartment_id, **kwargs):
        """
        Lists the steering policy attachments in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str id: (optional)
            The OCID of a resource.

        :param str display_name: (optional)
            The displayName of a resource.

        :param str steering_policy_id: (optional)
            Search by steering policy OCID.
            Will match any resource whose steering policy ID matches the provided value.

        :param str zone_id: (optional)
            Search by zone OCID.
            Will match any resource whose zone ID matches the provided value.

        :param str domain: (optional)
            Search by domain.
            Will match any record whose domain (case-insensitive) equals the provided value.

        :param str domain_contains: (optional)
            Search by domain.
            Will match any record whose domain (case-insensitive) contains the provided value.

        :param datetime time_created_greater_than_or_equal_to: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created on or after the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param datetime time_created_less_than: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created before the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "CREATING", "ACTIVE", "DELETING"

        :param str sort_by: (optional)
            The field by which to sort steering policy attachments. If unspecified, defaults to `timeCreated`.

            Allowed values are: "displayName", "timeCreated", "domainName"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.SteeringPolicyAttachmentSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_steering_policy_attachments.py.html>`__ to see an example of how to use list_steering_policy_attachments API.
        """
        resource_path = "/steeringPolicyAttachments"
        method = "GET"
        operation_name = "list_steering_policy_attachments"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicyAttachment/ListSteeringPolicyAttachments"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "id",
            "display_name",
            "steering_policy_id",
            "zone_id",
            "domain",
            "domain_contains",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_steering_policy_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "DELETING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "timeCreated", "domainName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "displayName": kwargs.get("display_name", missing),
            "steeringPolicyId": kwargs.get("steering_policy_id", missing),
            "zoneId": kwargs.get("zone_id", missing),
            "domain": kwargs.get("domain", missing),
            "domainContains": kwargs.get("domain_contains", missing),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SteeringPolicyAttachmentSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SteeringPolicyAttachmentSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_tsig_keys(self, compartment_id, **kwargs):
        """
        Gets a list of all TSIG keys in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str id: (optional)
            The OCID of a resource.

        :param str name: (optional)
            The name of a resource.

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"

        :param str sort_by: (optional)
            The field by which to sort TSIG keys. If unspecified, defaults to `timeCreated`.

            Allowed values are: "name", "timeCreated"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.TsigKeySummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_tsig_keys.py.html>`__ to see an example of how to use list_tsig_keys API.
        """
        resource_path = "/tsigKeys"
        method = "GET"
        operation_name = "list_tsig_keys"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/TsigKey/ListTsigKeys"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "id",
            "name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_tsig_keys got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "timeCreated"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[TsigKeySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[TsigKeySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_views(self, compartment_id, **kwargs):
        """
        Gets a list of all views within a compartment.

        The collection can be filtered by display name, id, or lifecycle state. It can be sorted
        on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState
        query parameter is provided, the collection does not include views in the DELETED
        lifecycleState to be consistent with other operations of the API.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str display_name: (optional)
            The displayName of a resource.

        :param str id: (optional)
            The OCID of a resource.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field by which to sort views.

            Allowed values are: "displayName", "timeCreated"

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "DELETED", "DELETING", "UPDATING"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.ViewSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_views.py.html>`__ to see an example of how to use list_views API.
        """
        resource_path = "/views"
        method = "GET"
        operation_name = "list_views"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/View/ListViews"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "display_name",
            "id",
            "page",
            "limit",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_views got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "timeCreated"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "DELETED", "DELETING", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ViewSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ViewSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_zone_transfer_servers(self, compartment_id, **kwargs):
        """
        Gets a list of IP addresses of OCI nameservers for inbound and outbound transfer of zones in the specified
        compartment (which must be the root compartment of a tenancy) that transfer zone data with external master or
        downstream nameservers.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.ZoneTransferServer`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_zone_transfer_servers.py.html>`__ to see an example of how to use list_zone_transfer_servers API.
        """
        resource_path = "/zoneTransferServers"
        method = "GET"
        operation_name = "list_zone_transfer_servers"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/ZoneTransferServer/ListZoneTransferServers"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "scope",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_zone_transfer_servers got unknown kwargs: {!r}".format(extra_kwargs))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "scope": kwargs.get("scope", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ZoneTransferServer]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ZoneTransferServer]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_zones(self, compartment_id, **kwargs):
        """
        Gets a list of all zones in the specified compartment.

        The collection can be filtered by name, time created, scope, associated view, and zone type.
        Filtering by view is only supported for private zones.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str name: (optional)
            A case-sensitive filter for zone names.
            Will match any zone with a name that equals the provided value.

        :param str name_contains: (optional)
            Search by zone name.
            Will match any zone whose name (case-insensitive) contains the provided value.

        :param str zone_type: (optional)
            Search by zone type, `PRIMARY` or `SECONDARY`.
            Will match any zone whose type equals the provided value.

            Allowed values are: "PRIMARY", "SECONDARY"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created on or after the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param datetime time_created_less_than: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created before the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"

        :param str sort_by: (optional)
            The field by which to sort zones.

            Allowed values are: "name", "zoneType", "timeCreated"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str tsig_key_id: (optional)
            Search for zones that are associated with a TSIG key.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.ZoneSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/list_zones.py.html>`__ to see an example of how to use list_zones API.
        """
        resource_path = "/zones"
        method = "GET"
        operation_name = "list_zones"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Zone/ListZones"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "name",
            "name_contains",
            "zone_type",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope",
            "view_id",
            "tsig_key_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_zones got unknown kwargs: {!r}".format(extra_kwargs))

        if 'zone_type' in kwargs:
            zone_type_allowed_values = ["PRIMARY", "SECONDARY"]
            if kwargs['zone_type'] not in zone_type_allowed_values:
                raise ValueError(
                    "Invalid value for `zone_type`, must be one of {0}".format(zone_type_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "zoneType", "timeCreated"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id,
            "name": kwargs.get("name", missing),
            "nameContains": kwargs.get("name_contains", missing),
            "zoneType": kwargs.get("zone_type", missing),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "tsigKeyId": kwargs.get("tsig_key_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ZoneSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ZoneSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def patch_domain_records(self, zone_name_or_id, domain, patch_domain_records_details, **kwargs):
        """
        Updates records in the specified zone at a domain.

        You can update one record or all records for the specified zone depending on the changes provided in the
        request body. You can also add or remove records using this function. When the zone name is provided as
        a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is
        required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param oci.dns.models.PatchDomainRecordsDetails patch_domain_records_details: (required)
            Operations describing how to modify the collection of records.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/patch_domain_records.py.html>`__ to see an example of how to use patch_domain_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "PATCH"
        operation_name = "patch_domain_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/PatchDomainRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "patch_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_domain_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_domain_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def patch_rr_set(self, zone_name_or_id, domain, rtype, patch_rr_set_details, **kwargs):
        """
        Updates records in the specified RRSet.

        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query
        parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param oci.dns.models.PatchRRSetDetails patch_rr_set_details: (required)
            Operations describing how to modify the collection of records.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/patch_rr_set.py.html>`__ to see an example of how to use patch_rr_set API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "PATCH"
        operation_name = "patch_rr_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/RRSet/PatchRrSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "patch_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_rr_set_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_rr_set_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def patch_zone_records(self, zone_name_or_id, patch_zone_records_details, **kwargs):
        """
        Updates a collection of records in the specified zone.

        You can update one record or all records for the specified zone depending on the changes provided in the
        request body. You can also add or remove records using this function. When the zone name is provided as
        a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is
        required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param oci.dns.models.PatchZoneRecordsDetails patch_zone_records_details: (required)
            The operations describing how to modify the collection of records.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/patch_zone_records.py.html>`__ to see an example of how to use patch_zone_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records"
        method = "PATCH"
        operation_name = "patch_zone_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/PatchZoneRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "patch_zone_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_zone_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_zone_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_domain_records(self, zone_name_or_id, domain, update_domain_records_details, **kwargs):
        """
        Replaces records in the specified zone at a domain with the records specified in the request body.

        If a specified record does not exist, it will be created. If the record exists, then it will be updated to
        represent the record in the body of the request. If a record in the zone does not exist in the request body,
        the record will be removed from the zone. When the zone name is provided as a path parameter and `PRIVATE`
        is used for the scope query parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param oci.dns.models.UpdateDomainRecordsDetails update_domain_records_details: (required)
            A full list of records for the domain.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_domain_records.py.html>`__ to see an example of how to use update_domain_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "PUT"
        operation_name = "update_domain_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/UpdateDomainRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_domain_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_domain_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_resolver(self, resolver_id, update_resolver_details, **kwargs):
        """
        Updates the specified resolver with your new information.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param oci.dns.models.UpdateResolverDetails update_resolver_details: (required)
            New data for the resolver.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Resolver`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_resolver.py.html>`__ to see an example of how to use update_resolver API.
        """
        resource_path = "/resolvers/{resolverId}"
        method = "PUT"
        operation_name = "update_resolver"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Resolver/UpdateResolver"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_resolver got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_resolver_details,
                response_type="Resolver",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_resolver_details,
                response_type="Resolver",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_resolver_endpoint(self, resolver_id, resolver_endpoint_name, update_resolver_endpoint_details, **kwargs):
        """
        Updates the specified resolver endpoint with your new information.


        :param str resolver_id: (required)
            The OCID of the target resolver.

        :param str resolver_endpoint_name: (required)
            The name of the target resolver endpoint.

        :param oci.dns.models.UpdateResolverEndpointDetails update_resolver_endpoint_details: (required)
            New data for the resolver endpoint.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.ResolverEndpoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_resolver_endpoint.py.html>`__ to see an example of how to use update_resolver_endpoint API.
        """
        resource_path = "/resolvers/{resolverId}/endpoints/{resolverEndpointName}"
        method = "PUT"
        operation_name = "update_resolver_endpoint"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/ResolverEndpoint/UpdateResolverEndpoint"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_resolver_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "resolverId": resolver_id,
            "resolverEndpointName": resolver_endpoint_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_resolver_endpoint_details,
                response_type="ResolverEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_resolver_endpoint_details,
                response_type="ResolverEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_rr_set(self, zone_name_or_id, domain, rtype, update_rr_set_details, **kwargs):
        """
        Replaces records in the specified RRSet.

        When the zone name is provided as a path parameter and `PRIVATE` is used for the scope
        query parameter then the viewId query parameter is required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param oci.dns.models.UpdateRRSetDetails update_rr_set_details: (required)
            A full list of records for the RRSet.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_rr_set.py.html>`__ to see an example of how to use update_rr_set API.
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "PUT"
        operation_name = "update_rr_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/RRSet/UpdateRrSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_rr_set_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_rr_set_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_steering_policy(self, steering_policy_id, update_steering_policy_details, **kwargs):
        """
        Updates the configuration of the specified steering policy.


        :param str steering_policy_id: (required)
            The OCID of the target steering policy.

        :param oci.dns.models.UpdateSteeringPolicyDetails update_steering_policy_details: (required)
            New data for the steering policy.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.SteeringPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_steering_policy.py.html>`__ to see an example of how to use update_steering_policy API.
        """
        resource_path = "/steeringPolicies/{steeringPolicyId}"
        method = "PUT"
        operation_name = "update_steering_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicy/UpdateSteeringPolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_steering_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyId": steering_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_steering_policy_details,
                response_type="SteeringPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_steering_policy_details,
                response_type="SteeringPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_steering_policy_attachment(self, steering_policy_attachment_id, update_steering_policy_attachment_details, **kwargs):
        """
        Updates the specified steering policy attachment with your new information.


        :param str steering_policy_attachment_id: (required)
            The OCID of the target steering policy attachment.

        :param oci.dns.models.UpdateSteeringPolicyAttachmentDetails update_steering_policy_attachment_details: (required)
            New data for the steering policy attachment.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.SteeringPolicyAttachment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_steering_policy_attachment.py.html>`__ to see an example of how to use update_steering_policy_attachment API.
        """
        resource_path = "/steeringPolicyAttachments/{steeringPolicyAttachmentId}"
        method = "PUT"
        operation_name = "update_steering_policy_attachment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/SteeringPolicyAttachment/UpdateSteeringPolicyAttachment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_steering_policy_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "steeringPolicyAttachmentId": steering_policy_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_steering_policy_attachment_details,
                response_type="SteeringPolicyAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_steering_policy_attachment_details,
                response_type="SteeringPolicyAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_tsig_key(self, tsig_key_id, update_tsig_key_details, **kwargs):
        """
        Updates the specified TSIG key.


        :param str tsig_key_id: (required)
            The OCID of the target TSIG key.

        :param oci.dns.models.UpdateTsigKeyDetails update_tsig_key_details: (required)
            New data for the TSIG key.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.TsigKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_tsig_key.py.html>`__ to see an example of how to use update_tsig_key API.
        """
        resource_path = "/tsigKeys/{tsigKeyId}"
        method = "PUT"
        operation_name = "update_tsig_key"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/TsigKey/UpdateTsigKey"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_tsig_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tsigKeyId": tsig_key_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_tsig_key_details,
                response_type="TsigKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_tsig_key_details,
                response_type="TsigKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_view(self, view_id, update_view_details, **kwargs):
        """
        Updates the specified view with your new information.


        :param str view_id: (required)
            The OCID of the target view.

        :param oci.dns.models.UpdateViewDetails update_view_details: (required)
            New data for the view.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.View`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_view.py.html>`__ to see an example of how to use update_view API.
        """
        resource_path = "/views/{viewId}"
        method = "PUT"
        operation_name = "update_view"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/View/UpdateView"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_view got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "viewId": view_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_view_details,
                response_type="View",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_view_details,
                response_type="View",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_zone(self, zone_name_or_id, update_zone_details, **kwargs):
        """
        Updates the zone with the specified information.

        Global secondary zones may have their external masters updated. For more information about secondary
        zones, see `Manage DNS Service Zone`__. When the zone name
        is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId
        query parameter is required.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param oci.dns.models.UpdateZoneDetails update_zone_details: (required)
            New data for the zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Zone`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_zone.py.html>`__ to see an example of how to use update_zone API.
        """
        resource_path = "/zones/{zoneNameOrId}"
        method = "PUT"
        operation_name = "update_zone"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Zone/UpdateZone"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_zone got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_details,
                response_type="Zone",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_details,
                response_type="Zone",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_zone_records(self, zone_name_or_id, update_zone_records_details, **kwargs):
        """
        Replaces records in the specified zone with the records specified in the request body.

        If a specified record does not exist, it will be created. If the record exists, then it will be updated
        to represent the record in the body of the request. If a record in the zone does not exist in the
        request body, the record will be removed from the zone. When the zone name is provided as a path
        parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is
        required.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param oci.dns.models.UpdateZoneRecordsDetails update_zone_records_details: (required)
            A full list of records for the zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need
            to contact Oracle about a particular request, please provide
            the request ID.

        :param str scope: (optional)
            Specifies to operate only on resources that have a matching DNS scope.

            Allowed values are: "GLOBAL", "PRIVATE"

        :param str view_id: (optional)
            The OCID of the view the resource is associated with.

        :param str compartment_id: (optional)
            The OCID of the compartment the zone belongs to.

            This parameter is deprecated and should be omitted.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.82.0/dns/update_zone_records.py.html>`__ to see an example of how to use update_zone_records API.
        """
        resource_path = "/zones/{zoneNameOrId}/records"
        method = "PUT"
        operation_name = "update_zone_records"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/dns/20180115/Records/UpdateZoneRecords"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "opc_request_id",
            "scope",
            "view_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_zone_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'scope' in kwargs:
            scope_allowed_values = ["GLOBAL", "PRIVATE"]
            if kwargs['scope'] not in scope_allowed_values:
                raise ValueError(
                    "Invalid value for `scope`, must be one of {0}".format(scope_allowed_values)
                )

        query_params = {
            "scope": kwargs.get("scope", missing),
            "viewId": kwargs.get("view_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_records_details,
                response_type="RecordCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
