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
#     /delphix-source-repository.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.ReadonlyNamedUserObject import ReadonlyNamedUserObject
from delphixpy.v1_11_9 import common

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

class SourceRepository(ReadonlyNamedUserObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.ReadonlyNamedUserObject` *)* A source
    repository represents a container for the source config.
    """
    def __init__(self, undef_enabled=True):
        super(SourceRepository, self).__init__()
        self._type = ("SourceRepository", True)
        self._version = (self.__undef__, True)
        self._provisioning_enabled = (self.__undef__, True)
        self._environment = (self.__undef__, True)
        self._staging = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceRepository, cls).from_dict(data, dirty, undef_enabled)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        obj._provisioning_enabled = (data.get("provisioningEnabled", obj.__undef__), dirty)
        if obj._provisioning_enabled[0] is not None and obj._provisioning_enabled[0] is not obj.__undef__:
            assert isinstance(obj._provisioning_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._provisioning_enabled[0], type(obj._provisioning_enabled[0])))
            common.validate_format(obj._provisioning_enabled[0], "None", None, None)
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        obj._staging = (data.get("staging", obj.__undef__), dirty)
        if obj._staging[0] is not None and obj._staging[0] is not obj.__undef__:
            assert isinstance(obj._staging[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._staging[0], type(obj._staging[0])))
            common.validate_format(obj._staging[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceRepository, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]) or isinstance(self.version, list) or belongs_to_parent)):
            dct["version"] = dictify(self.version)
        if "provisioning_enabled" == "type" or (self.provisioning_enabled is not self.__undef__ and (not (dirty and not self._provisioning_enabled[1]) or isinstance(self.provisioning_enabled, list) or belongs_to_parent)):
            dct["provisioningEnabled"] = dictify(self.provisioning_enabled)
        elif belongs_to_parent and self.provisioning_enabled is self.__undef__:
            dct["provisioningEnabled"] = True
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]) or isinstance(self.environment, list) or belongs_to_parent)):
            dct["environment"] = dictify(self.environment)
        if "staging" == "type" or (self.staging is not self.__undef__ and (not (dirty and not self._staging[1]) or isinstance(self.staging, list) or belongs_to_parent)):
            dct["staging"] = dictify(self.staging)
        elif belongs_to_parent and self.staging is self.__undef__:
            dct["staging"] = False
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._version = (self._version[0], True)
        self._provisioning_enabled = (self._provisioning_enabled[0], True)
        self._environment = (self._environment[0], True)
        self._staging = (self._staging[0], True)

    def is_dirty(self):
        return any([self._version[1], self._provisioning_enabled[1], self._environment[1], self._staging[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceRepository):
            return False
        return super(SourceRepository, self).__eq__(other) and \
               self.version == other.version and \
               self.provisioning_enabled == other.provisioning_enabled and \
               self.environment == other.environment and \
               self.staging == other.staging

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def version(self):
        """
        Version of the repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

    @property
    def provisioning_enabled(self):
        """
        *(default value: True)* Flag indicating whether the repository should
        be used for provisioning.

        :rtype: ``bool``
        """
        return self._provisioning_enabled[0]

    @provisioning_enabled.setter
    def provisioning_enabled(self, value):
        self._provisioning_enabled = (value, True)

    @property
    def environment(self):
        """
        Reference to the environment containing this repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

    @property
    def staging(self):
        """
        Flag indicating whether this repository can be used by the Delphix
        Engine for internal processing.

        :rtype: ``bool``
        """
        return self._staging[0]

    @staging.setter
    def staging(self, value):
        self._staging = (value, True)

