# coding: utf8
#
# Copyright 2022 by Delphix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This class has been automatically generated from:
#     /delphix-timeflow-bookmark.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_7_1 import common

class __Undef(object):
    def __repr__(self):
        return "undef"

    def __setattr__(self, name, value):
        raise Exception('Cannot modify attributes of __Undef.')

_UNDEFINED = __Undef()

try:
    TEXT_TYPE = unicode
except NameError:
    TEXT_TYPE = str

class TimeflowBookmark(NamedUserObject):
    """
    *(extends* :py:class:`v1_7_1.web.vo.NamedUserObject` *)* A TimeFlow
    bookmark is a user defined name for a TimeFlow point (location or timestamp
    within a TimeFlow).
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowBookmark, self).__init__()
        self._type = ("TimeflowBookmark", True)
        self._location = (self.__undef__, True)
        self._retention_proof = (self.__undef__, True)
        self._tag = (self.__undef__, True)
        self._timeflow = (self.__undef__, True)
        self._timestamp = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowBookmark, cls).from_dict(data, dirty, undef_enabled)
        obj._location = (data.get("location", obj.__undef__), dirty)
        if obj._location[0] is not None and obj._location[0] is not obj.__undef__:
            assert isinstance(obj._location[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._location[0], type(obj._location[0])))
            common.validate_format(obj._location[0], "None", None, None)
        obj._retention_proof = (data.get("retentionProof", obj.__undef__), dirty)
        if obj._retention_proof[0] is not None and obj._retention_proof[0] is not obj.__undef__:
            assert isinstance(obj._retention_proof[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._retention_proof[0], type(obj._retention_proof[0])))
            common.validate_format(obj._retention_proof[0], "None", None, None)
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", None, 64)
        if "timeflow" not in data:
            raise ValueError("Missing required property \"timeflow\".")
        obj._timeflow = (data.get("timeflow", obj.__undef__), dirty)
        if obj._timeflow[0] is not None and obj._timeflow[0] is not obj.__undef__:
            assert isinstance(obj._timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timeflow[0], type(obj._timeflow[0])))
            common.validate_format(obj._timeflow[0], "objectReference", None, None)
        obj._timestamp = (data.get("timestamp", obj.__undef__), dirty)
        if obj._timestamp[0] is not None and obj._timestamp[0] is not obj.__undef__:
            assert isinstance(obj._timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timestamp[0], type(obj._timestamp[0])))
            common.validate_format(obj._timestamp[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowBookmark, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "location" == "type" or (self.location is not self.__undef__ and (not (dirty and not self._location[1]))):
            dct["location"] = dictify(self.location)
        if "retention_proof" == "type" or (self.retention_proof is not self.__undef__ and (not (dirty and not self._retention_proof[1]) or isinstance(self.retention_proof, list) or belongs_to_parent)):
            dct["retentionProof"] = dictify(self.retention_proof)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]))):
            dct["tag"] = dictify(self.tag)
        if "timeflow" == "type" or (self.timeflow is not self.__undef__ and (not (dirty and not self._timeflow[1]) or isinstance(self.timeflow, list) or belongs_to_parent)):
            dct["timeflow"] = dictify(self.timeflow)
        if "timestamp" == "type" or (self.timestamp is not self.__undef__ and (not (dirty and not self._timestamp[1]))):
            dct["timestamp"] = dictify(self.timestamp)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._location = (self._location[0], True)
        self._retention_proof = (self._retention_proof[0], True)
        self._tag = (self._tag[0], True)
        self._timeflow = (self._timeflow[0], True)
        self._timestamp = (self._timestamp[0], True)

    def is_dirty(self):
        return any([self._location[1], self._retention_proof[1], self._tag[1], self._timeflow[1], self._timestamp[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowBookmark):
            return False
        return super(TimeflowBookmark, self).__eq__(other) and \
               self.location == other.location and \
               self.retention_proof == other.retention_proof and \
               self.tag == other.tag and \
               self.timeflow == other.timeflow and \
               self.timestamp == other.timestamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def location(self):
        """
        The TimeFlow location.

        :rtype: ``TEXT_TYPE``
        """
        return self._location[0]

    @location.setter
    def location(self, value):
        self._location = (value, True)

    @property
    def retention_proof(self):
        """
        Indicates whether retention should be allowed to clean up the TimeFlow
        bookmark and associated data.

        :rtype: ``bool``
        """
        return self._retention_proof[0]

    @retention_proof.setter
    def retention_proof(self, value):
        self._retention_proof = (value, True)

    @property
    def tag(self):
        """
        A tag for the bookmark that can be used to group TimeFlow bookmarks
        together or qualify the type of the bookmark.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

    @property
    def timeflow(self):
        """
        Reference to the TimeFlow for this bookmark.

        :rtype: ``TEXT_TYPE``
        """
        return self._timeflow[0]

    @timeflow.setter
    def timeflow(self, value):
        self._timeflow = (value, True)

    @property
    def timestamp(self):
        """
        The logical time corresponding to the TimeFlow location.

        :rtype: ``TEXT_TYPE``
        """
        return self._timestamp[0]

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = (value, True)

