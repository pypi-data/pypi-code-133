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
#     /delphix-oracle-staging-source-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.TypedObject import TypedObject
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

class OracleStagingSourceParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.TypedObject` *)* Parameters provided
    by the user to create a staging database.
    """
    def __init__(self, undef_enabled=True):
        super(OracleStagingSourceParameters, self).__init__()
        self._type = ("OracleStagingSourceParameters", True)
        self._repository = (self.__undef__, True)
        self._environment_user = (self.__undef__, True)
        self._mount_base = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._config_template = (self.__undef__, True)
        self._instance_name = (self.__undef__, True)
        self._physical_standby = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleStagingSourceParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._repository = (data.get("repository", obj.__undef__), dirty)
        if obj._repository[0] is not None and obj._repository[0] is not obj.__undef__:
            assert isinstance(obj._repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._repository[0], type(obj._repository[0])))
            common.validate_format(obj._repository[0], "objectReference", None, None)
        obj._environment_user = (data.get("environmentUser", obj.__undef__), dirty)
        if obj._environment_user[0] is not None and obj._environment_user[0] is not obj.__undef__:
            assert isinstance(obj._environment_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment_user[0], type(obj._environment_user[0])))
            common.validate_format(obj._environment_user[0], "objectReference", None, None)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "None", None, 256)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        obj._config_template = (data.get("configTemplate", obj.__undef__), dirty)
        if obj._config_template[0] is not None and obj._config_template[0] is not obj.__undef__:
            assert isinstance(obj._config_template[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._config_template[0], type(obj._config_template[0])))
            common.validate_format(obj._config_template[0], "objectReference", None, None)
        obj._instance_name = (data.get("instanceName", obj.__undef__), dirty)
        if obj._instance_name[0] is not None and obj._instance_name[0] is not obj.__undef__:
            assert isinstance(obj._instance_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._instance_name[0], type(obj._instance_name[0])))
            common.validate_format(obj._instance_name[0], "oracleInstanceName", None, 15)
        obj._physical_standby = (data.get("physicalStandby", obj.__undef__), dirty)
        if obj._physical_standby[0] is not None and obj._physical_standby[0] is not obj.__undef__:
            assert isinstance(obj._physical_standby[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._physical_standby[0], type(obj._physical_standby[0])))
            common.validate_format(obj._physical_standby[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleStagingSourceParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "repository" == "type" or (self.repository is not self.__undef__ and (not (dirty and not self._repository[1]) or isinstance(self.repository, list) or belongs_to_parent)):
            dct["repository"] = dictify(self.repository)
        if "environment_user" == "type" or (self.environment_user is not self.__undef__ and (not (dirty and not self._environment_user[1]) or isinstance(self.environment_user, list) or belongs_to_parent)):
            dct["environmentUser"] = dictify(self.environment_user)
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]) or isinstance(self.mount_base, list) or belongs_to_parent)):
            dct["mountBase"] = dictify(self.mount_base)
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        if "config_template" == "type" or (self.config_template is not self.__undef__ and (not (dirty and not self._config_template[1]) or isinstance(self.config_template, list) or belongs_to_parent)):
            dct["configTemplate"] = dictify(self.config_template)
        if "instance_name" == "type" or (self.instance_name is not self.__undef__ and (not (dirty and not self._instance_name[1]) or isinstance(self.instance_name, list) or belongs_to_parent)):
            dct["instanceName"] = dictify(self.instance_name)
        if "physical_standby" == "type" or (self.physical_standby is not self.__undef__ and (not (dirty and not self._physical_standby[1]) or isinstance(self.physical_standby, list) or belongs_to_parent)):
            dct["physicalStandby"] = dictify(self.physical_standby)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._repository = (self._repository[0], True)
        self._environment_user = (self._environment_user[0], True)
        self._mount_base = (self._mount_base[0], True)
        self._config_params = (self._config_params[0], True)
        self._config_template = (self._config_template[0], True)
        self._instance_name = (self._instance_name[0], True)
        self._physical_standby = (self._physical_standby[0], True)

    def is_dirty(self):
        return any([self._repository[1], self._environment_user[1], self._mount_base[1], self._config_params[1], self._config_template[1], self._instance_name[1], self._physical_standby[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleStagingSourceParameters):
            return False
        return super(OracleStagingSourceParameters, self).__eq__(other) and \
               self.repository == other.repository and \
               self.environment_user == other.environment_user and \
               self.mount_base == other.mount_base and \
               self.config_params == other.config_params and \
               self.config_template == other.config_template and \
               self.instance_name == other.instance_name and \
               self.physical_standby == other.physical_standby

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def repository(self):
        """
        The object reference of the source repository that will host the
        LogSync staging database.

        :rtype: ``TEXT_TYPE``
        """
        return self._repository[0]

    @repository.setter
    def repository(self, value):
        self._repository = (value, True)

    @property
    def environment_user(self):
        """
        The user used to create and manage the configuration.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment_user[0]

    @environment_user.setter
    def environment_user(self, value):
        self._environment_user = (value, True)

    @property
    def mount_base(self):
        """
        The base mount point to use for the NFS mounts.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_base[0]

    @mount_base.setter
    def mount_base(self, value):
        self._mount_base = (value, True)

    @property
    def config_params(self):
        """
        Oracle database configuration parameter overrides.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @config_params.setter
    def config_params(self, value):
        self._config_params = (value, True)

    @property
    def config_template(self):
        """
        Optional database template to use for staging database creation. If
        set, configParams will be ignored.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._config_template[0]

    @config_template.setter
    def config_template(self, value):
        self._config_template = (value, True)

    @property
    def instance_name(self):
        """
        The name (sid) of the instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._instance_name[0]

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = (value, True)

    @property
    def physical_standby(self):
        """
        Whether this staging database will be configured as a physical standby.

        :rtype: ``bool``
        """
        return self._physical_standby[0]

    @physical_standby.setter
    def physical_standby(self, value):
        self._physical_standby = (value, True)

