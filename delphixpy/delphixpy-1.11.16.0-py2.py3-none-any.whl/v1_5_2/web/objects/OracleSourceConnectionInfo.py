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
#     /delphix-oracle-source-connection-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_2.web.objects.SourceConnectionInfo import SourceConnectionInfo
from delphixpy.v1_5_2 import common

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

class OracleSourceConnectionInfo(SourceConnectionInfo):
    """
    *(extends* :py:class:`v1_5_2.web.vo.SourceConnectionInfo` *)* Contains
    information that can be used to connect to a single instance Oracle source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleSourceConnectionInfo, self).__init__()
        self._type = ("OracleSourceConnectionInfo", True)
        self._database_name = (self.__undef__, True)
        self._jdbc_strings = (self.__undef__, True)
        self._oracle_home = (self.__undef__, True)

    API_VERSION = "1.5.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleSourceConnectionInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._database_name = (data.get("databaseName", obj.__undef__), dirty)
        if obj._database_name[0] is not None and obj._database_name[0] is not obj.__undef__:
            assert isinstance(obj._database_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_name[0], type(obj._database_name[0])))
            common.validate_format(obj._database_name[0], "None", None, None)
        obj._jdbc_strings = []
        for item in data.get("jdbcStrings") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._jdbc_strings.append(item)
        obj._jdbc_strings = (obj._jdbc_strings, dirty)
        obj._oracle_home = (data.get("oracleHome", obj.__undef__), dirty)
        if obj._oracle_home[0] is not None and obj._oracle_home[0] is not obj.__undef__:
            assert isinstance(obj._oracle_home[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._oracle_home[0], type(obj._oracle_home[0])))
            common.validate_format(obj._oracle_home[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleSourceConnectionInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "database_name" == "type" or (self.database_name is not self.__undef__ and (not (dirty and not self._database_name[1]))):
            dct["databaseName"] = dictify(self.database_name)
        if "jdbc_strings" == "type" or (self.jdbc_strings is not self.__undef__ and (not (dirty and not self._jdbc_strings[1]))):
            dct["jdbcStrings"] = dictify(self.jdbc_strings)
        if "oracle_home" == "type" or (self.oracle_home is not self.__undef__ and (not (dirty and not self._oracle_home[1]))):
            dct["oracleHome"] = dictify(self.oracle_home)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._database_name = (self._database_name[0], True)
        self._jdbc_strings = (self._jdbc_strings[0], True)
        self._oracle_home = (self._oracle_home[0], True)

    def is_dirty(self):
        return any([self._database_name[1], self._jdbc_strings[1], self._oracle_home[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleSourceConnectionInfo):
            return False
        return super(OracleSourceConnectionInfo, self).__eq__(other) and \
               self.database_name == other.database_name and \
               self.jdbc_strings == other.jdbc_strings and \
               self.oracle_home == other.oracle_home

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def database_name(self):
        """
        The database name.

        :rtype: ``TEXT_TYPE``
        """
        return self._database_name[0]

    @database_name.setter
    def database_name(self, value):
        self._database_name = (value, True)

    @property
    def jdbc_strings(self):
        """
        The JDBC strings used to connect to the source.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._jdbc_strings[0]

    @jdbc_strings.setter
    def jdbc_strings(self, value):
        self._jdbc_strings = (value, True)

    @property
    def oracle_home(self):
        """
        The Oracle installation home.

        :rtype: ``TEXT_TYPE``
        """
        return self._oracle_home[0]

    @oracle_home.setter
    def oracle_home(self, value):
        self._oracle_home = (value, True)

