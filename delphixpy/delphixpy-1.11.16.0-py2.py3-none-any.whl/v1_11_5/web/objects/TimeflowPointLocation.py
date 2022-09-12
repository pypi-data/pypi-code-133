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
#     /delphix-timeflow-point-location.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_5.web.objects.TimeflowPointParameters import TimeflowPointParameters
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

class TimeflowPointLocation(TimeflowPointParameters):
    """
    *(extends* :py:class:`v1_11_5.web.vo.TimeflowPointParameters` *)* TimeFlow
    point based on a database-specific identifier (SCN, LSN, etc).
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowPointLocation, self).__init__()
        self._type = ("TimeflowPointLocation", True)
        self._location = (self.__undef__, True)
        self._timeflow = (self.__undef__, True)

    API_VERSION = "1.11.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowPointLocation, cls).from_dict(data, dirty, undef_enabled)
        if "location" not in data:
            raise ValueError("Missing required property \"location\".")
        obj._location = (data.get("location", obj.__undef__), dirty)
        if obj._location[0] is not None and obj._location[0] is not obj.__undef__:
            assert isinstance(obj._location[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._location[0], type(obj._location[0])))
            common.validate_format(obj._location[0], "None", None, None)
        if "timeflow" not in data:
            raise ValueError("Missing required property \"timeflow\".")
        obj._timeflow = (data.get("timeflow", obj.__undef__), dirty)
        if obj._timeflow[0] is not None and obj._timeflow[0] is not obj.__undef__:
            assert isinstance(obj._timeflow[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timeflow[0], type(obj._timeflow[0])))
            common.validate_format(obj._timeflow[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowPointLocation, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "location" == "type" or (self.location is not self.__undef__ and (not (dirty and not self._location[1]) or isinstance(self.location, list) or belongs_to_parent)):
            dct["location"] = dictify(self.location)
        if "timeflow" == "type" or (self.timeflow is not self.__undef__ and (not (dirty and not self._timeflow[1]) or isinstance(self.timeflow, list) or belongs_to_parent)):
            dct["timeflow"] = dictify(self.timeflow)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._location = (self._location[0], True)
        self._timeflow = (self._timeflow[0], True)

    def is_dirty(self):
        return any([self._location[1], self._timeflow[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowPointLocation):
            return False
        return super(TimeflowPointLocation, self).__eq__(other) and \
               self.location == other.location and \
               self.timeflow == other.timeflow

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def location(self):
        """
        The TimeFlow location.

        :rtype: ``TEXT_TYPE``
        """
        return self._location[0]

    @location.setter
    def location(self, value):
        self._location = (value, True)

    @property
    def timeflow(self):
        """
        Reference to TimeFlow containing this location.

        :rtype: ``TEXT_TYPE``
        """
        return self._timeflow[0]

    @timeflow.setter
    def timeflow(self, value):
        self._timeflow = (value, True)

