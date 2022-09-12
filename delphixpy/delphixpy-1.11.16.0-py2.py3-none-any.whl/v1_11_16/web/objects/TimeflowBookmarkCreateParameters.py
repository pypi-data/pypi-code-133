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
#     /delphix-timeflow-bookmark-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_16 import factory
from delphixpy.v1_11_16 import common

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

class TimeflowBookmarkCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.TypedObject` *)* The parameters to
    use as input to create TimeFlow bookmarks.
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowBookmarkCreateParameters, self).__init__()
        self._type = ("TimeflowBookmarkCreateParameters", True)
        self._timeflow_point = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._tag = (self.__undef__, True)
        self._retention_proof = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowBookmarkCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "timeflowPoint" not in data:
            raise ValueError("Missing required property \"timeflowPoint\".")
        if "timeflowPoint" in data and data["timeflowPoint"] is not None:
            obj._timeflow_point = (factory.create_object(data["timeflowPoint"], "TimeflowPoint"), dirty)
            factory.validate_type(obj._timeflow_point[0], "TimeflowPoint")
        else:
            obj._timeflow_point = (obj.__undef__, dirty)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", None, 64)
        obj._retention_proof = (data.get("retentionProof", obj.__undef__), dirty)
        if obj._retention_proof[0] is not None and obj._retention_proof[0] is not obj.__undef__:
            assert isinstance(obj._retention_proof[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._retention_proof[0], type(obj._retention_proof[0])))
            common.validate_format(obj._retention_proof[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowBookmarkCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "timeflow_point" == "type" or (self.timeflow_point is not self.__undef__ and (not (dirty and not self._timeflow_point[1]) or isinstance(self.timeflow_point, list) or belongs_to_parent)):
            dct["timeflowPoint"] = dictify(self.timeflow_point, prop_is_list_or_vo=True)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]) or isinstance(self.tag, list) or belongs_to_parent)):
            dct["tag"] = dictify(self.tag)
        if "retention_proof" == "type" or (self.retention_proof is not self.__undef__ and (not (dirty and not self._retention_proof[1]) or isinstance(self.retention_proof, list) or belongs_to_parent)):
            dct["retentionProof"] = dictify(self.retention_proof)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._timeflow_point = (self._timeflow_point[0], True)
        self._name = (self._name[0], True)
        self._tag = (self._tag[0], True)
        self._retention_proof = (self._retention_proof[0], True)

    def is_dirty(self):
        return any([self._timeflow_point[1], self._name[1], self._tag[1], self._retention_proof[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowBookmarkCreateParameters):
            return False
        return super(TimeflowBookmarkCreateParameters, self).__eq__(other) and \
               self.timeflow_point == other.timeflow_point and \
               self.name == other.name and \
               self.tag == other.tag and \
               self.retention_proof == other.retention_proof

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def timeflow_point(self):
        """
        The TimeFlow point which is referenced by this bookmark.

        :rtype: :py:class:`v1_11_16.web.vo.TimeflowPoint`
        """
        return self._timeflow_point[0]

    @timeflow_point.setter
    def timeflow_point(self, value):
        self._timeflow_point = (value, True)

    @property
    def name(self):
        """
        The bookmark name.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def tag(self):
        """
        A tag for the bookmark that can be used to group bookmarks together or
        qualify the type of the bookmark.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

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

