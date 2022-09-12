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
#     /delphix-about.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_2 import factory
from delphixpy.v1_9_2 import common

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

class PublicSystemInfo(TypedObject):
    """
    *(extends* :py:class:`v1_9_2.web.vo.TypedObject` *)* Retrieve static
    system-wide properties.
    """
    def __init__(self, undef_enabled=True):
        super(PublicSystemInfo, self).__init__()
        self._type = ("PublicSystemInfo", True)
        self._product_type = (self.__undef__, True)
        self._product_name = (self.__undef__, True)
        self._build_title = (self.__undef__, True)
        self._build_timestamp = (self.__undef__, True)
        self._build_version = (self.__undef__, True)
        self._configured = (self.__undef__, True)
        self._enabled_features = (self.__undef__, True)
        self._api_version = (self.__undef__, True)
        self._banner = (self.__undef__, True)
        self._locales = (self.__undef__, True)
        self._current_locale = (self.__undef__, True)
        self._kernel_name = (self.__undef__, True)

    API_VERSION = "1.9.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PublicSystemInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._product_type = (data.get("productType", obj.__undef__), dirty)
        if obj._product_type[0] is not None and obj._product_type[0] is not obj.__undef__:
            assert isinstance(obj._product_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._product_type[0], type(obj._product_type[0])))
            common.validate_format(obj._product_type[0], "None", None, None)
        obj._product_name = (data.get("productName", obj.__undef__), dirty)
        if obj._product_name[0] is not None and obj._product_name[0] is not obj.__undef__:
            assert isinstance(obj._product_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._product_name[0], type(obj._product_name[0])))
            common.validate_format(obj._product_name[0], "None", None, None)
        obj._build_title = (data.get("buildTitle", obj.__undef__), dirty)
        if obj._build_title[0] is not None and obj._build_title[0] is not obj.__undef__:
            assert isinstance(obj._build_title[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._build_title[0], type(obj._build_title[0])))
            common.validate_format(obj._build_title[0], "None", None, None)
        obj._build_timestamp = (data.get("buildTimestamp", obj.__undef__), dirty)
        if obj._build_timestamp[0] is not None and obj._build_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._build_timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._build_timestamp[0], type(obj._build_timestamp[0])))
            common.validate_format(obj._build_timestamp[0], "date", None, None)
        if "buildVersion" in data and data["buildVersion"] is not None:
            obj._build_version = (factory.create_object(data["buildVersion"], "VersionInfo"), dirty)
            factory.validate_type(obj._build_version[0], "VersionInfo")
        else:
            obj._build_version = (obj.__undef__, dirty)
        obj._configured = (data.get("configured", obj.__undef__), dirty)
        if obj._configured[0] is not None and obj._configured[0] is not obj.__undef__:
            assert isinstance(obj._configured[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._configured[0], type(obj._configured[0])))
            common.validate_format(obj._configured[0], "None", None, None)
        obj._enabled_features = []
        for item in data.get("enabledFeatures") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._enabled_features.append(item)
        obj._enabled_features = (obj._enabled_features, dirty)
        if "apiVersion" in data and data["apiVersion"] is not None:
            obj._api_version = (factory.create_object(data["apiVersion"], "APIVersion"), dirty)
            factory.validate_type(obj._api_version[0], "APIVersion")
        else:
            obj._api_version = (obj.__undef__, dirty)
        obj._banner = (data.get("banner", obj.__undef__), dirty)
        if obj._banner[0] is not None and obj._banner[0] is not obj.__undef__:
            assert isinstance(obj._banner[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._banner[0], type(obj._banner[0])))
            common.validate_format(obj._banner[0], "None", None, None)
        obj._locales = []
        for item in data.get("locales") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "locale", None, None)
            obj._locales.append(item)
        obj._locales = (obj._locales, dirty)
        obj._current_locale = (data.get("currentLocale", obj.__undef__), dirty)
        if obj._current_locale[0] is not None and obj._current_locale[0] is not obj.__undef__:
            assert isinstance(obj._current_locale[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._current_locale[0], type(obj._current_locale[0])))
            common.validate_format(obj._current_locale[0], "locale", None, None)
        obj._kernel_name = (data.get("kernelName", obj.__undef__), dirty)
        if obj._kernel_name[0] is not None and obj._kernel_name[0] is not obj.__undef__:
            assert isinstance(obj._kernel_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._kernel_name[0], type(obj._kernel_name[0])))
            common.validate_format(obj._kernel_name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PublicSystemInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "product_type" == "type" or (self.product_type is not self.__undef__ and (not (dirty and not self._product_type[1]))):
            dct["productType"] = dictify(self.product_type)
        if "product_name" == "type" or (self.product_name is not self.__undef__ and (not (dirty and not self._product_name[1]))):
            dct["productName"] = dictify(self.product_name)
        if "build_title" == "type" or (self.build_title is not self.__undef__ and (not (dirty and not self._build_title[1]))):
            dct["buildTitle"] = dictify(self.build_title)
        if "build_timestamp" == "type" or (self.build_timestamp is not self.__undef__ and (not (dirty and not self._build_timestamp[1]))):
            dct["buildTimestamp"] = dictify(self.build_timestamp)
        if "build_version" == "type" or (self.build_version is not self.__undef__ and (not (dirty and not self._build_version[1]))):
            dct["buildVersion"] = dictify(self.build_version)
        if "configured" == "type" or (self.configured is not self.__undef__ and (not (dirty and not self._configured[1]))):
            dct["configured"] = dictify(self.configured)
        if "enabled_features" == "type" or (self.enabled_features is not self.__undef__ and (not (dirty and not self._enabled_features[1]))):
            dct["enabledFeatures"] = dictify(self.enabled_features)
        if "api_version" == "type" or (self.api_version is not self.__undef__ and (not (dirty and not self._api_version[1]))):
            dct["apiVersion"] = dictify(self.api_version)
        if "banner" == "type" or (self.banner is not self.__undef__ and (not (dirty and not self._banner[1]))):
            dct["banner"] = dictify(self.banner)
        if "locales" == "type" or (self.locales is not self.__undef__ and (not (dirty and not self._locales[1]))):
            dct["locales"] = dictify(self.locales)
        if "current_locale" == "type" or (self.current_locale is not self.__undef__ and (not (dirty and not self._current_locale[1]))):
            dct["currentLocale"] = dictify(self.current_locale)
        if "kernel_name" == "type" or (self.kernel_name is not self.__undef__ and (not (dirty and not self._kernel_name[1]))):
            dct["kernelName"] = dictify(self.kernel_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._product_type = (self._product_type[0], True)
        self._product_name = (self._product_name[0], True)
        self._build_title = (self._build_title[0], True)
        self._build_timestamp = (self._build_timestamp[0], True)
        self._build_version = (self._build_version[0], True)
        self._configured = (self._configured[0], True)
        self._enabled_features = (self._enabled_features[0], True)
        self._api_version = (self._api_version[0], True)
        self._banner = (self._banner[0], True)
        self._locales = (self._locales[0], True)
        self._current_locale = (self._current_locale[0], True)
        self._kernel_name = (self._kernel_name[0], True)

    def is_dirty(self):
        return any([self._product_type[1], self._product_name[1], self._build_title[1], self._build_timestamp[1], self._build_version[1], self._configured[1], self._enabled_features[1], self._api_version[1], self._banner[1], self._locales[1], self._current_locale[1], self._kernel_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PublicSystemInfo):
            return False
        return super(PublicSystemInfo, self).__eq__(other) and \
               self.product_type == other.product_type and \
               self.product_name == other.product_name and \
               self.build_title == other.build_title and \
               self.build_timestamp == other.build_timestamp and \
               self.build_version == other.build_version and \
               self.configured == other.configured and \
               self.enabled_features == other.enabled_features and \
               self.api_version == other.api_version and \
               self.banner == other.banner and \
               self.locales == other.locales and \
               self.current_locale == other.current_locale and \
               self.kernel_name == other.kernel_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def product_type(self):
        """
        Product type.

        :rtype: ``TEXT_TYPE``
        """
        return self._product_type[0]

    @product_type.setter
    def product_type(self, value):
        self._product_type = (value, True)

    @property
    def product_name(self):
        """
        Name of the product that the system is running.

        :rtype: ``TEXT_TYPE``
        """
        return self._product_name[0]

    @product_name.setter
    def product_name(self, value):
        self._product_name = (value, True)

    @property
    def build_title(self):
        """
        Description of the current system software.

        :rtype: ``TEXT_TYPE``
        """
        return self._build_title[0]

    @build_title.setter
    def build_title(self, value):
        self._build_title = (value, True)

    @property
    def build_timestamp(self):
        """
        Time at which the current system software was built.

        :rtype: ``TEXT_TYPE``
        """
        return self._build_timestamp[0]

    @build_timestamp.setter
    def build_timestamp(self, value):
        self._build_timestamp = (value, True)

    @property
    def build_version(self):
        """
        Delphix version of the current system software.

        :rtype: :py:class:`v1_9_2.web.vo.VersionInfo`
        """
        return self._build_version[0]

    @build_version.setter
    def build_version(self, value):
        self._build_version = (value, True)

    @property
    def configured(self):
        """
        Indicates whether the server has gone through initial setup or not.

        :rtype: ``bool``
        """
        return self._configured[0]

    @configured.setter
    def configured(self, value):
        self._configured = (value, True)

    @property
    def enabled_features(self):
        """
        The list of enabled features on this Delphix Engine.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._enabled_features[0]

    @enabled_features.setter
    def enabled_features(self, value):
        self._enabled_features = (value, True)

    @property
    def api_version(self):
        """
        Maximum supported API version of the current system software.

        :rtype: :py:class:`v1_9_2.web.vo.APIVersion`
        """
        return self._api_version[0]

    @api_version.setter
    def api_version(self, value):
        self._api_version = (value, True)

    @property
    def banner(self):
        """
        Security banner to display prior to login.

        :rtype: ``TEXT_TYPE``
        """
        return self._banner[0]

    @banner.setter
    def banner(self, value):
        self._banner = (value, True)

    @property
    def locales(self):
        """
        List of available locales.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._locales[0]

    @locales.setter
    def locales(self, value):
        self._locales = (value, True)

    @property
    def current_locale(self):
        """
        The current system locale.

        :rtype: ``TEXT_TYPE``
        """
        return self._current_locale[0]

    @current_locale.setter
    def current_locale(self, value):
        self._current_locale = (value, True)

    @property
    def kernel_name(self):
        """
        The operating system kernel name.

        :rtype: ``TEXT_TYPE``
        """
        return self._kernel_name[0]

    @kernel_name.setter
    def kernel_name(self, value):
        self._kernel_name = (value, True)

