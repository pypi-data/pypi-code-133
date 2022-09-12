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
#     /delphix-mssql-si-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_1.web.objects.MSSqlDBConfig import MSSqlDBConfig
from delphixpy.v1_4_1 import factory
from delphixpy.v1_4_1 import common

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

class MSSqlSIConfig(MSSqlDBConfig):
    """
    *(extends* :py:class:`v1_4_1.web.vo.MSSqlDBConfig` *)* Configuration
    information for a single instance MSSQL Source
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlSIConfig, self).__init__()
        self._type = ("MSSqlSIConfig", True)
        self._instance = (self.__undef__, True)

    API_VERSION = "1.4.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlSIConfig, cls).from_dict(data, dirty, undef_enabled)
        if "instance" in data and data["instance"] is not None:
            obj._instance = (factory.create_object(data["instance"], "MSSqlInstanceConfig"), dirty)
            factory.validate_type(obj._instance[0], "MSSqlInstanceConfig")
        else:
            obj._instance = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlSIConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "instance" == "type" or (self.instance is not self.__undef__ and (not (dirty and not self._instance[1]) or isinstance(self.instance, list) or belongs_to_parent)):
            dct["instance"] = dictify(self.instance, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._instance = (self._instance[0], True)

    def is_dirty(self):
        return any([self._instance[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlSIConfig):
            return False
        return super(MSSqlSIConfig, self).__eq__(other) and \
               self.instance == other.instance

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def instance(self):
        """
        The MSSQL instance.

        :rtype: :py:class:`v1_4_1.web.vo.MSSqlInstanceConfig`
        """
        return self._instance[0]

    @instance.setter
    def instance(self, value):
        self._instance = (value, True)

