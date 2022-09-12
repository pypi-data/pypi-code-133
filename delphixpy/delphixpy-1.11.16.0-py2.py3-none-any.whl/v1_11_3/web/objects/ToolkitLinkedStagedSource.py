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
#     /delphix-toolkit-linked-staged-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.ToolkitLinkedSource import ToolkitLinkedSource
from delphixpy.v1_11_3 import common

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

class ToolkitLinkedStagedSource(ToolkitLinkedSource):
    """
    *(extends* :py:class:`v1_11_3.web.vo.ToolkitLinkedSource` *)* A linked
    staged source definition for Lua toolkits.
    """
    def __init__(self, undef_enabled=True):
        super(ToolkitLinkedStagedSource, self).__init__()
        self._type = ("ToolkitLinkedStagedSource", True)
        self._resync = (self.__undef__, True)
        self._start_staging = (self.__undef__, True)
        self._stop_staging = (self.__undef__, True)
        self._status = (self.__undef__, True)
        self._worker = (self.__undef__, True)
        self._mount_spec = (self.__undef__, True)
        self._ownership_spec = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ToolkitLinkedStagedSource, cls).from_dict(data, dirty, undef_enabled)
        if "resync" not in data:
            raise ValueError("Missing required property \"resync\".")
        obj._resync = (data.get("resync", obj.__undef__), dirty)
        if obj._resync[0] is not None and obj._resync[0] is not obj.__undef__:
            assert isinstance(obj._resync[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._resync[0], type(obj._resync[0])))
            common.validate_format(obj._resync[0], "None", None, None)
        if "startStaging" not in data:
            raise ValueError("Missing required property \"startStaging\".")
        obj._start_staging = (data.get("startStaging", obj.__undef__), dirty)
        if obj._start_staging[0] is not None and obj._start_staging[0] is not obj.__undef__:
            assert isinstance(obj._start_staging[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._start_staging[0], type(obj._start_staging[0])))
            common.validate_format(obj._start_staging[0], "None", None, None)
        if "stopStaging" not in data:
            raise ValueError("Missing required property \"stopStaging\".")
        obj._stop_staging = (data.get("stopStaging", obj.__undef__), dirty)
        if obj._stop_staging[0] is not None and obj._stop_staging[0] is not obj.__undef__:
            assert isinstance(obj._stop_staging[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._stop_staging[0], type(obj._stop_staging[0])))
            common.validate_format(obj._stop_staging[0], "None", None, None)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            common.validate_format(obj._status[0], "None", None, None)
        obj._worker = (data.get("worker", obj.__undef__), dirty)
        if obj._worker[0] is not None and obj._worker[0] is not obj.__undef__:
            assert isinstance(obj._worker[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._worker[0], type(obj._worker[0])))
            common.validate_format(obj._worker[0], "None", None, None)
        obj._mount_spec = (data.get("mountSpec", obj.__undef__), dirty)
        if obj._mount_spec[0] is not None and obj._mount_spec[0] is not obj.__undef__:
            assert isinstance(obj._mount_spec[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_spec[0], type(obj._mount_spec[0])))
            common.validate_format(obj._mount_spec[0], "None", None, None)
        obj._ownership_spec = (data.get("ownershipSpec", obj.__undef__), dirty)
        if obj._ownership_spec[0] is not None and obj._ownership_spec[0] is not obj.__undef__:
            assert isinstance(obj._ownership_spec[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._ownership_spec[0], type(obj._ownership_spec[0])))
            common.validate_format(obj._ownership_spec[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ToolkitLinkedStagedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "resync" == "type" or (self.resync is not self.__undef__ and (not (dirty and not self._resync[1]) or isinstance(self.resync, list) or belongs_to_parent)):
            dct["resync"] = dictify(self.resync)
        if "start_staging" == "type" or (self.start_staging is not self.__undef__ and (not (dirty and not self._start_staging[1]) or isinstance(self.start_staging, list) or belongs_to_parent)):
            dct["startStaging"] = dictify(self.start_staging)
        if "stop_staging" == "type" or (self.stop_staging is not self.__undef__ and (not (dirty and not self._stop_staging[1]) or isinstance(self.stop_staging, list) or belongs_to_parent)):
            dct["stopStaging"] = dictify(self.stop_staging)
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        if "worker" == "type" or (self.worker is not self.__undef__ and (not (dirty and not self._worker[1]))):
            dct["worker"] = dictify(self.worker)
        if "mount_spec" == "type" or (self.mount_spec is not self.__undef__ and (not (dirty and not self._mount_spec[1]))):
            dct["mountSpec"] = dictify(self.mount_spec)
        if "ownership_spec" == "type" or (self.ownership_spec is not self.__undef__ and (not (dirty and not self._ownership_spec[1]))):
            dct["ownershipSpec"] = dictify(self.ownership_spec)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._resync = (self._resync[0], True)
        self._start_staging = (self._start_staging[0], True)
        self._stop_staging = (self._stop_staging[0], True)
        self._status = (self._status[0], True)
        self._worker = (self._worker[0], True)
        self._mount_spec = (self._mount_spec[0], True)
        self._ownership_spec = (self._ownership_spec[0], True)

    def is_dirty(self):
        return any([self._resync[1], self._start_staging[1], self._stop_staging[1], self._status[1], self._worker[1], self._mount_spec[1], self._ownership_spec[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ToolkitLinkedStagedSource):
            return False
        return super(ToolkitLinkedStagedSource, self).__eq__(other) and \
               self.resync == other.resync and \
               self.start_staging == other.start_staging and \
               self.stop_staging == other.stop_staging and \
               self.status == other.status and \
               self.worker == other.worker and \
               self.mount_spec == other.mount_spec and \
               self.ownership_spec == other.ownership_spec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def resync(self):
        """
        A workflow script that builds the staging instance from production.

        :rtype: ``TEXT_TYPE``
        """
        return self._resync[0]

    @resync.setter
    def resync(self, value):
        self._resync = (value, True)

    @property
    def start_staging(self):
        """
        A workflow script that start the staged source. The staged files will
        be mounted and available.

        :rtype: ``TEXT_TYPE``
        """
        return self._start_staging[0]

    @start_staging.setter
    def start_staging(self, value):
        self._start_staging = (value, True)

    @property
    def stop_staging(self):
        """
        A workflow script that stop the staged source. The staged files will be
        mounted and available. Upon completion of this workflow, the staged
        files will be unmounted.

        :rtype: ``TEXT_TYPE``
        """
        return self._stop_staging[0]

    @stop_staging.setter
    def stop_staging(self, value):
        self._stop_staging = (value, True)

    @property
    def status(self):
        """
        A workflow script that returns whether or not the data source is
        active/inactive. The script should exit with an exit status of ACTIVE
        if the data source is available. The script should exit with an exit
        status of INACTIVE if the data source is unavailable. An exit status of
        UNKNOWN implies the script encountered an unexpected state or error. If
        no status script is supplied, the dSource will always be in an active
        state while enabled.

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

    @status.setter
    def status(self, value):
        self._status = (value, True)

    @property
    def worker(self):
        """
        A workflow script run periodically to monitor the health of the data
        source and staging environment. This script will be run every 10
        seconds.

        :rtype: ``TEXT_TYPE``
        """
        return self._worker[0]

    @worker.setter
    def worker(self, value):
        self._worker = (value, True)

    @property
    def mount_spec(self):
        """
        A workflow script that specifies where the storage for the copy of the
        application should be mounted.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_spec[0]

    @mount_spec.setter
    def mount_spec(self, value):
        self._mount_spec = (value, True)

    @property
    def ownership_spec(self):
        """
        A workflow script that specifies which user/group should own the mount
        where the application will be copied.

        :rtype: ``TEXT_TYPE``
        """
        return self._ownership_spec[0]

    @ownership_spec.setter
    def ownership_spec(self, value):
        self._ownership_spec = (value, True)

