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
#     /delphix-js-container-capacity-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_3 import common

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

class JSContainerCapacityData(TypedObject):
    """
    *(extends* :py:class:`v1_4_3.web.vo.TypedObject` *)* The capacity
    information for a data container.
    """
    def __init__(self, undef_enabled=True):
        super(JSContainerCapacityData, self).__init__()
        self._type = ("JSContainerCapacityData", True)
        self._data_container = (self.__undef__, True)
        self._referenced_by_self = (self.__undef__, True)
        self._referenced_by_siblings = (self.__undef__, True)
        self._unique = (self.__undef__, True)
        self._unvirtualized = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSContainerCapacityData, cls).from_dict(data, dirty, undef_enabled)
        obj._data_container = (data.get("dataContainer", obj.__undef__), dirty)
        if obj._data_container[0] is not None and obj._data_container[0] is not obj.__undef__:
            assert isinstance(obj._data_container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_container[0], type(obj._data_container[0])))
            common.validate_format(obj._data_container[0], "objectReference", None, None)
        obj._referenced_by_self = (data.get("referencedBySelf", obj.__undef__), dirty)
        if obj._referenced_by_self[0] is not None and obj._referenced_by_self[0] is not obj.__undef__:
            assert isinstance(obj._referenced_by_self[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._referenced_by_self[0], type(obj._referenced_by_self[0])))
            common.validate_format(obj._referenced_by_self[0], "None", None, None)
        obj._referenced_by_siblings = (data.get("referencedBySiblings", obj.__undef__), dirty)
        if obj._referenced_by_siblings[0] is not None and obj._referenced_by_siblings[0] is not obj.__undef__:
            assert isinstance(obj._referenced_by_siblings[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._referenced_by_siblings[0], type(obj._referenced_by_siblings[0])))
            common.validate_format(obj._referenced_by_siblings[0], "None", None, None)
        obj._unique = (data.get("unique", obj.__undef__), dirty)
        if obj._unique[0] is not None and obj._unique[0] is not obj.__undef__:
            assert isinstance(obj._unique[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._unique[0], type(obj._unique[0])))
            common.validate_format(obj._unique[0], "None", None, None)
        obj._unvirtualized = (data.get("unvirtualized", obj.__undef__), dirty)
        if obj._unvirtualized[0] is not None and obj._unvirtualized[0] is not obj.__undef__:
            assert isinstance(obj._unvirtualized[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._unvirtualized[0], type(obj._unvirtualized[0])))
            common.validate_format(obj._unvirtualized[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSContainerCapacityData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "data_container" == "type" or (self.data_container is not self.__undef__ and (not (dirty and not self._data_container[1]))):
            dct["dataContainer"] = dictify(self.data_container)
        if "referenced_by_self" == "type" or (self.referenced_by_self is not self.__undef__ and (not (dirty and not self._referenced_by_self[1]))):
            dct["referencedBySelf"] = dictify(self.referenced_by_self)
        if "referenced_by_siblings" == "type" or (self.referenced_by_siblings is not self.__undef__ and (not (dirty and not self._referenced_by_siblings[1]))):
            dct["referencedBySiblings"] = dictify(self.referenced_by_siblings)
        if "unique" == "type" or (self.unique is not self.__undef__ and (not (dirty and not self._unique[1]))):
            dct["unique"] = dictify(self.unique)
        if "unvirtualized" == "type" or (self.unvirtualized is not self.__undef__ and (not (dirty and not self._unvirtualized[1]))):
            dct["unvirtualized"] = dictify(self.unvirtualized)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._data_container = (self._data_container[0], True)
        self._referenced_by_self = (self._referenced_by_self[0], True)
        self._referenced_by_siblings = (self._referenced_by_siblings[0], True)
        self._unique = (self._unique[0], True)
        self._unvirtualized = (self._unvirtualized[0], True)

    def is_dirty(self):
        return any([self._data_container[1], self._referenced_by_self[1], self._referenced_by_siblings[1], self._unique[1], self._unvirtualized[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSContainerCapacityData):
            return False
        return super(JSContainerCapacityData, self).__eq__(other) and \
               self.data_container == other.data_container and \
               self.referenced_by_self == other.referenced_by_self and \
               self.referenced_by_siblings == other.referenced_by_siblings and \
               self.unique == other.unique and \
               self.unvirtualized == other.unvirtualized

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def data_container(self):
        """
        The data container that this capacity information is for.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_container[0]

    @data_container.setter
    def data_container(self, value):
        self._data_container = (value, True)

    @property
    def referenced_by_self(self):
        """
        The amount of space that cannot be freed on the parent data template
        (or sibling data containers) because it is being referenced by this
        data container due to restore operations.

        :rtype: ``float``
        """
        return self._referenced_by_self[0]

    @referenced_by_self.setter
    def referenced_by_self(self, value):
        self._referenced_by_self = (value, True)

    @property
    def referenced_by_siblings(self):
        """
        The amount of space that cannot be freed on this data container because
        it is being referenced by sibling data containers due to restore
        operations.

        :rtype: ``float``
        """
        return self._referenced_by_siblings[0]

    @referenced_by_siblings.setter
    def referenced_by_siblings(self, value):
        self._referenced_by_siblings = (value, True)

    @property
    def unique(self):
        """
        The amount of space that will be freed if a purge operation is
        performed on this data container.

        :rtype: ``float``
        """
        return self._unique[0]

    @unique.setter
    def unique(self, value):
        self._unique = (value, True)

    @property
    def unvirtualized(self):
        """
        The amount of space that would be consumed by the data in this
        container without Delphix.

        :rtype: ``float``
        """
        return self._unvirtualized[0]

    @unvirtualized.setter
    def unvirtualized(self, value):
        self._unvirtualized = (value, True)

