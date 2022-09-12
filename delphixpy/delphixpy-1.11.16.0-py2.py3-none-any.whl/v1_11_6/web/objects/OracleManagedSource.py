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
#     /delphix-oracle-managed-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_6.web.objects.OracleSource import OracleSource
from delphixpy.v1_11_6 import factory
from delphixpy.v1_11_6 import common

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

class OracleManagedSource(OracleSource):
    """
    *(extends* :py:class:`v1_11_6.web.vo.OracleSource` *)* Common properties
    for all Oracle sources managed by Delphix.
    """
    def __init__(self, undef_enabled=True):
        super(OracleManagedSource, self).__init__()
        self._type = ("OracleManagedSource", True)
        self._mount_base = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._config_template = (self.__undef__, True)
        self._node_listeners = (self.__undef__, True)
        self._runtime_mount_information = (self.__undef__, True)

    API_VERSION = "1.11.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleManagedSource, cls).from_dict(data, dirty, undef_enabled)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "unixrestrictedpath", None, 256)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        obj._config_template = (data.get("configTemplate", obj.__undef__), dirty)
        if obj._config_template[0] is not None and obj._config_template[0] is not obj.__undef__:
            assert isinstance(obj._config_template[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._config_template[0], type(obj._config_template[0])))
            common.validate_format(obj._config_template[0], "objectReference", None, None)
        obj._node_listeners = []
        for item in data.get("nodeListeners") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._node_listeners.append(item)
        obj._node_listeners = (obj._node_listeners, dirty)
        if "runtimeMountInformation" in data and data["runtimeMountInformation"] is not None:
            obj._runtime_mount_information = (factory.create_object(data["runtimeMountInformation"], "RuntimeMountInformation"), dirty)
            factory.validate_type(obj._runtime_mount_information[0], "RuntimeMountInformation")
        else:
            obj._runtime_mount_information = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleManagedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]) or isinstance(self.mount_base, list) or belongs_to_parent)):
            dct["mountBase"] = dictify(self.mount_base)
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        if "config_template" == "type" or (self.config_template is not self.__undef__ and (not (dirty and not self._config_template[1]) or isinstance(self.config_template, list) or belongs_to_parent)):
            dct["configTemplate"] = dictify(self.config_template)
        if "node_listeners" == "type" or (self.node_listeners is not self.__undef__ and (not (dirty and not self._node_listeners[1]) or isinstance(self.node_listeners, list) or belongs_to_parent)):
            dct["nodeListeners"] = dictify(self.node_listeners, prop_is_list_or_vo=True)
        if "runtime_mount_information" == "type" or (self.runtime_mount_information is not self.__undef__ and (not (dirty and not self._runtime_mount_information[1]))):
            dct["runtimeMountInformation"] = dictify(self.runtime_mount_information)
        if dirty and "runtimeMountInformation" in dct:
            del dct["runtimeMountInformation"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._mount_base = (self._mount_base[0], True)
        self._config_params = (self._config_params[0], True)
        self._config_template = (self._config_template[0], True)
        self._node_listeners = (self._node_listeners[0], True)
        self._runtime_mount_information = (self._runtime_mount_information[0], True)

    def is_dirty(self):
        return any([self._mount_base[1], self._config_params[1], self._config_template[1], self._node_listeners[1], self._runtime_mount_information[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleManagedSource):
            return False
        return super(OracleManagedSource, self).__eq__(other) and \
               self.mount_base == other.mount_base and \
               self.config_params == other.config_params and \
               self.config_template == other.config_template and \
               self.node_listeners == other.node_listeners and \
               self.runtime_mount_information == other.runtime_mount_information

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

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
        Optional database template to use for provisioning and refresh. If set,
        configParams will be ignored on provision or refresh.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._config_template[0]

    @config_template.setter
    def config_template(self, value):
        self._config_template = (value, True)

    @property
    def node_listeners(self):
        """
        A list of object references to Oracle Node Listeners selected for this
        Managed Database. Delphix picks one default listener from the target
        environment if this list is empty at virtual database provision time.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._node_listeners[0]

    @node_listeners.setter
    def node_listeners(self, value):
        self._node_listeners = (value, True)

    @property
    def runtime_mount_information(self):
        """
        The representation of runtime mount information.

        :rtype: :py:class:`v1_11_6.web.vo.RuntimeMountInformation`
        """
        return self._runtime_mount_information[0]

