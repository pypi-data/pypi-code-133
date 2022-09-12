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
#     /delphix-system-package.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_10_4 import common

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

class SystemPackage(NamedUserObject):
    """
    *(extends* :py:class:`v1_10_4.web.vo.NamedUserObject` *)* A package whose
    version can be changed by sysadmins.
    """
    def __init__(self, undef_enabled=True):
        super(SystemPackage, self).__init__()
        self._type = ("SystemPackage", True)
        self._version = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._possible_versions = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SystemPackage, cls).from_dict(data, dirty, undef_enabled)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "objectName", None, 256)
        obj._possible_versions = []
        for item in data.get("possibleVersions") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._possible_versions.append(item)
        obj._possible_versions = (obj._possible_versions, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SystemPackage, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]) or isinstance(self.version, list) or belongs_to_parent)):
            dct["version"] = dictify(self.version)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]))):
            dct["name"] = dictify(self.name)
        if "possible_versions" == "type" or (self.possible_versions is not self.__undef__ and (not (dirty and not self._possible_versions[1]))):
            dct["possibleVersions"] = dictify(self.possible_versions)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._version = (self._version[0], True)
        self._name = (self._name[0], True)
        self._possible_versions = (self._possible_versions[0], True)

    def is_dirty(self):
        return any([self._version[1], self._name[1], self._possible_versions[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SystemPackage):
            return False
        return super(SystemPackage, self).__eq__(other) and \
               self.version == other.version and \
               self.name == other.name and \
               self.possible_versions == other.possible_versions

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def version(self):
        """
        Current version of the package.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

    @property
    def name(self):
        """
        Package name.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def possible_versions(self):
        """
        Possible versions for this package.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._possible_versions[0]

    @possible_versions.setter
    def possible_versions(self, value):
        self._possible_versions = (value, True)

