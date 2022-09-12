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
#     /delphix-system.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.PublicSystemInfo import PublicSystemInfo
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

class SystemInfo(PublicSystemInfo):
    """
    *(extends* :py:class:`v1_10_6.web.vo.PublicSystemInfo` *)* Retrieve system-
    wide properties and manage the state of the system.
    """
    def __init__(self, undef_enabled=True):
        super(SystemInfo, self).__init__()
        self._type = ("SystemInfo", True)
        self._hostname = (self.__undef__, True)
        self._ssh_public_key = (self.__undef__, True)
        self._memory_size = (self.__undef__, True)
        self._platform = (self.__undef__, True)
        self._uuid = (self.__undef__, True)
        self._processors = (self.__undef__, True)
        self._storage_used = (self.__undef__, True)
        self._storage_total = (self.__undef__, True)
        self._installation_time = (self.__undef__, True)
        self._up_time = (self.__undef__, True)
        self._memory_reservation = (self.__undef__, True)
        self._cpu_reservation = (self.__undef__, True)
        self._hotfixes = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SystemInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._hostname = (data.get("hostname", obj.__undef__), dirty)
        if obj._hostname[0] is not None and obj._hostname[0] is not obj.__undef__:
            assert isinstance(obj._hostname[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._hostname[0], type(obj._hostname[0])))
            common.validate_format(obj._hostname[0], "hostname", None, None)
        obj._ssh_public_key = (data.get("sshPublicKey", obj.__undef__), dirty)
        if obj._ssh_public_key[0] is not None and obj._ssh_public_key[0] is not obj.__undef__:
            assert isinstance(obj._ssh_public_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._ssh_public_key[0], type(obj._ssh_public_key[0])))
            common.validate_format(obj._ssh_public_key[0], "None", None, None)
        obj._memory_size = (data.get("memorySize", obj.__undef__), dirty)
        if obj._memory_size[0] is not None and obj._memory_size[0] is not obj.__undef__:
            assert isinstance(obj._memory_size[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._memory_size[0], type(obj._memory_size[0])))
            common.validate_format(obj._memory_size[0], "None", None, None)
        obj._platform = (data.get("platform", obj.__undef__), dirty)
        if obj._platform[0] is not None and obj._platform[0] is not obj.__undef__:
            assert isinstance(obj._platform[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._platform[0], type(obj._platform[0])))
            common.validate_format(obj._platform[0], "None", None, None)
        obj._uuid = (data.get("uuid", obj.__undef__), dirty)
        if obj._uuid[0] is not None and obj._uuid[0] is not obj.__undef__:
            assert isinstance(obj._uuid[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._uuid[0], type(obj._uuid[0])))
            common.validate_format(obj._uuid[0], "None", None, None)
        obj._processors = []
        for item in data.get("processors") or []:
            obj._processors.append(factory.create_object(item))
            factory.validate_type(obj._processors[-1], "CPUInfo")
        obj._processors = (obj._processors, dirty)
        obj._storage_used = (data.get("storageUsed", obj.__undef__), dirty)
        if obj._storage_used[0] is not None and obj._storage_used[0] is not obj.__undef__:
            assert isinstance(obj._storage_used[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._storage_used[0], type(obj._storage_used[0])))
            common.validate_format(obj._storage_used[0], "None", None, None)
        obj._storage_total = (data.get("storageTotal", obj.__undef__), dirty)
        if obj._storage_total[0] is not None and obj._storage_total[0] is not obj.__undef__:
            assert isinstance(obj._storage_total[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._storage_total[0], type(obj._storage_total[0])))
            common.validate_format(obj._storage_total[0], "None", None, None)
        obj._installation_time = (data.get("installationTime", obj.__undef__), dirty)
        if obj._installation_time[0] is not None and obj._installation_time[0] is not obj.__undef__:
            assert isinstance(obj._installation_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._installation_time[0], type(obj._installation_time[0])))
            common.validate_format(obj._installation_time[0], "date", None, None)
        if "upTime" in data and data["upTime"] is not None:
            obj._up_time = (factory.create_object(data["upTime"], "UpTimeInfo"), dirty)
            factory.validate_type(obj._up_time[0], "UpTimeInfo")
        else:
            obj._up_time = (obj.__undef__, dirty)
        obj._memory_reservation = (data.get("memoryReservation", obj.__undef__), dirty)
        if obj._memory_reservation[0] is not None and obj._memory_reservation[0] is not obj.__undef__:
            assert isinstance(obj._memory_reservation[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._memory_reservation[0], type(obj._memory_reservation[0])))
            common.validate_format(obj._memory_reservation[0], "None", None, None)
        obj._cpu_reservation = (data.get("cpuReservation", obj.__undef__), dirty)
        if obj._cpu_reservation[0] is not None and obj._cpu_reservation[0] is not obj.__undef__:
            assert isinstance(obj._cpu_reservation[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._cpu_reservation[0], type(obj._cpu_reservation[0])))
            common.validate_format(obj._cpu_reservation[0], "None", None, None)
        obj._hotfixes = (data.get("hotfixes", obj.__undef__), dirty)
        if obj._hotfixes[0] is not None and obj._hotfixes[0] is not obj.__undef__:
            assert isinstance(obj._hotfixes[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._hotfixes[0], type(obj._hotfixes[0])))
            common.validate_format(obj._hotfixes[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SystemInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "hostname" == "type" or (self.hostname is not self.__undef__ and (not (dirty and not self._hostname[1]) or isinstance(self.hostname, list) or belongs_to_parent)):
            dct["hostname"] = dictify(self.hostname)
        if "ssh_public_key" == "type" or (self.ssh_public_key is not self.__undef__ and (not (dirty and not self._ssh_public_key[1]))):
            dct["sshPublicKey"] = dictify(self.ssh_public_key)
        if "memory_size" == "type" or (self.memory_size is not self.__undef__ and (not (dirty and not self._memory_size[1]))):
            dct["memorySize"] = dictify(self.memory_size)
        if "platform" == "type" or (self.platform is not self.__undef__ and (not (dirty and not self._platform[1]))):
            dct["platform"] = dictify(self.platform)
        if "uuid" == "type" or (self.uuid is not self.__undef__ and (not (dirty and not self._uuid[1]))):
            dct["uuid"] = dictify(self.uuid)
        if "processors" == "type" or (self.processors is not self.__undef__ and (not (dirty and not self._processors[1]))):
            dct["processors"] = dictify(self.processors)
        if "storage_used" == "type" or (self.storage_used is not self.__undef__ and (not (dirty and not self._storage_used[1]))):
            dct["storageUsed"] = dictify(self.storage_used)
        if "storage_total" == "type" or (self.storage_total is not self.__undef__ and (not (dirty and not self._storage_total[1]))):
            dct["storageTotal"] = dictify(self.storage_total)
        if "installation_time" == "type" or (self.installation_time is not self.__undef__ and (not (dirty and not self._installation_time[1]))):
            dct["installationTime"] = dictify(self.installation_time)
        if "up_time" == "type" or (self.up_time is not self.__undef__ and (not (dirty and not self._up_time[1]))):
            dct["upTime"] = dictify(self.up_time)
        if "memory_reservation" == "type" or (self.memory_reservation is not self.__undef__ and (not (dirty and not self._memory_reservation[1]))):
            dct["memoryReservation"] = dictify(self.memory_reservation)
        if "cpu_reservation" == "type" or (self.cpu_reservation is not self.__undef__ and (not (dirty and not self._cpu_reservation[1]))):
            dct["cpuReservation"] = dictify(self.cpu_reservation)
        if "hotfixes" == "type" or (self.hotfixes is not self.__undef__ and (not (dirty and not self._hotfixes[1]))):
            dct["hotfixes"] = dictify(self.hotfixes)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._hostname = (self._hostname[0], True)
        self._ssh_public_key = (self._ssh_public_key[0], True)
        self._memory_size = (self._memory_size[0], True)
        self._platform = (self._platform[0], True)
        self._uuid = (self._uuid[0], True)
        self._processors = (self._processors[0], True)
        self._storage_used = (self._storage_used[0], True)
        self._storage_total = (self._storage_total[0], True)
        self._installation_time = (self._installation_time[0], True)
        self._up_time = (self._up_time[0], True)
        self._memory_reservation = (self._memory_reservation[0], True)
        self._cpu_reservation = (self._cpu_reservation[0], True)
        self._hotfixes = (self._hotfixes[0], True)

    def is_dirty(self):
        return any([self._hostname[1], self._ssh_public_key[1], self._memory_size[1], self._platform[1], self._uuid[1], self._processors[1], self._storage_used[1], self._storage_total[1], self._installation_time[1], self._up_time[1], self._memory_reservation[1], self._cpu_reservation[1], self._hotfixes[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SystemInfo):
            return False
        return super(SystemInfo, self).__eq__(other) and \
               self.hostname == other.hostname and \
               self.ssh_public_key == other.ssh_public_key and \
               self.memory_size == other.memory_size and \
               self.platform == other.platform and \
               self.uuid == other.uuid and \
               self.processors == other.processors and \
               self.storage_used == other.storage_used and \
               self.storage_total == other.storage_total and \
               self.installation_time == other.installation_time and \
               self.up_time == other.up_time and \
               self.memory_reservation == other.memory_reservation and \
               self.cpu_reservation == other.cpu_reservation and \
               self.hotfixes == other.hotfixes

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def hostname(self):
        """
        System hostname.

        :rtype: ``TEXT_TYPE``
        """
        return self._hostname[0]

    @hostname.setter
    def hostname(self, value):
        self._hostname = (value, True)

    @property
    def ssh_public_key(self):
        """
        SSH public key to be added to SSH authorized_keys for environment users
        using the SystemKeyCredential authorization mechanism.

        :rtype: ``TEXT_TYPE``
        """
        return self._ssh_public_key[0]

    @ssh_public_key.setter
    def ssh_public_key(self, value):
        self._ssh_public_key = (value, True)

    @property
    def memory_size(self):
        """
        Total memory on the system, in bytes.

        :rtype: ``float``
        """
        return self._memory_size[0]

    @memory_size.setter
    def memory_size(self, value):
        self._memory_size = (value, True)

    @property
    def platform(self):
        """
        Description of the current system platform.

        :rtype: ``TEXT_TYPE``
        """
        return self._platform[0]

    @platform.setter
    def platform(self, value):
        self._platform = (value, True)

    @property
    def uuid(self):
        """
        Globally unique identifier for this software installation.

        :rtype: ``TEXT_TYPE``
        """
        return self._uuid[0]

    @uuid.setter
    def uuid(self, value):
        self._uuid = (value, True)

    @property
    def processors(self):
        """
        Processors on the system.

        :rtype: ``list`` of :py:class:`v1_10_6.web.vo.CPUInfo`
        """
        return self._processors[0]

    @processors.setter
    def processors(self, value):
        self._processors = (value, True)

    @property
    def storage_used(self):
        """
        Amount of raw storage used by dSources, VDBs and system metadata.

        :rtype: ``float``
        """
        return self._storage_used[0]

    @storage_used.setter
    def storage_used(self, value):
        self._storage_used = (value, True)

    @property
    def storage_total(self):
        """
        Total amount of raw storage allocated for dSources, VDBs, and system
        metadata. Zero if storage has not yet been configured.

        :rtype: ``float``
        """
        return self._storage_total[0]

    @storage_total.setter
    def storage_total(self, value):
        self._storage_total = (value, True)

    @property
    def installation_time(self):
        """
        The date and time that the Delphix Engine was installed.

        :rtype: ``TEXT_TYPE``
        """
        return self._installation_time[0]

    @installation_time.setter
    def installation_time(self, value):
        self._installation_time = (value, True)

    @property
    def up_time(self):
        """
        Delphix Engine up time.

        :rtype: :py:class:`v1_10_6.web.vo.UpTimeInfo`
        """
        return self._up_time[0]

    @up_time.setter
    def up_time(self, value):
        self._up_time = (value, True)

    @property
    def memory_reservation(self):
        """
        Amount of memory reserved on the host.

        :rtype: ``float``
        """
        return self._memory_reservation[0]

    @memory_reservation.setter
    def memory_reservation(self, value):
        self._memory_reservation = (value, True)

    @property
    def cpu_reservation(self):
        """
        Percentage of CPU reserved on the host.

        :rtype: ``float``
        """
        return self._cpu_reservation[0]

    @cpu_reservation.setter
    def cpu_reservation(self, value):
        self._cpu_reservation = (value, True)

    @property
    def hotfixes(self):
        """
        List of hotfixes that were applied to this host.

        :rtype: ``TEXT_TYPE``
        """
        return self._hotfixes[0]

    @hotfixes.setter
    def hotfixes(self, value):
        self._hotfixes = (value, True)

