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
#     /delphix-batch-container-refresh-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_2 import common

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

class BatchContainerRefreshParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_2.web.vo.TypedObject` *)* The parameters to use
    as input to batch container refresh requests.
    """
    def __init__(self, undef_enabled=True):
        super(BatchContainerRefreshParameters, self).__init__()
        self._type = ("BatchContainerRefreshParameters", True)
        self._containers = (self.__undef__, True)
        self._location = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(BatchContainerRefreshParameters, cls).from_dict(data, dirty, undef_enabled)
        if "containers" not in data:
            raise ValueError("Missing required property \"containers\".")
        obj._containers = []
        for item in data.get("containers") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._containers.append(item)
        obj._containers = (obj._containers, dirty)
        obj._location = (data.get("location", obj.__undef__), dirty)
        if obj._location[0] is not None and obj._location[0] is not obj.__undef__:
            assert isinstance(obj._location[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._location[0], type(obj._location[0])))
            assert obj._location[0] in ['LATEST_POINT', 'LATEST_SNAPSHOT'], "Expected enum ['LATEST_POINT', 'LATEST_SNAPSHOT'] but got %s" % obj._location[0]
            common.validate_format(obj._location[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(BatchContainerRefreshParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "containers" == "type" or (self.containers is not self.__undef__ and (not (dirty and not self._containers[1]) or isinstance(self.containers, list) or belongs_to_parent)):
            dct["containers"] = dictify(self.containers, prop_is_list_or_vo=True)
        if "location" == "type" or (self.location is not self.__undef__ and (not (dirty and not self._location[1]))):
            dct["location"] = dictify(self.location)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._containers = (self._containers[0], True)
        self._location = (self._location[0], True)

    def is_dirty(self):
        return any([self._containers[1], self._location[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, BatchContainerRefreshParameters):
            return False
        return super(BatchContainerRefreshParameters, self).__eq__(other) and \
               self.containers == other.containers and \
               self.location == other.location

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def containers(self):
        """
        Containers to refresh.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._containers[0]

    @containers.setter
    def containers(self, value):
        self._containers = (value, True)

    @property
    def location(self):
        """
        *(default value: LATEST_POINT)* A semantic description of a TimeFlow
        location. *(permitted values: LATEST_POINT, LATEST_SNAPSHOT)*

        :rtype: ``TEXT_TYPE``
        """
        return self._location[0]

    @location.setter
    def location(self, value):
        self._location = (value, True)

