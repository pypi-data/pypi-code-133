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
#     /delphix-appdata-create-transformation-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.CreateTransformationParameters import CreateTransformationParameters
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

class AppDataCreateTransformationParameters(CreateTransformationParameters):
    """
    *(extends* :py:class:`v1_11_15.web.vo.CreateTransformationParameters` *)*
    Represents the parameters of a createTransformation request for an AppData
    container.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataCreateTransformationParameters, self).__init__()
        self._type = ("AppDataCreateTransformationParameters", True)
        self._container = (self.__undef__, True)
        self._payload = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataCreateTransformationParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "AppDataContainer"), dirty)
            factory.validate_type(obj._container[0], "AppDataContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "payload" in data and data["payload"] is not None:
            obj._payload = (data["payload"], dirty)
        else:
            obj._payload = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataCreateTransformationParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "payload" == "type" or (self.payload is not self.__undef__ and (not (dirty and not self._payload[1]) or isinstance(self.payload, list) or belongs_to_parent)):
            dct["payload"] = dictify(self.payload, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._payload = (self._payload[0], True)

    def is_dirty(self):
        return any([self._container[1], self._payload[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataCreateTransformationParameters):
            return False
        return super(AppDataCreateTransformationParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.payload == other.payload

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        The container that will contain the transformed data associated with
        the newly created transformation; the "transformation container".

        :rtype: :py:class:`v1_11_15.web.vo.AppDataContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def payload(self):
        """
        The JSON payload conforming to the DraftV4 schema based on the type of
        application data being manipulated.

        :rtype: :py:class:`v1_11_15.web.vo.Json`
        """
        return self._payload[0]

    @payload.setter
    def payload(self, value):
        self._payload = (value, True)

