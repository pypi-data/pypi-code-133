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
#     /delphix-toolkit-upgrade-definition.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.TypedObject import TypedObject
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

class ToolkitUpgradeDefinition(TypedObject):
    """
    *(extends* :py:class:`v1_11_2.web.vo.TypedObject` *)* The toolkit upgrade
    logic to upgrade metadata from the previous version of the Lua toolkit.
    """
    def __init__(self, undef_enabled=True):
        super(ToolkitUpgradeDefinition, self).__init__()
        self._type = ("ToolkitUpgradeDefinition", True)
        self._upgrade_snapshot = (self.__undef__, True)
        self._upgrade_virtual_source = (self.__undef__, True)
        self._upgrade_linked_source = (self.__undef__, True)
        self._upgrade_manual_source_config = (self.__undef__, True)
        self._from_version = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ToolkitUpgradeDefinition, cls).from_dict(data, dirty, undef_enabled)
        if "upgradeSnapshot" not in data:
            raise ValueError("Missing required property \"upgradeSnapshot\".")
        obj._upgrade_snapshot = (data.get("upgradeSnapshot", obj.__undef__), dirty)
        if obj._upgrade_snapshot[0] is not None and obj._upgrade_snapshot[0] is not obj.__undef__:
            assert isinstance(obj._upgrade_snapshot[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._upgrade_snapshot[0], type(obj._upgrade_snapshot[0])))
            common.validate_format(obj._upgrade_snapshot[0], "None", None, None)
        if "upgradeVirtualSource" not in data:
            raise ValueError("Missing required property \"upgradeVirtualSource\".")
        obj._upgrade_virtual_source = (data.get("upgradeVirtualSource", obj.__undef__), dirty)
        if obj._upgrade_virtual_source[0] is not None and obj._upgrade_virtual_source[0] is not obj.__undef__:
            assert isinstance(obj._upgrade_virtual_source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._upgrade_virtual_source[0], type(obj._upgrade_virtual_source[0])))
            common.validate_format(obj._upgrade_virtual_source[0], "None", None, None)
        if "upgradeLinkedSource" not in data:
            raise ValueError("Missing required property \"upgradeLinkedSource\".")
        obj._upgrade_linked_source = (data.get("upgradeLinkedSource", obj.__undef__), dirty)
        if obj._upgrade_linked_source[0] is not None and obj._upgrade_linked_source[0] is not obj.__undef__:
            assert isinstance(obj._upgrade_linked_source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._upgrade_linked_source[0], type(obj._upgrade_linked_source[0])))
            common.validate_format(obj._upgrade_linked_source[0], "None", None, None)
        obj._upgrade_manual_source_config = (data.get("upgradeManualSourceConfig", obj.__undef__), dirty)
        if obj._upgrade_manual_source_config[0] is not None and obj._upgrade_manual_source_config[0] is not obj.__undef__:
            assert isinstance(obj._upgrade_manual_source_config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._upgrade_manual_source_config[0], type(obj._upgrade_manual_source_config[0])))
            common.validate_format(obj._upgrade_manual_source_config[0], "None", None, None)
        if "fromVersion" not in data:
            raise ValueError("Missing required property \"fromVersion\".")
        obj._from_version = (data.get("fromVersion", obj.__undef__), dirty)
        if obj._from_version[0] is not None and obj._from_version[0] is not obj.__undef__:
            assert isinstance(obj._from_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._from_version[0], type(obj._from_version[0])))
            common.validate_format(obj._from_version[0], "luaToolkitVersion", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ToolkitUpgradeDefinition, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "upgrade_snapshot" == "type" or (self.upgrade_snapshot is not self.__undef__ and (not (dirty and not self._upgrade_snapshot[1]) or isinstance(self.upgrade_snapshot, list) or belongs_to_parent)):
            dct["upgradeSnapshot"] = dictify(self.upgrade_snapshot)
        if "upgrade_virtual_source" == "type" or (self.upgrade_virtual_source is not self.__undef__ and (not (dirty and not self._upgrade_virtual_source[1]) or isinstance(self.upgrade_virtual_source, list) or belongs_to_parent)):
            dct["upgradeVirtualSource"] = dictify(self.upgrade_virtual_source)
        if "upgrade_linked_source" == "type" or (self.upgrade_linked_source is not self.__undef__ and (not (dirty and not self._upgrade_linked_source[1]) or isinstance(self.upgrade_linked_source, list) or belongs_to_parent)):
            dct["upgradeLinkedSource"] = dictify(self.upgrade_linked_source)
        if "upgrade_manual_source_config" == "type" or (self.upgrade_manual_source_config is not self.__undef__ and (not (dirty and not self._upgrade_manual_source_config[1]))):
            dct["upgradeManualSourceConfig"] = dictify(self.upgrade_manual_source_config)
        if "from_version" == "type" or (self.from_version is not self.__undef__ and (not (dirty and not self._from_version[1]) or isinstance(self.from_version, list) or belongs_to_parent)):
            dct["fromVersion"] = dictify(self.from_version)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._upgrade_snapshot = (self._upgrade_snapshot[0], True)
        self._upgrade_virtual_source = (self._upgrade_virtual_source[0], True)
        self._upgrade_linked_source = (self._upgrade_linked_source[0], True)
        self._upgrade_manual_source_config = (self._upgrade_manual_source_config[0], True)
        self._from_version = (self._from_version[0], True)

    def is_dirty(self):
        return any([self._upgrade_snapshot[1], self._upgrade_virtual_source[1], self._upgrade_linked_source[1], self._upgrade_manual_source_config[1], self._from_version[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ToolkitUpgradeDefinition):
            return False
        return super(ToolkitUpgradeDefinition, self).__eq__(other) and \
               self.upgrade_snapshot == other.upgrade_snapshot and \
               self.upgrade_virtual_source == other.upgrade_virtual_source and \
               self.upgrade_linked_source == other.upgrade_linked_source and \
               self.upgrade_manual_source_config == other.upgrade_manual_source_config and \
               self.from_version == other.from_version

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def upgrade_snapshot(self):
        """
        A workflow script to upgrade the snapshot metadata.

        :rtype: ``TEXT_TYPE``
        """
        return self._upgrade_snapshot[0]

    @upgrade_snapshot.setter
    def upgrade_snapshot(self, value):
        self._upgrade_snapshot = (value, True)

    @property
    def upgrade_virtual_source(self):
        """
        A workflow script to upgrade the virtual source parameters.

        :rtype: ``TEXT_TYPE``
        """
        return self._upgrade_virtual_source[0]

    @upgrade_virtual_source.setter
    def upgrade_virtual_source(self, value):
        self._upgrade_virtual_source = (value, True)

    @property
    def upgrade_linked_source(self):
        """
        A workflow script to upgrade the linked source parameters.

        :rtype: ``TEXT_TYPE``
        """
        return self._upgrade_linked_source[0]

    @upgrade_linked_source.setter
    def upgrade_linked_source(self, value):
        self._upgrade_linked_source = (value, True)

    @property
    def upgrade_manual_source_config(self):
        """
        A workflow script to upgrade the manually-discovered source config
        parameters.

        :rtype: ``TEXT_TYPE``
        """
        return self._upgrade_manual_source_config[0]

    @upgrade_manual_source_config.setter
    def upgrade_manual_source_config(self, value):
        self._upgrade_manual_source_config = (value, True)

    @property
    def from_version(self):
        """
        The version of the toolkit that we are upgrading from.

        :rtype: ``TEXT_TYPE``
        """
        return self._from_version[0]

    @from_version.setter
    def from_version(self, value):
        self._from_version = (value, True)

