# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Line(object):
    """
    The line of text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Line object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this Line.
        :type text: str

        :param confidence:
            The value to assign to the confidence property of this Line.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this Line.
        :type bounding_polygon: oci.ai_vision.models.BoundingPolygon

        :param word_indexes:
            The value to assign to the word_indexes property of this Line.
        :type word_indexes: list[int]

        """
        self.swagger_types = {
            'text': 'str',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon',
            'word_indexes': 'list[int]'
        }

        self.attribute_map = {
            'text': 'text',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon',
            'word_indexes': 'wordIndexes'
        }

        self._text = None
        self._confidence = None
        self._bounding_polygon = None
        self._word_indexes = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this Line.
        The text recognized.


        :return: The text of this Line.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Line.
        The text recognized.


        :param text: The text of this Line.
        :type: str
        """
        self._text = text

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this Line.
        The confidence score between 0 and 1.


        :return: The confidence of this Line.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Line.
        The confidence score between 0 and 1.


        :param confidence: The confidence of this Line.
        :type: float
        """
        self._confidence = confidence

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this Line.

        :return: The bounding_polygon of this Line.
        :rtype: oci.ai_vision.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this Line.

        :param bounding_polygon: The bounding_polygon of this Line.
        :type: oci.ai_vision.models.BoundingPolygon
        """
        self._bounding_polygon = bounding_polygon

    @property
    def word_indexes(self):
        """
        **[Required]** Gets the word_indexes of this Line.
        The array of words.


        :return: The word_indexes of this Line.
        :rtype: list[int]
        """
        return self._word_indexes

    @word_indexes.setter
    def word_indexes(self, word_indexes):
        """
        Sets the word_indexes of this Line.
        The array of words.


        :param word_indexes: The word_indexes of this Line.
        :type: list[int]
        """
        self._word_indexes = word_indexes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
