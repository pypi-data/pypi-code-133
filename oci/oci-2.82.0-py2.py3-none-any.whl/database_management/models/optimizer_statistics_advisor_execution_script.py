# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerStatisticsAdvisorExecutionScript(object):
    """
    The Oracle system-generated script for the Optimizer Statistics Advisor execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerStatisticsAdvisorExecutionScript object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param script:
            The value to assign to the script property of this OptimizerStatisticsAdvisorExecutionScript.
        :type script: str

        """
        self.swagger_types = {
            'script': 'str'
        }

        self.attribute_map = {
            'script': 'script'
        }

        self._script = None

    @property
    def script(self):
        """
        **[Required]** Gets the script of this OptimizerStatisticsAdvisorExecutionScript.
        The Optimizer Statistics Advisor execution script.


        :return: The script of this OptimizerStatisticsAdvisorExecutionScript.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this OptimizerStatisticsAdvisorExecutionScript.
        The Optimizer Statistics Advisor execution script.


        :param script: The script of this OptimizerStatisticsAdvisorExecutionScript.
        :type: str
        """
        self._script = script

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
