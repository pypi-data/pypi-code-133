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
#     /delphix-js-source-data-timestamp-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_1 import common

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

class JSSourceDataTimestampParameters(TypedObject):
    """
    *(extends* :py:class:`v1_9_1.web.vo.TypedObject` *)* Input parameters for
    the API that given a point in time, returns the timestamps of the latest
    provisionable points, before the specified time and from the given branch,
    for each data source in the branch's data layout.
    """
    def __init__(self, undef_enabled=True):
        super(JSSourceDataTimestampParameters, self).__init__()
        self._type = ("JSSourceDataTimestampParameters", True)
        self._time = (self.__undef__, True)
        self._branch = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSSourceDataTimestampParameters, cls).from_dict(data, dirty, undef_enabled)
        if "time" not in data:
            raise ValueError("Missing required property \"time\".")
        obj._time = (data.get("time", obj.__undef__), dirty)
        if obj._time[0] is not None and obj._time[0] is not obj.__undef__:
            assert isinstance(obj._time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._time[0], type(obj._time[0])))
            common.validate_format(obj._time[0], "date", None, None)
        if "branch" not in data:
            raise ValueError("Missing required property \"branch\".")
        obj._branch = (data.get("branch", obj.__undef__), dirty)
        if obj._branch[0] is not None and obj._branch[0] is not obj.__undef__:
            assert isinstance(obj._branch[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._branch[0], type(obj._branch[0])))
            common.validate_format(obj._branch[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSSourceDataTimestampParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "time" == "type" or (self.time is not self.__undef__ and (not (dirty and not self._time[1]) or isinstance(self.time, list) or belongs_to_parent)):
            dct["time"] = dictify(self.time)
        if "branch" == "type" or (self.branch is not self.__undef__ and (not (dirty and not self._branch[1]) or isinstance(self.branch, list) or belongs_to_parent)):
            dct["branch"] = dictify(self.branch)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._time = (self._time[0], True)
        self._branch = (self._branch[0], True)

    def is_dirty(self):
        return any([self._time[1], self._branch[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSSourceDataTimestampParameters):
            return False
        return super(JSSourceDataTimestampParameters, self).__eq__(other) and \
               self.time == other.time and \
               self.branch == other.branch

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def time(self):
        """
        The time that will be used to find provisionable timestamps for the
        sources in the branch's data layout.

        :rtype: ``TEXT_TYPE``
        """
        return self._time[0]

    @time.setter
    def time(self, value):
        self._time = (value, True)

    @property
    def branch(self):
        """
        A reference to the Jet Stream branch.

        :rtype: ``TEXT_TYPE``
        """
        return self._branch[0]

    @branch.setter
    def branch(self, value):
        self._branch = (value, True)

