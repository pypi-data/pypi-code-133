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
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_0.web.objects.Operation import Operation
from delphixpy.v1_9_0 import common

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

class RunPowerShellOperation(Operation):
    """
    *(extends* :py:class:`v1_9_0.web.vo.Operation` *)* A user-specifiable
    operation that runs a PowerShell command on the target host.
    """
    def __init__(self, undef_enabled=True):
        super(RunPowerShellOperation, self).__init__()
        self._type = ("RunPowerShellOperation", True)
        self._command = (self.__undef__, True)
        self._environment = (self.__undef__, True)
        self._host = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._variables = (self.__undef__, True)
        self._output_schema = (self.__undef__, True)

    API_VERSION = "1.9.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RunPowerShellOperation, cls).from_dict(data, dirty, undef_enabled)
        obj._command = (data.get("command", obj.__undef__), dirty)
        if obj._command[0] is not None and obj._command[0] is not obj.__undef__:
            assert isinstance(obj._command[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._command[0], type(obj._command[0])))
            common.validate_format(obj._command[0], "None", None, None)
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        obj._host = (data.get("host", obj.__undef__), dirty)
        if obj._host[0] is not None and obj._host[0] is not obj.__undef__:
            assert isinstance(obj._host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._host[0], type(obj._host[0])))
            common.validate_format(obj._host[0], "objectReference", None, None)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "objectReference", None, None)
        obj._variables = (data.get("variables", obj.__undef__), dirty)
        if obj._variables[0] is not None and obj._variables[0] is not obj.__undef__:
            assert isinstance(obj._variables[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._variables[0], type(obj._variables[0])))
            common.validate_format(obj._variables[0], "None", None, None)
        if "outputSchema" in data and data["outputSchema"] is not None:
            obj._output_schema = (data["outputSchema"], dirty)
        else:
            obj._output_schema = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RunPowerShellOperation, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "command" == "type" or (self.command is not self.__undef__ and (not (dirty and not self._command[1]) or isinstance(self.command, list) or belongs_to_parent)):
            dct["command"] = dictify(self.command)
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]) or isinstance(self.environment, list) or belongs_to_parent)):
            dct["environment"] = dictify(self.environment)
        if "host" == "type" or (self.host is not self.__undef__ and (not (dirty and not self._host[1]) or isinstance(self.host, list) or belongs_to_parent)):
            dct["host"] = dictify(self.host)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        if "variables" == "type" or (self.variables is not self.__undef__ and (not (dirty and not self._variables[1]) or isinstance(self.variables, list) or belongs_to_parent)):
            dct["variables"] = dictify(self.variables, prop_is_list_or_vo=True)
        if "output_schema" == "type" or (self.output_schema is not self.__undef__ and (not (dirty and not self._output_schema[1]))):
            dct["outputSchema"] = dictify(self.output_schema)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._command = (self._command[0], True)
        self._environment = (self._environment[0], True)
        self._host = (self._host[0], True)
        self._user = (self._user[0], True)
        self._variables = (self._variables[0], True)
        self._output_schema = (self._output_schema[0], True)

    def is_dirty(self):
        return any([self._command[1], self._environment[1], self._host[1], self._user[1], self._variables[1], self._output_schema[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RunPowerShellOperation):
            return False
        return super(RunPowerShellOperation, self).__eq__(other) and \
               self.command == other.command and \
               self.environment == other.environment and \
               self.host == other.host and \
               self.user == other.user and \
               self.variables == other.variables and \
               self.output_schema == other.output_schema

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def command(self):
        """
        The PowerShell command to execute on the target host.

        :rtype: ``TEXT_TYPE``
        """
        return self._command[0]

    @command.setter
    def command(self, value):
        self._command = (value, True)

    @property
    def environment(self):
        """
        The environment to execute the command on.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

    @property
    def host(self):
        """
        The host to execute the command on.

        :rtype: ``TEXT_TYPE``
        """
        return self._host[0]

    @host.setter
    def host(self, value):
        self._host = (value, True)

    @property
    def user(self):
        """
        The environment user to execute the command as.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def variables(self):
        """
        Environment variables to set when executing the command.

        :rtype: ``dict``
        """
        return self._variables[0]

    @variables.setter
    def variables(self, value):
        self._variables = (value, True)

    @property
    def output_schema(self):
        """
        An optional user defined schema for the expected output of this
        function.

        :rtype: :py:class:`v1_9_0.web.vo.SchemaDraftV4`
        """
        return self._output_schema[0]

    @output_schema.setter
    def output_schema(self, value):
        self._output_schema = (value, True)

