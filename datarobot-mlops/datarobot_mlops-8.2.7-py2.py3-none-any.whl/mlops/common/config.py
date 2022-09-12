#  Copyright (c) 2019 DataRobot, Inc. and its affiliates. All rights reserved.
#  Last updated 2022.
#
#  DataRobot, Inc. Confidential.
#  This is unpublished proprietary source code of DataRobot, Inc. and its affiliates.
#  The copyright notice above does not evidence any actual or intended publication of
#  such source code.
#
#  This file and its contents are subject to DataRobot Tool and Utility Agreement.
#  For details, see
#  https://www.datarobot.com/wp-content/uploads/2021/07/DataRobot-Tool-and-Utility-Agreement.pdf.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import dict
from builtins import map
from builtins import int
from builtins import object
from builtins import str
import datarobot.mlops.install_aliases  # noqa: F401
from collections import namedtuple
import logging
import os

import six

from datarobot.mlops.common import exception
from datarobot.mlops.common.enums import SpoolerType
from datarobot.mlops.common.exception import (
    DRConfigKeyNotFound, DRUnsupportedType, DRCommonException
)

logger = logging.getLogger(__name__)

__prioritized_config = {}

ConfigKey = namedtuple("ConfigKey", ["name", "type"])

# DEPRECATED NAMES
# map old name --> new name
renameMap = {
    "MLOPS_OUTPUT_TYPE": "MLOPS_SPOOLER_TYPE",
    "MLOPS_SPOOLER_DIR_PATH": "MLOPS_FILESYSTEM_DIRECTORY",
    "MLOPS_SPOOLER_FILE_MAX_SIZE": "MLOPS_FILESYSTEM_MAX_FILE_SIZE",
    "MLOPS_SPOOLER_MAX_FILES": "MLOPS_FILESYSTEM_MAX_NUM_FILES",
    "MLOPS_RABBITMQ_URL": "MLOPS_RABBITMQ_QUEUE_URL"
}

# map old name --> new name
spoolerRemap = {
       "OUTPUT_DIR": "FILESYSTEM",
       "RABBIT_MQ": "RABBITMQ"
}


def get_new_name(name):
    for old_name, new_name in renameMap.items():
        if old_name.endswith(name.upper()):
            return new_name
    return None


def get_old_name(name):
    for old_name, new_name in renameMap.items():
        if name == new_name:
            return old_name
    return None


def get_config(config_key):
    value = os.environ.get(config_key.name)
    if value is None:
        # First check in env vars using new name, if not present
        # Then check if it is set programmatically
        if config_key.name in __prioritized_config:
            return __prioritized_config[config_key.name]

        old_name = get_old_name(config_key.name)
        if old_name is not None:
            value = os.environ.get(old_name)
        if value is None:
            # Similar to previous check, using old name
            if old_name in __prioritized_config:
                return __prioritized_config[old_name]
            else:
                raise DRConfigKeyNotFound(
                    "Config key '{}' not found. Export as an environment variable "
                    "or set programmatically.".format(config_key.name)
                )

    if config_key.name == ConfigConstants.SPOOLER_TYPE.name:
        # verify this is a valid SPOOLER type
        spooler_name = value.upper()
        try:
            _ = SpoolerType.from_name(spooler_name)
            return spooler_name
        except ValueError:
            # check whether this is an old name for a spooler type
            if spooler_name in spoolerRemap:
                spooler_name = spoolerRemap.get(spooler_name)
                return spooler_name
            else:
                raise DRCommonException("Invalid value for spooler_type: {}".format(value))

    if config_key.type == bool:
        return True if value.lower() in ["true", "yes", "1"] else False

    elif config_key.type == int:
        return int(value) if value else 0

    elif config_key.type == float:
        return float(value) if value else 0.0

    elif config_key.type == str:
        return value

    else:
        raise exception.DRUnsupportedType("Unsupported config variable type: {}"
                                          .format(config_key.type))


def get_config_default(config_key, default_val):
    try:
        return get_config(config_key)
    except DRConfigKeyNotFound:
        return default_val


def _set_config(config_key, value):
    # For Python 2.7 compatibility we need to treat the `str` type special.
    required_type = config_key.type if config_key.type != str else six.string_types

    if not isinstance(value, required_type):
        raise DRUnsupportedType("Wrong value type for config key {}. Expected: {}, provided: {}"
                                .format(config_key.name, config_key.type, type(value)))
    __prioritized_config[config_key.name] = value


def clear_config():
    __prioritized_config.clear()


