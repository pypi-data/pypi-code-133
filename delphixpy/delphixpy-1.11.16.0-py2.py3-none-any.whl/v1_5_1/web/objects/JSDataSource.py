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
#     /delphix-js-data-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_1.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_5_1 import factory
from delphixpy.v1_5_1 import common

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

class JSDataSource(NamedUserObject):
    """
    *(extends* :py:class:`v1_5_1.web.vo.NamedUserObject` *)* The data source
    used for Jet Stream data layouts.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataSource, self).__init__()
        self._type = ("JSDataSource", True)
        self._container = (self.__undef__, True)
        self._data_layout = (self.__undef__, True)
        self._description = (self.__undef__, True)
        self._enabled = (self.__undef__, True)
        self._properties = (self.__undef__, True)
        self._runtime = (self.__undef__, True)

    API_VERSION = "1.5.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataSource, cls).from_dict(data, dirty, undef_enabled)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._data_layout = (data.get("dataLayout", obj.__undef__), dirty)
        if obj._data_layout[0] is not None and obj._data_layout[0] is not obj.__undef__:
            assert isinstance(obj._data_layout[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_layout[0], type(obj._data_layout[0])))
            common.validate_format(obj._data_layout[0], "objectReference", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, 4096)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._properties = (data.get("properties", obj.__undef__), dirty)
        if obj._properties[0] is not None and obj._properties[0] is not obj.__undef__:
            assert isinstance(obj._properties[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._properties[0], type(obj._properties[0])))
            common.validate_format(obj._properties[0], "None", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "SourceConnectionInfo"), dirty)
            factory.validate_type(obj._runtime[0], "SourceConnectionInfo")
        else:
            obj._runtime = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]))):
            dct["container"] = dictify(self.container)
        if "data_layout" == "type" or (self.data_layout is not self.__undef__ and (not (dirty and not self._data_layout[1]))):
            dct["dataLayout"] = dictify(self.data_layout)
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]))):
            dct["enabled"] = dictify(self.enabled)
        if "properties" == "type" or (self.properties is not self.__undef__ and (not (dirty and not self._properties[1]) or isinstance(self.properties, list) or belongs_to_parent)):
            dct["properties"] = dictify(self.properties, prop_is_list_or_vo=True)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._data_layout = (self._data_layout[0], True)
        self._description = (self._description[0], True)
        self._enabled = (self._enabled[0], True)
        self._properties = (self._properties[0], True)
        self._runtime = (self._runtime[0], True)

    def is_dirty(self):
        return any([self._container[1], self._data_layout[1], self._description[1], self._enabled[1], self._properties[1], self._runtime[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataSource):
            return False
        return super(JSDataSource, self).__eq__(other) and \
               self.container == other.container and \
               self.data_layout == other.data_layout and \
               self.description == other.description and \
               self.enabled == other.enabled and \
               self.properties == other.properties and \
               self.runtime == other.runtime

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        A reference to the underlying container.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def data_layout(self):
        """
        A reference to the Jet Stream data layout to which this source belongs.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_layout[0]

    @data_layout.setter
    def data_layout(self, value):
        self._data_layout = (value, True)

    @property
    def description(self):
        """
        A description of this data source.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def enabled(self):
        """
        Flag indicating whether the source is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def properties(self):
        """
        Key/value pairs used to specify attributes for this data source.

        :rtype: ``dict``
        """
        return self._properties[0]

    @properties.setter
    def properties(self, value):
        self._properties = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this data source.

        :rtype: :py:class:`v1_5_1.web.vo.SourceConnectionInfo`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

