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
#     /delphix-mysql-linked-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.MySQLSource import MySQLSource
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

class MySQLLinkedSource(MySQLSource):
    """
    *(extends* :py:class:`v1_11_9.web.vo.MySQLSource` *)* A linked MySQL
    source.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLLinkedSource, self).__init__()
        self._type = ("MySQLLinkedSource", True)
        self._config = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._staging_source = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._config_params = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLLinkedSource, cls).from_dict(data, dirty, undef_enabled)
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._staging_source = (data.get("stagingSource", obj.__undef__), dirty)
        if obj._staging_source[0] is not None and obj._staging_source[0] is not obj.__undef__:
            assert isinstance(obj._staging_source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_source[0], type(obj._staging_source[0])))
            common.validate_format(obj._staging_source[0], "objectReference", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "MySQLSourceRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "MySQLSourceRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLLinkedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "staging_source" == "type" or (self.staging_source is not self.__undef__ and (not (dirty and not self._staging_source[1]))):
            dct["stagingSource"] = dictify(self.staging_source)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._operations = (self._operations[0], True)
        self._staging_source = (self._staging_source[0], True)
        self._runtime = (self._runtime[0], True)
        self._config_params = (self._config_params[0], True)

    def is_dirty(self):
        return any([self._config[1], self._operations[1], self._staging_source[1], self._runtime[1], self._config_params[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLLinkedSource):
            return False
        return super(MySQLLinkedSource, self).__eq__(other) and \
               self.config == other.config and \
               self.operations == other.operations and \
               self.staging_source == other.staging_source and \
               self.runtime == other.runtime and \
               self.config_params == other.config_params

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
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_11_9.web.vo.LinkedSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def staging_source(self):
        """
        The staging source for validated sync of the database.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_source[0]

    @staging_source.setter
    def staging_source(self, value):
        self._staging_source = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this source.

        :rtype: :py:class:`v1_11_9.web.vo.MySQLSourceRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def config_params(self):
        """
        MySQL database configuration parameter overrides.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @config_params.setter
    def config_params(self, value):
        self._config_params = (value, True)

