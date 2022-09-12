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
#     /delphix-compatibility-criteria.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.TypedObject import TypedObject
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

class CompatibilityCriteria(TypedObject):
    """
    *(extends* :py:class:`v1_11_13.web.vo.TypedObject` *)* The compatibility
    criteria to use for selecting compatible repositories. Parameters with a
    value of null are not considered when selecting compatible repositories.
    """
    def __init__(self, undef_enabled=True):
        super(CompatibilityCriteria, self).__init__()
        self._type = ("CompatibilityCriteria", True)
        self._os = (self.__undef__, True)
        self._processor = (self.__undef__, True)
        self._architecture = (self.__undef__, True)
        self._staging_enabled = (self.__undef__, True)
        self._environment = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CompatibilityCriteria, cls).from_dict(data, dirty, undef_enabled)
        obj._os = (data.get("os", obj.__undef__), dirty)
        if obj._os[0] is not None and obj._os[0] is not obj.__undef__:
            assert isinstance(obj._os[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._os[0], type(obj._os[0])))
            assert obj._os[0] in ['Linux', 'AIX', 'HPUX', 'SunOS', 'Windows'], "Expected enum ['Linux', 'AIX', 'HPUX', 'SunOS', 'Windows'] but got %s" % obj._os[0]
            common.validate_format(obj._os[0], "None", None, None)
        obj._processor = (data.get("processor", obj.__undef__), dirty)
        if obj._processor[0] is not None and obj._processor[0] is not obj.__undef__:
            assert isinstance(obj._processor[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._processor[0], type(obj._processor[0])))
            assert obj._processor[0] in ['x86', 'ia64', 'powerpc', 'sparc'], "Expected enum ['x86', 'ia64', 'powerpc', 'sparc'] but got %s" % obj._processor[0]
            common.validate_format(obj._processor[0], "None", None, None)
        obj._architecture = (data.get("architecture", obj.__undef__), dirty)
        if obj._architecture[0] is not None and obj._architecture[0] is not obj.__undef__:
            assert isinstance(obj._architecture[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._architecture[0], type(obj._architecture[0])))
            common.validate_format(obj._architecture[0], "None", None, None)
        obj._staging_enabled = (data.get("stagingEnabled", obj.__undef__), dirty)
        if obj._staging_enabled[0] is not None and obj._staging_enabled[0] is not obj.__undef__:
            assert isinstance(obj._staging_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._staging_enabled[0], type(obj._staging_enabled[0])))
            common.validate_format(obj._staging_enabled[0], "None", None, None)
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CompatibilityCriteria, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "os" == "type" or (self.os is not self.__undef__ and (not (dirty and not self._os[1]))):
            dct["os"] = dictify(self.os)
        if "processor" == "type" or (self.processor is not self.__undef__ and (not (dirty and not self._processor[1]))):
            dct["processor"] = dictify(self.processor)
        if "architecture" == "type" or (self.architecture is not self.__undef__ and (not (dirty and not self._architecture[1]))):
            dct["architecture"] = dictify(self.architecture)
        if "staging_enabled" == "type" or (self.staging_enabled is not self.__undef__ and (not (dirty and not self._staging_enabled[1]))):
            dct["stagingEnabled"] = dictify(self.staging_enabled)
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]))):
            dct["environment"] = dictify(self.environment)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._os = (self._os[0], True)
        self._processor = (self._processor[0], True)
        self._architecture = (self._architecture[0], True)
        self._staging_enabled = (self._staging_enabled[0], True)
        self._environment = (self._environment[0], True)

    def is_dirty(self):
        return any([self._os[1], self._processor[1], self._architecture[1], self._staging_enabled[1], self._environment[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CompatibilityCriteria):
            return False
        return super(CompatibilityCriteria, self).__eq__(other) and \
               self.os == other.os and \
               self.processor == other.processor and \
               self.architecture == other.architecture and \
               self.staging_enabled == other.staging_enabled and \
               self.environment == other.environment

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def os(self):
        """
        Selected repositories are installed on a host with this OS. *(permitted
        values: Linux, AIX, HPUX, SunOS, Windows)*

        :rtype: ``TEXT_TYPE``
        """
        return self._os[0]

    @os.setter
    def os(self, value):
        self._os = (value, True)

    @property
    def processor(self):
        """
        Selected repositories are installed on a host with this type of
        processor. *(permitted values: x86, ia64, powerpc, sparc)*

        :rtype: ``TEXT_TYPE``
        """
        return self._processor[0]

    @processor.setter
    def processor(self, value):
        self._processor = (value, True)

    @property
    def architecture(self):
        """
        Selected repositories are installed on a host with this architecture
        (32-bit or 64-bit).

        :rtype: ``int``
        """
        return self._architecture[0]

    @architecture.setter
    def architecture(self, value):
        self._architecture = (value, True)

    @property
    def staging_enabled(self):
        """
        If true, selected repositories have staging enabled.

        :rtype: ``bool``
        """
        return self._staging_enabled[0]

    @staging_enabled.setter
    def staging_enabled(self, value):
        self._staging_enabled = (value, True)

    @property
    def environment(self):
        """
        Selected repositories are installed on this environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

