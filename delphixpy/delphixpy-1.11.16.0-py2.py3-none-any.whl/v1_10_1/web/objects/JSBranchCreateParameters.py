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
#     /delphix-js-branch-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_1 import factory
from delphixpy.v1_10_1 import common

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

class JSBranchCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_10_1.web.vo.TypedObject` *)* The parameters used
    to create a Self-Service branch.
    """
    def __init__(self, undef_enabled=True):
        super(JSBranchCreateParameters, self).__init__()
        self._type = ("JSBranchCreateParameters", True)
        self._name = (self.__undef__, True)
        self._data_container = (self.__undef__, True)
        self._timeline_point_parameters = (self.__undef__, True)

    API_VERSION = "1.10.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSBranchCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        if "dataContainer" not in data:
            raise ValueError("Missing required property \"dataContainer\".")
        obj._data_container = (data.get("dataContainer", obj.__undef__), dirty)
        if obj._data_container[0] is not None and obj._data_container[0] is not obj.__undef__:
            assert isinstance(obj._data_container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_container[0], type(obj._data_container[0])))
            common.validate_format(obj._data_container[0], "objectReference", None, None)
        if "timelinePointParameters" not in data:
            raise ValueError("Missing required property \"timelinePointParameters\".")
        if "timelinePointParameters" in data and data["timelinePointParameters"] is not None:
            obj._timeline_point_parameters = (factory.create_object(data["timelinePointParameters"], "JSTimelinePointParameters"), dirty)
            factory.validate_type(obj._timeline_point_parameters[0], "JSTimelinePointParameters")
        else:
            obj._timeline_point_parameters = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSBranchCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "data_container" == "type" or (self.data_container is not self.__undef__ and (not (dirty and not self._data_container[1]) or isinstance(self.data_container, list) or belongs_to_parent)):
            dct["dataContainer"] = dictify(self.data_container)
        if "timeline_point_parameters" == "type" or (self.timeline_point_parameters is not self.__undef__ and (not (dirty and not self._timeline_point_parameters[1]) or isinstance(self.timeline_point_parameters, list) or belongs_to_parent)):
            dct["timelinePointParameters"] = dictify(self.timeline_point_parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._name = (self._name[0], True)
        self._data_container = (self._data_container[0], True)
        self._timeline_point_parameters = (self._timeline_point_parameters[0], True)

    def is_dirty(self):
        return any([self._name[1], self._data_container[1], self._timeline_point_parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSBranchCreateParameters):
            return False
        return super(JSBranchCreateParameters, self).__eq__(other) and \
               self.name == other.name and \
               self.data_container == other.data_container and \
               self.timeline_point_parameters == other.timeline_point_parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def name(self):
        """
        The name of the branch.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def data_container(self):
        """
        A reference to the data container to create this branch on.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_container[0]

    @data_container.setter
    def data_container(self, value):
        self._data_container = (value, True)

    @property
    def timeline_point_parameters(self):
        """
        The Self-Service data timeline point from which the branch will be
        created.

        :rtype: :py:class:`v1_10_1.web.vo.JSTimelinePointParameters`
        """
        return self._timeline_point_parameters[0]

    @timeline_point_parameters.setter
    def timeline_point_parameters(self, value):
        self._timeline_point_parameters = (value, True)

