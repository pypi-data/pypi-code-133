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
#     /delphix-appdata-link-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.LinkData import LinkData
from delphixpy.v1_10_5 import factory
from delphixpy.v1_10_5 import common

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

class AppDataLinkData(LinkData):
    """
    *(extends* :py:class:`v1_10_5.web.vo.LinkData` *)* Represents the AppData
    specific parameters of a link request.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataLinkData, self).__init__()
        self._type = ("AppDataLinkData", True)
        self._environment_user = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._parameters = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataLinkData, cls).from_dict(data, dirty, undef_enabled)
        if "environmentUser" not in data:
            raise ValueError("Missing required property \"environmentUser\".")
        obj._environment_user = (data.get("environmentUser", obj.__undef__), dirty)
        if obj._environment_user[0] is not None and obj._environment_user[0] is not obj.__undef__:
            assert isinstance(obj._environment_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment_user[0], type(obj._environment_user[0])))
            common.validate_format(obj._environment_user[0], "objectReference", None, None)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        if "parameters" not in data:
            raise ValueError("Missing required property \"parameters\".")
        if "parameters" in data and data["parameters"] is not None:
            obj._parameters = (data["parameters"], dirty)
        else:
            obj._parameters = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataLinkData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "environment_user" == "type" or (self.environment_user is not self.__undef__ and (not (dirty and not self._environment_user[1]) or isinstance(self.environment_user, list) or belongs_to_parent)):
            dct["environmentUser"] = dictify(self.environment_user)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "parameters" == "type" or (self.parameters is not self.__undef__ and (not (dirty and not self._parameters[1]) or isinstance(self.parameters, list) or belongs_to_parent)):
            dct["parameters"] = dictify(self.parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._environment_user = (self._environment_user[0], True)
        self._operations = (self._operations[0], True)
        self._parameters = (self._parameters[0], True)

    def is_dirty(self):
        return any([self._environment_user[1], self._operations[1], self._parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataLinkData):
            return False
        return super(AppDataLinkData, self).__eq__(other) and \
               self.environment_user == other.environment_user and \
               self.operations == other.operations and \
               self.parameters == other.parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def environment_user(self):
        """
        The OS user to use for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment_user[0]

    @environment_user.setter
    def environment_user(self, value):
        self._environment_user = (value, True)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_10_5.web.vo.LinkedSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def parameters(self):
        """
        The JSON payload conforming to the DraftV4 schema based on the type of
        application data being manipulated.

        :rtype: :py:class:`v1_10_5.web.vo.Json`
        """
        return self._parameters[0]

    @parameters.setter
    def parameters(self, value):
        self._parameters = (value, True)

