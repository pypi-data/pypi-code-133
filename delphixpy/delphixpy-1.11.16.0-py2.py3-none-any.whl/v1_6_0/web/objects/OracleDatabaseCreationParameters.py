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
#     /delphix-oracle-database-creation-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.EmptyDatasetCreationParameters import EmptyDatasetCreationParameters
from delphixpy.v1_6_0 import factory
from delphixpy.v1_6_0 import common

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

class OracleDatabaseCreationParameters(EmptyDatasetCreationParameters):
    """
    *(extends* :py:class:`v1_6_0.web.vo.EmptyDatasetCreationParameters` *)* The
    parameters to use as input when creating a new Oracle database.
    """
    def __init__(self, undef_enabled=True):
        super(OracleDatabaseCreationParameters, self).__init__()
        self._type = ("OracleDatabaseCreationParameters", True)
        self._character_set = (self.__undef__, True)
        self._container = (self.__undef__, True)
        self._delphix_password = (self.__undef__, True)
        self._delphix_username = (self.__undef__, True)
        self._force_logging = (self.__undef__, True)
        self._grant_select_any_dictionary = (self.__undef__, True)
        self._max_data_files = (self.__undef__, True)
        self._max_instances = (self.__undef__, True)
        self._max_log_files = (self.__undef__, True)
        self._max_log_history = (self.__undef__, True)
        self._national_character_set = (self.__undef__, True)
        self._redo_logs = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._source_config = (self.__undef__, True)
        self._sys_datafile = (self.__undef__, True)
        self._sys_password = (self.__undef__, True)
        self._sysaux_datafile = (self.__undef__, True)
        self._system_password = (self.__undef__, True)
        self._temp_tablespace = (self.__undef__, True)
        self._timezone_file_version = (self.__undef__, True)
        self._undo_tablespace = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleDatabaseCreationParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._character_set = (data.get("characterSet", obj.__undef__), dirty)
        if obj._character_set[0] is not None and obj._character_set[0] is not obj.__undef__:
            assert isinstance(obj._character_set[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._character_set[0], type(obj._character_set[0])))
            common.validate_format(obj._character_set[0], "None", None, None)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "OracleDatabaseContainer"), dirty)
            factory.validate_type(obj._container[0], "OracleDatabaseContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "delphixPassword" not in data:
            raise ValueError("Missing required property \"delphixPassword\".")
        obj._delphix_password = (data.get("delphixPassword", obj.__undef__), dirty)
        if obj._delphix_password[0] is not None and obj._delphix_password[0] is not obj.__undef__:
            assert isinstance(obj._delphix_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._delphix_password[0], type(obj._delphix_password[0])))
            common.validate_format(obj._delphix_password[0], "password", None, None)
        if "delphixUsername" not in data:
            raise ValueError("Missing required property \"delphixUsername\".")
        obj._delphix_username = (data.get("delphixUsername", obj.__undef__), dirty)
        if obj._delphix_username[0] is not None and obj._delphix_username[0] is not obj.__undef__:
            assert isinstance(obj._delphix_username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._delphix_username[0], type(obj._delphix_username[0])))
            common.validate_format(obj._delphix_username[0], "None", None, None)
        obj._force_logging = (data.get("forceLogging", obj.__undef__), dirty)
        if obj._force_logging[0] is not None and obj._force_logging[0] is not obj.__undef__:
            assert isinstance(obj._force_logging[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._force_logging[0], type(obj._force_logging[0])))
            common.validate_format(obj._force_logging[0], "None", None, None)
        obj._grant_select_any_dictionary = (data.get("grantSelectAnyDictionary", obj.__undef__), dirty)
        if obj._grant_select_any_dictionary[0] is not None and obj._grant_select_any_dictionary[0] is not obj.__undef__:
            assert isinstance(obj._grant_select_any_dictionary[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._grant_select_any_dictionary[0], type(obj._grant_select_any_dictionary[0])))
            common.validate_format(obj._grant_select_any_dictionary[0], "None", None, None)
        obj._max_data_files = (data.get("maxDataFiles", obj.__undef__), dirty)
        if obj._max_data_files[0] is not None and obj._max_data_files[0] is not obj.__undef__:
            assert isinstance(obj._max_data_files[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._max_data_files[0], type(obj._max_data_files[0])))
            common.validate_format(obj._max_data_files[0], "None", None, None)
        obj._max_instances = (data.get("maxInstances", obj.__undef__), dirty)
        if obj._max_instances[0] is not None and obj._max_instances[0] is not obj.__undef__:
            assert isinstance(obj._max_instances[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._max_instances[0], type(obj._max_instances[0])))
            common.validate_format(obj._max_instances[0], "None", None, None)
        obj._max_log_files = (data.get("maxLogFiles", obj.__undef__), dirty)
        if obj._max_log_files[0] is not None and obj._max_log_files[0] is not obj.__undef__:
            assert isinstance(obj._max_log_files[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._max_log_files[0], type(obj._max_log_files[0])))
            common.validate_format(obj._max_log_files[0], "None", None, None)
        obj._max_log_history = (data.get("maxLogHistory", obj.__undef__), dirty)
        if obj._max_log_history[0] is not None and obj._max_log_history[0] is not obj.__undef__:
            assert isinstance(obj._max_log_history[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._max_log_history[0], type(obj._max_log_history[0])))
            common.validate_format(obj._max_log_history[0], "None", None, None)
        obj._national_character_set = (data.get("nationalCharacterSet", obj.__undef__), dirty)
        if obj._national_character_set[0] is not None and obj._national_character_set[0] is not obj.__undef__:
            assert isinstance(obj._national_character_set[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._national_character_set[0], type(obj._national_character_set[0])))
            assert obj._national_character_set[0] in ['AL16UTF16', 'UTF8'], "Expected enum ['AL16UTF16', 'UTF8'] but got %s" % obj._national_character_set[0]
            common.validate_format(obj._national_character_set[0], "None", None, None)
        obj._redo_logs = []
        for item in data.get("redoLogs") or []:
            obj._redo_logs.append(factory.create_object(item))
            factory.validate_type(obj._redo_logs[-1], "OracleRedoLogFileSpecification")
        obj._redo_logs = (obj._redo_logs, dirty)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "OracleWarehouseSource"), dirty)
            factory.validate_type(obj._source[0], "OracleWarehouseSource")
        else:
            obj._source = (obj.__undef__, dirty)
        if "sourceConfig" not in data:
            raise ValueError("Missing required property \"sourceConfig\".")
        if "sourceConfig" in data and data["sourceConfig"] is not None:
            obj._source_config = (factory.create_object(data["sourceConfig"], "OracleBaseDBConfig"), dirty)
            factory.validate_type(obj._source_config[0], "OracleBaseDBConfig")
        else:
            obj._source_config = (obj.__undef__, dirty)
        if "sysDatafile" in data and data["sysDatafile"] is not None:
            obj._sys_datafile = (factory.create_object(data["sysDatafile"], "OracleSystemDatafileSpecification"), dirty)
            factory.validate_type(obj._sys_datafile[0], "OracleSystemDatafileSpecification")
        else:
            obj._sys_datafile = (obj.__undef__, dirty)
        if "sysPassword" not in data:
            raise ValueError("Missing required property \"sysPassword\".")
        obj._sys_password = (data.get("sysPassword", obj.__undef__), dirty)
        if obj._sys_password[0] is not None and obj._sys_password[0] is not obj.__undef__:
            assert isinstance(obj._sys_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._sys_password[0], type(obj._sys_password[0])))
            common.validate_format(obj._sys_password[0], "password", None, None)
        if "sysauxDatafile" in data and data["sysauxDatafile"] is not None:
            obj._sysaux_datafile = (factory.create_object(data["sysauxDatafile"], "OracleSysauxDatafileSpecification"), dirty)
            factory.validate_type(obj._sysaux_datafile[0], "OracleSysauxDatafileSpecification")
        else:
            obj._sysaux_datafile = (obj.__undef__, dirty)
        if "systemPassword" not in data:
            raise ValueError("Missing required property \"systemPassword\".")
        obj._system_password = (data.get("systemPassword", obj.__undef__), dirty)
        if obj._system_password[0] is not None and obj._system_password[0] is not obj.__undef__:
            assert isinstance(obj._system_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._system_password[0], type(obj._system_password[0])))
            common.validate_format(obj._system_password[0], "password", None, None)
        if "tempTablespace" in data and data["tempTablespace"] is not None:
            obj._temp_tablespace = (factory.create_object(data["tempTablespace"], "OracleTempfileSpecification"), dirty)
            factory.validate_type(obj._temp_tablespace[0], "OracleTempfileSpecification")
        else:
            obj._temp_tablespace = (obj.__undef__, dirty)
        obj._timezone_file_version = (data.get("timezoneFileVersion", obj.__undef__), dirty)
        if obj._timezone_file_version[0] is not None and obj._timezone_file_version[0] is not obj.__undef__:
            assert isinstance(obj._timezone_file_version[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._timezone_file_version[0], type(obj._timezone_file_version[0])))
            common.validate_format(obj._timezone_file_version[0], "None", None, None)
        if "undoTablespace" in data and data["undoTablespace"] is not None:
            obj._undo_tablespace = (factory.create_object(data["undoTablespace"], "OracleUndoDatafileSpecification"), dirty)
            factory.validate_type(obj._undo_tablespace[0], "OracleUndoDatafileSpecification")
        else:
            obj._undo_tablespace = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleDatabaseCreationParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "character_set" == "type" or (self.character_set is not self.__undef__ and (not (dirty and not self._character_set[1]) or isinstance(self.character_set, list) or belongs_to_parent)):
            dct["characterSet"] = dictify(self.character_set)
        elif belongs_to_parent and self.character_set is self.__undef__:
            dct["characterSet"] = "AL32UTF8"
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "delphix_password" == "type" or (self.delphix_password is not self.__undef__ and (not (dirty and not self._delphix_password[1]) or isinstance(self.delphix_password, list) or belongs_to_parent)):
            dct["delphixPassword"] = dictify(self.delphix_password)
        if "delphix_username" == "type" or (self.delphix_username is not self.__undef__ and (not (dirty and not self._delphix_username[1]) or isinstance(self.delphix_username, list) or belongs_to_parent)):
            dct["delphixUsername"] = dictify(self.delphix_username)
        if "force_logging" == "type" or (self.force_logging is not self.__undef__ and (not (dirty and not self._force_logging[1]) or isinstance(self.force_logging, list) or belongs_to_parent)):
            dct["forceLogging"] = dictify(self.force_logging)
        elif belongs_to_parent and self.force_logging is self.__undef__:
            dct["forceLogging"] = False
        if "grant_select_any_dictionary" == "type" or (self.grant_select_any_dictionary is not self.__undef__ and (not (dirty and not self._grant_select_any_dictionary[1]) or isinstance(self.grant_select_any_dictionary, list) or belongs_to_parent)):
            dct["grantSelectAnyDictionary"] = dictify(self.grant_select_any_dictionary)
        elif belongs_to_parent and self.grant_select_any_dictionary is self.__undef__:
            dct["grantSelectAnyDictionary"] = True
        if "max_data_files" == "type" or (self.max_data_files is not self.__undef__ and (not (dirty and not self._max_data_files[1]) or isinstance(self.max_data_files, list) or belongs_to_parent)):
            dct["maxDataFiles"] = dictify(self.max_data_files)
        elif belongs_to_parent and self.max_data_files is self.__undef__:
            dct["maxDataFiles"] = 32
        if "max_instances" == "type" or (self.max_instances is not self.__undef__ and (not (dirty and not self._max_instances[1]) or isinstance(self.max_instances, list) or belongs_to_parent)):
            dct["maxInstances"] = dictify(self.max_instances)
        elif belongs_to_parent and self.max_instances is self.__undef__:
            dct["maxInstances"] = 32
        if "max_log_files" == "type" or (self.max_log_files is not self.__undef__ and (not (dirty and not self._max_log_files[1]) or isinstance(self.max_log_files, list) or belongs_to_parent)):
            dct["maxLogFiles"] = dictify(self.max_log_files)
        elif belongs_to_parent and self.max_log_files is self.__undef__:
            dct["maxLogFiles"] = 64
        if "max_log_history" == "type" or (self.max_log_history is not self.__undef__ and (not (dirty and not self._max_log_history[1]) or isinstance(self.max_log_history, list) or belongs_to_parent)):
            dct["maxLogHistory"] = dictify(self.max_log_history)
        elif belongs_to_parent and self.max_log_history is self.__undef__:
            dct["maxLogHistory"] = 100
        if "national_character_set" == "type" or (self.national_character_set is not self.__undef__ and (not (dirty and not self._national_character_set[1]) or isinstance(self.national_character_set, list) or belongs_to_parent)):
            dct["nationalCharacterSet"] = dictify(self.national_character_set)
        elif belongs_to_parent and self.national_character_set is self.__undef__:
            dct["nationalCharacterSet"] = "AL16UTF16"
        if "redo_logs" == "type" or (self.redo_logs is not self.__undef__ and (not (dirty and not self._redo_logs[1]) or isinstance(self.redo_logs, list) or belongs_to_parent)):
            dct["redoLogs"] = dictify(self.redo_logs, prop_is_list_or_vo=True)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        if "source_config" == "type" or (self.source_config is not self.__undef__ and (not (dirty and not self._source_config[1]) or isinstance(self.source_config, list) or belongs_to_parent)):
            dct["sourceConfig"] = dictify(self.source_config, prop_is_list_or_vo=True)
        if "sys_datafile" == "type" or (self.sys_datafile is not self.__undef__ and (not (dirty and not self._sys_datafile[1]) or isinstance(self.sys_datafile, list) or belongs_to_parent)):
            dct["sysDatafile"] = dictify(self.sys_datafile, prop_is_list_or_vo=True)
        if "sys_password" == "type" or (self.sys_password is not self.__undef__ and (not (dirty and not self._sys_password[1]) or isinstance(self.sys_password, list) or belongs_to_parent)):
            dct["sysPassword"] = dictify(self.sys_password)
        if "sysaux_datafile" == "type" or (self.sysaux_datafile is not self.__undef__ and (not (dirty and not self._sysaux_datafile[1]) or isinstance(self.sysaux_datafile, list) or belongs_to_parent)):
            dct["sysauxDatafile"] = dictify(self.sysaux_datafile, prop_is_list_or_vo=True)
        if "system_password" == "type" or (self.system_password is not self.__undef__ and (not (dirty and not self._system_password[1]) or isinstance(self.system_password, list) or belongs_to_parent)):
            dct["systemPassword"] = dictify(self.system_password)
        if "temp_tablespace" == "type" or (self.temp_tablespace is not self.__undef__ and (not (dirty and not self._temp_tablespace[1]) or isinstance(self.temp_tablespace, list) or belongs_to_parent)):
            dct["tempTablespace"] = dictify(self.temp_tablespace, prop_is_list_or_vo=True)
        if "timezone_file_version" == "type" or (self.timezone_file_version is not self.__undef__ and (not (dirty and not self._timezone_file_version[1]) or isinstance(self.timezone_file_version, list) or belongs_to_parent)):
            dct["timezoneFileVersion"] = dictify(self.timezone_file_version)
        if "undo_tablespace" == "type" or (self.undo_tablespace is not self.__undef__ and (not (dirty and not self._undo_tablespace[1]) or isinstance(self.undo_tablespace, list) or belongs_to_parent)):
            dct["undoTablespace"] = dictify(self.undo_tablespace, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._character_set = (self._character_set[0], True)
        self._container = (self._container[0], True)
        self._delphix_password = (self._delphix_password[0], True)
        self._delphix_username = (self._delphix_username[0], True)
        self._force_logging = (self._force_logging[0], True)
        self._grant_select_any_dictionary = (self._grant_select_any_dictionary[0], True)
        self._max_data_files = (self._max_data_files[0], True)
        self._max_instances = (self._max_instances[0], True)
        self._max_log_files = (self._max_log_files[0], True)
        self._max_log_history = (self._max_log_history[0], True)
        self._national_character_set = (self._national_character_set[0], True)
        self._redo_logs = (self._redo_logs[0], True)
        self._source = (self._source[0], True)
        self._source_config = (self._source_config[0], True)
        self._sys_datafile = (self._sys_datafile[0], True)
        self._sys_password = (self._sys_password[0], True)
        self._sysaux_datafile = (self._sysaux_datafile[0], True)
        self._system_password = (self._system_password[0], True)
        self._temp_tablespace = (self._temp_tablespace[0], True)
        self._timezone_file_version = (self._timezone_file_version[0], True)
        self._undo_tablespace = (self._undo_tablespace[0], True)

    def is_dirty(self):
        return any([self._character_set[1], self._container[1], self._delphix_password[1], self._delphix_username[1], self._force_logging[1], self._grant_select_any_dictionary[1], self._max_data_files[1], self._max_instances[1], self._max_log_files[1], self._max_log_history[1], self._national_character_set[1], self._redo_logs[1], self._source[1], self._source_config[1], self._sys_datafile[1], self._sys_password[1], self._sysaux_datafile[1], self._system_password[1], self._temp_tablespace[1], self._timezone_file_version[1], self._undo_tablespace[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleDatabaseCreationParameters):
            return False
        return super(OracleDatabaseCreationParameters, self).__eq__(other) and \
               self.character_set == other.character_set and \
               self.container == other.container and \
               self.delphix_password == other.delphix_password and \
               self.delphix_username == other.delphix_username and \
               self.force_logging == other.force_logging and \
               self.grant_select_any_dictionary == other.grant_select_any_dictionary and \
               self.max_data_files == other.max_data_files and \
               self.max_instances == other.max_instances and \
               self.max_log_files == other.max_log_files and \
               self.max_log_history == other.max_log_history and \
               self.national_character_set == other.national_character_set and \
               self.redo_logs == other.redo_logs and \
               self.source == other.source and \
               self.source_config == other.source_config and \
               self.sys_datafile == other.sys_datafile and \
               self.sys_password == other.sys_password and \
               self.sysaux_datafile == other.sysaux_datafile and \
               self.system_password == other.system_password and \
               self.temp_tablespace == other.temp_tablespace and \
               self.timezone_file_version == other.timezone_file_version and \
               self.undo_tablespace == other.undo_tablespace

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def character_set(self):
        """
        *(default value: AL32UTF8)* The character set the database uses to
        store data.

        :rtype: ``TEXT_TYPE``
        """
        return self._character_set[0]

    @character_set.setter
    def character_set(self, value):
        self._character_set = (value, True)

    @property
    def container(self):
        """
        The new container for the created database.

        :rtype: :py:class:`v1_6_0.web.vo.OracleDatabaseContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def delphix_password(self):
        """
        The password for the Delphix database user.

        :rtype: ``TEXT_TYPE``
        """
        return self._delphix_password[0]

    @delphix_password.setter
    def delphix_password(self, value):
        self._delphix_password = (value, True)

    @property
    def delphix_username(self):
        """
        The name of the Delphix database user.

        :rtype: ``TEXT_TYPE``
        """
        return self._delphix_username[0]

    @delphix_username.setter
    def delphix_username(self, value):
        self._delphix_username = (value, True)

    @property
    def force_logging(self):
        """
        Puts the database into FORCE LOGGING mode. Oracle Database will log all
        changes in the database except for changes in temporary tablespaces and
        temporary segments.

        :rtype: ``bool``
        """
        return self._force_logging[0]

    @force_logging.setter
    def force_logging(self, value):
        self._force_logging = (value, True)

    @property
    def grant_select_any_dictionary(self):
        """
        *(default value: True)* Grants the SELECT ANY DICTIONARY system
        privilege to the Delphix database user. If disabled, the Delphix
        database user will only have SELECT access to a limited set of views.

        :rtype: ``bool``
        """
        return self._grant_select_any_dictionary[0]

    @grant_select_any_dictionary.setter
    def grant_select_any_dictionary(self, value):
        self._grant_select_any_dictionary = (value, True)

    @property
    def max_data_files(self):
        """
        *(default value: 32)* The initial sizing of the data files section of
        the control file at CREATE DATABASE or CREATE CONTROLFILE time.

        :rtype: ``int``
        """
        return self._max_data_files[0]

    @max_data_files.setter
    def max_data_files(self, value):
        self._max_data_files = (value, True)

    @property
    def max_instances(self):
        """
        *(default value: 32)* The maximum number of instances that can
        simultaneously have this database mounted and open.

        :rtype: ``int``
        """
        return self._max_instances[0]

    @max_instances.setter
    def max_instances(self, value):
        self._max_instances = (value, True)

    @property
    def max_log_files(self):
        """
        *(default value: 64)* The maximum number of redo log files that can
        ever be created for the database.

        :rtype: ``int``
        """
        return self._max_log_files[0]

    @max_log_files.setter
    def max_log_files(self, value):
        self._max_log_files = (value, True)

    @property
    def max_log_history(self):
        """
        *(default value: 100)* The maximum number of archived redo log files
        for automatic media recovery of Oracle RAC.

        :rtype: ``int``
        """
        return self._max_log_history[0]

    @max_log_history.setter
    def max_log_history(self, value):
        self._max_log_history = (value, True)

    @property
    def national_character_set(self):
        """
        *(default value: AL16UTF16)* The national character set used to store
        data in columns specifically defined as NCHAR, NCLOB, or NVARCHAR2.
        *(permitted values: AL16UTF16, UTF8)*

        :rtype: ``TEXT_TYPE``
        """
        return self._national_character_set[0]

    @national_character_set.setter
    def national_character_set(self, value):
        self._national_character_set = (value, True)

    @property
    def redo_logs(self):
        """
        The redo log files. If no filename is provided, Oracle-managed files
        will be used.

        :rtype: ``list`` of
            :py:class:`v1_6_0.web.vo.OracleRedoLogFileSpecification`
        """
        return self._redo_logs[0]

    @redo_logs.setter
    def redo_logs(self, value):
        self._redo_logs = (value, True)

    @property
    def source(self):
        """
        The source that describes the created database instance.

        :rtype: :py:class:`v1_6_0.web.vo.OracleWarehouseSource`
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

        :rtype: :py:class:`v1_6_0.web.vo.OracleBaseDBConfig`
        """
        return self._source_config[0]

    @source_config.setter
    def source_config(self, value):
        self._source_config = (value, True)

    @property
    def sys_datafile(self):
        """
        The datafile for the SYSTEM tablespace. If no filename is provided,
        Oracle-managed files will be used.

        :rtype: :py:class:`v1_6_0.web.vo.OracleSystemDatafileSpecification`
        """
        return self._sys_datafile[0]

    @sys_datafile.setter
    def sys_datafile(self, value):
        self._sys_datafile = (value, True)

    @property
    def sys_password(self):
        """
        The password for the SYS user.

        :rtype: ``TEXT_TYPE``
        """
        return self._sys_password[0]

    @sys_password.setter
    def sys_password(self, value):
        self._sys_password = (value, True)

    @property
    def sysaux_datafile(self):
        """
        The datafile for the SYSAUX tablespace. If no filename is provided,
        Oracle-managed files will be used.

        :rtype: :py:class:`v1_6_0.web.vo.OracleSysauxDatafileSpecification`
        """
        return self._sysaux_datafile[0]

    @sysaux_datafile.setter
    def sysaux_datafile(self, value):
        self._sysaux_datafile = (value, True)

    @property
    def system_password(self):
        """
        The password for the SYSTEM user.

        :rtype: ``TEXT_TYPE``
        """
        return self._system_password[0]

    @system_password.setter
    def system_password(self, value):
        self._system_password = (value, True)

    @property
    def temp_tablespace(self):
        """
        The tempfile for the database. If no filename is provided, Oracle-
        managed files will be used.

        :rtype: :py:class:`v1_6_0.web.vo.OracleTempfileSpecification`
        """
        return self._temp_tablespace[0]

    @temp_tablespace.setter
    def temp_tablespace(self, value):
        self._temp_tablespace = (value, True)

    @property
    def timezone_file_version(self):
        """
        Indicates the timezone file version that will be used to create the
        database.

        :rtype: ``int``
        """
        return self._timezone_file_version[0]

    @timezone_file_version.setter
    def timezone_file_version(self, value):
        self._timezone_file_version = (value, True)

    @property
    def undo_tablespace(self):
        """
        The datafile to be used for undo data. If no filename is provided,
        Oracle-managed files will be used.

        :rtype: :py:class:`v1_6_0.web.vo.OracleUndoDatafileSpecification`
        """
        return self._undo_tablespace[0]

    @undo_tablespace.setter
    def undo_tablespace(self, value):
        self._undo_tablespace = (value, True)

