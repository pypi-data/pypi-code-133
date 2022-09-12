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
#     /delphix-db-container.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_2.web.objects.Container import Container
from delphixpy.v1_8_2 import factory
from delphixpy.v1_8_2 import common

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

class DatabaseContainer(Container):
    """
    *(extends* :py:class:`v1_8_2.web.vo.Container` *)* A container holding
    database data.
    """
    def __init__(self, undef_enabled=True):
        super(DatabaseContainer, self).__init__()
        self._type = ("DatabaseContainer", True)
        self._os = (self.__undef__, True)
        self._performance_mode = (self.__undef__, True)
        self._processor = (self.__undef__, True)
        self._sourcing_policy = (self.__undef__, True)

    API_VERSION = "1.8.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DatabaseContainer, cls).from_dict(data, dirty, undef_enabled)
        obj._os = (data.get("os", obj.__undef__), dirty)
        if obj._os[0] is not None and obj._os[0] is not obj.__undef__:
            assert isinstance(obj._os[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._os[0], type(obj._os[0])))
            common.validate_format(obj._os[0], "None", None, None)
        obj._performance_mode = (data.get("performanceMode", obj.__undef__), dirty)
        if obj._performance_mode[0] is not None and obj._performance_mode[0] is not obj.__undef__:
            assert isinstance(obj._performance_mode[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._performance_mode[0], type(obj._performance_mode[0])))
            assert obj._performance_mode[0] in ['ENABLED', 'DISABLED'], "Expected enum ['ENABLED', 'DISABLED'] but got %s" % obj._performance_mode[0]
            common.validate_format(obj._performance_mode[0], "None", None, None)
        obj._processor = (data.get("processor", obj.__undef__), dirty)
        if obj._processor[0] is not None and obj._processor[0] is not obj.__undef__:
            assert isinstance(obj._processor[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._processor[0], type(obj._processor[0])))
            common.validate_format(obj._processor[0], "None", None, None)
        if "sourcingPolicy" in data and data["sourcingPolicy"] is not None:
            obj._sourcing_policy = (factory.create_object(data["sourcingPolicy"], "SourcingPolicy"), dirty)
            factory.validate_type(obj._sourcing_policy[0], "SourcingPolicy")
        else:
            obj._sourcing_policy = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DatabaseContainer, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "os" == "type" or (self.os is not self.__undef__ and (not (dirty and not self._os[1]))):
            dct["os"] = dictify(self.os)
        if "performance_mode" == "type" or (self.performance_mode is not self.__undef__ and (not (dirty and not self._performance_mode[1]))):
            dct["performanceMode"] = dictify(self.performance_mode)
        if dirty and "performanceMode" in dct:
            del dct["performanceMode"]
        if "processor" == "type" or (self.processor is not self.__undef__ and (not (dirty and not self._processor[1]))):
            dct["processor"] = dictify(self.processor)
        if "sourcing_policy" == "type" or (self.sourcing_policy is not self.__undef__ and (not (dirty and not self._sourcing_policy[1]) or isinstance(self.sourcing_policy, list) or belongs_to_parent)):
            dct["sourcingPolicy"] = dictify(self.sourcing_policy, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._os = (self._os[0], True)
        self._performance_mode = (self._performance_mode[0], True)
        self._processor = (self._processor[0], True)
        self._sourcing_policy = (self._sourcing_policy[0], True)

    def is_dirty(self):
        return any([self._os[1], self._performance_mode[1], self._processor[1], self._sourcing_policy[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DatabaseContainer):
            return False
        return super(DatabaseContainer, self).__eq__(other) and \
               self.os == other.os and \
               self.performance_mode == other.performance_mode and \
               self.processor == other.processor and \
               self.sourcing_policy == other.sourcing_policy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def os(self):
        """
        Native operating system of the original database source system.

        :rtype: ``TEXT_TYPE``
        """
        return self._os[0]

    @os.setter
    def os(self, value):
        self._os = (value, True)

    @property
    def performance_mode(self):
        """
        *(default value: DISABLED)* Whether to enable high performance mode.
        *(permitted values: ENABLED, DISABLED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._performance_mode[0]

    @property
    def processor(self):
        """
        Native processor type of the original database source system.

        :rtype: ``TEXT_TYPE``
        """
        return self._processor[0]

    @processor.setter
    def processor(self, value):
        self._processor = (value, True)

    @property
    def sourcing_policy(self):
        """
        Policies for managing LogSync and SnapSync across sources.

        :rtype: :py:class:`v1_8_2.web.vo.SourcingPolicy`
        """
        return self._sourcing_policy[0]

    @sourcing_policy.setter
    def sourcing_policy(self, value):
        self._sourcing_policy = (value, True)

