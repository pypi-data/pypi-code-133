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
#     /delphix-db-container-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_7 import factory
from delphixpy.v1_11_7 import common

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

class DBContainerRuntime(TypedObject):
    """
    *(extends* :py:class:`v1_11_7.web.vo.TypedObject` *)* Runtime properties of
    a database container.
    """
    def __init__(self, undef_enabled=True):
        super(DBContainerRuntime, self).__init__()
        self._type = ("DBContainerRuntime", True)
        self._log_sync_active = (self.__undef__, True)
        self._pre_provisioning_status = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DBContainerRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._log_sync_active = (data.get("logSyncActive", obj.__undef__), dirty)
        if obj._log_sync_active[0] is not None and obj._log_sync_active[0] is not obj.__undef__:
            assert isinstance(obj._log_sync_active[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._log_sync_active[0], type(obj._log_sync_active[0])))
            common.validate_format(obj._log_sync_active[0], "None", None, None)
        if "preProvisioningStatus" in data and data["preProvisioningStatus"] is not None:
            obj._pre_provisioning_status = (factory.create_object(data["preProvisioningStatus"], "PreProvisioningRuntime"), dirty)
            factory.validate_type(obj._pre_provisioning_status[0], "PreProvisioningRuntime")
        else:
            obj._pre_provisioning_status = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DBContainerRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "log_sync_active" == "type" or (self.log_sync_active is not self.__undef__ and (not (dirty and not self._log_sync_active[1]))):
            dct["logSyncActive"] = dictify(self.log_sync_active)
        if "pre_provisioning_status" == "type" or (self.pre_provisioning_status is not self.__undef__ and (not (dirty and not self._pre_provisioning_status[1]))):
            dct["preProvisioningStatus"] = dictify(self.pre_provisioning_status)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._log_sync_active = (self._log_sync_active[0], True)
        self._pre_provisioning_status = (self._pre_provisioning_status[0], True)

    def is_dirty(self):
        return any([self._log_sync_active[1], self._pre_provisioning_status[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DBContainerRuntime):
            return False
        return super(DBContainerRuntime, self).__eq__(other) and \
               self.log_sync_active == other.log_sync_active and \
               self.pre_provisioning_status == other.pre_provisioning_status

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def log_sync_active(self):
        """
        True if the LogSync is enabled and running for this container.

        :rtype: ``bool``
        """
        return self._log_sync_active[0]

    @log_sync_active.setter
    def log_sync_active(self, value):
        self._log_sync_active = (value, True)

    @property
    def pre_provisioning_status(self):
        """
        The pre-provisioning runtime for the container.

        :rtype: :py:class:`v1_11_7.web.vo.PreProvisioningRuntime`
        """
        return self._pre_provisioning_status[0]

    @pre_provisioning_status.setter
    def pre_provisioning_status(self, value):
        self._pre_provisioning_status = (value, True)

