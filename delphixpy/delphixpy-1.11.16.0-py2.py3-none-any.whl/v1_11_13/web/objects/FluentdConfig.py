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
#     /delphix-fluentd-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.UserObject import UserObject
from delphixpy.v1_11_13 import factory
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

class FluentdConfig(UserObject):
    """
    *(extends* :py:class:`v1_11_13.web.vo.UserObject` *)* Fluentd configuration
    information.
    """
    def __init__(self, undef_enabled=True):
        super(FluentdConfig, self).__init__()
        self._type = ("FluentdConfig", True)
        self._enabled = (self.__undef__, True)
        self._plugin = (self.__undef__, True)
        self._attributes = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(FluentdConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._plugin = (data.get("plugin", obj.__undef__), dirty)
        if obj._plugin[0] is not None and obj._plugin[0] is not obj.__undef__:
            assert isinstance(obj._plugin[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._plugin[0], type(obj._plugin[0])))
            common.validate_format(obj._plugin[0], "None", None, None)
        obj._attributes = []
        for item in data.get("attributes") or []:
            obj._attributes.append(factory.create_object(item))
            factory.validate_type(obj._attributes[-1], "FluentdAttribute")
        obj._attributes = (obj._attributes, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(FluentdConfig, self).to_dict(dirty, belongs_to_parent)

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
            dct["enabled"] = False
        if "plugin" == "type" or (self.plugin is not self.__undef__ and (not (dirty and not self._plugin[1]) or isinstance(self.plugin, list) or belongs_to_parent)):
            dct["plugin"] = dictify(self.plugin)
        if "attributes" == "type" or (self.attributes is not self.__undef__ and (not (dirty and not self._attributes[1]) or isinstance(self.attributes, list) or belongs_to_parent)):
            dct["attributes"] = dictify(self.attributes, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._enabled = (self._enabled[0], True)
        self._plugin = (self._plugin[0], True)
        self._attributes = (self._attributes[0], True)

    def is_dirty(self):
        return any([self._enabled[1], self._plugin[1], self._attributes[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, FluentdConfig):
            return False
        return super(FluentdConfig, self).__eq__(other) and \
               self.enabled == other.enabled and \
               self.plugin == other.plugin and \
               self.attributes == other.attributes

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def enabled(self):
        """
        Whether we should send Delphix Insight data using this configuration.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def plugin(self):
        """
        Name of the fluentd plugin.

        :rtype: ``TEXT_TYPE``
        """
        return self._plugin[0]

    @plugin.setter
    def plugin(self, value):
        self._plugin = (value, True)

    @property
    def attributes(self):
        """
        List of attributes to configure fluentd.

        :rtype: ``list`` of :py:class:`v1_11_13.web.vo.FluentdAttribute`
        """
        return self._attributes[0]

    @attributes.setter
    def attributes(self, value):
        self._attributes = (value, True)

