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
#     /delphix-dynamic-parameter.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_1 import common

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

class DynamicParameter(TypedObject):
    """
    *(extends* :py:class:`v1_5_1.web.vo.TypedObject` *)* The description of how
    a dynamic parameter is presented to clients and what validation clients can
    do on user input for the parameter.
    """
    def __init__(self, undef_enabled=True):
        super(DynamicParameter, self).__init__()
        self._type = ("DynamicParameter", True)
        self._description = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._pretty_name = (self.__undef__, True)

    API_VERSION = "1.5.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DynamicParameter, cls).from_dict(data, dirty, undef_enabled)
        if "description" not in data:
            raise ValueError("Missing required property \"description\".")
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, None)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", 1, None)
        if "prettyName" not in data:
            raise ValueError("Missing required property \"prettyName\".")
        obj._pretty_name = (data.get("prettyName", obj.__undef__), dirty)
        if obj._pretty_name[0] is not None and obj._pretty_name[0] is not obj.__undef__:
            assert isinstance(obj._pretty_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pretty_name[0], type(obj._pretty_name[0])))
            common.validate_format(obj._pretty_name[0], "None", 1, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DynamicParameter, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "pretty_name" == "type" or (self.pretty_name is not self.__undef__ and (not (dirty and not self._pretty_name[1]) or isinstance(self.pretty_name, list) or belongs_to_parent)):
            dct["prettyName"] = dictify(self.pretty_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._description = (self._description[0], True)
        self._name = (self._name[0], True)
        self._pretty_name = (self._pretty_name[0], True)

    def is_dirty(self):
        return any([self._description[1], self._name[1], self._pretty_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DynamicParameter):
            return False
        return super(DynamicParameter, self).__eq__(other) and \
               self.description == other.description and \
               self.name == other.name and \
               self.pretty_name == other.pretty_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def description(self):
        """
        The description of what this property means and how it is used.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def name(self):
        """
        The name clients should use when setting the parameter's value.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def pretty_name(self):
        """
        A short, human-readable name for clients to use instead of 'name' when
        requesting user input. For example, while 'name' might be 'portNumber',
        'prettyName' could be 'Port Number'.

        :rtype: ``TEXT_TYPE``
        """
        return self._pretty_name[0]

    @pretty_name.setter
    def pretty_name(self, value):
        self._pretty_name = (value, True)

