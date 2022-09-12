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
#     /delphix-validate-java-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_6 import factory
from delphixpy.v1_10_6 import common

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

class ValidateJavaParameters(TypedObject):
    """
    *(extends* :py:class:`v1_10_6.web.vo.TypedObject` *)* Mechanism to test the
    user-provided version of Java on a remote host.
    """
    def __init__(self, undef_enabled=True):
        super(ValidateJavaParameters, self).__init__()
        self._type = ("ValidateJavaParameters", True)
        self._connectivity_parameters = (self.__undef__, True)
        self._java_home = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ValidateJavaParameters, cls).from_dict(data, dirty, undef_enabled)
        if "connectivityParameters" not in data:
            raise ValueError("Missing required property \"connectivityParameters\".")
        if "connectivityParameters" in data and data["connectivityParameters"] is not None:
            obj._connectivity_parameters = (factory.create_object(data["connectivityParameters"], "ConnectivityParameters"), dirty)
            factory.validate_type(obj._connectivity_parameters[0], "ConnectivityParameters")
        else:
            obj._connectivity_parameters = (obj.__undef__, dirty)
        if "javaHome" not in data:
            raise ValueError("Missing required property \"javaHome\".")
        obj._java_home = (data.get("javaHome", obj.__undef__), dirty)
        if obj._java_home[0] is not None and obj._java_home[0] is not obj.__undef__:
            assert isinstance(obj._java_home[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._java_home[0], type(obj._java_home[0])))
            common.validate_format(obj._java_home[0], "None", 1, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ValidateJavaParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "connectivity_parameters" == "type" or (self.connectivity_parameters is not self.__undef__ and (not (dirty and not self._connectivity_parameters[1]) or isinstance(self.connectivity_parameters, list) or belongs_to_parent)):
            dct["connectivityParameters"] = dictify(self.connectivity_parameters, prop_is_list_or_vo=True)
        if "java_home" == "type" or (self.java_home is not self.__undef__ and (not (dirty and not self._java_home[1]) or isinstance(self.java_home, list) or belongs_to_parent)):
            dct["javaHome"] = dictify(self.java_home)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._connectivity_parameters = (self._connectivity_parameters[0], True)
        self._java_home = (self._java_home[0], True)

    def is_dirty(self):
        return any([self._connectivity_parameters[1], self._java_home[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ValidateJavaParameters):
            return False
        return super(ValidateJavaParameters, self).__eq__(other) and \
               self.connectivity_parameters == other.connectivity_parameters and \
               self.java_home == other.java_home

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def connectivity_parameters(self):
        """
        Parameters required to connect to the host.

        :rtype: :py:class:`v1_10_6.web.vo.ConnectivityParameters`
        """
        return self._connectivity_parameters[0]

    @connectivity_parameters.setter
    def connectivity_parameters(self, value):
        self._connectivity_parameters = (value, True)

    @property
    def java_home(self):
        """
        The path to the user managed Java Development Kit (JDK).

        :rtype: ``TEXT_TYPE``
        """
        return self._java_home[0]

    @java_home.setter
    def java_home(self, value):
        self._java_home = (value, True)

