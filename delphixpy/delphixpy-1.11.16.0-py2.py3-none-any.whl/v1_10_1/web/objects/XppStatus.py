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
#     /delphix-xpp-status.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_1.web.objects.Checklist import Checklist
from delphixpy.v1_10_1 import factory
from delphixpy.v1_10_1 import common

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

class XppStatus(Checklist):
    """
    *(extends* :py:class:`v1_10_1.web.vo.Checklist` *)* The current cross-
    platform provisioning status of a container.
    """
    def __init__(self, undef_enabled=True):
        super(XppStatus, self).__init__()
        self._type = ("XppStatus", True)
        self._staging_status = (self.__undef__, True)
        self._target_status = (self.__undef__, True)
        self._validate_status = (self.__undef__, True)
        self._last_run_status = (self.__undef__, True)

    API_VERSION = "1.10.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(XppStatus, cls).from_dict(data, dirty, undef_enabled)
        if "stagingStatus" in data and data["stagingStatus"] is not None:
            obj._staging_status = (factory.create_object(data["stagingStatus"], "XppStagingStatus"), dirty)
            factory.validate_type(obj._staging_status[0], "XppStagingStatus")
        else:
            obj._staging_status = (obj.__undef__, dirty)
        if "targetStatus" in data and data["targetStatus"] is not None:
            obj._target_status = (factory.create_object(data["targetStatus"], "XppTargetStatus"), dirty)
            factory.validate_type(obj._target_status[0], "XppTargetStatus")
        else:
            obj._target_status = (obj.__undef__, dirty)
        if "validateStatus" in data and data["validateStatus"] is not None:
            obj._validate_status = (factory.create_object(data["validateStatus"], "XppValidateStatus"), dirty)
            factory.validate_type(obj._validate_status[0], "XppValidateStatus")
        else:
            obj._validate_status = (obj.__undef__, dirty)
        if "lastRunStatus" in data and data["lastRunStatus"] is not None:
            obj._last_run_status = (factory.create_object(data["lastRunStatus"], "XppLastRunStatus"), dirty)
            factory.validate_type(obj._last_run_status[0], "XppLastRunStatus")
        else:
            obj._last_run_status = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(XppStatus, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "staging_status" == "type" or (self.staging_status is not self.__undef__ and (not (dirty and not self._staging_status[1]))):
            dct["stagingStatus"] = dictify(self.staging_status)
        if "target_status" == "type" or (self.target_status is not self.__undef__ and (not (dirty and not self._target_status[1]))):
            dct["targetStatus"] = dictify(self.target_status)
        if "validate_status" == "type" or (self.validate_status is not self.__undef__ and (not (dirty and not self._validate_status[1]))):
            dct["validateStatus"] = dictify(self.validate_status)
        if "last_run_status" == "type" or (self.last_run_status is not self.__undef__ and (not (dirty and not self._last_run_status[1]))):
            dct["lastRunStatus"] = dictify(self.last_run_status)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._staging_status = (self._staging_status[0], True)
        self._target_status = (self._target_status[0], True)
        self._validate_status = (self._validate_status[0], True)
        self._last_run_status = (self._last_run_status[0], True)

    def is_dirty(self):
        return any([self._staging_status[1], self._target_status[1], self._validate_status[1], self._last_run_status[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, XppStatus):
            return False
        return super(XppStatus, self).__eq__(other) and \
               self.staging_status == other.staging_status and \
               self.target_status == other.target_status and \
               self.validate_status == other.validate_status and \
               self.last_run_status == other.last_run_status

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def staging_status(self):
        """
        Status of the cross-platform provisioning staging environment.

        :rtype: :py:class:`v1_10_1.web.vo.XppStagingStatus`
        """
        return self._staging_status[0]

    @staging_status.setter
    def staging_status(self, value):
        self._staging_status = (value, True)

    @property
    def target_status(self):
        """
        Status of the cross-platform provisioning target environment.

        :rtype: :py:class:`v1_10_1.web.vo.XppTargetStatus`
        """
        return self._target_status[0]

    @target_status.setter
    def target_status(self, value):
        self._target_status = (value, True)

    @property
    def validate_status(self):
        """
        Cross-platform provisioning validation status of the container.

        :rtype: :py:class:`v1_10_1.web.vo.XppValidateStatus`
        """
        return self._validate_status[0]

    @validate_status.setter
    def validate_status(self, value):
        self._validate_status = (value, True)

    @property
    def last_run_status(self):
        """
        Status of the last cross-platform provision of the container.

        :rtype: :py:class:`v1_10_1.web.vo.XppLastRunStatus`
        """
        return self._last_run_status[0]

    @last_run_status.setter
    def last_run_status(self, value):
        self._last_run_status = (value, True)

