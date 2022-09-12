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
#     /delphix-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_0.web.objects.UserObject import UserObject
from delphixpy.v1_7_0 import factory
from delphixpy.v1_7_0 import common

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

class Source(UserObject):
    """
    *(extends* :py:class:`v1_7_0.web.vo.UserObject` *)* A source represents an
    external database instance outside the Delphix system.
    """
    def __init__(self, undef_enabled=True):
        super(Source, self).__init__()
        self._type = ("Source", True)
        self._config = (self.__undef__, True)
        self._container = (self.__undef__, True)
        self._description = (self.__undef__, True)
        self._linked = (self.__undef__, True)
        self._restoration = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._staging = (self.__undef__, True)
        self._status = (self.__undef__, True)
        self._virtual = (self.__undef__, True)

    API_VERSION = "1.7.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Source, cls).from_dict(data, dirty, undef_enabled)
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, None)
        obj._linked = (data.get("linked", obj.__undef__), dirty)
        if obj._linked[0] is not None and obj._linked[0] is not obj.__undef__:
            assert isinstance(obj._linked[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._linked[0], type(obj._linked[0])))
            common.validate_format(obj._linked[0], "None", None, None)
        obj._restoration = (data.get("restoration", obj.__undef__), dirty)
        if obj._restoration[0] is not None and obj._restoration[0] is not obj.__undef__:
            assert isinstance(obj._restoration[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._restoration[0], type(obj._restoration[0])))
            common.validate_format(obj._restoration[0], "None", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "SourceRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "SourceRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        obj._staging = (data.get("staging", obj.__undef__), dirty)
        if obj._staging[0] is not None and obj._staging[0] is not obj.__undef__:
            assert isinstance(obj._staging[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._staging[0], type(obj._staging[0])))
            common.validate_format(obj._staging[0], "None", None, None)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            assert obj._status[0] in ['DEFAULT', 'PENDING_UPGRADE'], "Expected enum ['DEFAULT', 'PENDING_UPGRADE'] but got %s" % obj._status[0]
            common.validate_format(obj._status[0], "None", None, None)
        obj._virtual = (data.get("virtual", obj.__undef__), dirty)
        if obj._virtual[0] is not None and obj._virtual[0] is not obj.__undef__:
            assert isinstance(obj._virtual[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._virtual[0], type(obj._virtual[0])))
            common.validate_format(obj._virtual[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Source, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]))):
            dct["container"] = dictify(self.container)
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]))):
            dct["description"] = dictify(self.description)
        if "linked" == "type" or (self.linked is not self.__undef__ and (not (dirty and not self._linked[1]))):
            dct["linked"] = dictify(self.linked)
        if "restoration" == "type" or (self.restoration is not self.__undef__ and (not (dirty and not self._restoration[1]))):
            dct["restoration"] = dictify(self.restoration)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "staging" == "type" or (self.staging is not self.__undef__ and (not (dirty and not self._staging[1]))):
            dct["staging"] = dictify(self.staging)
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        if "virtual" == "type" or (self.virtual is not self.__undef__ and (not (dirty and not self._virtual[1]))):
            dct["virtual"] = dictify(self.virtual)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._container = (self._container[0], True)
        self._description = (self._description[0], True)
        self._linked = (self._linked[0], True)
        self._restoration = (self._restoration[0], True)
        self._runtime = (self._runtime[0], True)
        self._staging = (self._staging[0], True)
        self._status = (self._status[0], True)
        self._virtual = (self._virtual[0], True)

    def is_dirty(self):
        return any([self._config[1], self._container[1], self._description[1], self._linked[1], self._restoration[1], self._runtime[1], self._staging[1], self._status[1], self._virtual[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Source):
            return False
        return super(Source, self).__eq__(other) and \
               self.config == other.config and \
               self.container == other.container and \
               self.description == other.description and \
               self.linked == other.linked and \
               self.restoration == other.restoration and \
               self.runtime == other.runtime and \
               self.staging == other.staging and \
               self.status == other.status and \
               self.virtual == other.virtual

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
    def container(self):
        """
        Reference to the container being fed by this source, if any.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def description(self):
        """
        A user-provided description of the source.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def linked(self):
        """
        Flag indicating whether the source is a linked source in the Delphix
        system.

        :rtype: ``bool``
        """
        return self._linked[0]

    @linked.setter
    def linked(self, value):
        self._linked = (value, True)

    @property
    def restoration(self):
        """
        Flag indicating whether the source is a restoration source in the
        Delphix system.

        :rtype: ``bool``
        """
        return self._restoration[0]

    @restoration.setter
    def restoration(self, value):
        self._restoration = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this source.

        :rtype: :py:class:`v1_7_0.web.vo.SourceRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def staging(self):
        """
        Flag indicating whether the source is used as a staging source for pre-
        provisioning. Staging sources are managed by the Delphix system.

        :rtype: ``bool``
        """
        return self._staging[0]

    @staging.setter
    def staging(self, value):
        self._staging = (value, True)

    @property
    def status(self):
        """
        Status of this source. *(permitted values: DEFAULT, PENDING_UPGRADE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

    @status.setter
    def status(self, value):
        self._status = (value, True)

    @property
    def virtual(self):
        """
        Flag indicating whether the source is a virtual source in the Delphix
        system.

        :rtype: ``bool``
        """
        return self._virtual[0]

    @virtual.setter
    def virtual(self, value):
        self._virtual = (value, True)

