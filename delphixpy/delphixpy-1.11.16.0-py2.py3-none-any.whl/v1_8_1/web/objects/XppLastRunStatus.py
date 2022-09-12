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
#     /delphix-xpp-last-run-status.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.ChecklistItem import ChecklistItem
from delphixpy.v1_8_1 import factory
from delphixpy.v1_8_1 import common

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

class XppLastRunStatus(ChecklistItem):
    """
    *(extends* :py:class:`v1_8_1.web.vo.ChecklistItem` *)* Status of the last
    cross-platform provision of the container.
    """
    def __init__(self, undef_enabled=True):
        super(XppLastRunStatus, self).__init__()
        self._type = ("XppLastRunStatus", True)
        self._error_message = (self.__undef__, True)
        self._job = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(XppLastRunStatus, cls).from_dict(data, dirty, undef_enabled)
        obj._error_message = (data.get("errorMessage", obj.__undef__), dirty)
        if obj._error_message[0] is not None and obj._error_message[0] is not obj.__undef__:
            assert isinstance(obj._error_message[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._error_message[0], type(obj._error_message[0])))
            common.validate_format(obj._error_message[0], "None", None, None)
        if "job" in data and data["job"] is not None:
            obj._job = (factory.create_object(data["job"], "Job"), dirty)
            factory.validate_type(obj._job[0], "Job")
        else:
            obj._job = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(XppLastRunStatus, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "error_message" == "type" or (self.error_message is not self.__undef__ and (not (dirty and not self._error_message[1]))):
            dct["errorMessage"] = dictify(self.error_message)
        if "job" == "type" or (self.job is not self.__undef__ and (not (dirty and not self._job[1]))):
            dct["job"] = dictify(self.job)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._error_message = (self._error_message[0], True)
        self._job = (self._job[0], True)

    def is_dirty(self):
        return any([self._error_message[1], self._job[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, XppLastRunStatus):
            return False
        return super(XppLastRunStatus, self).__eq__(other) and \
               self.error_message == other.error_message and \
               self.job == other.job

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def error_message(self):
        """
        Error message associated with the last run, if any.

        :rtype: ``TEXT_TYPE``
        """
        return self._error_message[0]

    @error_message.setter
    def error_message(self, value):
        self._error_message = (value, True)

    @property
    def job(self):
        """
        Last cross-platform provision job run on the container.

        :rtype: :py:class:`v1_8_1.web.vo.Job`
        """
        return self._job[0]

    @job.setter
    def job(self, value):
        self._job = (value, True)

