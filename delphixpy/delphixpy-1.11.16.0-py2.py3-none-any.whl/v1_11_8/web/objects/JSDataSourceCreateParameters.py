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
#     /delphix-js-data-source-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_8.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_8 import factory
from delphixpy.v1_11_8 import common

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

class JSDataSourceCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_8.web.vo.TypedObject` *)* The parameters used
    to create the Self-Service data sources.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataSourceCreateParameters, self).__init__()
        self._type = ("JSDataSourceCreateParameters", True)
        self._source = (self.__undef__, True)
        self._container = (self.__undef__, True)
        self._properties = (self.__undef__, True)

    API_VERSION = "1.11.8"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataSourceCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "JSDataSource"), dirty)
            factory.validate_type(obj._source[0], "JSDataSource")
        else:
            obj._source = (obj.__undef__, dirty)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._properties = (data.get("properties", obj.__undef__), dirty)
        if obj._properties[0] is not None and obj._properties[0] is not obj.__undef__:
            assert isinstance(obj._properties[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._properties[0], type(obj._properties[0])))
            common.validate_format(obj._properties[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataSourceCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container)
        if "properties" == "type" or (self.properties is not self.__undef__ and (not (dirty and not self._properties[1]) or isinstance(self.properties, list) or belongs_to_parent)):
            dct["properties"] = dictify(self.properties, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source = (self._source[0], True)
        self._container = (self._container[0], True)
        self._properties = (self._properties[0], True)

    def is_dirty(self):
        return any([self._source[1], self._container[1], self._properties[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataSourceCreateParameters):
            return False
        return super(JSDataSourceCreateParameters, self).__eq__(other) and \
               self.source == other.source and \
               self.container == other.container and \
               self.properties == other.properties

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source(self):
        """
        The Self-Service data source object.

        :rtype: :py:class:`v1_11_8.web.vo.JSDataSource`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def container(self):
        """
        A reference to the underlying container object.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

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

