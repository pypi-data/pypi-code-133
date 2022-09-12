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
#     /delphix-ase-provision-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.ProvisionParameters import ProvisionParameters
from delphixpy.v1_11_16 import factory
from delphixpy.v1_11_16 import common

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

class ASEProvisionParameters(ProvisionParameters):
    """
    *(extends* :py:class:`v1_11_16.web.vo.ProvisionParameters` *)* The
    parameters to use as input to provision SAP ASE databases.
    """
    def __init__(self, undef_enabled=True):
        super(ASEProvisionParameters, self).__init__()
        self._type = ("ASEProvisionParameters", True)
        self._container = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._source_config = (self.__undef__, True)
        self._truncate_log_on_checkpoint = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASEProvisionParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "ASEDBContainer"), dirty)
            factory.validate_type(obj._container[0], "ASEDBContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "ASEVirtualSource"), dirty)
            factory.validate_type(obj._source[0], "ASEVirtualSource")
        else:
            obj._source = (obj.__undef__, dirty)
        if "sourceConfig" not in data:
            raise ValueError("Missing required property \"sourceConfig\".")
        if "sourceConfig" in data and data["sourceConfig"] is not None:
            obj._source_config = (factory.create_object(data["sourceConfig"], "ASEDBConfig"), dirty)
            factory.validate_type(obj._source_config[0], "ASEDBConfig")
        else:
            obj._source_config = (obj.__undef__, dirty)
        obj._truncate_log_on_checkpoint = (data.get("truncateLogOnCheckpoint", obj.__undef__), dirty)
        if obj._truncate_log_on_checkpoint[0] is not None and obj._truncate_log_on_checkpoint[0] is not obj.__undef__:
            assert isinstance(obj._truncate_log_on_checkpoint[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._truncate_log_on_checkpoint[0], type(obj._truncate_log_on_checkpoint[0])))
            common.validate_format(obj._truncate_log_on_checkpoint[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASEProvisionParameters, self).to_dict(dirty, belongs_to_parent)

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
        if "truncate_log_on_checkpoint" == "type" or (self.truncate_log_on_checkpoint is not self.__undef__ and (not (dirty and not self._truncate_log_on_checkpoint[1]) or isinstance(self.truncate_log_on_checkpoint, list) or belongs_to_parent)):
            dct["truncateLogOnCheckpoint"] = dictify(self.truncate_log_on_checkpoint)
        elif belongs_to_parent and self.truncate_log_on_checkpoint is self.__undef__:
            dct["truncateLogOnCheckpoint"] = True
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._source = (self._source[0], True)
        self._source_config = (self._source_config[0], True)
        self._truncate_log_on_checkpoint = (self._truncate_log_on_checkpoint[0], True)

    def is_dirty(self):
        return any([self._container[1], self._source[1], self._source_config[1], self._truncate_log_on_checkpoint[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASEProvisionParameters):
            return False
        return super(ASEProvisionParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.source == other.source and \
               self.source_config == other.source_config and \
               self.truncate_log_on_checkpoint == other.truncate_log_on_checkpoint

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

        :rtype: :py:class:`v1_11_16.web.vo.ASEDBContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def source(self):
        """
        The source that describes an external database instance.

        :rtype: :py:class:`v1_11_16.web.vo.ASEVirtualSource`
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

        :rtype: :py:class:`v1_11_16.web.vo.ASEDBConfig`
        """
        return self._source_config[0]

    @source_config.setter
    def source_config(self, value):
        self._source_config = (value, True)

    @property
    def truncate_log_on_checkpoint(self):
        """
        *(default value: True)* Set the "trunc log on chkpt" database option.

        :rtype: ``bool``
        """
        return self._truncate_log_on_checkpoint[0]

    @truncate_log_on_checkpoint.setter
    def truncate_log_on_checkpoint(self, value):
        self._truncate_log_on_checkpoint = (value, True)

