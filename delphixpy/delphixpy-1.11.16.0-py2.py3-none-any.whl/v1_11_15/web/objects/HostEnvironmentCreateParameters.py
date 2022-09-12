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
#     /delphix-host-environment-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.SourceEnvironmentCreateParameters import SourceEnvironmentCreateParameters
from delphixpy.v1_11_15 import factory
from delphixpy.v1_11_15 import common

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

class HostEnvironmentCreateParameters(SourceEnvironmentCreateParameters):
    """
    *(extends* :py:class:`v1_11_15.web.vo.SourceEnvironmentCreateParameters`
    *)* The parameters used for the host environment create operation.
    """
    def __init__(self, undef_enabled=True):
        super(HostEnvironmentCreateParameters, self).__init__()
        self._type = ("HostEnvironmentCreateParameters", True)
        self._host_environment = (self.__undef__, True)
        self._host_parameters = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HostEnvironmentCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "hostEnvironment" in data and data["hostEnvironment"] is not None:
            obj._host_environment = (factory.create_object(data["hostEnvironment"], "HostEnvironment"), dirty)
            factory.validate_type(obj._host_environment[0], "HostEnvironment")
        else:
            obj._host_environment = (obj.__undef__, dirty)
        if "hostParameters" in data and data["hostParameters"] is not None:
            obj._host_parameters = (factory.create_object(data["hostParameters"], "HostCreateParameters"), dirty)
            factory.validate_type(obj._host_parameters[0], "HostCreateParameters")
        else:
            obj._host_parameters = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(HostEnvironmentCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "host_environment" == "type" or (self.host_environment is not self.__undef__ and (not (dirty and not self._host_environment[1]) or isinstance(self.host_environment, list) or belongs_to_parent)):
            dct["hostEnvironment"] = dictify(self.host_environment, prop_is_list_or_vo=True)
        if "host_parameters" == "type" or (self.host_parameters is not self.__undef__ and (not (dirty and not self._host_parameters[1]) or isinstance(self.host_parameters, list) or belongs_to_parent)):
            dct["hostParameters"] = dictify(self.host_parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._host_environment = (self._host_environment[0], True)
        self._host_parameters = (self._host_parameters[0], True)

    def is_dirty(self):
        return any([self._host_environment[1], self._host_parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HostEnvironmentCreateParameters):
            return False
        return super(HostEnvironmentCreateParameters, self).__eq__(other) and \
               self.host_environment == other.host_environment and \
               self.host_parameters == other.host_parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def host_environment(self):
        """
        The host environment.

        :rtype: :py:class:`v1_11_15.web.vo.HostEnvironment`
        """
        return self._host_environment[0]

    @host_environment.setter
    def host_environment(self, value):
        self._host_environment = (value, True)

    @property
    def host_parameters(self):
        """
        The host parameters used to add a host.

        :rtype: :py:class:`v1_11_15.web.vo.HostCreateParameters`
        """
        return self._host_parameters[0]

    @host_parameters.setter
    def host_parameters(self, value):
        self._host_parameters = (value, True)

