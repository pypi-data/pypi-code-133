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
#     /delphix-appdata-source-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.SourceConfig import SourceConfig
from delphixpy.v1_4_3 import common

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

class AppDataSourceConfig(SourceConfig):
    """
    *(extends* :py:class:`v1_4_3.web.vo.SourceConfig` *)* Source config for
    AppDataToolkits.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataSourceConfig, self).__init__()
        self._type = ("AppDataSourceConfig", True)
        self._excludes = (self.__undef__, True)
        self._follow_symlinks = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._path = (self.__undef__, True)
        self._repository = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataSourceConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._excludes = []
        for item in data.get("excludes") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._excludes.append(item)
        obj._excludes = (obj._excludes, dirty)
        obj._follow_symlinks = []
        for item in data.get("followSymlinks") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._follow_symlinks.append(item)
        obj._follow_symlinks = (obj._follow_symlinks, dirty)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        obj._path = (data.get("path", obj.__undef__), dirty)
        if obj._path[0] is not None and obj._path[0] is not obj.__undef__:
            assert isinstance(obj._path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._path[0], type(obj._path[0])))
            common.validate_format(obj._path[0], "None", None, 1024)
        obj._repository = (data.get("repository", obj.__undef__), dirty)
        if obj._repository[0] is not None and obj._repository[0] is not obj.__undef__:
            assert isinstance(obj._repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._repository[0], type(obj._repository[0])))
            common.validate_format(obj._repository[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataSourceConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "excludes" == "type" or (self.excludes is not self.__undef__ and (not (dirty and not self._excludes[1]) or isinstance(self.excludes, list) or belongs_to_parent)):
            dct["excludes"] = dictify(self.excludes, prop_is_list_or_vo=True)
        if "follow_symlinks" == "type" or (self.follow_symlinks is not self.__undef__ and (not (dirty and not self._follow_symlinks[1]) or isinstance(self.follow_symlinks, list) or belongs_to_parent)):
            dct["followSymlinks"] = dictify(self.follow_symlinks, prop_is_list_or_vo=True)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "path" == "type" or (self.path is not self.__undef__ and (not (dirty and not self._path[1]) or isinstance(self.path, list) or belongs_to_parent)):
            dct["path"] = dictify(self.path)
        if "repository" == "type" or (self.repository is not self.__undef__ and (not (dirty and not self._repository[1]) or isinstance(self.repository, list) or belongs_to_parent)):
            dct["repository"] = dictify(self.repository)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._excludes = (self._excludes[0], True)
        self._follow_symlinks = (self._follow_symlinks[0], True)
        self._name = (self._name[0], True)
        self._path = (self._path[0], True)
        self._repository = (self._repository[0], True)

    def is_dirty(self):
        return any([self._excludes[1], self._follow_symlinks[1], self._name[1], self._path[1], self._repository[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataSourceConfig):
            return False
        return super(AppDataSourceConfig, self).__eq__(other) and \
               self.excludes == other.excludes and \
               self.follow_symlinks == other.follow_symlinks and \
               self.name == other.name and \
               self.path == other.path and \
               self.repository == other.repository

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def excludes(self):
        """
        List of subdirectories in the source to exclude when running rsync.
        These paths are relative to the root of the source directory.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._excludes[0]

    @excludes.setter
    def excludes(self, value):
        self._excludes = (value, True)

    @property
    def follow_symlinks(self):
        """
        List of symlinks in the source to follow when running rsync. These
        paths are relative to the root of the source directory. All other
        symlinks are preserved.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._follow_symlinks[0]

    @follow_symlinks.setter
    def follow_symlinks(self, value):
        self._follow_symlinks = (value, True)

    @property
    def name(self):
        """
        The name of the config.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def path(self):
        """
        The path to the data to be synced.

        :rtype: ``TEXT_TYPE``
        """
        return self._path[0]

    @path.setter
    def path(self, value):
        self._path = (value, True)

    @property
    def repository(self):
        """
        The object reference of the source repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._repository[0]

    @repository.setter
    def repository(self, value):
        self._repository = (value, True)

