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
#     /delphix-appdata-virtual-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_5.web.objects.AppDataManagedSource import AppDataManagedSource
from delphixpy.v1_11_5 import factory
from delphixpy.v1_11_5 import common

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

class AppDataVirtualSource(AppDataManagedSource):
    """
    *(extends* :py:class:`v1_11_5.web.vo.AppDataManagedSource` *)* A virtual
    AppData source.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataVirtualSource, self).__init__()
        self._type = ("AppDataVirtualSource", True)
        self._operations = (self.__undef__, True)
        self._parameters = (self.__undef__, True)
        self._additional_mount_points = (self.__undef__, True)
        self._allow_auto_vdb_restart_on_host_reboot = (self.__undef__, True)
        self._runtime_mount_information = (self.__undef__, True)

    API_VERSION = "1.11.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataVirtualSource, cls).from_dict(data, dirty, undef_enabled)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "VirtualSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "VirtualSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        if "parameters" in data and data["parameters"] is not None:
            obj._parameters = (data["parameters"], dirty)
        else:
            obj._parameters = (obj.__undef__, dirty)
        obj._additional_mount_points = []
        for item in data.get("additionalMountPoints") or []:
            obj._additional_mount_points.append(factory.create_object(item))
            factory.validate_type(obj._additional_mount_points[-1], "AppDataAdditionalMountPoint")
        obj._additional_mount_points = (obj._additional_mount_points, dirty)
        obj._allow_auto_vdb_restart_on_host_reboot = (data.get("allowAutoVDBRestartOnHostReboot", obj.__undef__), dirty)
        if obj._allow_auto_vdb_restart_on_host_reboot[0] is not None and obj._allow_auto_vdb_restart_on_host_reboot[0] is not obj.__undef__:
            assert isinstance(obj._allow_auto_vdb_restart_on_host_reboot[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._allow_auto_vdb_restart_on_host_reboot[0], type(obj._allow_auto_vdb_restart_on_host_reboot[0])))
            common.validate_format(obj._allow_auto_vdb_restart_on_host_reboot[0], "None", None, None)
        if "runtimeMountInformation" in data and data["runtimeMountInformation"] is not None:
            obj._runtime_mount_information = (factory.create_object(data["runtimeMountInformation"], "RuntimeMountInformation"), dirty)
            factory.validate_type(obj._runtime_mount_information[0], "RuntimeMountInformation")
        else:
            obj._runtime_mount_information = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataVirtualSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "parameters" == "type" or (self.parameters is not self.__undef__ and (not (dirty and not self._parameters[1]) or isinstance(self.parameters, list) or belongs_to_parent)):
            dct["parameters"] = dictify(self.parameters, prop_is_list_or_vo=True)
        if "additional_mount_points" == "type" or (self.additional_mount_points is not self.__undef__ and (not (dirty and not self._additional_mount_points[1]) or isinstance(self.additional_mount_points, list) or belongs_to_parent)):
            if self.runtime is self.__undef__ or self.runtime.enabled != "ENABLED":
                dct["additionalMountPoints"] = dictify(self.additional_mount_points, prop_is_list_or_vo=True)
        if "allow_auto_vdb_restart_on_host_reboot" == "type" or (self.allow_auto_vdb_restart_on_host_reboot is not self.__undef__ and (not (dirty and not self._allow_auto_vdb_restart_on_host_reboot[1]) or isinstance(self.allow_auto_vdb_restart_on_host_reboot, list) or belongs_to_parent)):
            dct["allowAutoVDBRestartOnHostReboot"] = dictify(self.allow_auto_vdb_restart_on_host_reboot)
        if "runtime_mount_information" == "type" or (self.runtime_mount_information is not self.__undef__ and (not (dirty and not self._runtime_mount_information[1]))):
            dct["runtimeMountInformation"] = dictify(self.runtime_mount_information)
        if dirty and "runtimeMountInformation" in dct:
            del dct["runtimeMountInformation"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._operations = (self._operations[0], True)
        self._parameters = (self._parameters[0], True)
        self._additional_mount_points = (self._additional_mount_points[0], True)
        self._allow_auto_vdb_restart_on_host_reboot = (self._allow_auto_vdb_restart_on_host_reboot[0], True)
        self._runtime_mount_information = (self._runtime_mount_information[0], True)

    def is_dirty(self):
        return any([self._operations[1], self._parameters[1], self._additional_mount_points[1], self._allow_auto_vdb_restart_on_host_reboot[1], self._runtime_mount_information[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataVirtualSource):
            return False
        return super(AppDataVirtualSource, self).__eq__(other) and \
               self.operations == other.operations and \
               self.parameters == other.parameters and \
               self.additional_mount_points == other.additional_mount_points and \
               self.allow_auto_vdb_restart_on_host_reboot == other.allow_auto_vdb_restart_on_host_reboot and \
               self.runtime_mount_information == other.runtime_mount_information

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_11_5.web.vo.VirtualSourceOperations`
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

        :rtype: :py:class:`v1_11_5.web.vo.Json`
        """
        return self._parameters[0]

    @parameters.setter
    def parameters(self, value):
        self._parameters = (value, True)

    @property
    def additional_mount_points(self):
        """
        Locations to mount subdirectories of the AppData in addition to the
        normal target mount point. These paths will be mounted and unmounted as
        part of enabling and disabling this source.

        :rtype: ``list`` of
            :py:class:`v1_11_5.web.vo.AppDataAdditionalMountPoint`
        """
        return self._additional_mount_points[0]

    @additional_mount_points.setter
    def additional_mount_points(self, value):
        self._additional_mount_points = (value, True)

    @property
    def allow_auto_vdb_restart_on_host_reboot(self):
        """
        Indicates whether Delphix should automatically restart this virtual
        source when target host reboot is detected.

        :rtype: ``bool``
        """
        return self._allow_auto_vdb_restart_on_host_reboot[0]

    @allow_auto_vdb_restart_on_host_reboot.setter
    def allow_auto_vdb_restart_on_host_reboot(self, value):
        self._allow_auto_vdb_restart_on_host_reboot = (value, True)

    @property
    def runtime_mount_information(self):
        """
        The representation of runtime mount information.

        :rtype: :py:class:`v1_11_5.web.vo.RuntimeMountInformation`
        """
        return self._runtime_mount_information[0]

