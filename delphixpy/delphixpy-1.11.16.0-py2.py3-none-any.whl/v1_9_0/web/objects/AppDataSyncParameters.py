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
#     /delphix-appdata-sync-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_0.web.objects.SyncParameters import SyncParameters
from delphixpy.v1_9_0 import common

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

class AppDataSyncParameters(SyncParameters):
    """
    *(extends* :py:class:`v1_9_0.web.vo.SyncParameters` *)* The parameters to
    use as input to sync an AppData source.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataSyncParameters, self).__init__()
        self._type = ("AppDataSyncParameters", True)
        self._resync = (self.__undef__, True)

    API_VERSION = "1.9.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataSyncParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._resync = (data.get("resync", obj.__undef__), dirty)
        if obj._resync[0] is not None and obj._resync[0] is not obj.__undef__:
            assert isinstance(obj._resync[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._resync[0], type(obj._resync[0])))
            common.validate_format(obj._resync[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataSyncParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "resync" == "type" or (self.resync is not self.__undef__ and (not (dirty and not self._resync[1]))):
            dct["resync"] = dictify(self.resync)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._resync = (self._resync[0], True)

    def is_dirty(self):
        return any([self._resync[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataSyncParameters):
            return False
        return super(AppDataSyncParameters, self).__eq__(other) and \
               self.resync == other.resync

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def resync(self):
        """
        Whether or not to force a non-incremental load of data prior to taking
        a snapshot.

        :rtype: ``bool``
        """
        return self._resync[0]

    @resync.setter
    def resync(self, value):
        self._resync = (value, True)

