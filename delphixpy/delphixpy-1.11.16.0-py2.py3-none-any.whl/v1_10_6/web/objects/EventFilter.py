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
#     /delphix-alert-event-filter.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.AlertFilter import AlertFilter
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

class EventFilter(AlertFilter):
    """
    *(extends* :py:class:`v1_10_6.web.vo.AlertFilter` *)* An event filter that
    specifies which event types to match against.
    """
    def __init__(self, undef_enabled=True):
        super(EventFilter, self).__init__()
        self._type = ("EventFilter", True)
        self._event_types = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(EventFilter, cls).from_dict(data, dirty, undef_enabled)
        obj._event_types = []
        for item in data.get("eventTypes") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._event_types.append(item)
        obj._event_types = (obj._event_types, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(EventFilter, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "event_types" == "type" or (self.event_types is not self.__undef__ and (not (dirty and not self._event_types[1]) or isinstance(self.event_types, list) or belongs_to_parent)):
            dct["eventTypes"] = dictify(self.event_types, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._event_types = (self._event_types[0], True)

    def is_dirty(self):
        return any([self._event_types[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, EventFilter):
            return False
        return super(EventFilter, self).__eq__(other) and \
               self.event_types == other.event_types

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def event_types(self):
        """
        List of event types. Only alerts of the given event type are included.
        Each event type is a string representing the event class of the
        corresponding alerts. Wildcards are supported to include classes of
        events.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._event_types[0]

    @event_types.setter
    def event_types(self, value):
        self._event_types = (value, True)

