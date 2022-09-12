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
#     /delphix-syslog-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_15 import factory
from delphixpy.v1_11_15 import common

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

class SyslogConfig(TypedObject):
    """
    *(extends* :py:class:`v1_11_15.web.vo.TypedObject` *)* Syslog
    configuration.
    """
    def __init__(self, undef_enabled=True):
        super(SyslogConfig, self).__init__()
        self._type = ("SyslogConfig", True)
        self._enabled = (self.__undef__, True)
        self._severity = (self.__undef__, True)
        self._pattern = (self.__undef__, True)
        self._format = (self.__undef__, True)
        self._servers = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SyslogConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._severity = (data.get("severity", obj.__undef__), dirty)
        if obj._severity[0] is not None and obj._severity[0] is not obj.__undef__:
            assert isinstance(obj._severity[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._severity[0], type(obj._severity[0])))
            assert obj._severity[0] in ['EMERGENCY', 'ALERT', 'CRITICAL', 'ERROR', 'WARNING', 'NOTICE', 'INFORMATIONAL', 'DEBUG'], "Expected enum ['EMERGENCY', 'ALERT', 'CRITICAL', 'ERROR', 'WARNING', 'NOTICE', 'INFORMATIONAL', 'DEBUG'] but got %s" % obj._severity[0]
            common.validate_format(obj._severity[0], "None", None, None)
        obj._pattern = (data.get("pattern", obj.__undef__), dirty)
        if obj._pattern[0] is not None and obj._pattern[0] is not obj.__undef__:
            assert isinstance(obj._pattern[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pattern[0], type(obj._pattern[0])))
            common.validate_format(obj._pattern[0], "None", None, None)
        obj._format = (data.get("format", obj.__undef__), dirty)
        if obj._format[0] is not None and obj._format[0] is not obj.__undef__:
            assert isinstance(obj._format[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._format[0], type(obj._format[0])))
            assert obj._format[0] in ['TEXT', 'JSON'], "Expected enum ['TEXT', 'JSON'] but got %s" % obj._format[0]
            common.validate_format(obj._format[0], "None", None, None)
        obj._servers = []
        for item in data.get("servers") or []:
            obj._servers.append(factory.create_object(item))
            factory.validate_type(obj._servers[-1], "SyslogServer")
        obj._servers = (obj._servers, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SyslogConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]) or isinstance(self.enabled, list) or belongs_to_parent)):
            dct["enabled"] = dictify(self.enabled)
        elif belongs_to_parent and self.enabled is self.__undef__:
            dct["enabled"] = True
        if "severity" == "type" or (self.severity is not self.__undef__ and (not (dirty and not self._severity[1]) or isinstance(self.severity, list) or belongs_to_parent)):
            dct["severity"] = dictify(self.severity)
        elif belongs_to_parent and self.severity is self.__undef__:
            dct["severity"] = "WARNING"
        if "pattern" == "type" or (self.pattern is not self.__undef__ and (not (dirty and not self._pattern[1]) or isinstance(self.pattern, list) or belongs_to_parent)):
            dct["pattern"] = dictify(self.pattern)
        elif belongs_to_parent and self.pattern is self.__undef__:
            dct["pattern"] = "%-5p delphix : %m%n"
        if "format" == "type" or (self.format is not self.__undef__ and (not (dirty and not self._format[1]) or isinstance(self.format, list) or belongs_to_parent)):
            dct["format"] = dictify(self.format)
        elif belongs_to_parent and self.format is self.__undef__:
            dct["format"] = "TEXT"
        if "servers" == "type" or (self.servers is not self.__undef__ and (not (dirty and not self._servers[1]) or isinstance(self.servers, list) or belongs_to_parent)):
            dct["servers"] = dictify(self.servers, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._enabled = (self._enabled[0], True)
        self._severity = (self._severity[0], True)
        self._pattern = (self._pattern[0], True)
        self._format = (self._format[0], True)
        self._servers = (self._servers[0], True)

    def is_dirty(self):
        return any([self._enabled[1], self._severity[1], self._pattern[1], self._format[1], self._servers[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SyslogConfig):
            return False
        return super(SyslogConfig, self).__eq__(other) and \
               self.enabled == other.enabled and \
               self.severity == other.severity and \
               self.pattern == other.pattern and \
               self.format == other.format and \
               self.servers == other.servers

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def enabled(self):
        """
        *(default value: True)* True if the syslog service is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def severity(self):
        """
        *(default value: WARNING)* Syslog logging severity. Only events at or
        above this severity will be logged. *(permitted values: EMERGENCY,
        ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG)*

        :rtype: ``TEXT_TYPE``
        """
        return self._severity[0]

    @severity.setter
    def severity(self, value):
        self._severity = (value, True)

    @property
    def pattern(self):
        """
        *(default value: %-5p delphix : %m%n)* Syslog logging pattern. Events
        will be logged in the pattern as specified.

        :rtype: ``TEXT_TYPE``
        """
        return self._pattern[0]

    @pattern.setter
    def pattern(self, value):
        self._pattern = (value, True)

    @property
    def format(self):
        """
        *(default value: TEXT)* Syslog message format. *(permitted values:
        TEXT, JSON)*

        :rtype: ``TEXT_TYPE``
        """
        return self._format[0]

    @format.setter
    def format(self, value):
        self._format = (value, True)

    @property
    def servers(self):
        """
        List of syslog servers. At least one syslog server must be specified.

        :rtype: ``list`` of :py:class:`v1_11_15.web.vo.SyslogServer`
        """
        return self._servers[0]

    @servers.setter
    def servers(self, value):
        self._servers = (value, True)

