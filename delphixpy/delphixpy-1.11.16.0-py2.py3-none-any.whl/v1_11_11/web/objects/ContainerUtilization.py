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
#     /delphix-container-utilization.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_11 import factory
from delphixpy.v1_11_11 import common

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

class ContainerUtilization(TypedObject):
    """
    *(extends* :py:class:`v1_11_11.web.vo.TypedObject` *)* Represents the
    utilization of all containers during a particular period of time.
    """
    def __init__(self, undef_enabled=True):
        super(ContainerUtilization, self).__init__()
        self._type = ("ContainerUtilization", True)
        self._container = (self.__undef__, True)
        self._utilization = (self.__undef__, True)
        self._deleted = (self.__undef__, True)
        self._hidden = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ContainerUtilization, cls).from_dict(data, dirty, undef_enabled)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._utilization = []
        for item in data.get("utilization") or []:
            obj._utilization.append(factory.create_object(item))
            factory.validate_type(obj._utilization[-1], "ContainerUtilizationInterval")
        obj._utilization = (obj._utilization, dirty)
        obj._deleted = (data.get("deleted", obj.__undef__), dirty)
        if obj._deleted[0] is not None and obj._deleted[0] is not obj.__undef__:
            assert isinstance(obj._deleted[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._deleted[0], type(obj._deleted[0])))
            common.validate_format(obj._deleted[0], "None", None, None)
        obj._hidden = (data.get("hidden", obj.__undef__), dirty)
        if obj._hidden[0] is not None and obj._hidden[0] is not obj.__undef__:
            assert isinstance(obj._hidden[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._hidden[0], type(obj._hidden[0])))
            common.validate_format(obj._hidden[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ContainerUtilization, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]))):
            dct["container"] = dictify(self.container)
        if "utilization" == "type" or (self.utilization is not self.__undef__ and (not (dirty and not self._utilization[1]))):
            dct["utilization"] = dictify(self.utilization)
        if "deleted" == "type" or (self.deleted is not self.__undef__ and (not (dirty and not self._deleted[1]))):
            dct["deleted"] = dictify(self.deleted)
        if "hidden" == "type" or (self.hidden is not self.__undef__ and (not (dirty and not self._hidden[1]))):
            dct["hidden"] = dictify(self.hidden)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._utilization = (self._utilization[0], True)
        self._deleted = (self._deleted[0], True)
        self._hidden = (self._hidden[0], True)

    def is_dirty(self):
        return any([self._container[1], self._utilization[1], self._deleted[1], self._hidden[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ContainerUtilization):
            return False
        return super(ContainerUtilization, self).__eq__(other) and \
               self.container == other.container and \
               self.utilization == other.utilization and \
               self.deleted == other.deleted and \
               self.hidden == other.hidden

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        Reference to the container whose utilization we are describing.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def utilization(self):
        """
        A list of container utilization statistics corresponding to this period
        of time, one for each sampling interval.

        :rtype: ``list`` of
            :py:class:`v1_11_11.web.vo.ContainerUtilizationInterval`
        """
        return self._utilization[0]

    @utilization.setter
    def utilization(self, value):
        self._utilization = (value, True)

    @property
    def deleted(self):
        """
        True if this container has been deleted.

        :rtype: ``bool``
        """
        return self._deleted[0]

    @deleted.setter
    def deleted(self, value):
        self._deleted = (value, True)

    @property
    def hidden(self):
        """
        True if the current user does not have access to this container.

        :rtype: ``bool``
        """
        return self._hidden[0]

    @hidden.setter
    def hidden(self, value):
        self._hidden = (value, True)

