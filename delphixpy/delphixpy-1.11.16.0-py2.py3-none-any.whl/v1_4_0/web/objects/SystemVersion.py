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
#     /delphix-upgrade-version.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_0.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_4_0 import common

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

class SystemVersion(NamedUserObject):
    """
    *(extends* :py:class:`v1_4_0.web.vo.NamedUserObject` *)* Describes a
    Delphix software revision.
    """
    def __init__(self, undef_enabled=True):
        super(SystemVersion, self).__init__()
        self._type = ("SystemVersion", True)
        self._build_date = (self.__undef__, True)
        self._min_os_version = (self.__undef__, True)
        self._min_version = (self.__undef__, True)
        self._os_running = (self.__undef__, True)
        self._os_version = (self.__undef__, True)
        self._status = (self.__undef__, True)
        self._version = (self.__undef__, True)

    API_VERSION = "1.4.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SystemVersion, cls).from_dict(data, dirty, undef_enabled)
        obj._build_date = (data.get("buildDate", obj.__undef__), dirty)
        if obj._build_date[0] is not None and obj._build_date[0] is not obj.__undef__:
            assert isinstance(obj._build_date[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._build_date[0], type(obj._build_date[0])))
            common.validate_format(obj._build_date[0], "None", None, None)
        obj._min_os_version = (data.get("minOsVersion", obj.__undef__), dirty)
        if obj._min_os_version[0] is not None and obj._min_os_version[0] is not obj.__undef__:
            assert isinstance(obj._min_os_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._min_os_version[0], type(obj._min_os_version[0])))
            common.validate_format(obj._min_os_version[0], "None", None, None)
        obj._min_version = (data.get("minVersion", obj.__undef__), dirty)
        if obj._min_version[0] is not None and obj._min_version[0] is not obj.__undef__:
            assert isinstance(obj._min_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._min_version[0], type(obj._min_version[0])))
            common.validate_format(obj._min_version[0], "None", None, None)
        obj._os_running = (data.get("osRunning", obj.__undef__), dirty)
        if obj._os_running[0] is not None and obj._os_running[0] is not obj.__undef__:
            assert isinstance(obj._os_running[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._os_running[0], type(obj._os_running[0])))
            common.validate_format(obj._os_running[0], "None", None, None)
        obj._os_version = (data.get("osVersion", obj.__undef__), dirty)
        if obj._os_version[0] is not None and obj._os_version[0] is not obj.__undef__:
            assert isinstance(obj._os_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._os_version[0], type(obj._os_version[0])))
            common.validate_format(obj._os_version[0], "None", None, None)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            common.validate_format(obj._status[0], "None", None, None)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SystemVersion, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "build_date" == "type" or (self.build_date is not self.__undef__ and (not (dirty and not self._build_date[1]))):
            dct["buildDate"] = dictify(self.build_date)
        if "min_os_version" == "type" or (self.min_os_version is not self.__undef__ and (not (dirty and not self._min_os_version[1]))):
            dct["minOsVersion"] = dictify(self.min_os_version)
        if "min_version" == "type" or (self.min_version is not self.__undef__ and (not (dirty and not self._min_version[1]))):
            dct["minVersion"] = dictify(self.min_version)
        if "os_running" == "type" or (self.os_running is not self.__undef__ and (not (dirty and not self._os_running[1]))):
            dct["osRunning"] = dictify(self.os_running)
        if "os_version" == "type" or (self.os_version is not self.__undef__ and (not (dirty and not self._os_version[1]))):
            dct["osVersion"] = dictify(self.os_version)
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]))):
            dct["version"] = dictify(self.version)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._build_date = (self._build_date[0], True)
        self._min_os_version = (self._min_os_version[0], True)
        self._min_version = (self._min_version[0], True)
        self._os_running = (self._os_running[0], True)
        self._os_version = (self._os_version[0], True)
        self._status = (self._status[0], True)
        self._version = (self._version[0], True)

    def is_dirty(self):
        return any([self._build_date[1], self._min_os_version[1], self._min_version[1], self._os_running[1], self._os_version[1], self._status[1], self._version[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SystemVersion):
            return False
        return super(SystemVersion, self).__eq__(other) and \
               self.build_date == other.build_date and \
               self.min_os_version == other.min_os_version and \
               self.min_version == other.min_version and \
               self.os_running == other.os_running and \
               self.os_version == other.os_version and \
               self.status == other.status and \
               self.version == other.version

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def build_date(self):
        """
        Date on which the version was built

        :rtype: ``TEXT_TYPE``
        """
        return self._build_date[0]

    @build_date.setter
    def build_date(self, value):
        self._build_date = (value, True)

    @property
    def min_os_version(self):
        """
        The minimum DelphixOS version supported by this Delphix version

        :rtype: ``TEXT_TYPE``
        """
        return self._min_os_version[0]

    @min_os_version.setter
    def min_os_version(self, value):
        self._min_os_version = (value, True)

    @property
    def min_version(self):
        """
        The minimum required Delphix version in order to upgrade

        :rtype: ``TEXT_TYPE``
        """
        return self._min_version[0]

    @min_version.setter
    def min_version(self, value):
        self._min_version = (value, True)

    @property
    def os_running(self):
        """
        DelphixOS is running from this version.

        :rtype: ``bool``
        """
        return self._os_running[0]

    @os_running.setter
    def os_running(self, value):
        self._os_running = (value, True)

    @property
    def os_version(self):
        """
        The DelphixOS version number

        :rtype: ``TEXT_TYPE``
        """
        return self._os_version[0]

    @os_version.setter
    def os_version(self, value):
        self._os_version = (value, True)

    @property
    def status(self):
        """
        The state of the version

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

    @status.setter
    def status(self, value):
        self._status = (value, True)

    @property
    def version(self):
        """
        The Delphix version number

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

