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
#     /delphix-appdata-direct-source-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_2.web.objects.AppDataSourceConfig import AppDataSourceConfig
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

class AppDataDirectSourceConfig(AppDataSourceConfig):
    """
    *(extends* :py:class:`v1_8_2.web.vo.AppDataSourceConfig` *)* Source config
    for directly linked AppData sources.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataDirectSourceConfig, self).__init__()
        self._type = ("AppDataDirectSourceConfig", True)
        self._path = (self.__undef__, True)
        self._restoration = (self.__undef__, True)

    API_VERSION = "1.8.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataDirectSourceConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._path = (data.get("path", obj.__undef__), dirty)
        if obj._path[0] is not None and obj._path[0] is not obj.__undef__:
            assert isinstance(obj._path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._path[0], type(obj._path[0])))
            common.validate_format(obj._path[0], "None", None, 1024)
        obj._restoration = (data.get("restoration", obj.__undef__), dirty)
        if obj._restoration[0] is not None and obj._restoration[0] is not obj.__undef__:
            assert isinstance(obj._restoration[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._restoration[0], type(obj._restoration[0])))
            common.validate_format(obj._restoration[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataDirectSourceConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "path" == "type" or (self.path is not self.__undef__ and (not (dirty and not self._path[1]) or isinstance(self.path, list) or belongs_to_parent)):
            dct["path"] = dictify(self.path)
        if "restoration" == "type" or (self.restoration is not self.__undef__ and (not (dirty and not self._restoration[1]))):
            dct["restoration"] = dictify(self.restoration)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._path = (self._path[0], True)
        self._restoration = (self._restoration[0], True)

    def is_dirty(self):
        return any([self._path[1], self._restoration[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataDirectSourceConfig):
            return False
        return super(AppDataDirectSourceConfig, self).__eq__(other) and \
               self.path == other.path and \
               self.restoration == other.restoration

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

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
    def restoration(self):
        """
        True if this source config is part of a restoration dataset.

        :rtype: ``bool``
        """
        return self._restoration[0]

    @restoration.setter
    def restoration(self, value):
        self._restoration = (value, True)

