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
#     /delphix-plugin.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.AbstractToolkit import AbstractToolkit
from delphixpy.v1_11_2 import factory
from delphixpy.v1_11_2 import common

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

class Plugin(AbstractToolkit):
    """
    *(extends* :py:class:`v1_11_2.web.vo.AbstractToolkit` *)* An installed
    plugin.
    """
    def __init__(self, undef_enabled=True):
        super(Plugin, self).__init__()
        self._type = ("Plugin", True)
        self._external_version = (self.__undef__, True)
        self._build_number = (self.__undef__, True)
        self._virtual_source_definition = (self.__undef__, True)
        self._linked_source_definition = (self.__undef__, True)
        self._discovery_definition = (self.__undef__, True)
        self._upgrade_definition = (self.__undef__, True)
        self._entry_point = (self.__undef__, True)
        self._source_code = (self.__undef__, True)
        self._manifest = (self.__undef__, True)
        self._status = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Plugin, cls).from_dict(data, dirty, undef_enabled)
        obj._external_version = (data.get("externalVersion", obj.__undef__), dirty)
        if obj._external_version[0] is not None and obj._external_version[0] is not obj.__undef__:
            assert isinstance(obj._external_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._external_version[0], type(obj._external_version[0])))
            common.validate_format(obj._external_version[0], "None", None, None)
        if "buildNumber" not in data:
            raise ValueError("Missing required property \"buildNumber\".")
        obj._build_number = (data.get("buildNumber", obj.__undef__), dirty)
        if obj._build_number[0] is not None and obj._build_number[0] is not obj.__undef__:
            assert isinstance(obj._build_number[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._build_number[0], type(obj._build_number[0])))
            common.validate_format(obj._build_number[0], "dotDecimal", None, None)
        if "virtualSourceDefinition" not in data:
            raise ValueError("Missing required property \"virtualSourceDefinition\".")
        if "virtualSourceDefinition" in data and data["virtualSourceDefinition"] is not None:
            obj._virtual_source_definition = (factory.create_object(data["virtualSourceDefinition"], "PluginVirtualSourceDefinition"), dirty)
            factory.validate_type(obj._virtual_source_definition[0], "PluginVirtualSourceDefinition")
        else:
            obj._virtual_source_definition = (obj.__undef__, dirty)
        if "linkedSourceDefinition" not in data:
            raise ValueError("Missing required property \"linkedSourceDefinition\".")
        if "linkedSourceDefinition" in data and data["linkedSourceDefinition"] is not None:
            obj._linked_source_definition = (factory.create_object(data["linkedSourceDefinition"], "PluginLinkedSourceDefinition"), dirty)
            factory.validate_type(obj._linked_source_definition[0], "PluginLinkedSourceDefinition")
        else:
            obj._linked_source_definition = (obj.__undef__, dirty)
        if "discoveryDefinition" not in data:
            raise ValueError("Missing required property \"discoveryDefinition\".")
        if "discoveryDefinition" in data and data["discoveryDefinition"] is not None:
            obj._discovery_definition = (factory.create_object(data["discoveryDefinition"], "PluginDiscoveryDefinition"), dirty)
            factory.validate_type(obj._discovery_definition[0], "PluginDiscoveryDefinition")
        else:
            obj._discovery_definition = (obj.__undef__, dirty)
        if "upgradeDefinition" in data and data["upgradeDefinition"] is not None:
            obj._upgrade_definition = (factory.create_object(data["upgradeDefinition"], "PluginUpgradeDefinition"), dirty)
            factory.validate_type(obj._upgrade_definition[0], "PluginUpgradeDefinition")
        else:
            obj._upgrade_definition = (obj.__undef__, dirty)
        if "entryPoint" not in data:
            raise ValueError("Missing required property \"entryPoint\".")
        obj._entry_point = (data.get("entryPoint", obj.__undef__), dirty)
        if obj._entry_point[0] is not None and obj._entry_point[0] is not obj.__undef__:
            assert isinstance(obj._entry_point[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._entry_point[0], type(obj._entry_point[0])))
            common.validate_format(obj._entry_point[0], "None", None, None)
        if "sourceCode" not in data:
            raise ValueError("Missing required property \"sourceCode\".")
        obj._source_code = (data.get("sourceCode", obj.__undef__), dirty)
        if obj._source_code[0] is not None and obj._source_code[0] is not obj.__undef__:
            assert isinstance(obj._source_code[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_code[0], type(obj._source_code[0])))
            common.validate_format(obj._source_code[0], "None", None, None)
        if "manifest" not in data:
            raise ValueError("Missing required property \"manifest\".")
        if "manifest" in data and data["manifest"] is not None:
            obj._manifest = (factory.create_object(data["manifest"], "PluginManifest"), dirty)
            factory.validate_type(obj._manifest[0], "PluginManifest")
        else:
            obj._manifest = (obj.__undef__, dirty)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            assert obj._status[0] in ['ACTIVE', 'INACTIVE'], "Expected enum ['ACTIVE', 'INACTIVE'] but got %s" % obj._status[0]
            common.validate_format(obj._status[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Plugin, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "external_version" == "type" or (self.external_version is not self.__undef__ and (not (dirty and not self._external_version[1]))):
            dct["externalVersion"] = dictify(self.external_version)
        if "build_number" == "type" or (self.build_number is not self.__undef__ and (not (dirty and not self._build_number[1]) or isinstance(self.build_number, list) or belongs_to_parent)):
            dct["buildNumber"] = dictify(self.build_number)
        if "virtual_source_definition" == "type" or (self.virtual_source_definition is not self.__undef__ and (not (dirty and not self._virtual_source_definition[1]) or isinstance(self.virtual_source_definition, list) or belongs_to_parent)):
            dct["virtualSourceDefinition"] = dictify(self.virtual_source_definition, prop_is_list_or_vo=True)
        if "linked_source_definition" == "type" or (self.linked_source_definition is not self.__undef__ and (not (dirty and not self._linked_source_definition[1]) or isinstance(self.linked_source_definition, list) or belongs_to_parent)):
            dct["linkedSourceDefinition"] = dictify(self.linked_source_definition, prop_is_list_or_vo=True)
        if "discovery_definition" == "type" or (self.discovery_definition is not self.__undef__ and (not (dirty and not self._discovery_definition[1]) or isinstance(self.discovery_definition, list) or belongs_to_parent)):
            dct["discoveryDefinition"] = dictify(self.discovery_definition, prop_is_list_or_vo=True)
        if "upgrade_definition" == "type" or (self.upgrade_definition is not self.__undef__ and (not (dirty and not self._upgrade_definition[1]))):
            dct["upgradeDefinition"] = dictify(self.upgrade_definition)
        if "entry_point" == "type" or (self.entry_point is not self.__undef__ and (not (dirty and not self._entry_point[1]) or isinstance(self.entry_point, list) or belongs_to_parent)):
            dct["entryPoint"] = dictify(self.entry_point)
        if "source_code" == "type" or (self.source_code is not self.__undef__ and (not (dirty and not self._source_code[1]) or isinstance(self.source_code, list) or belongs_to_parent)):
            dct["sourceCode"] = dictify(self.source_code)
        if "manifest" == "type" or (self.manifest is not self.__undef__ and (not (dirty and not self._manifest[1]) or isinstance(self.manifest, list) or belongs_to_parent)):
            dct["manifest"] = dictify(self.manifest, prop_is_list_or_vo=True)
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        if dirty and "status" in dct:
            del dct["status"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._external_version = (self._external_version[0], True)
        self._build_number = (self._build_number[0], True)
        self._virtual_source_definition = (self._virtual_source_definition[0], True)
        self._linked_source_definition = (self._linked_source_definition[0], True)
        self._discovery_definition = (self._discovery_definition[0], True)
        self._upgrade_definition = (self._upgrade_definition[0], True)
        self._entry_point = (self._entry_point[0], True)
        self._source_code = (self._source_code[0], True)
        self._manifest = (self._manifest[0], True)
        self._status = (self._status[0], True)

    def is_dirty(self):
        return any([self._external_version[1], self._build_number[1], self._virtual_source_definition[1], self._linked_source_definition[1], self._discovery_definition[1], self._upgrade_definition[1], self._entry_point[1], self._source_code[1], self._manifest[1], self._status[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Plugin):
            return False
        return super(Plugin, self).__eq__(other) and \
               self.external_version == other.external_version and \
               self.build_number == other.build_number and \
               self.virtual_source_definition == other.virtual_source_definition and \
               self.linked_source_definition == other.linked_source_definition and \
               self.discovery_definition == other.discovery_definition and \
               self.upgrade_definition == other.upgrade_definition and \
               self.entry_point == other.entry_point and \
               self.source_code == other.source_code and \
               self.manifest == other.manifest and \
               self.status == other.status

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def external_version(self):
        """
        The user-facing version of the plugin that can be any format. If not
        set, the build number will be used.

        :rtype: ``TEXT_TYPE``
        """
        return self._external_version[0]

    @external_version.setter
    def external_version(self, value):
        self._external_version = (value, True)

    @property
    def build_number(self):
        """
        The internal build number of the plugin used to determine if a version
        of the plugin should be accepted.

        :rtype: ``TEXT_TYPE``
        """
        return self._build_number[0]

    @build_number.setter
    def build_number(self, value):
        self._build_number = (value, True)

    @property
    def virtual_source_definition(self):
        """
        Definition of how to provision virtual sources of this type.

        :rtype: :py:class:`v1_11_2.web.vo.PluginVirtualSourceDefinition`
        """
        return self._virtual_source_definition[0]

    @virtual_source_definition.setter
    def virtual_source_definition(self, value):
        self._virtual_source_definition = (value, True)

    @property
    def linked_source_definition(self):
        """
        Definition of how to link sources of this type.

        :rtype: :py:class:`v1_11_2.web.vo.PluginLinkedSourceDefinition`
        """
        return self._linked_source_definition[0]

    @linked_source_definition.setter
    def linked_source_definition(self, value):
        self._linked_source_definition = (value, True)

    @property
    def discovery_definition(self):
        """
        Definition of how to discover sources of this type.

        :rtype: :py:class:`v1_11_2.web.vo.PluginDiscoveryDefinition`
        """
        return self._discovery_definition[0]

    @discovery_definition.setter
    def discovery_definition(self, value):
        self._discovery_definition = (value, True)

    @property
    def upgrade_definition(self):
        """
        Definition of how to upgrade sources of this type.

        :rtype: :py:class:`v1_11_2.web.vo.PluginUpgradeDefinition`
        """
        return self._upgrade_definition[0]

    @upgrade_definition.setter
    def upgrade_definition(self, value):
        self._upgrade_definition = (value, True)

    @property
    def entry_point(self):
        """
        A fully qualified symbol that in the plugin's source code that is used
        to execute a plugin operation.

        :rtype: ``TEXT_TYPE``
        """
        return self._entry_point[0]

    @entry_point.setter
    def entry_point(self, value):
        self._entry_point = (value, True)

    @property
    def source_code(self):
        """
        Source code for this plugin.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_code[0]

    @source_code.setter
    def source_code(self, value):
        self._source_code = (value, True)

    @property
    def manifest(self):
        """
        A manifest describing the plugin.

        :rtype: :py:class:`v1_11_2.web.vo.PluginManifest`
        """
        return self._manifest[0]

    @manifest.setter
    def manifest(self, value):
        self._manifest = (value, True)

    @property
    def status(self):
        """
        The status of the plugin. ACTIVE indicates plugin is actively
        referenced and in use. INACTIVE means plugin needs to go through a
        manual upgrade operation before it can be used. *(permitted values:
        ACTIVE, INACTIVE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

