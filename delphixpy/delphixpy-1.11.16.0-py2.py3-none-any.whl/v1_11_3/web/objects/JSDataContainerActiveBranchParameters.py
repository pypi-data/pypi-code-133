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
#     /delphix-js-data-container-active-branch-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_3 import common

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

class JSDataContainerActiveBranchParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_3.web.vo.TypedObject` *)* Input parameters for
    the API that given a point in time, returns the active branch of the data
    container.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataContainerActiveBranchParameters, self).__init__()
        self._type = ("JSDataContainerActiveBranchParameters", True)
        self._time = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataContainerActiveBranchParameters, cls).from_dict(data, dirty, undef_enabled)
        if "time" not in data:
            raise ValueError("Missing required property \"time\".")
        obj._time = (data.get("time", obj.__undef__), dirty)
        if obj._time[0] is not None and obj._time[0] is not obj.__undef__:
            assert isinstance(obj._time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._time[0], type(obj._time[0])))
            common.validate_format(obj._time[0], "date", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataContainerActiveBranchParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "time" == "type" or (self.time is not self.__undef__ and (not (dirty and not self._time[1]) or isinstance(self.time, list) or belongs_to_parent)):
            dct["time"] = dictify(self.time)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._time = (self._time[0], True)

    def is_dirty(self):
        return any([self._time[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataContainerActiveBranchParameters):
            return False
        return super(JSDataContainerActiveBranchParameters, self).__eq__(other) and \
               self.time == other.time

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def time(self):
        """
        The time that will be used to find which branch was active in the data
        layout.

        :rtype: ``TEXT_TYPE``
        """
        return self._time[0]

    @time.setter
    def time(self, value):
        self._time = (value, True)

