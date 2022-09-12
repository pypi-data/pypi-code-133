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
#     /delphix-toolkit-linked-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_3 import factory
from delphixpy.v1_5_3 import common

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

class ToolkitLinkedSource(TypedObject):
    """
    *(extends* :py:class:`v1_5_3.web.vo.TypedObject` *)* A linked source
    definition for toolkits.
    """
    def __init__(self, undef_enabled=True):
        super(ToolkitLinkedSource, self).__init__()
        self._type = ("ToolkitLinkedSource", True)
        self._parameters = (self.__undef__, True)

    API_VERSION = "1.5.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ToolkitLinkedSource, cls).from_dict(data, dirty, undef_enabled)
        if "parameters" not in data:
            raise ValueError("Missing required property \"parameters\".")
        obj._parameters = []
        for item in data.get("parameters") or []:
            obj._parameters.append(factory.create_object(item))
            factory.validate_type(obj._parameters[-1], "ToolkitParameter")
        obj._parameters = (obj._parameters, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ToolkitLinkedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "parameters" == "type" or (self.parameters is not self.__undef__ and (not (dirty and not self._parameters[1]) or isinstance(self.parameters, list) or belongs_to_parent)):
            dct["parameters"] = dictify(self.parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._parameters = (self._parameters[0], True)

    def is_dirty(self):
        return any([self._parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ToolkitLinkedSource):
            return False
        return super(ToolkitLinkedSource, self).__eq__(other) and \
               self.parameters == other.parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def parameters(self):
        """
        Dynamic parameters the user must enter as input when linking data of
        this type.

        :rtype: ``list`` of :py:class:`v1_5_3.web.vo.ToolkitParameter`
        """
        return self._parameters[0]

    @parameters.setter
    def parameters(self, value):
        self._parameters = (value, True)

