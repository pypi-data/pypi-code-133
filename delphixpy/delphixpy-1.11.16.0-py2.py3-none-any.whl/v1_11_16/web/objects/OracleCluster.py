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
#     /delphix-oracle-cluster.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.SourceEnvironment import SourceEnvironment
from delphixpy.v1_11_16 import common

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

class OracleCluster(SourceEnvironment):
    """
    *(extends* :py:class:`v1_11_16.web.vo.SourceEnvironment` *)* The
    representation of an oracle cluster environment object.
    """
    def __init__(self, undef_enabled=True):
        super(OracleCluster, self).__init__()
        self._type = ("OracleCluster", True)
        self._cluster_user = (self.__undef__, True)
        self._crs_cluster_name = (self.__undef__, True)
        self._crs_cluster_home = (self.__undef__, True)
        self._remote_listener = (self.__undef__, True)
        self._scan = (self.__undef__, True)
        self._scan_manual = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleCluster, cls).from_dict(data, dirty, undef_enabled)
        obj._cluster_user = (data.get("clusterUser", obj.__undef__), dirty)
        if obj._cluster_user[0] is not None and obj._cluster_user[0] is not obj.__undef__:
            assert isinstance(obj._cluster_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cluster_user[0], type(obj._cluster_user[0])))
            common.validate_format(obj._cluster_user[0], "objectReference", None, None)
        obj._crs_cluster_name = (data.get("crsClusterName", obj.__undef__), dirty)
        if obj._crs_cluster_name[0] is not None and obj._crs_cluster_name[0] is not obj.__undef__:
            assert isinstance(obj._crs_cluster_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._crs_cluster_name[0], type(obj._crs_cluster_name[0])))
            common.validate_format(obj._crs_cluster_name[0], "None", None, 15)
        obj._crs_cluster_home = (data.get("crsClusterHome", obj.__undef__), dirty)
        if obj._crs_cluster_home[0] is not None and obj._crs_cluster_home[0] is not obj.__undef__:
            assert isinstance(obj._crs_cluster_home[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._crs_cluster_home[0], type(obj._crs_cluster_home[0])))
            common.validate_format(obj._crs_cluster_home[0], "None", None, 256)
        obj._remote_listener = (data.get("remoteListener", obj.__undef__), dirty)
        if obj._remote_listener[0] is not None and obj._remote_listener[0] is not obj.__undef__:
            assert isinstance(obj._remote_listener[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._remote_listener[0], type(obj._remote_listener[0])))
            common.validate_format(obj._remote_listener[0], "None", None, 256)
        obj._scan = (data.get("scan", obj.__undef__), dirty)
        if obj._scan[0] is not None and obj._scan[0] is not obj.__undef__:
            assert isinstance(obj._scan[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._scan[0], type(obj._scan[0])))
            common.validate_format(obj._scan[0], "None", None, 256)
        obj._scan_manual = (data.get("scanManual", obj.__undef__), dirty)
        if obj._scan_manual[0] is not None and obj._scan_manual[0] is not obj.__undef__:
            assert isinstance(obj._scan_manual[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._scan_manual[0], type(obj._scan_manual[0])))
            common.validate_format(obj._scan_manual[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleCluster, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cluster_user" == "type" or (self.cluster_user is not self.__undef__ and (not (dirty and not self._cluster_user[1]) or isinstance(self.cluster_user, list) or belongs_to_parent)):
            dct["clusterUser"] = dictify(self.cluster_user)
        if "crs_cluster_name" == "type" or (self.crs_cluster_name is not self.__undef__ and (not (dirty and not self._crs_cluster_name[1]) or isinstance(self.crs_cluster_name, list) or belongs_to_parent)):
            dct["crsClusterName"] = dictify(self.crs_cluster_name)
        if "crs_cluster_home" == "type" or (self.crs_cluster_home is not self.__undef__ and (not (dirty and not self._crs_cluster_home[1]) or isinstance(self.crs_cluster_home, list) or belongs_to_parent)):
            dct["crsClusterHome"] = dictify(self.crs_cluster_home)
        if "remote_listener" == "type" or (self.remote_listener is not self.__undef__ and (not (dirty and not self._remote_listener[1]) or isinstance(self.remote_listener, list) or belongs_to_parent)):
            dct["remoteListener"] = dictify(self.remote_listener)
        if "scan" == "type" or (self.scan is not self.__undef__ and (not (dirty and not self._scan[1]) or isinstance(self.scan, list) or belongs_to_parent)):
            dct["scan"] = dictify(self.scan)
        if "scan_manual" == "type" or (self.scan_manual is not self.__undef__ and (not (dirty and not self._scan_manual[1]))):
            dct["scanManual"] = dictify(self.scan_manual)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cluster_user = (self._cluster_user[0], True)
        self._crs_cluster_name = (self._crs_cluster_name[0], True)
        self._crs_cluster_home = (self._crs_cluster_home[0], True)
        self._remote_listener = (self._remote_listener[0], True)
        self._scan = (self._scan[0], True)
        self._scan_manual = (self._scan_manual[0], True)

    def is_dirty(self):
        return any([self._cluster_user[1], self._crs_cluster_name[1], self._crs_cluster_home[1], self._remote_listener[1], self._scan[1], self._scan_manual[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleCluster):
            return False
        return super(OracleCluster, self).__eq__(other) and \
               self.cluster_user == other.cluster_user and \
               self.crs_cluster_name == other.crs_cluster_name and \
               self.crs_cluster_home == other.crs_cluster_home and \
               self.remote_listener == other.remote_listener and \
               self.scan == other.scan and \
               self.scan_manual == other.scan_manual

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cluster_user(self):
        """
        A reference to the cluster user.

        :rtype: ``TEXT_TYPE``
        """
        return self._cluster_user[0]

    @cluster_user.setter
    def cluster_user(self, value):
        self._cluster_user = (value, True)

    @property
    def crs_cluster_name(self):
        """
        The name of the cluster.

        :rtype: ``TEXT_TYPE``
        """
        return self._crs_cluster_name[0]

    @crs_cluster_name.setter
    def crs_cluster_name(self, value):
        self._crs_cluster_name = (value, True)

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

    @property
    def scan_manual(self):
        """
        Indicates whether the Single Client Access Name of the cluster is
        manually configured.

        :rtype: ``bool``
        """
        return self._scan_manual[0]

    @scan_manual.setter
    def scan_manual(self, value):
        self._scan_manual = (value, True)

