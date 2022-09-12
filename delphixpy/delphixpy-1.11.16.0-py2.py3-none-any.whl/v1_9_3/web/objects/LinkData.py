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
#     /delphix-link-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_3 import factory
from delphixpy.v1_9_3 import common

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

class LinkData(TypedObject):
    """
    *(extends* :py:class:`v1_9_3.web.vo.TypedObject` *)* Base type for specific
    parameters for a link request.
    """
    def __init__(self, undef_enabled=True):
        super(LinkData, self).__init__()
        self._type = ("LinkData", True)
        self._config = (self.__undef__, True)
        self._sourcing_policy = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(LinkData, cls).from_dict(data, dirty, undef_enabled)
        if "config" not in data:
            raise ValueError("Missing required property \"config\".")
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        if "sourcingPolicy" in data and data["sourcingPolicy"] is not None:
            obj._sourcing_policy = (factory.create_object(data["sourcingPolicy"], "SourcingPolicy"), dirty)
            factory.validate_type(obj._sourcing_policy[0], "SourcingPolicy")
        else:
            obj._sourcing_policy = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(LinkData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "sourcing_policy" == "type" or (self.sourcing_policy is not self.__undef__ and (not (dirty and not self._sourcing_policy[1]) or isinstance(self.sourcing_policy, list) or belongs_to_parent)):
            dct["sourcingPolicy"] = dictify(self.sourcing_policy, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._sourcing_policy = (self._sourcing_policy[0], True)

    def is_dirty(self):
        return any([self._config[1], self._sourcing_policy[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, LinkData):
            return False
        return super(LinkData, self).__eq__(other) and \
               self.config == other.config and \
               self.sourcing_policy == other.sourcing_policy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def config(self):
        """
        Reference to the configuration for the source.

        :rtype: ``TEXT_TYPE``
        """
        return self._config[0]

    @config.setter
    def config(self, value):
        self._config = (value, True)

    @property
    def sourcing_policy(self):
        """
        Policies for managing LogSync and SnapSync across sources.

        :rtype: :py:class:`v1_9_3.web.vo.SourcingPolicy`
        """
        return self._sourcing_policy[0]

    @sourcing_policy.setter
    def sourcing_policy(self, value):
        self._sourcing_policy = (value, True)

