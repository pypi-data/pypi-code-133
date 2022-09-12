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
#     /delphix-tunable-identifier.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_8.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_8 import common

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

class TunableIdentifier(TypedObject):
    """
    *(extends* :py:class:`v1_11_8.web.vo.TypedObject` *)* The subsystem and
    name for a tunable.
    """
    def __init__(self, undef_enabled=True):
        super(TunableIdentifier, self).__init__()
        self._type = ("TunableIdentifier", True)
        self._subsystem = (self.__undef__, True)
        self._name = (self.__undef__, True)

    API_VERSION = "1.11.8"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TunableIdentifier, cls).from_dict(data, dirty, undef_enabled)
        if "subsystem" not in data:
            raise ValueError("Missing required property \"subsystem\".")
        obj._subsystem = (data.get("subsystem", obj.__undef__), dirty)
        if obj._subsystem[0] is not None and obj._subsystem[0] is not obj.__undef__:
            assert isinstance(obj._subsystem[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._subsystem[0], type(obj._subsystem[0])))
            assert obj._subsystem[0] in ['virtualization', 'kernel', 'sysctl', 'service'], "Expected enum ['virtualization', 'kernel', 'sysctl', 'service'] but got %s" % obj._subsystem[0]
            common.validate_format(obj._subsystem[0], "None", None, None)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TunableIdentifier, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "subsystem" == "type" or (self.subsystem is not self.__undef__ and (not (dirty and not self._subsystem[1]) or isinstance(self.subsystem, list) or belongs_to_parent)):
            dct["subsystem"] = dictify(self.subsystem)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._subsystem = (self._subsystem[0], True)
        self._name = (self._name[0], True)

    def is_dirty(self):
        return any([self._subsystem[1], self._name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TunableIdentifier):
            return False
        return super(TunableIdentifier, self).__eq__(other) and \
               self.subsystem == other.subsystem and \
               self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def subsystem(self):
        """
        The subsytem of the tunable represented by this object. *(permitted
        values: virtualization, kernel, sysctl, service)*

        :rtype: ``TEXT_TYPE``
        """
        return self._subsystem[0]

    @subsystem.setter
    def subsystem(self, value):
        self._subsystem = (value, True)

    @property
    def name(self):
        """
        Name of the tunable.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

