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
#     /delphix-quota-policy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.Policy import Policy
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

class QuotaPolicy(Policy):
    """
    *(extends* :py:class:`v1_8_1.web.vo.Policy` *)* This policy limits the
    maximum amount of space an object (group or database) can use.
    """
    def __init__(self, undef_enabled=True):
        super(QuotaPolicy, self).__init__()
        self._type = ("QuotaPolicy", True)
        self._crit_alert_time = (self.__undef__, True)
        self._size = (self.__undef__, True)
        self._warn_alert_time = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(QuotaPolicy, cls).from_dict(data, dirty, undef_enabled)
        obj._crit_alert_time = (data.get("critAlertTime", obj.__undef__), dirty)
        if obj._crit_alert_time[0] is not None and obj._crit_alert_time[0] is not obj.__undef__:
            assert isinstance(obj._crit_alert_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._crit_alert_time[0], type(obj._crit_alert_time[0])))
            common.validate_format(obj._crit_alert_time[0], "date", None, None)
        obj._size = (data.get("size", obj.__undef__), dirty)
        if obj._size[0] is not None and obj._size[0] is not obj.__undef__:
            assert isinstance(obj._size[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._size[0], type(obj._size[0])))
            common.validate_format(obj._size[0], "None", None, None)
        obj._warn_alert_time = (data.get("warnAlertTime", obj.__undef__), dirty)
        if obj._warn_alert_time[0] is not None and obj._warn_alert_time[0] is not obj.__undef__:
            assert isinstance(obj._warn_alert_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._warn_alert_time[0], type(obj._warn_alert_time[0])))
            common.validate_format(obj._warn_alert_time[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(QuotaPolicy, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "crit_alert_time" == "type" or (self.crit_alert_time is not self.__undef__ and (not (dirty and not self._crit_alert_time[1]))):
            dct["critAlertTime"] = dictify(self.crit_alert_time)
        if "size" == "type" or (self.size is not self.__undef__ and (not (dirty and not self._size[1]) or isinstance(self.size, list) or belongs_to_parent)):
            dct["size"] = dictify(self.size)
        if "warn_alert_time" == "type" or (self.warn_alert_time is not self.__undef__ and (not (dirty and not self._warn_alert_time[1]))):
            dct["warnAlertTime"] = dictify(self.warn_alert_time)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._crit_alert_time = (self._crit_alert_time[0], True)
        self._size = (self._size[0], True)
        self._warn_alert_time = (self._warn_alert_time[0], True)

    def is_dirty(self):
        return any([self._crit_alert_time[1], self._size[1], self._warn_alert_time[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, QuotaPolicy):
            return False
        return super(QuotaPolicy, self).__eq__(other) and \
               self.crit_alert_time == other.crit_alert_time and \
               self.size == other.size and \
               self.warn_alert_time == other.warn_alert_time

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def crit_alert_time(self):
        """
        Last time a critical alert was generated.

        :rtype: ``TEXT_TYPE``
        """
        return self._crit_alert_time[0]

    @crit_alert_time.setter
    def crit_alert_time(self, value):
        self._crit_alert_time = (value, True)

    @property
    def size(self):
        """
        Size of the quota, in bytes.

        :rtype: ``float``
        """
        return self._size[0]

    @size.setter
    def size(self, value):
        self._size = (value, True)

    @property
    def warn_alert_time(self):
        """
        Last time a warning alert was generated.

        :rtype: ``TEXT_TYPE``
        """
        return self._warn_alert_time[0]

    @warn_alert_time.setter
    def warn_alert_time(self, value):
        self._warn_alert_time = (value, True)

