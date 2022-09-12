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
#     /delphix-oracle-custom-env-var-pair.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_4.web.objects.OracleCustomEnvVar import OracleCustomEnvVar
from delphixpy.v1_11_4 import common

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

class OracleCustomEnvVarPair(OracleCustomEnvVar):
    """
    *(extends* :py:class:`v1_11_4.web.vo.OracleCustomEnvVar` *)* Dictates a
    single environment variable name and value to be set when the Delphix
    Engine administers an Oracle virtual database.
    """
    def __init__(self, undef_enabled=True):
        super(OracleCustomEnvVarPair, self).__init__()
        self._type = ("OracleCustomEnvVarPair", True)
        self._var_name = (self.__undef__, True)
        self._var_value = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleCustomEnvVarPair, cls).from_dict(data, dirty, undef_enabled)
        if "varName" not in data:
            raise ValueError("Missing required property \"varName\".")
        obj._var_name = (data.get("varName", obj.__undef__), dirty)
        if obj._var_name[0] is not None and obj._var_name[0] is not obj.__undef__:
            assert isinstance(obj._var_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._var_name[0], type(obj._var_name[0])))
            common.validate_format(obj._var_name[0], "envvarIdentifier", None, None)
        if "varValue" not in data:
            raise ValueError("Missing required property \"varValue\".")
        obj._var_value = (data.get("varValue", obj.__undef__), dirty)
        if obj._var_value[0] is not None and obj._var_value[0] is not obj.__undef__:
            assert isinstance(obj._var_value[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._var_value[0], type(obj._var_value[0])))
            common.validate_format(obj._var_value[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleCustomEnvVarPair, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "var_name" == "type" or (self.var_name is not self.__undef__ and (not (dirty and not self._var_name[1]) or isinstance(self.var_name, list) or belongs_to_parent)):
            dct["varName"] = dictify(self.var_name)
        if "var_value" == "type" or (self.var_value is not self.__undef__ and (not (dirty and not self._var_value[1]) or isinstance(self.var_value, list) or belongs_to_parent)):
            dct["varValue"] = dictify(self.var_value)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._var_name = (self._var_name[0], True)
        self._var_value = (self._var_value[0], True)

    def is_dirty(self):
        return any([self._var_name[1], self._var_value[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleCustomEnvVarPair):
            return False
        return super(OracleCustomEnvVarPair, self).__eq__(other) and \
               self.var_name == other.var_name and \
               self.var_value == other.var_value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def var_name(self):
        """
        The name of the environment variable.

        :rtype: ``TEXT_TYPE``
        """
        return self._var_name[0]

    @var_name.setter
    def var_name(self, value):
        self._var_name = (value, True)

    @property
    def var_value(self):
        """
        The value of the environment variable.

        :rtype: ``TEXT_TYPE``
        """
        return self._var_value[0]

    @var_value.setter
    def var_value(self, value):
        self._var_value = (value, True)

