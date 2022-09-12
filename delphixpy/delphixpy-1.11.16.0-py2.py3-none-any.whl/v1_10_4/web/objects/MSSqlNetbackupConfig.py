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
#     /delphix-mssql-netbackup-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_4 import common

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

class MSSqlNetbackupConfig(TypedObject):
    """
    *(extends* :py:class:`v1_10_4.web.vo.TypedObject` *)* MSSql NetBackup
    configuration.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlNetbackupConfig, self).__init__()
        self._type = ("MSSqlNetbackupConfig", True)
        self._master_name = (self.__undef__, True)
        self._source_client_name = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._config_template = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlNetbackupConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._master_name = (data.get("masterName", obj.__undef__), dirty)
        if obj._master_name[0] is not None and obj._master_name[0] is not obj.__undef__:
            assert isinstance(obj._master_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._master_name[0], type(obj._master_name[0])))
            common.validate_format(obj._master_name[0], "None", None, 256)
        obj._source_client_name = (data.get("sourceClientName", obj.__undef__), dirty)
        if obj._source_client_name[0] is not None and obj._source_client_name[0] is not obj.__undef__:
            assert isinstance(obj._source_client_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_client_name[0], type(obj._source_client_name[0])))
            common.validate_format(obj._source_client_name[0], "None", None, 256)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        obj._config_template = (data.get("configTemplate", obj.__undef__), dirty)
        if obj._config_template[0] is not None and obj._config_template[0] is not obj.__undef__:
            assert isinstance(obj._config_template[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._config_template[0], type(obj._config_template[0])))
            common.validate_format(obj._config_template[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlNetbackupConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "master_name" == "type" or (self.master_name is not self.__undef__ and (not (dirty and not self._master_name[1]) or isinstance(self.master_name, list) or belongs_to_parent)):
            dct["masterName"] = dictify(self.master_name)
        if "source_client_name" == "type" or (self.source_client_name is not self.__undef__ and (not (dirty and not self._source_client_name[1]) or isinstance(self.source_client_name, list) or belongs_to_parent)):
            dct["sourceClientName"] = dictify(self.source_client_name)
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        if "config_template" == "type" or (self.config_template is not self.__undef__ and (not (dirty and not self._config_template[1]) or isinstance(self.config_template, list) or belongs_to_parent)):
            dct["configTemplate"] = dictify(self.config_template)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._master_name = (self._master_name[0], True)
        self._source_client_name = (self._source_client_name[0], True)
        self._config_params = (self._config_params[0], True)
        self._config_template = (self._config_template[0], True)

    def is_dirty(self):
        return any([self._master_name[1], self._source_client_name[1], self._config_params[1], self._config_template[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlNetbackupConfig):
            return False
        return super(MSSqlNetbackupConfig, self).__eq__(other) and \
               self.master_name == other.master_name and \
               self.source_client_name == other.source_client_name and \
               self.config_params == other.config_params and \
               self.config_template == other.config_template

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def master_name(self):
        """
        The master server name of this NetBackup configuration.

        :rtype: ``TEXT_TYPE``
        """
        return self._master_name[0]

    @master_name.setter
    def master_name(self, value):
        self._master_name = (value, True)

    @property
    def source_client_name(self):
        """
        The source's client server name of this NetBackup configuration.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_client_name[0]

    @source_client_name.setter
    def source_client_name(self, value):
        self._source_client_name = (value, True)

    @property
    def config_params(self):
        """
        NetBackup configuration parameter overrides.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @config_params.setter
    def config_params(self, value):
        self._config_params = (value, True)

    @property
    def config_template(self):
        """
        Optional config template selection for NetBackup configurations. If
        set, configParams will be ignored.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._config_template[0]

    @config_template.setter
    def config_template(self, value):
        self._config_template = (value, True)