def dump_config():
    # Query all the environment variables and add it to the dictionary
    config = {}
    for env_var in ConfigConstants.all():
        try:
            # get_config will get it either from environment or the actual
            # configured value
            config[env_var.name] = get_config(env_var)
        except (DRConfigKeyNotFound, DRCommonException):
            # If key not found, simply continue, we just want to get
            # all config in a dict
            continue
    return config


def set_channel_config_from_str(output_settings):
    """
    Configure multiple settings provided in a semicolon separated string.
    First split the setting into key=value params, then iterate over them
    setting the correct config key and value.

    :param output_settings:
    :return:
    :throw: exception.DRCommonException if provided string does not meet requirement
    """
    # Do not raise exception if empty, just return (nothing to configure)
    if not output_settings:
        return

    try:
        params = dict(map(lambda x: x.split("="), output_settings.split(";")))
    except ValueError:
        raise DRCommonException("Invalid output settings provided '{}' - 'key=value'"
                                " params separated by ';' required".format(output_settings))

    for key, value in params.items():
        config_key = ConfigConstants.get_config_key(key)

        if config_key is None:
            new_name = get_new_name(key)
            if new_name is not None:
                config_key = ConfigConstants.get_config_key(new_name)
            if config_key is None:
                raise DRCommonException("Invalid parameter '{}'".format(key))

        if config_key.type == bool:
            value = True if value.lower() in ["true", "yes", "1"] else False
        elif config_key.type == int:
            value = int(value) if value else 0
        elif config_key.type == float:
            value = float(value) if value else 0.0

        set_config_safely(config_key, value)


def set_config_safely(config_key, value):
    """
    Allow setting a given configuration only once.

    :param config_key:  a config key of a 'ConfigKey' type
    :param value:  the config value
    :return:
    :throw:  exception.DRConfigKeyAlreadyAssigned if the given config key was already configured
             programmatically before
    """
    if config_key.name == ConfigConstants.SPOOLER_TYPE.name:
        # verify this is a valid SPOOLER type
        spooler_name = value
        if spooler_name.upper() in spoolerRemap:
            spooler_name = spoolerRemap.get(spooler_name.upper())
        try:
            _ = SpoolerType.from_name(spooler_name)
        except ValueError:
            raise DRCommonException("Invalid value for spooler_type: {}".format(value))
        value = spooler_name

    if config_key.name in __prioritized_config:
        raise exception.DRConfigKeyAlreadyAssigned(
            "Config key already configured. key: {}, prev-value:{}, new-value: {}"
            .format(config_key.name, __prioritized_config[config_key.name], value))

    _set_config(config_key, value)


class ConfigKeys(object):
    # string definitions
    MLOPS_FEATURE_DATA_ROWS_IN_ONE_MESSAGE_STR = "MLOPS_FEATURE_DATA_ROWS_IN_ONE_MESSAGE"


