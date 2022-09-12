# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerImageCollection(object):
    """
    List container image results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerImageCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this ContainerImageCollection.
        :type items: list[oci.artifacts.models.ContainerImageSummary]

        :param remaining_items_count:
            The value to assign to the remaining_items_count property of this ContainerImageCollection.
        :type remaining_items_count: int

        """
        self.swagger_types = {
            'items': 'list[ContainerImageSummary]',
            'remaining_items_count': 'int'
        }

        self.attribute_map = {
            'items': 'items',
            'remaining_items_count': 'remainingItemsCount'
        }

        self._items = None
        self._remaining_items_count = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ContainerImageCollection.
        Page of matching container images.


        :return: The items of this ContainerImageCollection.
        :rtype: list[oci.artifacts.models.ContainerImageSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ContainerImageCollection.
        Page of matching container images.


        :param items: The items of this ContainerImageCollection.
        :type: list[oci.artifacts.models.ContainerImageSummary]
        """
        self._items = items

    @property
    def remaining_items_count(self):
        """
        **[Required]** Gets the remaining_items_count of this ContainerImageCollection.
        Estimated number of remaining results.


        :return: The remaining_items_count of this ContainerImageCollection.
        :rtype: int
        """
        return self._remaining_items_count

    @remaining_items_count.setter
    def remaining_items_count(self, remaining_items_count):
        """
        Sets the remaining_items_count of this ContainerImageCollection.
        Estimated number of remaining results.


        :param remaining_items_count: The remaining_items_count of this ContainerImageCollection.
        :type: int
        """
        self._remaining_items_count = remaining_items_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
