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
#     /delphix-oracle-rac-source-connection-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.OracleSourceConnectionInfo import OracleSourceConnectionInfo
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

class OracleRACSourceConnectionInfo(OracleSourceConnectionInfo):
    """
    *(extends* :py:class:`v1_4_3.web.vo.OracleSourceConnectionInfo` *)*
    Contains information that can be used to connect to a single instance
    Oracle source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleRACSourceConnectionInfo, self).__init__()
        self._type = ("OracleRACSourceConnectionInfo", True)
        self._crs_cluster_home = (self.__undef__, True)
        self._nodes = (self.__undef__, True)
        self._remote_listener = (self.__undef__, True)
        self._scan = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleRACSourceConnectionInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._crs_cluster_home = (data.get("crsClusterHome", obj.__undef__), dirty)
        if obj._crs_cluster_home[0] is not None and obj._crs_cluster_home[0] is not obj.__undef__:
            assert isinstance(obj._crs_cluster_home[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._crs_cluster_home[0], type(obj._crs_cluster_home[0])))
            common.validate_format(obj._crs_cluster_home[0], "None", None, None)
        obj._nodes = []
        for item in data.get("nodes") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._nodes.append(item)
        obj._nodes = (obj._nodes, dirty)
        obj._remote_listener = (data.get("remoteListener", obj.__undef__), dirty)
        if obj._remote_listener[0] is not None and obj._remote_listener[0] is not obj.__undef__:
            assert isinstance(obj._remote_listener[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._remote_listener[0], type(obj._remote_listener[0])))
            common.validate_format(obj._remote_listener[0], "None", None, None)
        obj._scan = (data.get("scan", obj.__undef__), dirty)
        if obj._scan[0] is not None and obj._scan[0] is not obj.__undef__:
            assert isinstance(obj._scan[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._scan[0], type(obj._scan[0])))
            common.validate_format(obj._scan[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleRACSourceConnectionInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "crs_cluster_home" == "type" or (self.crs_cluster_home is not self.__undef__ and (not (dirty and not self._crs_cluster_home[1]))):
            dct["crsClusterHome"] = dictify(self.crs_cluster_home)
        if "nodes" == "type" or (self.nodes is not self.__undef__ and (not (dirty and not self._nodes[1]))):
            dct["nodes"] = dictify(self.nodes)
        if "remote_listener" == "type" or (self.remote_listener is not self.__undef__ and (not (dirty and not self._remote_listener[1]))):
            dct["remoteListener"] = dictify(self.remote_listener)
        if "scan" == "type" or (self.scan is not self.__undef__ and (not (dirty and not self._scan[1]))):
            dct["scan"] = dictify(self.scan)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._crs_cluster_home = (self._crs_cluster_home[0], True)
        self._nodes = (self._nodes[0], True)
        self._remote_listener = (self._remote_listener[0], True)
        self._scan = (self._scan[0], True)

    def is_dirty(self):
        return any([self._crs_cluster_home[1], self._nodes[1], self._remote_listener[1], self._scan[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleRACSourceConnectionInfo):
            return False
        return super(OracleRACSourceConnectionInfo, self).__eq__(other) and \
               self.crs_cluster_home == other.crs_cluster_home and \
               self.nodes == other.nodes and \
               self.remote_listener == other.remote_listener and \
               self.scan == other.scan

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def crs_cluster_home(self):
        """
        The location of the cluster installation.

        :rtype: ``TEXT_TYPE``
        """
        return self._crs_cluster_home[0]

    @crs_cluster_home.setter
    def crs_cluster_home(self, value):
        self._crs_cluster_home = (value, True)

    @property
    def nodes(self):
        """
        The addresses for the nodes on which the source resides.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._nodes[0]

    @nodes.setter
    def nodes(self, value):
        self._nodes = (value, True)

    @property
    def remote_listener(self):
        """
        The default remote_listener parameter to be used for databases on the
        cluster.

        :rtype: ``TEXT_TYPE``
        """
        return self._remote_listener[0]

    @remote_listener.setter
    def remote_listener(self, value):
        self._remote_listener = (value, True)

    @property
    def scan(self):
        """
        The Single Client Access Name of the cluster (11.2 and greater clusters
        only).

        :rtype: ``TEXT_TYPE``
        """
        return self._scan[0]

    @scan.setter
    def scan(self, value):
        self._scan = (value, True)