class ConfigConstants(object):

    # general configuration
    DEPLOYMENT_ID = ConfigKey("MLOPS_DEPLOYMENT_ID", str)
    MODEL_ID = ConfigKey("MLOPS_MODEL_ID", str)

    FEATURE_TYPES_FILENAME = ConfigKey("MLOPS_FEATURE_TYPES_FILENAME", str)
    FEATURE_TYPES_JSON = ConfigKey("MLOPS_FEATURE_TYPES_JSON", str)

    # mlops async queuing configuration
    ASYNC_REPORTING = ConfigKey("MLOPS_ASYNC_REPORTING", bool)
    REPORT_QUEUE_NUM_LISTS = ConfigKey("MLOPS_REPORT_QUEUE_NUM_LISTS", int)
    REPORT_QUEUE_LIST_SIZE = ConfigKey("MLOPS_REPORT_QUEUE_LIST_SIZE", int)
    REPORT_QUEUE_MAX_SIZE = ConfigKey("MLOPS_REPORT_QUEUE_MAX_SIZE", int)
    TIMEOUT_PROCESS_QUEUE_MS = ConfigKey("MLOPS_TIMEOUT_PROCESS_QUEUE_MS", int)

    # spooler-generic configuration
    SPOOLER_TYPE = ConfigKey("MLOPS_SPOOLER_TYPE", str)
    SPOOLER_ACTION = ConfigKey("MLOPS_SPOOLER_ACTION", str)
    SPOOLER_CHECKSUM = ConfigKey("MLOPS_SPOOLER_CHECKSUM", bool)
    FEATURE_DATA_ROWS_IN_ONE_MESSAGE = ConfigKey(
        ConfigKeys.MLOPS_FEATURE_DATA_ROWS_IN_ONE_MESSAGE_STR, int)
    SPOOLER_DATA_FORMAT = ConfigKey("MLOPS_SPOOLER_DATA_FORMAT", str)
    SPOOLER_DEQUEUE_ACK_RECORDS = ConfigKey("MLOPS_SPOOLER_DEQUEUE_ACK_RECORDS", bool)
    SPOOLER_DEQUEUE_MAX_RECORDS_PER_CALL = ConfigKey(
        "MLOPS_SPOOLER_DEQUEUE_MAX_RECORDS_PER_CALL", int
    )

    # spooler-specific configuration
    FILESYSTEM_DIRECTORY = ConfigKey("MLOPS_FILESYSTEM_DIRECTORY", str)
    FILESYSTEM_MAX_FILE_SIZE = ConfigKey("MLOPS_FILESYSTEM_MAX_FILE_SIZE", int)
    FILESYSTEM_MAX_NUM_FILES = ConfigKey("MLOPS_FILESYSTEM_MAX_NUM_FILES", int)
    FILESYSTEM_ACK_DEADLINE_STR = ConfigKey("MLOPS_FILESYSTEM_ACKNOWLEDGEMENT_DEADLINE", int)

    SQS_QUEUE_URL = ConfigKey("MLOPS_SQS_QUEUE_URL", str)
    SQS_QUEUE_NAME = ConfigKey("MLOPS_SQS_QUEUE_NAME", str)  # used for testing purposes only

    RABBITMQ_QUEUE_URL = ConfigKey("MLOPS_RABBITMQ_QUEUE_URL", str)
    RABBITMQ_QUEUE_NAME = ConfigKey("MLOPS_RABBITMQ_QUEUE_NAME", str)
    RABBITMQ_SSL_CERTIFICATE_PATH = ConfigKey("MLOPS_RABBITMQ_SSL_CERTIFICATE_PATH", str)
    RABBITMQ_SSL_KEYFILE_PATH = ConfigKey("MLOPS_RABBITMQ_SSL_KEYFILE_PATH", str)
    RABBITMQ_SSL_CA_CERTIFICATE_PATH = ConfigKey("MLOPS_RABBITMQ_SSL_CA_CERTIFICATE_PATH", str)
    RABBITMQ_SSL_TLS_VERSION = ConfigKey("MLOPS_RABBITMQ_SSL_TLS_VERSION", str)

    PUBSUB_PROJECT_ID = ConfigKey("MLOPS_PUBSUB_PROJECT_ID", str)
    PUBSUB_TOPIC_NAME = ConfigKey("MLOPS_PUBSUB_TOPIC_NAME", str)
    PUBSUB_MAX_FLUSH_SECONDS = ConfigKey("MLOPS_PUBSUB_MAX_FLUSH_SECONDS", int)
    PUBSUB_SUBSCRIPTION_NAME = ConfigKey("MLOPS_PUBSUB_SUBSCRIPTION_NAME", str)
    PUBSUB_ACK_DEADLINE_SECONDS = ConfigKey("MLOPS_PUBSUB_ACK_DEADLINE", int)

    MEMORY_MAX_QUEUE_SIZE = ConfigKey("MLOPS_MEMORY_MAX_QUEUE_SIZE", int)
    ASYNC_MEMORY_URL = ConfigKey("MLOPS_ASYNC_MEMORY_URL", str)
    ASYNC_MEMORY_ENQUEUE_DELAY_MS = ConfigKey("MLOPS_ASYNC_MEMORY_ENQUEUE_DELAY_MS", int)
    ASYNC_MEMORY_DEQUEUE_DELAY_MS = ConfigKey("MLOPS_ASYNC_MEMORY_DEQUEUE_DELAY_MS", int)

    KAFKA_TOPIC_NAME = ConfigKey("MLOPS_KAFKA_TOPIC_NAME", str)
    KAFKA_BOOTSTRAP_SERVERS = ConfigKey("MLOPS_KAFKA_BOOTSTRAP_SERVERS", str)
    KAFKA_MAX_FLUSH_MS = ConfigKey("MLOPS_KAFKA_MAX_FLUSH_MS", int)
    KAFKA_BUFFER_MAX_KB = ConfigKey("MLOPS_KAFKA_BUFFER_MAX_KB", int)
    KAFKA_CONSUMER_GROUP_ID = ConfigKey("MLOPS_KAFKA_CONSUMER_GROUP_ID", str)
    KAFKA_CONSUMER_POLL_TIMEOUT_MS = ConfigKey("MLOPS_KAFKA_CONSUMER_POLL_TIMEOUT_MS", int)
    KAFKA_CONSUMER_MAX_NUM_MESSAGES = ConfigKey("MLOPS_KAFKA_CONSUMER_MAX_NUM_MESSAGES", int)
    KAFKA_MESSAGE_BYTE_SIZE_LIMIT = ConfigKey("MLOPS_KAFKA_MESSAGE_BYTE_SIZE_LIMIT", int)
    KAFKA_ACK_DEADLINE_STR = ConfigKey("MLOPS_KAFKA_ACK_DEADLINE", int)
    KAFKA_REQUEST_TIMEOUT_MS = ConfigKey("MLOPS_KAFKA_REQUEST_TIMEOUT_MS", int)
    KAFKA_SESSION_TIMEOUT_MS = ConfigKey("MLOPS_KAFKA_SESSION_TIMEOUT_MS", int)
    KAFKA_DELIVERY_TIMEOUT_MS = ConfigKey("MLOPS_KAFKA_DELIVERY_TIMEOUT_MS", int)
    KAFKA_SOCKET_TIMEOUT_MS = ConfigKey("MLOPS_KAFKA_SOCKET_TIMEOUT_MS", int)
    KAFKA_METADATA_MAX_AGE_MS = ConfigKey("MLOPS_KAFKA_METADATA_MAX_AGE_MS", int)
    KAFKA_LINGER_MS = ConfigKey("MLOPS_KAFKA_LINGER_MS", int)
    KAFKA_SECURITY_PROTOCOL = ConfigKey("MLOPS_KAFKA_SECURITY_PROTOCOL", str)
    KAFKA_SSL_CA_LOCATION = ConfigKey("MLOPS_KAFKA_SSL_CA_LOCATION", str)
    KAFKA_SSL_KEY_LOCATION = ConfigKey("MLOPS_KAFKA_SSL_KEY_LOCATION", str)
    KAFKA_SSL_KEY_PASSWORD = ConfigKey("MLOPS_KAFKA_SSL_KEY_PASSWORD", str)
    KAFKA_SASL_MECHANISM = ConfigKey("MLOPS_KAFKA_SASL_MECHANISM", str)
    KAFKA_SASL_USERNAME = ConfigKey("MLOPS_KAFKA_SASL_USERNAME", str)
    KAFKA_SASL_PASSWORD = ConfigKey("MLOPS_KAFKA_SASL_PASSWORD", str)
    KAFKA_SASL_OAUTHBEARER_CONFIG = ConfigKey("MLOPS_KAFKA_SASL_OAUTHBEARER_CONFIG", str)
    KAFKA_SOCKET_KEEPALIVE = ConfigKey("MLOPS_KAFKA_SOCKET_KEEPALIVE", bool)

    STATS_AGGREGATION_HISTOGRAM_BIN_COUNT = ConfigKey(
        "MLOPS_STATS_AGGREGATION_HISTOGRAM_BIN_COUNT", int)
    STATS_AGGREGATION_DISTINCT_CATEGORY_COUNT = ConfigKey(
        "MLOPS_STATS_AGGREGATION_DISTINCT_CATEGORY_COUNT", int)
    STATS_AGGREGATION_MAX_RECORDS = ConfigKey("MLOPS_STATS_AGGREGATION_MAX_RECORDS", int)
    STATS_AGGREGATION_SEGMENT_VALUE_COUNT = ConfigKey(
        "MLOPS_STATS_AGGREGATION_SEGMENT_VALUE_COUNT", int)
    STATS_AGGREGATION_SEGMENT_ATTRIBUTES = ConfigKey(
        "MLOPS_STATS_AGGREGATION_SEGMENT_ATTRIBUTES", str)
    STATS_AGGREGATION_PREDICTION_TS_COLUMN_NAME = ConfigKey(
        "MLOPS_STATS_AGGREGATION_PREDICTION_TS_COLUMN_NAME", str)
    STATS_AGGREGATION_PREDICTION_TS_COLUMN_FORMAT = ConfigKey(
        "MLOPS_STATS_AGGREGATION_PREDICTION_TS_COLUMN_FORMAT", str)

    @staticmethod
    def get_config_key(name):
        found = []
        for attr in ConfigConstants.__dict__:
            attr_val = getattr(ConfigConstants, attr)
            if isinstance(attr_val, ConfigKey) and attr_val.name.endswith(name.upper()):
                found.append(attr_val)
        if not found:
            return None
        elif len(found) == 1:
            return found[0]
        else:
            logger.warning("Key '%s' is ambiguous and in the future this warning will be an error."
                           " We have resolved it to config '%s' out of: %s. Please qualify the"
                           " config key more to disambiguate it in the future.",
                           name, found[0], found)
            return found[0]

    @classmethod
    def all(cls):
        attr_names = []
        for attr in ConfigConstants.__dict__:
            attr_val = getattr(ConfigConstants, attr)
            if isinstance(attr_val, ConfigKey) and attr_val.name.startswith("MLOPS"):
                attr_names.append(attr_val)
        return attr_names
