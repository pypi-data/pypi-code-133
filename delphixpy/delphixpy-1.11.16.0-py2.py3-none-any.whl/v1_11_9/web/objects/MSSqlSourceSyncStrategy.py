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
#     /delphix-mssql-source-sync-strategy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.MSSqlSyncStrategy import MSSqlSyncStrategy
from delphixpy.v1_11_9 import factory
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

class MSSqlSourceSyncStrategy(MSSqlSyncStrategy):
    """
    *(extends* :py:class:`v1_11_9.web.vo.MSSqlSyncStrategy` *)* MSSQL specific
    parameters for source based sync strategy.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlSourceSyncStrategy, self).__init__()
        self._type = ("MSSqlSourceSyncStrategy", True)
        self._config = (self.__undef__, True)
        self._mssql_user = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlSourceSyncStrategy, cls).from_dict(data, dirty, undef_enabled)
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        if "mssqlUser" in data and data["mssqlUser"] is not None:
            obj._mssql_user = (factory.create_object(data["mssqlUser"], "MSSqlUser"), dirty)
            factory.validate_type(obj._mssql_user[0], "MSSqlUser")
        else:
            obj._mssql_user = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlSourceSyncStrategy, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "mssql_user" == "type" or (self.mssql_user is not self.__undef__ and (not (dirty and not self._mssql_user[1]) or isinstance(self.mssql_user, list) or belongs_to_parent)):
            dct["mssqlUser"] = dictify(self.mssql_user, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._mssql_user = (self._mssql_user[0], True)

    def is_dirty(self):
        return any([self._config[1], self._mssql_user[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlSourceSyncStrategy):
            return False
        return super(MSSqlSourceSyncStrategy, self).__eq__(other) and \
               self.config == other.config and \
               self.mssql_user == other.mssql_user

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def config(self):
        """
        Reference to the configuration for the source.

        :rtype: ``TEXT_TYPE``
        """
        return self._config[0]

    @config.setter
    def config(self, value):
        self._config = (value, True)

    @property
    def mssql_user(self):
        """
        Information about the mssql user for linking.

        :rtype: :py:class:`v1_11_9.web.vo.MSSqlUser`
        """
        return self._mssql_user[0]

    @mssql_user.setter
    def mssql_user(self, value):
        self._mssql_user = (value, True)

