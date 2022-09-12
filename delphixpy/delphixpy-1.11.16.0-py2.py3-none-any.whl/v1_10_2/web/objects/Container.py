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
#     /delphix-container.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_10_2 import factory
from delphixpy.v1_10_2 import common

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

class Container(NamedUserObject):
    """
    *(extends* :py:class:`v1_10_2.web.vo.NamedUserObject` *)* A container
    holding data.
    """
    def __init__(self, undef_enabled=True):
        super(Container, self).__init__()
        self._type = ("Container", True)
        self._group = (self.__undef__, True)
        self._provision_container = (self.__undef__, True)
        self._creation_time = (self.__undef__, True)
        self._current_timeflow = (self.__undef__, True)
        self._previous_timeflow = (self.__undef__, True)
        self._description = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._transformation = (self.__undef__, True)
        self._masked = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Container, cls).from_dict(data, dirty, undef_enabled)
        obj._group = (data.get("group", obj.__undef__), dirty)
        if obj._group[0] is not None and obj._group[0] is not obj.__undef__:
            assert isinstance(obj._group[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._group[0], type(obj._group[0])))
            common.validate_format(obj._group[0], "objectReference", None, None)
        obj._provision_container = (data.get("provisionContainer", obj.__undef__), dirty)
        if obj._provision_container[0] is not None and obj._provision_container[0] is not obj.__undef__:
            assert isinstance(obj._provision_container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._provision_container[0], type(obj._provision_container[0])))
            common.validate_format(obj._provision_container[0], "objectReference", None, None)
        obj._creation_time = (data.get("creationTime", obj.__undef__), dirty)
        if obj._creation_time[0] is not None and obj._creation_time[0] is not obj.__undef__:
            assert isinstance(obj._creation_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._creation_time[0], type(obj._creation_time[0])))
            common.validate_format(obj._creation_time[0], "date", None, None)
        obj._current_timeflow = (data.get("currentTimeflow", obj.__undef__), dirty)
        if obj._current_timeflow[0] is not None and obj._current_timeflow[0] is not obj.__undef__:
            assert isinstance(obj._current_timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._current_timeflow[0], type(obj._current_timeflow[0])))
            common.validate_format(obj._current_timeflow[0], "objectReference", None, None)
        obj._previous_timeflow = (data.get("previousTimeflow", obj.__undef__), dirty)
        if obj._previous_timeflow[0] is not None and obj._previous_timeflow[0] is not obj.__undef__:
            assert isinstance(obj._previous_timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._previous_timeflow[0], type(obj._previous_timeflow[0])))
            common.validate_format(obj._previous_timeflow[0], "objectReference", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, 1024)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "DBContainerRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "DBContainerRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        obj._transformation = (data.get("transformation", obj.__undef__), dirty)
        if obj._transformation[0] is not None and obj._transformation[0] is not obj.__undef__:
            assert isinstance(obj._transformation[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._transformation[0], type(obj._transformation[0])))
            common.validate_format(obj._transformation[0], "None", None, None)
        obj._masked = (data.get("masked", obj.__undef__), dirty)
        if obj._masked[0] is not None and obj._masked[0] is not obj.__undef__:
            assert isinstance(obj._masked[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._masked[0], type(obj._masked[0])))
            common.validate_format(obj._masked[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Container, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "group" == "type" or (self.group is not self.__undef__ and (not (dirty and not self._group[1]) or isinstance(self.group, list) or belongs_to_parent)):
            dct["group"] = dictify(self.group)
        if "provision_container" == "type" or (self.provision_container is not self.__undef__ and (not (dirty and not self._provision_container[1]))):
            dct["provisionContainer"] = dictify(self.provision_container)
        if "creation_time" == "type" or (self.creation_time is not self.__undef__ and (not (dirty and not self._creation_time[1]))):
            dct["creationTime"] = dictify(self.creation_time)
        if "current_timeflow" == "type" or (self.current_timeflow is not self.__undef__ and (not (dirty and not self._current_timeflow[1]))):
            dct["currentTimeflow"] = dictify(self.current_timeflow)
        if "previous_timeflow" == "type" or (self.previous_timeflow is not self.__undef__ and (not (dirty and not self._previous_timeflow[1]))):
            dct["previousTimeflow"] = dictify(self.previous_timeflow)
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "transformation" == "type" or (self.transformation is not self.__undef__ and (not (dirty and not self._transformation[1]))):
            dct["transformation"] = dictify(self.transformation)
        if "masked" == "type" or (self.masked is not self.__undef__ and (not (dirty and not self._masked[1]))):
            dct["masked"] = dictify(self.masked)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._group = (self._group[0], True)
        self._provision_container = (self._provision_container[0], True)
        self._creation_time = (self._creation_time[0], True)
        self._current_timeflow = (self._current_timeflow[0], True)
        self._previous_timeflow = (self._previous_timeflow[0], True)
        self._description = (self._description[0], True)
        self._runtime = (self._runtime[0], True)
        self._transformation = (self._transformation[0], True)
        self._masked = (self._masked[0], True)

    def is_dirty(self):
        return any([self._group[1], self._provision_container[1], self._creation_time[1], self._current_timeflow[1], self._previous_timeflow[1], self._description[1], self._runtime[1], self._transformation[1], self._masked[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Container):
            return False
        return super(Container, self).__eq__(other) and \
               self.group == other.group and \
               self.provision_container == other.provision_container and \
               self.creation_time == other.creation_time and \
               self.current_timeflow == other.current_timeflow and \
               self.previous_timeflow == other.previous_timeflow and \
               self.description == other.description and \
               self.runtime == other.runtime and \
               self.transformation == other.transformation and \
               self.masked == other.masked

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def group(self):
        """
        A reference to the group containing this container.

        :rtype: ``TEXT_TYPE``
        """
        return self._group[0]

    @group.setter
    def group(self, value):
        self._group = (value, True)

    @property
    def provision_container(self):
        """
        A reference to the container this container was provisioned from.

        :rtype: ``TEXT_TYPE``
        """
        return self._provision_container[0]

    @provision_container.setter
    def provision_container(self, value):
        self._provision_container = (value, True)

    @property
    def creation_time(self):
        """
        The date this container was created.

        :rtype: ``TEXT_TYPE``
        """
        return self._creation_time[0]

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = (value, True)

    @property
    def current_timeflow(self):
        """
        A reference to the currently active TimeFlow for this container.

        :rtype: ``TEXT_TYPE``
        """
        return self._current_timeflow[0]

    @current_timeflow.setter
    def current_timeflow(self, value):
        self._current_timeflow = (value, True)

    @property
    def previous_timeflow(self):
        """
        A reference to the previous TimeFlow for this container.

        :rtype: ``TEXT_TYPE``
        """
        return self._previous_timeflow[0]

    @previous_timeflow.setter
    def previous_timeflow(self, value):
        self._previous_timeflow = (value, True)

    @property
    def description(self):
        """
        Optional user-provided description for the container.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this container.

        :rtype: :py:class:`v1_10_2.web.vo.DBContainerRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def transformation(self):
        """
        True if this container is a transformation container.

        :rtype: ``bool``
        """
        return self._transformation[0]

    @transformation.setter
    def transformation(self, value):
        self._transformation = (value, True)

    @property
    def masked(self):
        """
        True if this container is a masked container.

        :rtype: ``bool``
        """
        return self._masked[0]

    @masked.setter
    def masked(self, value):
        self._masked = (value, True)

