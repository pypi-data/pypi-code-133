# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiffChunk(object):
    """
    Details about a group of changes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiffChunk object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param base_line:
            The value to assign to the base_line property of this DiffChunk.
        :type base_line: int

        :param base_span:
            The value to assign to the base_span property of this DiffChunk.
        :type base_span: int

        :param target_line:
            The value to assign to the target_line property of this DiffChunk.
        :type target_line: int

        :param target_span:
            The value to assign to the target_span property of this DiffChunk.
        :type target_span: int

        :param diff_sections:
            The value to assign to the diff_sections property of this DiffChunk.
        :type diff_sections: list[oci.devops.models.DiffSection]

        """
        self.swagger_types = {
            'base_line': 'int',
            'base_span': 'int',
            'target_line': 'int',
            'target_span': 'int',
            'diff_sections': 'list[DiffSection]'
        }

        self.attribute_map = {
            'base_line': 'baseLine',
            'base_span': 'baseSpan',
            'target_line': 'targetLine',
            'target_span': 'targetSpan',
            'diff_sections': 'diffSections'
        }

        self._base_line = None
        self._base_span = None
        self._target_line = None
        self._target_span = None
        self._diff_sections = None

    @property
    def base_line(self):
        """
        Gets the base_line of this DiffChunk.
        Line number in base version where changes begin.


        :return: The base_line of this DiffChunk.
        :rtype: int
        """
        return self._base_line

    @base_line.setter
    def base_line(self, base_line):
        """
        Sets the base_line of this DiffChunk.
        Line number in base version where changes begin.


        :param base_line: The base_line of this DiffChunk.
        :type: int
        """
        self._base_line = base_line

    @property
    def base_span(self):
        """
        Gets the base_span of this DiffChunk.
        Number of lines chunk spans in base version.


        :return: The base_span of this DiffChunk.
        :rtype: int
        """
        return self._base_span

    @base_span.setter
    def base_span(self, base_span):
        """
        Sets the base_span of this DiffChunk.
        Number of lines chunk spans in base version.


        :param base_span: The base_span of this DiffChunk.
        :type: int
        """
        self._base_span = base_span

    @property
    def target_line(self):
        """
        Gets the target_line of this DiffChunk.
        Line number in target version where changes begin.


        :return: The target_line of this DiffChunk.
        :rtype: int
        """
        return self._target_line

    @target_line.setter
    def target_line(self, target_line):
        """
        Sets the target_line of this DiffChunk.
        Line number in target version where changes begin.


        :param target_line: The target_line of this DiffChunk.
        :type: int
        """
        self._target_line = target_line

    @property
    def target_span(self):
        """
        Gets the target_span of this DiffChunk.
        Number of lines chunk spans in target version.


        :return: The target_span of this DiffChunk.
        :rtype: int
        """
        return self._target_span

    @target_span.setter
    def target_span(self, target_span):
        """
        Sets the target_span of this DiffChunk.
        Number of lines chunk spans in target version.


        :param target_span: The target_span of this DiffChunk.
        :type: int
        """
        self._target_span = target_span

    @property
    def diff_sections(self):
        """
        Gets the diff_sections of this DiffChunk.
        List of difference section.


        :return: The diff_sections of this DiffChunk.
        :rtype: list[oci.devops.models.DiffSection]
        """
        return self._diff_sections

    @diff_sections.setter
    def diff_sections(self, diff_sections):
        """
        Sets the diff_sections of this DiffChunk.
        List of difference section.


        :param diff_sections: The diff_sections of this DiffChunk.
        :type: list[oci.devops.models.DiffSection]
        """
        self._diff_sections = diff_sections

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
