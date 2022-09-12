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
#     /delphix-base-support-bundle-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_1 import common

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

class BaseSupportBundleParameters(TypedObject):
    """
    *(extends* :py:class:`v1_10_1.web.vo.TypedObject` *)* Parameters to be used
    when generating a support bundle.
    """
    def __init__(self, undef_enabled=True):
        super(BaseSupportBundleParameters, self).__init__()
        self._type = ("BaseSupportBundleParameters", True)
        self._include_analytics_data = (self.__undef__, True)
        self._bundle_type = (self.__undef__, True)
        self._environments = (self.__undef__, True)
        self._sources = (self.__undef__, True)

    API_VERSION = "1.10.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(BaseSupportBundleParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._include_analytics_data = (data.get("includeAnalyticsData", obj.__undef__), dirty)
        if obj._include_analytics_data[0] is not None and obj._include_analytics_data[0] is not obj.__undef__:
            assert isinstance(obj._include_analytics_data[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._include_analytics_data[0], type(obj._include_analytics_data[0])))
            common.validate_format(obj._include_analytics_data[0], "None", None, None)
        obj._bundle_type = (data.get("bundleType", obj.__undef__), dirty)
        if obj._bundle_type[0] is not None and obj._bundle_type[0] is not obj.__undef__:
            assert isinstance(obj._bundle_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._bundle_type[0], type(obj._bundle_type[0])))
            assert obj._bundle_type[0] in ['PHONEHOME', 'MDS', 'OS', 'CORE', 'LOG', 'DROPBOX', 'STORAGE_TEST', 'MASKING', 'ALL'], "Expected enum ['PHONEHOME', 'MDS', 'OS', 'CORE', 'LOG', 'DROPBOX', 'STORAGE_TEST', 'MASKING', 'ALL'] but got %s" % obj._bundle_type[0]
            common.validate_format(obj._bundle_type[0], "None", None, None)
        obj._environments = []
        for item in data.get("environments") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._environments.append(item)
        obj._environments = (obj._environments, dirty)
        obj._sources = []
        for item in data.get("sources") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._sources.append(item)
        obj._sources = (obj._sources, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(BaseSupportBundleParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "include_analytics_data" == "type" or (self.include_analytics_data is not self.__undef__ and (not (dirty and not self._include_analytics_data[1]))):
            dct["includeAnalyticsData"] = dictify(self.include_analytics_data)
        if "bundle_type" == "type" or (self.bundle_type is not self.__undef__ and (not (dirty and not self._bundle_type[1]))):
            dct["bundleType"] = dictify(self.bundle_type)
        if "environments" == "type" or (self.environments is not self.__undef__ and (not (dirty and not self._environments[1]))):
            dct["environments"] = dictify(self.environments)
        if "sources" == "type" or (self.sources is not self.__undef__ and (not (dirty and not self._sources[1]))):
            dct["sources"] = dictify(self.sources)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._include_analytics_data = (self._include_analytics_data[0], True)
        self._bundle_type = (self._bundle_type[0], True)
        self._environments = (self._environments[0], True)
        self._sources = (self._sources[0], True)

    def is_dirty(self):
        return any([self._include_analytics_data[1], self._bundle_type[1], self._environments[1], self._sources[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, BaseSupportBundleParameters):
            return False
        return super(BaseSupportBundleParameters, self).__eq__(other) and \
               self.include_analytics_data == other.include_analytics_data and \
               self.bundle_type == other.bundle_type and \
               self.environments == other.environments and \
               self.sources == other.sources

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def include_analytics_data(self):
        """
        *(default value: false)* Whether or not to include the analytics data
        in the support bundle which is generated. Including analytics data may
        significantly increase the support bundle size and upload time, but
        enables analysis of performance characteristics of the Delphix Engine.

        :rtype: ``bool``
        """
        return self._include_analytics_data[0]

    @include_analytics_data.setter
    def include_analytics_data(self, value):
        self._include_analytics_data = (value, True)

    @property
    def bundle_type(self):
        """
        *(default value: ALL)* Type of support bundle to generate. Reserved for
        Delphix support use. *(permitted values: PHONEHOME, MDS, OS, CORE, LOG,
        DROPBOX, STORAGE_TEST, MASKING, ALL)*

        :rtype: ``TEXT_TYPE``
        """
        return self._bundle_type[0]

    @bundle_type.setter
    def bundle_type(self, value):
        self._bundle_type = (value, True)

    @property
    def environments(self):
        """
        The list of environments from which logs should be collected.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._environments[0]

    @environments.setter
    def environments(self, value):
        self._environments = (value, True)

    @property
    def sources(self):
        """
        The list of sources from which logs should be collected.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._sources[0]

    @sources.setter
    def sources(self, value):
        self._sources = (value, True)

