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
#     /delphix-oracle-cluster-node-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_2 import factory
from delphixpy.v1_5_2 import common

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

class OracleClusterNodeCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_5_2.web.vo.TypedObject` *)* The parameters used
    for oracle cluster node operations.
    """
    def __init__(self, undef_enabled=True):
        super(OracleClusterNodeCreateParameters, self).__init__()
        self._type = ("OracleClusterNodeCreateParameters", True)
        self._cluster = (self.__undef__, True)
        self._host_parameters = (self.__undef__, True)
        self._name = (self.__undef__, True)
        self._virtual_i_ps = (self.__undef__, True)

    API_VERSION = "1.5.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleClusterNodeCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._cluster = (data.get("cluster", obj.__undef__), dirty)
        if obj._cluster[0] is not None and obj._cluster[0] is not obj.__undef__:
            assert isinstance(obj._cluster[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cluster[0], type(obj._cluster[0])))
            common.validate_format(obj._cluster[0], "objectReference", None, None)
        if "hostParameters" in data and data["hostParameters"] is not None:
            obj._host_parameters = (factory.create_object(data["hostParameters"], "HostCreateParameters"), dirty)
            factory.validate_type(obj._host_parameters[0], "HostCreateParameters")
        else:
            obj._host_parameters = (obj.__undef__, dirty)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        obj._virtual_i_ps = []
        for item in data.get("virtualIPs") or []:
            obj._virtual_i_ps.append(factory.create_object(item))
            factory.validate_type(obj._virtual_i_ps[-1], "OracleVirtualIP")
        obj._virtual_i_ps = (obj._virtual_i_ps, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleClusterNodeCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cluster" == "type" or (self.cluster is not self.__undef__ and (not (dirty and not self._cluster[1]) or isinstance(self.cluster, list) or belongs_to_parent)):
            dct["cluster"] = dictify(self.cluster)
        if "host_parameters" == "type" or (self.host_parameters is not self.__undef__ and (not (dirty and not self._host_parameters[1]) or isinstance(self.host_parameters, list) or belongs_to_parent)):
            dct["hostParameters"] = dictify(self.host_parameters, prop_is_list_or_vo=True)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "virtual_i_ps" == "type" or (self.virtual_i_ps is not self.__undef__ and (not (dirty and not self._virtual_i_ps[1]) or isinstance(self.virtual_i_ps, list) or belongs_to_parent)):
            dct["virtualIPs"] = dictify(self.virtual_i_ps, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cluster = (self._cluster[0], True)
        self._host_parameters = (self._host_parameters[0], True)
        self._name = (self._name[0], True)
        self._virtual_i_ps = (self._virtual_i_ps[0], True)

    def is_dirty(self):
        return any([self._cluster[1], self._host_parameters[1], self._name[1], self._virtual_i_ps[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleClusterNodeCreateParameters):
            return False
        return super(OracleClusterNodeCreateParameters, self).__eq__(other) and \
               self.cluster == other.cluster and \
               self.host_parameters == other.host_parameters and \
               self.name == other.name and \
               self.virtual_i_ps == other.virtual_i_ps

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cluster(self):
        """
        The cluster to which the node belongs.

        :rtype: ``TEXT_TYPE``
        """
        return self._cluster[0]

    @cluster.setter
    def cluster(self, value):
        self._cluster = (value, True)

    @property
    def host_parameters(self):
        """
        The host object associated with the cluster node.

        :rtype: :py:class:`v1_5_2.web.vo.HostCreateParameters`
        """
        return self._host_parameters[0]

    @host_parameters.setter
    def host_parameters(self, value):
        self._host_parameters = (value, True)

    @property
    def name(self):
        """
        The name of the cluster node.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def virtual_i_ps(self):
        """
        The list of virtual IPs belonging to this node.

        :rtype: ``list`` of :py:class:`v1_5_2.web.vo.OracleVirtualIP`
        """
        return self._virtual_i_ps[0]

    @virtual_i_ps.setter
    def virtual_i_ps(self, value):
        self._virtual_i_ps = (value, True)

