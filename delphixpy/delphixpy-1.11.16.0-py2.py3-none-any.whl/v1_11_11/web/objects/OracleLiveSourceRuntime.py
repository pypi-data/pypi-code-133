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
#     /delphix-oracle-live-source-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.OracleBaseSourceRuntime import OracleBaseSourceRuntime
from delphixpy.v1_11_11 import common

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

class OracleLiveSourceRuntime(OracleBaseSourceRuntime):
    """
    *(extends* :py:class:`v1_11_11.web.vo.OracleBaseSourceRuntime` *)* Runtime
    (non-persistent) properties of an Oracle LiveSource.
    """
    def __init__(self, undef_enabled=True):
        super(OracleLiveSourceRuntime, self).__init__()
        self._type = ("OracleLiveSourceRuntime", True)
        self._current_data_age = (self.__undef__, True)
        self._is_data_age_warning_exceeded = (self.__undef__, True)
        self._transport_status = (self.__undef__, True)
        self._apply_status = (self.__undef__, True)
        self._non_logged_data_detected = (self.__undef__, True)
        self._source_resetlogs_id_change_detected = (self.__undef__, True)
        self._unexpected_role_change_detected = (self.__undef__, True)
        self._last_update_time = (self.__undef__, True)
        self._source_database_timezone = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleLiveSourceRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._current_data_age = (data.get("currentDataAge", obj.__undef__), dirty)
        if obj._current_data_age[0] is not None and obj._current_data_age[0] is not obj.__undef__:
            assert isinstance(obj._current_data_age[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._current_data_age[0], type(obj._current_data_age[0])))
            common.validate_format(obj._current_data_age[0], "None", None, None)
        obj._is_data_age_warning_exceeded = (data.get("isDataAgeWarningExceeded", obj.__undef__), dirty)
        if obj._is_data_age_warning_exceeded[0] is not None and obj._is_data_age_warning_exceeded[0] is not obj.__undef__:
            assert isinstance(obj._is_data_age_warning_exceeded[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._is_data_age_warning_exceeded[0], type(obj._is_data_age_warning_exceeded[0])))
            common.validate_format(obj._is_data_age_warning_exceeded[0], "None", None, None)
        obj._transport_status = (data.get("transportStatus", obj.__undef__), dirty)
        if obj._transport_status[0] is not None and obj._transport_status[0] is not obj.__undef__:
            assert isinstance(obj._transport_status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._transport_status[0], type(obj._transport_status[0])))
            assert obj._transport_status[0] in ['UNKNOWN', 'WORKING', 'NO_INITIAL_DATA', 'NO_NEW_DATA'], "Expected enum ['UNKNOWN', 'WORKING', 'NO_INITIAL_DATA', 'NO_NEW_DATA'] but got %s" % obj._transport_status[0]
            common.validate_format(obj._transport_status[0], "None", None, None)
        obj._apply_status = (data.get("applyStatus", obj.__undef__), dirty)
        if obj._apply_status[0] is not None and obj._apply_status[0] is not obj.__undef__:
            assert isinstance(obj._apply_status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._apply_status[0], type(obj._apply_status[0])))
            assert obj._apply_status[0] in ['UNKNOWN', 'WORKING', 'APPLY_FAILED', 'APPLY_ON_WRONG_INCARNATION', 'UNRESOLVABLE_GAP_DETECTED'], "Expected enum ['UNKNOWN', 'WORKING', 'APPLY_FAILED', 'APPLY_ON_WRONG_INCARNATION', 'UNRESOLVABLE_GAP_DETECTED'] but got %s" % obj._apply_status[0]
            common.validate_format(obj._apply_status[0], "None", None, None)
        obj._non_logged_data_detected = (data.get("nonLoggedDataDetected", obj.__undef__), dirty)
        if obj._non_logged_data_detected[0] is not None and obj._non_logged_data_detected[0] is not obj.__undef__:
            assert isinstance(obj._non_logged_data_detected[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._non_logged_data_detected[0], type(obj._non_logged_data_detected[0])))
            common.validate_format(obj._non_logged_data_detected[0], "None", None, None)
        obj._source_resetlogs_id_change_detected = (data.get("sourceResetlogsIDChangeDetected", obj.__undef__), dirty)
        if obj._source_resetlogs_id_change_detected[0] is not None and obj._source_resetlogs_id_change_detected[0] is not obj.__undef__:
            assert isinstance(obj._source_resetlogs_id_change_detected[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._source_resetlogs_id_change_detected[0], type(obj._source_resetlogs_id_change_detected[0])))
            common.validate_format(obj._source_resetlogs_id_change_detected[0], "None", None, None)
        obj._unexpected_role_change_detected = (data.get("unexpectedRoleChangeDetected", obj.__undef__), dirty)
        if obj._unexpected_role_change_detected[0] is not None and obj._unexpected_role_change_detected[0] is not obj.__undef__:
            assert isinstance(obj._unexpected_role_change_detected[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._unexpected_role_change_detected[0], type(obj._unexpected_role_change_detected[0])))
            common.validate_format(obj._unexpected_role_change_detected[0], "None", None, None)
        obj._last_update_time = (data.get("lastUpdateTime", obj.__undef__), dirty)
        if obj._last_update_time[0] is not None and obj._last_update_time[0] is not obj.__undef__:
            assert isinstance(obj._last_update_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_update_time[0], type(obj._last_update_time[0])))
            common.validate_format(obj._last_update_time[0], "date", None, None)
        obj._source_database_timezone = (data.get("sourceDatabaseTimezone", obj.__undef__), dirty)
        if obj._source_database_timezone[0] is not None and obj._source_database_timezone[0] is not obj.__undef__:
            assert isinstance(obj._source_database_timezone[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_database_timezone[0], type(obj._source_database_timezone[0])))
            common.validate_format(obj._source_database_timezone[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleLiveSourceRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "current_data_age" == "type" or (self.current_data_age is not self.__undef__ and (not (dirty and not self._current_data_age[1]))):
            dct["currentDataAge"] = dictify(self.current_data_age)
        if "is_data_age_warning_exceeded" == "type" or (self.is_data_age_warning_exceeded is not self.__undef__ and (not (dirty and not self._is_data_age_warning_exceeded[1]))):
            dct["isDataAgeWarningExceeded"] = dictify(self.is_data_age_warning_exceeded)
        if "transport_status" == "type" or (self.transport_status is not self.__undef__ and (not (dirty and not self._transport_status[1]))):
            dct["transportStatus"] = dictify(self.transport_status)
        if "apply_status" == "type" or (self.apply_status is not self.__undef__ and (not (dirty and not self._apply_status[1]))):
            dct["applyStatus"] = dictify(self.apply_status)
        if "non_logged_data_detected" == "type" or (self.non_logged_data_detected is not self.__undef__ and (not (dirty and not self._non_logged_data_detected[1]))):
            dct["nonLoggedDataDetected"] = dictify(self.non_logged_data_detected)
        if "source_resetlogs_id_change_detected" == "type" or (self.source_resetlogs_id_change_detected is not self.__undef__ and (not (dirty and not self._source_resetlogs_id_change_detected[1]))):
            dct["sourceResetlogsIDChangeDetected"] = dictify(self.source_resetlogs_id_change_detected)
        if "unexpected_role_change_detected" == "type" or (self.unexpected_role_change_detected is not self.__undef__ and (not (dirty and not self._unexpected_role_change_detected[1]))):
            dct["unexpectedRoleChangeDetected"] = dictify(self.unexpected_role_change_detected)
        if "last_update_time" == "type" or (self.last_update_time is not self.__undef__ and (not (dirty and not self._last_update_time[1]))):
            dct["lastUpdateTime"] = dictify(self.last_update_time)
        if "source_database_timezone" == "type" or (self.source_database_timezone is not self.__undef__ and (not (dirty and not self._source_database_timezone[1]))):
            dct["sourceDatabaseTimezone"] = dictify(self.source_database_timezone)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._current_data_age = (self._current_data_age[0], True)
        self._is_data_age_warning_exceeded = (self._is_data_age_warning_exceeded[0], True)
        self._transport_status = (self._transport_status[0], True)
        self._apply_status = (self._apply_status[0], True)
        self._non_logged_data_detected = (self._non_logged_data_detected[0], True)
        self._source_resetlogs_id_change_detected = (self._source_resetlogs_id_change_detected[0], True)
        self._unexpected_role_change_detected = (self._unexpected_role_change_detected[0], True)
        self._last_update_time = (self._last_update_time[0], True)
        self._source_database_timezone = (self._source_database_timezone[0], True)

    def is_dirty(self):
        return any([self._current_data_age[1], self._is_data_age_warning_exceeded[1], self._transport_status[1], self._apply_status[1], self._non_logged_data_detected[1], self._source_resetlogs_id_change_detected[1], self._unexpected_role_change_detected[1], self._last_update_time[1], self._source_database_timezone[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleLiveSourceRuntime):
            return False
        return super(OracleLiveSourceRuntime, self).__eq__(other) and \
               self.current_data_age == other.current_data_age and \
               self.is_data_age_warning_exceeded == other.is_data_age_warning_exceeded and \
               self.transport_status == other.transport_status and \
               self.apply_status == other.apply_status and \
               self.non_logged_data_detected == other.non_logged_data_detected and \
               self.source_resetlogs_id_change_detected == other.source_resetlogs_id_change_detected and \
               self.unexpected_role_change_detected == other.unexpected_role_change_detected and \
               self.last_update_time == other.last_update_time and \
               self.source_database_timezone == other.source_database_timezone

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def current_data_age(self):
        """
        Current data lag between LiveSource and source database in seconds.

        :rtype: ``int``
        """
        return self._current_data_age[0]

    @current_data_age.setter
    def current_data_age(self, value):
        self._current_data_age = (value, True)

    @property
    def is_data_age_warning_exceeded(self):
        """
        Has data age exceeded the user specified threshold.

        :rtype: ``bool``
        """
        return self._is_data_age_warning_exceeded[0]

    @is_data_age_warning_exceeded.setter
    def is_data_age_warning_exceeded(self, value):
        self._is_data_age_warning_exceeded = (value, True)

    @property
    def transport_status(self):
        """
        Redo log transport status from the source database to the LiveSource.
        *(permitted values: UNKNOWN, WORKING, NO_INITIAL_DATA, NO_NEW_DATA)*

        :rtype: ``TEXT_TYPE``
        """
        return self._transport_status[0]

    @transport_status.setter
    def transport_status(self, value):
        self._transport_status = (value, True)

    @property
    def apply_status(self):
        """
        MRP apply status for the standby database associated with the
        LiveSource. *(permitted values: UNKNOWN, WORKING, APPLY_FAILED,
        APPLY_ON_WRONG_INCARNATION, UNRESOLVABLE_GAP_DETECTED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._apply_status[0]

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = (value, True)

    @property
    def non_logged_data_detected(self):
        """
        Indicates whether there is non-logged data on the standby.

        :rtype: ``bool``
        """
        return self._non_logged_data_detected[0]

    @non_logged_data_detected.setter
    def non_logged_data_detected(self, value):
        self._non_logged_data_detected = (value, True)

    @property
    def source_resetlogs_id_change_detected(self):
        """
        Indicates whether the incarnation ID changed on the primary database.

        :rtype: ``bool``
        """
        return self._source_resetlogs_id_change_detected[0]

    @source_resetlogs_id_change_detected.setter
    def source_resetlogs_id_change_detected(self, value):
        self._source_resetlogs_id_change_detected = (value, True)

    @property
    def unexpected_role_change_detected(self):
        """
        Indicates whether the LiveSource is not in standby mode.

        :rtype: ``bool``
        """
        return self._unexpected_role_change_detected[0]

    @unexpected_role_change_detected.setter
    def unexpected_role_change_detected(self, value):
        self._unexpected_role_change_detected = (value, True)

    @property
    def last_update_time(self):
        """
        The time at which this runtime data was updated.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_update_time[0]

    @last_update_time.setter
    def last_update_time(self, value):
        self._last_update_time = (value, True)

    @property
    def source_database_timezone(self):
        """
        Time zone of the source database at the time the runtime data was
        updated.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_database_timezone[0]

    @source_database_timezone.setter
    def source_database_timezone(self, value):
        self._source_database_timezone = (value, True)

