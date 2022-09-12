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
#     /delphix-appdata-additional-mount-point.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_8_2 import common

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

class AppDataAdditionalMountPoint(TypedObject):
    """
    *(extends* :py:class:`v1_8_2.web.vo.TypedObject` *)* Specifies an
    additional location on which to mount a subdirectory of an AppData
    container.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataAdditionalMountPoint, self).__init__()
        self._type = ("AppDataAdditionalMountPoint", True)
        self._environment = (self.__undef__, True)
        self._mount_path = (self.__undef__, True)
        self._shared_path = (self.__undef__, True)

    API_VERSION = "1.8.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataAdditionalMountPoint, cls).from_dict(data, dirty, undef_enabled)
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        obj._mount_path = (data.get("mountPath", obj.__undef__), dirty)
        if obj._mount_path[0] is not None and obj._mount_path[0] is not obj.__undef__:
            assert isinstance(obj._mount_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_path[0], type(obj._mount_path[0])))
            common.validate_format(obj._mount_path[0], "unixpath", None, None)
        obj._shared_path = (data.get("sharedPath", obj.__undef__), dirty)
        if obj._shared_path[0] is not None and obj._shared_path[0] is not obj.__undef__:
            assert isinstance(obj._shared_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._shared_path[0], type(obj._shared_path[0])))
            common.validate_format(obj._shared_path[0], "unixpath", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataAdditionalMountPoint, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]) or isinstance(self.environment, list) or belongs_to_parent)):
            dct["environment"] = dictify(self.environment)
        if "mount_path" == "type" or (self.mount_path is not self.__undef__ and (not (dirty and not self._mount_path[1]) or isinstance(self.mount_path, list) or belongs_to_parent)):
            dct["mountPath"] = dictify(self.mount_path)
        if "shared_path" == "type" or (self.shared_path is not self.__undef__ and (not (dirty and not self._shared_path[1]) or isinstance(self.shared_path, list) or belongs_to_parent)):
            dct["sharedPath"] = dictify(self.shared_path)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._environment = (self._environment[0], True)
        self._mount_path = (self._mount_path[0], True)
        self._shared_path = (self._shared_path[0], True)

    def is_dirty(self):
        return any([self._environment[1], self._mount_path[1], self._shared_path[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataAdditionalMountPoint):
            return False
        return super(AppDataAdditionalMountPoint, self).__eq__(other) and \
               self.environment == other.environment and \
               self.mount_path == other.mount_path and \
               self.shared_path == other.shared_path

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def environment(self):
        """
        Reference to the environment on which the file system will be mounted.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

    @property
    def mount_path(self):
        """
        Absolute path on the target environment were the filesystem should be
        mounted.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_path[0]

    @mount_path.setter
    def mount_path(self, value):
        self._mount_path = (value, True)

    @property
    def shared_path(self):
        """
        Relative path within the container of the directory that should be
        mounted.

        :rtype: ``TEXT_TYPE``
        """
        return self._shared_path[0]

    @shared_path.setter
    def shared_path(self, value):
        self._shared_path = (value, True)

