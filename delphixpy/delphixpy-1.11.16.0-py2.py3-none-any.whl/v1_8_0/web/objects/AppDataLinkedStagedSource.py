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
#     /delphix-appdata-linked-staged-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_0.web.objects.AppDataLinkedSource import AppDataLinkedSource
from delphixpy.v1_8_0 import common

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

class AppDataLinkedStagedSource(AppDataLinkedSource):
    """
    *(extends* :py:class:`v1_8_0.web.vo.AppDataLinkedSource` *)* An AppData
    linked source with a staging source.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataLinkedStagedSource, self).__init__()
        self._type = ("AppDataLinkedStagedSource", True)
        self._staging_environment = (self.__undef__, True)
        self._staging_environment_user = (self.__undef__, True)
        self._staging_mount_base = (self.__undef__, True)

    API_VERSION = "1.8.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataLinkedStagedSource, cls).from_dict(data, dirty, undef_enabled)
        obj._staging_environment = (data.get("stagingEnvironment", obj.__undef__), dirty)
        if obj._staging_environment[0] is not None and obj._staging_environment[0] is not obj.__undef__:
            assert isinstance(obj._staging_environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_environment[0], type(obj._staging_environment[0])))
            common.validate_format(obj._staging_environment[0], "objectReference", None, None)
        obj._staging_environment_user = (data.get("stagingEnvironmentUser", obj.__undef__), dirty)
        if obj._staging_environment_user[0] is not None and obj._staging_environment_user[0] is not obj.__undef__:
            assert isinstance(obj._staging_environment_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_environment_user[0], type(obj._staging_environment_user[0])))
            common.validate_format(obj._staging_environment_user[0], "objectReference", None, None)
        obj._staging_mount_base = (data.get("stagingMountBase", obj.__undef__), dirty)
        if obj._staging_mount_base[0] is not None and obj._staging_mount_base[0] is not obj.__undef__:
            assert isinstance(obj._staging_mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_mount_base[0], type(obj._staging_mount_base[0])))
            common.validate_format(obj._staging_mount_base[0], "None", None, 256)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataLinkedStagedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "staging_environment" == "type" or (self.staging_environment is not self.__undef__ and (not (dirty and not self._staging_environment[1]) or isinstance(self.staging_environment, list) or belongs_to_parent)):
            dct["stagingEnvironment"] = dictify(self.staging_environment)
        if "staging_environment_user" == "type" or (self.staging_environment_user is not self.__undef__ and (not (dirty and not self._staging_environment_user[1]) or isinstance(self.staging_environment_user, list) or belongs_to_parent)):
            dct["stagingEnvironmentUser"] = dictify(self.staging_environment_user)
        if "staging_mount_base" == "type" or (self.staging_mount_base is not self.__undef__ and (not (dirty and not self._staging_mount_base[1]) or isinstance(self.staging_mount_base, list) or belongs_to_parent)):
            dct["stagingMountBase"] = dictify(self.staging_mount_base)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._staging_environment = (self._staging_environment[0], True)
        self._staging_environment_user = (self._staging_environment_user[0], True)
        self._staging_mount_base = (self._staging_mount_base[0], True)

    def is_dirty(self):
        return any([self._staging_environment[1], self._staging_environment_user[1], self._staging_mount_base[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataLinkedStagedSource):
            return False
        return super(AppDataLinkedStagedSource, self).__eq__(other) and \
               self.staging_environment == other.staging_environment and \
               self.staging_environment_user == other.staging_environment_user and \
               self.staging_mount_base == other.staging_mount_base

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def staging_environment(self):
        """
        The environment used as an intermediate stage to pull data into
        Delphix.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_environment[0]

    @staging_environment.setter
    def staging_environment(self, value):
        self._staging_environment = (value, True)

    @property
    def staging_environment_user(self):
        """
        The environment user used to access the staging environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_environment_user[0]

    @staging_environment_user.setter
    def staging_environment_user(self, value):
        self._staging_environment_user = (value, True)

    @property
    def staging_mount_base(self):
        """
        The base mount point for the NFS mount on the staging environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_mount_base[0]

    @staging_mount_base.setter
    def staging_mount_base(self, value):
        self._staging_mount_base = (value, True)

