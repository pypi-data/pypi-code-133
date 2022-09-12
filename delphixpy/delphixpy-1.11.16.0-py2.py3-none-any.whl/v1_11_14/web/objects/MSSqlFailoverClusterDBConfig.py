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
#     /delphix-mssql-failover-cluster-db-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_14.web.objects.MSSqlDBConfig import MSSqlDBConfig
from delphixpy.v1_11_14 import common

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

class MSSqlFailoverClusterDBConfig(MSSqlDBConfig):
    """
    *(extends* :py:class:`v1_11_14.web.vo.MSSqlDBConfig` *)* Database for a SQL
    Server Failover Cluster.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlFailoverClusterDBConfig, self).__init__()
        self._type = ("MSSqlFailoverClusterDBConfig", True)
        self._drive_letter = (self.__undef__, True)
        self._linking_enabled = (self.__undef__, True)

    API_VERSION = "1.11.14"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlFailoverClusterDBConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._drive_letter = (data.get("driveLetter", obj.__undef__), dirty)
        if obj._drive_letter[0] is not None and obj._drive_letter[0] is not obj.__undef__:
            assert isinstance(obj._drive_letter[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._drive_letter[0], type(obj._drive_letter[0])))
            common.validate_format(obj._drive_letter[0], "None", 1, 1)
        obj._linking_enabled = (data.get("linkingEnabled", obj.__undef__), dirty)
        if obj._linking_enabled[0] is not None and obj._linking_enabled[0] is not obj.__undef__:
            assert isinstance(obj._linking_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._linking_enabled[0], type(obj._linking_enabled[0])))
            common.validate_format(obj._linking_enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlFailoverClusterDBConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "drive_letter" == "type" or (self.drive_letter is not self.__undef__ and (not (dirty and not self._drive_letter[1]) or isinstance(self.drive_letter, list) or belongs_to_parent)):
            dct["driveLetter"] = dictify(self.drive_letter)
        if "linking_enabled" == "type" or (self.linking_enabled is not self.__undef__ and (not (dirty and not self._linking_enabled[1]))):
            dct["linkingEnabled"] = dictify(self.linking_enabled)
        if dirty and "linkingEnabled" in dct:
            del dct["linkingEnabled"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._drive_letter = (self._drive_letter[0], True)
        self._linking_enabled = (self._linking_enabled[0], True)

    def is_dirty(self):
        return any([self._drive_letter[1], self._linking_enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlFailoverClusterDBConfig):
            return False
        return super(MSSqlFailoverClusterDBConfig, self).__eq__(other) and \
               self.drive_letter == other.drive_letter and \
               self.linking_enabled == other.linking_enabled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def drive_letter(self):
        """
        Base drive letter location for mount points.

        :rtype: ``TEXT_TYPE``
        """
        return self._drive_letter[0]

    @drive_letter.setter
    def drive_letter(self, value):
        self._drive_letter = (value, True)

    @property
    def linking_enabled(self):
        """
        Whether this source should be used for linking.

        :rtype: ``bool``
        """
        return self._linking_enabled[0]

