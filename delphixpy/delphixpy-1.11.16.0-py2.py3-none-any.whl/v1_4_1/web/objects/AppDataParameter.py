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
#     /delphix-appdata-parameter.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_1.web.objects.TypedObject import TypedObject
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

class AppDataParameter(TypedObject):
    """
    *(extends* :py:class:`v1_4_1.web.vo.TypedObject` *)* Specifies input
    parameters to operations on AppData.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataParameter, self).__init__()
        self._type = ("AppDataParameter", True)
        self._default = (self.__undef__, True)
        self._environment_variable = (self.__undef__, True)
        self._parameter = (self.__undef__, True)

    API_VERSION = "1.4.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataParameter, cls).from_dict(data, dirty, undef_enabled)
        if "default" not in data:
            raise ValueError("Missing required property \"default\".")
        obj._default = (data.get("default", obj.__undef__), dirty)
        if obj._default[0] is not None and obj._default[0] is not obj.__undef__:
            assert isinstance(obj._default[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._default[0], type(obj._default[0])))
            common.validate_format(obj._default[0], "None", None, None)
        if "environmentVariable" not in data:
            raise ValueError("Missing required property \"environmentVariable\".")
        obj._environment_variable = (data.get("environmentVariable", obj.__undef__), dirty)
        if obj._environment_variable[0] is not None and obj._environment_variable[0] is not obj.__undef__:
            assert isinstance(obj._environment_variable[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment_variable[0], type(obj._environment_variable[0])))
            common.validate_format(obj._environment_variable[0], "None", None, None)
        if "parameter" not in data:
            raise ValueError("Missing required property \"parameter\".")
        if "parameter" in data and data["parameter"] is not None:
            obj._parameter = (factory.create_object(data["parameter"], "DynamicParameter"), dirty)
            factory.validate_type(obj._parameter[0], "DynamicParameter")
        else:
            obj._parameter = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataParameter, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "default" == "type" or (self.default is not self.__undef__ and (not (dirty and not self._default[1]) or isinstance(self.default, list) or belongs_to_parent)):
            dct["default"] = dictify(self.default)
        if "environment_variable" == "type" or (self.environment_variable is not self.__undef__ and (not (dirty and not self._environment_variable[1]) or isinstance(self.environment_variable, list) or belongs_to_parent)):
            dct["environmentVariable"] = dictify(self.environment_variable)
        if "parameter" == "type" or (self.parameter is not self.__undef__ and (not (dirty and not self._parameter[1]) or isinstance(self.parameter, list) or belongs_to_parent)):
            dct["parameter"] = dictify(self.parameter, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._default = (self._default[0], True)
        self._environment_variable = (self._environment_variable[0], True)
        self._parameter = (self._parameter[0], True)

    def is_dirty(self):
        return any([self._default[1], self._environment_variable[1], self._parameter[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataParameter):
            return False
        return super(AppDataParameter, self).__eq__(other) and \
               self.default == other.default and \
               self.environment_variable == other.environment_variable and \
               self.parameter == other.parameter

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def default(self):
        """
        The default value for this input. This value must pass validation as
        the dynamic parameter type given for this parameter.

        :rtype: ``TEXT_TYPE``
        """
        return self._default[0]

    @default.setter
    def default(self, value):
        self._default = (value, True)

    @property
    def environment_variable(self):
        """
        The name of the environment variable that will be used to pass this
        input to scripts on the target host. This name must contain only upper-
        case letters, numbers, and underscores and begin with a letter. Names
        should be prefixed with a unique name to avoid collisions with existing
        environment variables, for example use 'DLPX_WEBSERVER_PORT' instead of
        'PORT'.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment_variable[0]

    @environment_variable.setter
    def environment_variable(self, value):
        self._environment_variable = (value, True)

    @property
    def parameter(self):
        """
        The dynamic parameter to give to clients when requesting input.

        :rtype: :py:class:`v1_4_1.web.vo.DynamicParameter`
        """
        return self._parameter[0]

    @parameter.setter
    def parameter(self, value):
        self._parameter = (value, True)

