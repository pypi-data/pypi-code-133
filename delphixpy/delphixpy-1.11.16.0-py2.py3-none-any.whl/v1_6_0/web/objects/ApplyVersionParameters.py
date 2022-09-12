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
#     /delphix-apply-version-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_0 import common

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

class ApplyVersionParameters(TypedObject):
    """
    *(extends* :py:class:`v1_6_0.web.vo.TypedObject` *)* The parameters to use
    as input to upgrade.
    """
    def __init__(self, undef_enabled=True):
        super(ApplyVersionParameters, self).__init__()
        self._type = ("ApplyVersionParameters", True)
        self._defer = (self.__undef__, True)
        self._enable_sources_on_failure = (self.__undef__, True)
        self._quiesce_sources = (self.__undef__, True)
        self._reboot = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ApplyVersionParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._defer = (data.get("defer", obj.__undef__), dirty)
        if obj._defer[0] is not None and obj._defer[0] is not obj.__undef__:
            assert isinstance(obj._defer[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._defer[0], type(obj._defer[0])))
            common.validate_format(obj._defer[0], "None", None, None)
        obj._enable_sources_on_failure = (data.get("enableSourcesOnFailure", obj.__undef__), dirty)
        if obj._enable_sources_on_failure[0] is not None and obj._enable_sources_on_failure[0] is not obj.__undef__:
            assert isinstance(obj._enable_sources_on_failure[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_sources_on_failure[0], type(obj._enable_sources_on_failure[0])))
            common.validate_format(obj._enable_sources_on_failure[0], "None", None, None)
        obj._quiesce_sources = (data.get("quiesceSources", obj.__undef__), dirty)
        if obj._quiesce_sources[0] is not None and obj._quiesce_sources[0] is not obj.__undef__:
            assert isinstance(obj._quiesce_sources[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._quiesce_sources[0], type(obj._quiesce_sources[0])))
            common.validate_format(obj._quiesce_sources[0], "None", None, None)
        obj._reboot = (data.get("reboot", obj.__undef__), dirty)
        if obj._reboot[0] is not None and obj._reboot[0] is not obj.__undef__:
            assert isinstance(obj._reboot[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._reboot[0], type(obj._reboot[0])))
            common.validate_format(obj._reboot[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ApplyVersionParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "defer" == "type" or (self.defer is not self.__undef__ and (not (dirty and not self._defer[1]) or isinstance(self.defer, list) or belongs_to_parent)):
            dct["defer"] = dictify(self.defer)
        elif belongs_to_parent and self.defer is self.__undef__:
            dct["defer"] = False
        if "enable_sources_on_failure" == "type" or (self.enable_sources_on_failure is not self.__undef__ and (not (dirty and not self._enable_sources_on_failure[1]) or isinstance(self.enable_sources_on_failure, list) or belongs_to_parent)):
            dct["enableSourcesOnFailure"] = dictify(self.enable_sources_on_failure)
        elif belongs_to_parent and self.enable_sources_on_failure is self.__undef__:
            dct["enableSourcesOnFailure"] = True
        if "quiesce_sources" == "type" or (self.quiesce_sources is not self.__undef__ and (not (dirty and not self._quiesce_sources[1]) or isinstance(self.quiesce_sources, list) or belongs_to_parent)):
            dct["quiesceSources"] = dictify(self.quiesce_sources)
        elif belongs_to_parent and self.quiesce_sources is self.__undef__:
            dct["quiesceSources"] = True
        if "reboot" == "type" or (self.reboot is not self.__undef__ and (not (dirty and not self._reboot[1]) or isinstance(self.reboot, list) or belongs_to_parent)):
            dct["reboot"] = dictify(self.reboot)
        elif belongs_to_parent and self.reboot is self.__undef__:
            dct["reboot"] = True
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._defer = (self._defer[0], True)
        self._enable_sources_on_failure = (self._enable_sources_on_failure[0], True)
        self._quiesce_sources = (self._quiesce_sources[0], True)
        self._reboot = (self._reboot[0], True)

    def is_dirty(self):
        return any([self._defer[1], self._enable_sources_on_failure[1], self._quiesce_sources[1], self._reboot[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ApplyVersionParameters):
            return False
        return super(ApplyVersionParameters, self).__eq__(other) and \
               self.defer == other.defer and \
               self.enable_sources_on_failure == other.enable_sources_on_failure and \
               self.quiesce_sources == other.quiesce_sources and \
               self.reboot == other.reboot

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def defer(self):
        """
        If true, the Delphix Engine is upgraded without updating the OS
        software. The operation will fail gracefully if the upgrade version
        requires a version of the OS that is newer than what is currently
        running. The OS software can subsequently be upgraded by applying any
        version and setting defer to false. It is possible to catch up to the
        current OS version on a previously deferred upgrade by re-applying the
        running version with a defer setting of false.

        :rtype: ``bool``
        """
        return self._defer[0]

    @defer.setter
    def defer(self, value):
        self._defer = (value, True)

    @property
    def enable_sources_on_failure(self):
        """
        *(default value: True)* This property governs whether or not data
        sources are re-enabled or left disabled in the event that upgrade fails
        before the Delphix Engine is restarted.

        :rtype: ``bool``
        """
        return self._enable_sources_on_failure[0]

    @enable_sources_on_failure.setter
    def enable_sources_on_failure(self, value):
        self._enable_sources_on_failure = (value, True)

    @property
    def quiesce_sources(self):
        """
        *(default value: True)* If true, all data sources (VDBs and dSources)
        are automatically disabled prior to upgrade, and re-enabled after
        upgrade. If any source cannot be disabled, then the upgrade fails and
        the recovery semantics are governed by the "enableSourcesOnFailure"
        property.

        :rtype: ``bool``
        """
        return self._quiesce_sources[0]

    @quiesce_sources.setter
    def quiesce_sources(self, value):
        self._quiesce_sources = (value, True)

    @property
    def reboot(self):
        """
        *(default value: True)* If true, the system reboots immediately after
        upgrade. If false, the system is shutdown.

        :rtype: ``bool``
        """
        return self._reboot[0]

    @reboot.setter
    def reboot(self, value):
        self._reboot = (value, True)

