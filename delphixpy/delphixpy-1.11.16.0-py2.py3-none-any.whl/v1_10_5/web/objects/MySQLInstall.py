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
#     /delphix-mysql-install.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.SourceRepository import SourceRepository
from delphixpy.v1_10_5 import factory
from delphixpy.v1_10_5 import common

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

class MySQLInstall(SourceRepository):
    """
    *(extends* :py:class:`v1_10_5.web.vo.SourceRepository` *)* A MySQL
    installation.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLInstall, self).__init__()
        self._type = ("MySQLInstall", True)
        self._version = (self.__undef__, True)
        self._internal_version = (self.__undef__, True)
        self._installation_path = (self.__undef__, True)
        self._discovered = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLInstall, cls).from_dict(data, dirty, undef_enabled)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        if "internalVersion" in data and data["internalVersion"] is not None:
            obj._internal_version = (factory.create_object(data["internalVersion"], "MySQLVersion"), dirty)
            factory.validate_type(obj._internal_version[0], "MySQLVersion")
        else:
            obj._internal_version = (obj.__undef__, dirty)
        obj._installation_path = (data.get("installationPath", obj.__undef__), dirty)
        if obj._installation_path[0] is not None and obj._installation_path[0] is not obj.__undef__:
            assert isinstance(obj._installation_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._installation_path[0], type(obj._installation_path[0])))
            common.validate_format(obj._installation_path[0], "None", None, None)
        obj._discovered = (data.get("discovered", obj.__undef__), dirty)
        if obj._discovered[0] is not None and obj._discovered[0] is not obj.__undef__:
            assert isinstance(obj._discovered[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._discovered[0], type(obj._discovered[0])))
            common.validate_format(obj._discovered[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLInstall, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]))):
            dct["version"] = dictify(self.version)
        if dirty and "version" in dct:
            del dct["version"]
        if "internal_version" == "type" or (self.internal_version is not self.__undef__ and (not (dirty and not self._internal_version[1]))):
            dct["internalVersion"] = dictify(self.internal_version)
        if "installation_path" == "type" or (self.installation_path is not self.__undef__ and (not (dirty and not self._installation_path[1]) or isinstance(self.installation_path, list) or belongs_to_parent)):
            dct["installationPath"] = dictify(self.installation_path)
        if "discovered" == "type" or (self.discovered is not self.__undef__ and (not (dirty and not self._discovered[1]))):
            dct["discovered"] = dictify(self.discovered)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._version = (self._version[0], True)
        self._internal_version = (self._internal_version[0], True)
        self._installation_path = (self._installation_path[0], True)
        self._discovered = (self._discovered[0], True)

    def is_dirty(self):
        return any([self._version[1], self._internal_version[1], self._installation_path[1], self._discovered[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLInstall):
            return False
        return super(MySQLInstall, self).__eq__(other) and \
               self.version == other.version and \
               self.internal_version == other.internal_version and \
               self.installation_path == other.installation_path and \
               self.discovered == other.discovered

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def version(self):
        """
        Version string for the repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @property
    def internal_version(self):
        """
        Version of the MySQL installation.

        :rtype: :py:class:`v1_10_5.web.vo.MySQLVersion`
        """
        return self._internal_version[0]

    @internal_version.setter
    def internal_version(self, value):
        self._internal_version = (value, True)

    @property
    def installation_path(self):
        """
        Directory path where the MySQL installation is located.

        :rtype: ``TEXT_TYPE``
        """
        return self._installation_path[0]

    @installation_path.setter
    def installation_path(self, value):
        self._installation_path = (value, True)

    @property
    def discovered(self):
        """
        Flag indicating whether the MySQL installation was discovered or
        manually entered.

        :rtype: ``bool``
        """
        return self._discovered[0]

    @discovered.setter
    def discovered(self, value):
        self._discovered = (value, True)

