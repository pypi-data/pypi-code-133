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
#     /delphix-js-usage-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_11_13 import common

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

class JSUsageData(PersistentObject):
    """
    *(extends* :py:class:`v1_11_13.web.vo.PersistentObject` *)* Usage data used
    to draw graphs on the Self-Service pages.
    """
    def __init__(self, undef_enabled=True):
        super(JSUsageData, self).__init__()
        self._type = ("JSUsageData", True)
        self._usage_object = (self.__undef__, True)
        self._start_date = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSUsageData, cls).from_dict(data, dirty, undef_enabled)
        obj._usage_object = (data.get("usageObject", obj.__undef__), dirty)
        if obj._usage_object[0] is not None and obj._usage_object[0] is not obj.__undef__:
            assert isinstance(obj._usage_object[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._usage_object[0], type(obj._usage_object[0])))
            common.validate_format(obj._usage_object[0], "objectReference", None, None)
        obj._start_date = (data.get("startDate", obj.__undef__), dirty)
        if obj._start_date[0] is not None and obj._start_date[0] is not obj.__undef__:
            assert isinstance(obj._start_date[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._start_date[0], type(obj._start_date[0])))
            common.validate_format(obj._start_date[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSUsageData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "usage_object" == "type" or (self.usage_object is not self.__undef__ and (not (dirty and not self._usage_object[1]))):
            dct["usageObject"] = dictify(self.usage_object)
        if "start_date" == "type" or (self.start_date is not self.__undef__ and (not (dirty and not self._start_date[1]))):
            dct["startDate"] = dictify(self.start_date)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._usage_object = (self._usage_object[0], True)
        self._start_date = (self._start_date[0], True)

    def is_dirty(self):
        return any([self._usage_object[1], self._start_date[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSUsageData):
            return False
        return super(JSUsageData, self).__eq__(other) and \
               self.usage_object == other.usage_object and \
               self.start_date == other.start_date

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def usage_object(self):
        """
        The object the usage data is centered around.

        :rtype: ``TEXT_TYPE``
        """
        return self._usage_object[0]

    @usage_object.setter
    def usage_object(self, value):
        self._usage_object = (value, True)

    @property
    def start_date(self):
        """
        The date at the beginning of the time period this datapoint corresponds
        to. The time period itself varies between datapoint types.

        :rtype: ``TEXT_TYPE``
        """
        return self._start_date[0]

    @start_date.setter
    def start_date(self, value):
        self._start_date = (value, True)

