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
#     /delphix-toolkit.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_14.web.objects.AbstractToolkit import AbstractToolkit
from delphixpy.v1_11_14 import factory
from delphixpy.v1_11_14 import common

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

class Toolkit(AbstractToolkit):
    """
    *(extends* :py:class:`v1_11_14.web.vo.AbstractToolkit` *)* An installed Lua
    toolkit.
    """
    def __init__(self, undef_enabled=True):
        super(Toolkit, self).__init__()
        self._type = ("Toolkit", True)
        self._name = (self.__undef__, True)
        self._pretty_name = (self.__undef__, True)
        self._version = (self.__undef__, True)
        self._resources = (self.__undef__, True)
        self._virtual_source_definition = (self.__undef__, True)
        self._linked_source_definition = (self.__undef__, True)
        self._discovery_definition = (self.__undef__, True)
        self._upgrade_definition = (self.__undef__, True)

    API_VERSION = "1.11.14"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Toolkit, cls).from_dict(data, dirty, undef_enabled)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        if "prettyName" not in data:
            raise ValueError("Missing required property \"prettyName\".")
        obj._pretty_name = (data.get("prettyName", obj.__undef__), dirty)
        if obj._pretty_name[0] is not None and obj._pretty_name[0] is not obj.__undef__:
            assert isinstance(obj._pretty_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pretty_name[0], type(obj._pretty_name[0])))
            common.validate_format(obj._pretty_name[0], "None", None, 256)
        if "version" not in data:
            raise ValueError("Missing required property \"version\".")
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "luaToolkitVersion", None, None)
        if "resources" not in data:
            raise ValueError("Missing required property \"resources\".")
        obj._resources = (data.get("resources", obj.__undef__), dirty)
        if obj._resources[0] is not None and obj._resources[0] is not obj.__undef__:
            assert isinstance(obj._resources[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._resources[0], type(obj._resources[0])))
            common.validate_format(obj._resources[0], "None", None, None)
        if "virtualSourceDefinition" not in data:
            raise ValueError("Missing required property \"virtualSourceDefinition\".")
        if "virtualSourceDefinition" in data and data["virtualSourceDefinition"] is not None:
            obj._virtual_source_definition = (factory.create_object(data["virtualSourceDefinition"], "ToolkitVirtualSource"), dirty)
            factory.validate_type(obj._virtual_source_definition[0], "ToolkitVirtualSource")
        else:
            obj._virtual_source_definition = (obj.__undef__, dirty)
        if "linkedSourceDefinition" not in data:
            raise ValueError("Missing required property \"linkedSourceDefinition\".")
        if "linkedSourceDefinition" in data and data["linkedSourceDefinition"] is not None:
            obj._linked_source_definition = (factory.create_object(data["linkedSourceDefinition"], "ToolkitLinkedSource"), dirty)
            factory.validate_type(obj._linked_source_definition[0], "ToolkitLinkedSource")
        else:
            obj._linked_source_definition = (obj.__undef__, dirty)
        if "discoveryDefinition" in data and data["discoveryDefinition"] is not None:
            obj._discovery_definition = (factory.create_object(data["discoveryDefinition"], "ToolkitDiscoveryDefinition"), dirty)
            factory.validate_type(obj._discovery_definition[0], "ToolkitDiscoveryDefinition")
        else:
            obj._discovery_definition = (obj.__undef__, dirty)
        if "upgradeDefinition" in data and data["upgradeDefinition"] is not None:
            obj._upgrade_definition = (factory.create_object(data["upgradeDefinition"], "ToolkitUpgradeDefinition"), dirty)
            factory.validate_type(obj._upgrade_definition[0], "ToolkitUpgradeDefinition")
        else:
            obj._upgrade_definition = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Toolkit, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "pretty_name" == "type" or (self.pretty_name is not self.__undef__ and (not (dirty and not self._pretty_name[1]) or isinstance(self.pretty_name, list) or belongs_to_parent)):
            dct["prettyName"] = dictify(self.pretty_name)
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]) or isinstance(self.version, list) or belongs_to_parent)):
            dct["version"] = dictify(self.version)
        if "resources" == "type" or (self.resources is not self.__undef__ and (not (dirty and not self._resources[1]) or isinstance(self.resources, list) or belongs_to_parent)):
            dct["resources"] = dictify(self.resources, prop_is_list_or_vo=True)
        if "virtual_source_definition" == "type" or (self.virtual_source_definition is not self.__undef__ and (not (dirty and not self._virtual_source_definition[1]) or isinstance(self.virtual_source_definition, list) or belongs_to_parent)):
            dct["virtualSourceDefinition"] = dictify(self.virtual_source_definition, prop_is_list_or_vo=True)
        if "linked_source_definition" == "type" or (self.linked_source_definition is not self.__undef__ and (not (dirty and not self._linked_source_definition[1]) or isinstance(self.linked_source_definition, list) or belongs_to_parent)):
            dct["linkedSourceDefinition"] = dictify(self.linked_source_definition, prop_is_list_or_vo=True)
        if "discovery_definition" == "type" or (self.discovery_definition is not self.__undef__ and (not (dirty and not self._discovery_definition[1]))):
            dct["discoveryDefinition"] = dictify(self.discovery_definition)
        if "upgrade_definition" == "type" or (self.upgrade_definition is not self.__undef__ and (not (dirty and not self._upgrade_definition[1]))):
            dct["upgradeDefinition"] = dictify(self.upgrade_definition)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._name = (self._name[0], True)
        self._pretty_name = (self._pretty_name[0], True)
        self._version = (self._version[0], True)
        self._resources = (self._resources[0], True)
        self._virtual_source_definition = (self._virtual_source_definition[0], True)
        self._linked_source_definition = (self._linked_source_definition[0], True)
        self._discovery_definition = (self._discovery_definition[0], True)
        self._upgrade_definition = (self._upgrade_definition[0], True)

    def is_dirty(self):
        return any([self._name[1], self._pretty_name[1], self._version[1], self._resources[1], self._virtual_source_definition[1], self._linked_source_definition[1], self._discovery_definition[1], self._upgrade_definition[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Toolkit):
            return False
        return super(Toolkit, self).__eq__(other) and \
               self.name == other.name and \
               self.pretty_name == other.pretty_name and \
               self.version == other.version and \
               self.resources == other.resources and \
               self.virtual_source_definition == other.virtual_source_definition and \
               self.linked_source_definition == other.linked_source_definition and \
               self.discovery_definition == other.discovery_definition and \
               self.upgrade_definition == other.upgrade_definition

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def name(self):
        """
        A unique and descriptive name for the toolkit.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def pretty_name(self):
        """
        A human readable name for the toolkit.

        :rtype: ``TEXT_TYPE``
        """
        return self._pretty_name[0]

    @pretty_name.setter
    def pretty_name(self, value):
        self._pretty_name = (value, True)

    @property
    def version(self):
        """
        The version of the toolkit.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

    @property
    def resources(self):
        """
        Resources for use by workflows in this toolkit.

        :rtype: ``dict``
        """
        return self._resources[0]

    @resources.setter
    def resources(self, value):
        self._resources = (value, True)

    @property
    def virtual_source_definition(self):
        """
        Definition of how to provision virtual sources of this type.

        :rtype: :py:class:`v1_11_14.web.vo.ToolkitVirtualSource`
        """
        return self._virtual_source_definition[0]

    @virtual_source_definition.setter
    def virtual_source_definition(self, value):
        self._virtual_source_definition = (value, True)

    @property
    def linked_source_definition(self):
        """
        Definition of how to link sources of this type.

        :rtype: :py:class:`v1_11_14.web.vo.ToolkitLinkedSource`
        """
        return self._linked_source_definition[0]

    @linked_source_definition.setter
    def linked_source_definition(self, value):
        self._linked_source_definition = (value, True)

    @property
    def discovery_definition(self):
        """
        Definition of how to discover sources of this type.

        :rtype: :py:class:`v1_11_14.web.vo.ToolkitDiscoveryDefinition`
        """
        return self._discovery_definition[0]

    @discovery_definition.setter
    def discovery_definition(self, value):
        self._discovery_definition = (value, True)

    @property
    def upgrade_definition(self):
        """
        Definition of how to upgrade sources of this type.

        :rtype: :py:class:`v1_11_14.web.vo.ToolkitUpgradeDefinition`
        """
        return self._upgrade_definition[0]

    @upgrade_definition.setter
    def upgrade_definition(self, value):
        self._upgrade_definition = (value, True)

