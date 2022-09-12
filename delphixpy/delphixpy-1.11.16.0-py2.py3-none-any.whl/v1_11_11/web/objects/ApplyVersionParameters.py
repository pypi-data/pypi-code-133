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

from delphixpy.v1_11_11.web.objects.TypedObject import TypedObject
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

class ApplyVersionParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_11.web.vo.TypedObject` *)* The parameters to
    use as input to upgrade.
    """
    def __init__(self, undef_enabled=True):
        super(ApplyVersionParameters, self).__init__()
        self._type = ("ApplyVersionParameters", True)
        self._quiesce_sources = (self.__undef__, True)
        self._enable_sources_on_failure = (self.__undef__, True)
        self._verify = (self.__undef__, True)
        self._ignore_quiesce_sources_failures = (self.__undef__, True)
        self._upgrade_type = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ApplyVersionParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._quiesce_sources = (data.get("quiesceSources", obj.__undef__), dirty)
        if obj._quiesce_sources[0] is not None and obj._quiesce_sources[0] is not obj.__undef__:
            assert isinstance(obj._quiesce_sources[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._quiesce_sources[0], type(obj._quiesce_sources[0])))
            common.validate_format(obj._quiesce_sources[0], "None", None, None)
        obj._enable_sources_on_failure = (data.get("enableSourcesOnFailure", obj.__undef__), dirty)
        if obj._enable_sources_on_failure[0] is not None and obj._enable_sources_on_failure[0] is not obj.__undef__:
            assert isinstance(obj._enable_sources_on_failure[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_sources_on_failure[0], type(obj._enable_sources_on_failure[0])))
            common.validate_format(obj._enable_sources_on_failure[0], "None", None, None)
        obj._verify = (data.get("verify", obj.__undef__), dirty)
        if obj._verify[0] is not None and obj._verify[0] is not obj.__undef__:
            assert isinstance(obj._verify[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._verify[0], type(obj._verify[0])))
            common.validate_format(obj._verify[0], "None", None, None)
        obj._ignore_quiesce_sources_failures = (data.get("ignoreQuiesceSourcesFailures", obj.__undef__), dirty)
        if obj._ignore_quiesce_sources_failures[0] is not None and obj._ignore_quiesce_sources_failures[0] is not obj.__undef__:
            assert isinstance(obj._ignore_quiesce_sources_failures[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._ignore_quiesce_sources_failures[0], type(obj._ignore_quiesce_sources_failures[0])))
            common.validate_format(obj._ignore_quiesce_sources_failures[0], "None", None, None)
        obj._upgrade_type = (data.get("upgradeType", obj.__undef__), dirty)
        if obj._upgrade_type[0] is not None and obj._upgrade_type[0] is not obj.__undef__:
            assert isinstance(obj._upgrade_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._upgrade_type[0], type(obj._upgrade_type[0])))
            assert obj._upgrade_type[0] in ['DEFERRED', 'FINISH_DEFERRED', 'FULL'], "Expected enum ['DEFERRED', 'FINISH_DEFERRED', 'FULL'] but got %s" % obj._upgrade_type[0]
            common.validate_format(obj._upgrade_type[0], "None", None, None)
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
        if "quiesce_sources" == "type" or (self.quiesce_sources is not self.__undef__ and (not (dirty and not self._quiesce_sources[1]) or isinstance(self.quiesce_sources, list) or belongs_to_parent)):
            dct["quiesceSources"] = dictify(self.quiesce_sources)
        elif belongs_to_parent and self.quiesce_sources is self.__undef__:
            dct["quiesceSources"] = True
        if "enable_sources_on_failure" == "type" or (self.enable_sources_on_failure is not self.__undef__ and (not (dirty and not self._enable_sources_on_failure[1]) or isinstance(self.enable_sources_on_failure, list) or belongs_to_parent)):
            dct["enableSourcesOnFailure"] = dictify(self.enable_sources_on_failure)
        elif belongs_to_parent and self.enable_sources_on_failure is self.__undef__:
            dct["enableSourcesOnFailure"] = True
        if "verify" == "type" or (self.verify is not self.__undef__ and (not (dirty and not self._verify[1]) or isinstance(self.verify, list) or belongs_to_parent)):
            dct["verify"] = dictify(self.verify)
        elif belongs_to_parent and self.verify is self.__undef__:
            dct["verify"] = False
        if "ignore_quiesce_sources_failures" == "type" or (self.ignore_quiesce_sources_failures is not self.__undef__ and (not (dirty and not self._ignore_quiesce_sources_failures[1]) or isinstance(self.ignore_quiesce_sources_failures, list) or belongs_to_parent)):
            dct["ignoreQuiesceSourcesFailures"] = dictify(self.ignore_quiesce_sources_failures)
        elif belongs_to_parent and self.ignore_quiesce_sources_failures is self.__undef__:
            dct["ignoreQuiesceSourcesFailures"] = False
        if "upgrade_type" == "type" or (self.upgrade_type is not self.__undef__ and (not (dirty and not self._upgrade_type[1]))):
            dct["upgradeType"] = dictify(self.upgrade_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._quiesce_sources = (self._quiesce_sources[0], True)
        self._enable_sources_on_failure = (self._enable_sources_on_failure[0], True)
        self._verify = (self._verify[0], True)
        self._ignore_quiesce_sources_failures = (self._ignore_quiesce_sources_failures[0], True)
        self._upgrade_type = (self._upgrade_type[0], True)

    def is_dirty(self):
        return any([self._quiesce_sources[1], self._enable_sources_on_failure[1], self._verify[1], self._ignore_quiesce_sources_failures[1], self._upgrade_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ApplyVersionParameters):
            return False
        return super(ApplyVersionParameters, self).__eq__(other) and \
               self.quiesce_sources == other.quiesce_sources and \
               self.enable_sources_on_failure == other.enable_sources_on_failure and \
               self.verify == other.verify and \
               self.ignore_quiesce_sources_failures == other.ignore_quiesce_sources_failures and \
               self.upgrade_type == other.upgrade_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def quiesce_sources(self):
        """
        *(default value: True)* If true for non-deferred upgrade, all data
        sources (VDBs and dSources) are automatically disabled prior to
        upgrade, and re-enabled after upgrade. If any source cannot be
        disabled, the recovery semantics are governed by the
        "ignoreQuiesceSourcesFailures" and "enableSourcesOnFailure" properties.
        This parameter has no affect for deferred upgrades.

        :rtype: ``bool``
        """
        return self._quiesce_sources[0]

    @quiesce_sources.setter
    def quiesce_sources(self, value):
        self._quiesce_sources = (value, True)

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
    def verify(self):
        """
        If set to false, disables verification before applying the upgrade.
        This will only disable verification if a successful verification has
        been run in the past hour.

        :rtype: ``bool``
        """
        return self._verify[0]

    @verify.setter
    def verify(self, value):
        self._verify = (value, True)

    @property
    def ignore_quiesce_sources_failures(self):
        """
        If true, a failure to quiesce sources will not block the upgrade.

        :rtype: ``bool``
        """
        return self._ignore_quiesce_sources_failures[0]

    @ignore_quiesce_sources_failures.setter
    def ignore_quiesce_sources_failures(self, value):
        self._ignore_quiesce_sources_failures = (value, True)

    @property
    def upgrade_type(self):
        """
        *(default value: DEFERRED)* Type of upgrade. *(permitted values:
        DEFERRED, FINISH_DEFERRED, FULL)*

        :rtype: ``TEXT_TYPE``
        """
        return self._upgrade_type[0]

    @upgrade_type.setter
    def upgrade_type(self, value):
        self._upgrade_type = (value, True)

