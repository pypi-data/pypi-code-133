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
#     /delphix-registration-status.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_3 import common

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

class RegistrationStatus(TypedObject):
    """
    *(extends* :py:class:`v1_5_3.web.vo.TypedObject` *)* Information on the
    status of the Delphix Engine's registration.
    """
    def __init__(self, undef_enabled=True):
        super(RegistrationStatus, self).__init__()
        self._type = ("RegistrationStatus", True)
        self._status = (self.__undef__, True)
        self._timestamp = (self.__undef__, True)

    API_VERSION = "1.5.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RegistrationStatus, cls).from_dict(data, dirty, undef_enabled)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            common.validate_format(obj._status[0], "None", None, None)
        obj._timestamp = (data.get("timestamp", obj.__undef__), dirty)
        if obj._timestamp[0] is not None and obj._timestamp[0] is not obj.__undef__:
            assert isinstance(obj._timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timestamp[0], type(obj._timestamp[0])))
            common.validate_format(obj._timestamp[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RegistrationStatus, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        if "timestamp" == "type" or (self.timestamp is not self.__undef__ and (not (dirty and not self._timestamp[1]))):
            dct["timestamp"] = dictify(self.timestamp)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._status = (self._status[0], True)
        self._timestamp = (self._timestamp[0], True)

    def is_dirty(self):
        return any([self._status[1], self._timestamp[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RegistrationStatus):
            return False
        return super(RegistrationStatus, self).__eq__(other) and \
               self.status == other.status and \
               self.timestamp == other.timestamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def status(self):
        """
        The status of the Delphix Engine's registration. It may be unknown,
        unregistered, in-progress, or registered.

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

    @status.setter
    def status(self, value):
        self._status = (value, True)

    @property
    def timestamp(self):
        """
        The time at which the registration status was last updated.

        :rtype: ``TEXT_TYPE``
        """
        return self._timestamp[0]

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = (value, True)

