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
#     /delphix-appdata-empty-vfiles-creation-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_3.web.objects.EmptyDatasetCreationParameters import EmptyDatasetCreationParameters
from delphixpy.v1_5_3 import factory
from delphixpy.v1_5_3 import common

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

class AppDataEmptyVFilesCreationParameters(EmptyDatasetCreationParameters):
    """
    *(extends* :py:class:`v1_5_3.web.vo.EmptyDatasetCreationParameters` *)* The
    parameters to use as input when creating a new empty vFiles dataset.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataEmptyVFilesCreationParameters, self).__init__()
        self._type = ("AppDataEmptyVFilesCreationParameters", True)
        self._container = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._source_config = (self.__undef__, True)

    API_VERSION = "1.5.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataEmptyVFilesCreationParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "AppDataContainer"), dirty)
            factory.validate_type(obj._container[0], "AppDataContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "AppDataVirtualSource"), dirty)
            factory.validate_type(obj._source[0], "AppDataVirtualSource")
        else:
            obj._source = (obj.__undef__, dirty)
        if "sourceConfig" not in data:
            raise ValueError("Missing required property \"sourceConfig\".")
        if "sourceConfig" in data and data["sourceConfig"] is not None:
            obj._source_config = (factory.create_object(data["sourceConfig"], "AppDataSourceConfig"), dirty)
            factory.validate_type(obj._source_config[0], "AppDataSourceConfig")
        else:
            obj._source_config = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataEmptyVFilesCreationParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        if "source_config" == "type" or (self.source_config is not self.__undef__ and (not (dirty and not self._source_config[1]) or isinstance(self.source_config, list) or belongs_to_parent)):
            dct["sourceConfig"] = dictify(self.source_config, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._source = (self._source[0], True)
        self._source_config = (self._source_config[0], True)

    def is_dirty(self):
        return any([self._container[1], self._source[1], self._source_config[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataEmptyVFilesCreationParameters):
            return False
        return super(AppDataEmptyVFilesCreationParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.source == other.source and \
               self.source_config == other.source_config

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        The new container for the created dataset.

        :rtype: :py:class:`v1_5_3.web.vo.AppDataContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def source(self):
        """
        The source that describes an external dataset instance.

        :rtype: :py:class:`v1_5_3.web.vo.AppDataVirtualSource`
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

        :rtype: :py:class:`v1_5_3.web.vo.AppDataSourceConfig`
        """
        return self._source_config[0]

    @source_config.setter
    def source_config(self, value):
        self._source_config = (value, True)

