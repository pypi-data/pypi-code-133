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
#     /delphix-oracle-provision-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_0.web.objects.ProvisionParameters import ProvisionParameters
from delphixpy.v1_4_0 import factory
from delphixpy.v1_4_0 import common

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

class OracleProvisionParameters(ProvisionParameters):
    """
    *(extends* :py:class:`v1_4_0.web.vo.ProvisionParameters` *)* The parameters
    to use as input to provision oracle databases.
    """
    def __init__(self, undef_enabled=True):
        super(OracleProvisionParameters, self).__init__()
        self._type = ("OracleProvisionParameters", True)
        self._container = (self.__undef__, True)
        self._credential = (self.__undef__, True)
        self._open_resetlogs = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._source_config = (self.__undef__, True)
        self._username = (self.__undef__, True)

    API_VERSION = "1.4.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleProvisionParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "OracleDatabaseContainer"), dirty)
            factory.validate_type(obj._container[0], "OracleDatabaseContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "credential" in data and data["credential"] is not None:
            obj._credential = (factory.create_object(data["credential"], "Credential"), dirty)
            factory.validate_type(obj._credential[0], "Credential")
        else:
            obj._credential = (obj.__undef__, dirty)
        obj._open_resetlogs = (data.get("openResetlogs", obj.__undef__), dirty)
        if obj._open_resetlogs[0] is not None and obj._open_resetlogs[0] is not obj.__undef__:
            assert isinstance(obj._open_resetlogs[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._open_resetlogs[0], type(obj._open_resetlogs[0])))
            common.validate_format(obj._open_resetlogs[0], "None", None, None)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "OracleVirtualSource"), dirty)
            factory.validate_type(obj._source[0], "OracleVirtualSource")
        else:
            obj._source = (obj.__undef__, dirty)
        if "sourceConfig" not in data:
            raise ValueError("Missing required property \"sourceConfig\".")
        if "sourceConfig" in data and data["sourceConfig"] is not None:
            obj._source_config = (factory.create_object(data["sourceConfig"], "OracleBaseDBConfig"), dirty)
            factory.validate_type(obj._source_config[0], "OracleBaseDBConfig")
        else:
            obj._source_config = (obj.__undef__, dirty)
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleProvisionParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "credential" == "type" or (self.credential is not self.__undef__ and (not (dirty and not self._credential[1]) or isinstance(self.credential, list) or belongs_to_parent)):
            dct["credential"] = dictify(self.credential, prop_is_list_or_vo=True)
        if "open_resetlogs" == "type" or (self.open_resetlogs is not self.__undef__ and (not (dirty and not self._open_resetlogs[1]) or isinstance(self.open_resetlogs, list) or belongs_to_parent)):
            dct["openResetlogs"] = dictify(self.open_resetlogs)
        elif belongs_to_parent and self.open_resetlogs is self.__undef__:
            dct["openResetlogs"] = True
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        if "source_config" == "type" or (self.source_config is not self.__undef__ and (not (dirty and not self._source_config[1]) or isinstance(self.source_config, list) or belongs_to_parent)):
            dct["sourceConfig"] = dictify(self.source_config, prop_is_list_or_vo=True)
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]) or isinstance(self.username, list) or belongs_to_parent)):
            dct["username"] = dictify(self.username)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._credential = (self._credential[0], True)
        self._open_resetlogs = (self._open_resetlogs[0], True)
        self._source = (self._source[0], True)
        self._source_config = (self._source_config[0], True)
        self._username = (self._username[0], True)

    def is_dirty(self):
        return any([self._container[1], self._credential[1], self._open_resetlogs[1], self._source[1], self._source_config[1], self._username[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleProvisionParameters):
            return False
        return super(OracleProvisionParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.credential == other.credential and \
               self.open_resetlogs == other.open_resetlogs and \
               self.source == other.source and \
               self.source_config == other.source_config and \
               self.username == other.username

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        The new container for the provisioned database.

        :rtype: :py:class:`v1_4_0.web.vo.OracleDatabaseContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def credential(self):
        """
        The security credential of the privileged user to run the provision
        operation as.

        :rtype: :py:class:`v1_4_0.web.vo.Credential`
        """
        return self._credential[0]

    @credential.setter
    def credential(self, value):
        self._credential = (value, True)

    @property
    def open_resetlogs(self):
        """
        *(default value: True)* Flag indicating whether to open the database
        after provision.

        :rtype: ``bool``
        """
        return self._open_resetlogs[0]

    @open_resetlogs.setter
    def open_resetlogs(self, value):
        self._open_resetlogs = (value, True)

    @property
    def source(self):
        """
        The source that describes an external database instance.

        :rtype: :py:class:`v1_4_0.web.vo.OracleVirtualSource`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def source_config(self):
        """
        The source config including dynamically discovered attributes of the
        source.

        :rtype: :py:class:`v1_4_0.web.vo.OracleBaseDBConfig`
        """
        return self._source_config[0]

    @source_config.setter
    def source_config(self, value):
        self._source_config = (value, True)

    @property
    def username(self):
        """
        The name of the privileged user to run the provision operation as.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

