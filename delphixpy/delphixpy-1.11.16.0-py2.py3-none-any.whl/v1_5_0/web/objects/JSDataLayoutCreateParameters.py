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
#     /delphix-js-data-layout-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_0 import factory
from delphixpy.v1_5_0 import common

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

class JSDataLayoutCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_5_0.web.vo.TypedObject` *)* The parameters used to
    create a data layout.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataLayoutCreateParameters, self).__init__()
        self._type = ("JSDataLayoutCreateParameters", True)
        self._data_sources = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._notes = (self.__undef__, True)
        self._properties = (self.__undef__, True)

    API_VERSION = "1.5.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataLayoutCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "dataSources" not in data:
            raise ValueError("Missing required property \"dataSources\".")
        obj._data_sources = []
        for item in data.get("dataSources") or []:
            obj._data_sources.append(factory.create_object(item))
            factory.validate_type(obj._data_sources[-1], "JSDataSourceCreateParameters")
        obj._data_sources = (obj._data_sources, dirty)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        obj._notes = (data.get("notes", obj.__undef__), dirty)
        if obj._notes[0] is not None and obj._notes[0] is not obj.__undef__:
            assert isinstance(obj._notes[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._notes[0], type(obj._notes[0])))
            common.validate_format(obj._notes[0], "None", None, 4096)
        obj._properties = (data.get("properties", obj.__undef__), dirty)
        if obj._properties[0] is not None and obj._properties[0] is not obj.__undef__:
            assert isinstance(obj._properties[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._properties[0], type(obj._properties[0])))
            common.validate_format(obj._properties[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataLayoutCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "data_sources" == "type" or (self.data_sources is not self.__undef__ and (not (dirty and not self._data_sources[1]) or isinstance(self.data_sources, list) or belongs_to_parent)):
            dct["dataSources"] = dictify(self.data_sources, prop_is_list_or_vo=True)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "notes" == "type" or (self.notes is not self.__undef__ and (not (dirty and not self._notes[1]) or isinstance(self.notes, list) or belongs_to_parent)):
            dct["notes"] = dictify(self.notes)
        if "properties" == "type" or (self.properties is not self.__undef__ and (not (dirty and not self._properties[1]) or isinstance(self.properties, list) or belongs_to_parent)):
            dct["properties"] = dictify(self.properties, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._data_sources = (self._data_sources[0], True)
        self._name = (self._name[0], True)
        self._notes = (self._notes[0], True)
        self._properties = (self._properties[0], True)

    def is_dirty(self):
        return any([self._data_sources[1], self._name[1], self._notes[1], self._properties[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataLayoutCreateParameters):
            return False
        return super(JSDataLayoutCreateParameters, self).__eq__(other) and \
               self.data_sources == other.data_sources and \
               self.name == other.name and \
               self.notes == other.notes and \
               self.properties == other.properties

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def data_sources(self):
        """
        The set of data sources that belong to this data layout.

        :rtype: ``list`` of
            :py:class:`v1_5_0.web.vo.JSDataSourceCreateParameters`
        """
        return self._data_sources[0]

    @data_sources.setter
    def data_sources(self, value):
        self._data_sources = (value, True)

    @property
    def name(self):
        """
        The name of the data layout.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def notes(self):
        """
        A description of this data layout to define what it is used for.

        :rtype: ``TEXT_TYPE``
        """
        return self._notes[0]

    @notes.setter
    def notes(self, value):
        self._notes = (value, True)

    @property
    def properties(self):
        """
        Key/value pairs used to specify attributes for this data layout.

        :rtype: ``dict``
        """
        return self._properties[0]

    @properties.setter
    def properties(self, value):
        self._properties = (value, True)

