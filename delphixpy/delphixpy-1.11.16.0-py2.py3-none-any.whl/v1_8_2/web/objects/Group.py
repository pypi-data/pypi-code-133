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
#     /delphix-group.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_2.web.objects.NamedUserObject import NamedUserObject
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

class Group(NamedUserObject):
    """
    *(extends* :py:class:`v1_8_2.web.vo.NamedUserObject` *)* Database group.
    """
    def __init__(self, undef_enabled=True):
        super(Group, self).__init__()
        self._type = ("Group", True)
        self._data_node = (self.__undef__, True)
        self._description = (self.__undef__, True)

    API_VERSION = "1.8.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Group, cls).from_dict(data, dirty, undef_enabled)
        obj._data_node = (data.get("dataNode", obj.__undef__), dirty)
        if obj._data_node[0] is not None and obj._data_node[0] is not obj.__undef__:
            assert isinstance(obj._data_node[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_node[0], type(obj._data_node[0])))
            common.validate_format(obj._data_node[0], "objectReference", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, 1024)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Group, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "data_node" == "type" or (self.data_node is not self.__undef__ and (not (dirty and not self._data_node[1]) or isinstance(self.data_node, list) or belongs_to_parent)):
            dct["dataNode"] = dictify(self.data_node)
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._data_node = (self._data_node[0], True)
        self._description = (self._description[0], True)

    def is_dirty(self):
        return any([self._data_node[1], self._description[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Group):
            return False
        return super(Group, self).__eq__(other) and \
               self.data_node == other.data_node and \
               self.description == other.description

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def data_node(self):
        """
        The data node where databases of this group will be located.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_node[0]

    @data_node.setter
    def data_node(self, value):
        self._data_node = (value, True)

    @property
    def description(self):
        """
        Optional description for the group.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

