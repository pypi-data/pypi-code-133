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
#     /delphix-oracle-db-container-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_10.web.objects.DBContainerRuntime import DBContainerRuntime
from delphixpy.v1_11_10 import common

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

class OracleDBContainerRuntime(DBContainerRuntime):
    """
    *(extends* :py:class:`v1_11_10.web.vo.DBContainerRuntime` *)* Runtime
    properties of an Oracle database container.
    """
    def __init__(self, undef_enabled=True):
        super(OracleDBContainerRuntime, self).__init__()
        self._type = ("OracleDBContainerRuntime", True)
        self._live_source_eligible = (self.__undef__, True)

    API_VERSION = "1.11.10"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleDBContainerRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._live_source_eligible = (data.get("liveSourceEligible", obj.__undef__), dirty)
        if obj._live_source_eligible[0] is not None and obj._live_source_eligible[0] is not obj.__undef__:
            assert isinstance(obj._live_source_eligible[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._live_source_eligible[0], type(obj._live_source_eligible[0])))
            common.validate_format(obj._live_source_eligible[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleDBContainerRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "live_source_eligible" == "type" or (self.live_source_eligible is not self.__undef__ and (not (dirty and not self._live_source_eligible[1]))):
            dct["liveSourceEligible"] = dictify(self.live_source_eligible)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._live_source_eligible = (self._live_source_eligible[0], True)

    def is_dirty(self):
        return any([self._live_source_eligible[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleDBContainerRuntime):
            return False
        return super(OracleDBContainerRuntime, self).__eq__(other) and \
               self.live_source_eligible == other.live_source_eligible

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def live_source_eligible(self):
        """
        Indicates whether or not a LiveSource can be added to the given
        container.

        :rtype: ``bool``
        """
        return self._live_source_eligible[0]

    @live_source_eligible.setter
    def live_source_eligible(self, value):
        self._live_source_eligible = (value, True)

