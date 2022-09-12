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
#     /delphix-mysql-gtid-coordinates.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.MySQLReplicationCoordinates import MySQLReplicationCoordinates
from delphixpy.v1_11_0 import common

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

class MySQLGtidCoordinates(MySQLReplicationCoordinates):
    """
    *(extends* :py:class:`v1_11_0.web.vo.MySQLReplicationCoordinates` *)* The
    GTID coordinates on the master when a MySQL backup was taken.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLGtidCoordinates, self).__init__()
        self._type = ("MySQLGtidCoordinates", True)
        self._gtids = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLGtidCoordinates, cls).from_dict(data, dirty, undef_enabled)
        if "gtids" not in data:
            raise ValueError("Missing required property \"gtids\".")
        obj._gtids = []
        for item in data.get("gtids") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._gtids.append(item)
        obj._gtids = (obj._gtids, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLGtidCoordinates, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "gtids" == "type" or (self.gtids is not self.__undef__ and (not (dirty and not self._gtids[1]) or isinstance(self.gtids, list) or belongs_to_parent)):
            dct["gtids"] = dictify(self.gtids, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._gtids = (self._gtids[0], True)

    def is_dirty(self):
        return any([self._gtids[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLGtidCoordinates):
            return False
        return super(MySQLGtidCoordinates, self).__eq__(other) and \
               self.gtids == other.gtids

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def gtids(self):
        """
        The GTID coordinates on the master to start replication from.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._gtids[0]

    @gtids.setter
    def gtids(self, value):
        self._gtids = (value, True)

