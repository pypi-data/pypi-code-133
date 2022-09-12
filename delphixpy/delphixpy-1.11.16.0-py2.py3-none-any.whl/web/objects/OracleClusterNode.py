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
#     /delphix-oracle-cluster-node.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.NamedUserObject import NamedUserObject
from delphixpy import factory
from delphixpy import common

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

class OracleClusterNode(NamedUserObject):
    """
    *(extends* :py:class:`delphixpy.web.vo.NamedUserObject` *)* The
    representation of an oracle cluster node object.
    """
    def __init__(self, undef_enabled=True):
        super(OracleClusterNode, self).__init__()
        self._type = ("OracleClusterNode", True)
        self._cluster = (self.__undef__, True)
        self._host = (self.__undef__, True)
        self._virtual_i_ps = (self.__undef__, True)
        self._discovered = (self.__undef__, True)
        self._enabled = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleClusterNode, cls).from_dict(data, dirty, undef_enabled)
        obj._cluster = (data.get("cluster", obj.__undef__), dirty)
        if obj._cluster[0] is not None and obj._cluster[0] is not obj.__undef__:
            assert isinstance(obj._cluster[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cluster[0], type(obj._cluster[0])))
            common.validate_format(obj._cluster[0], "objectReference", None, None)
        obj._host = (data.get("host", obj.__undef__), dirty)
        if obj._host[0] is not None and obj._host[0] is not obj.__undef__:
            assert isinstance(obj._host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._host[0], type(obj._host[0])))
            common.validate_format(obj._host[0], "objectReference", None, None)
        obj._virtual_i_ps = []
        for item in data.get("virtualIPs") or []:
            obj._virtual_i_ps.append(factory.create_object(item))
            factory.validate_type(obj._virtual_i_ps[-1], "OracleVirtualIP")
        obj._virtual_i_ps = (obj._virtual_i_ps, dirty)
        obj._discovered = (data.get("discovered", obj.__undef__), dirty)
        if obj._discovered[0] is not None and obj._discovered[0] is not obj.__undef__:
            assert isinstance(obj._discovered[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._discovered[0], type(obj._discovered[0])))
            common.validate_format(obj._discovered[0], "None", None, None)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleClusterNode, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cluster" == "type" or (self.cluster is not self.__undef__ and (not (dirty and not self._cluster[1]))):
            dct["cluster"] = dictify(self.cluster)
        if "host" == "type" or (self.host is not self.__undef__ and (not (dirty and not self._host[1]))):
            dct["host"] = dictify(self.host)
        if "virtual_i_ps" == "type" or (self.virtual_i_ps is not self.__undef__ and (not (dirty and not self._virtual_i_ps[1]) or isinstance(self.virtual_i_ps, list) or belongs_to_parent)):
            dct["virtualIPs"] = dictify(self.virtual_i_ps, prop_is_list_or_vo=True)
        if "discovered" == "type" or (self.discovered is not self.__undef__ and (not (dirty and not self._discovered[1]))):
            dct["discovered"] = dictify(self.discovered)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]) or isinstance(self.enabled, list) or belongs_to_parent)):
            dct["enabled"] = dictify(self.enabled)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cluster = (self._cluster[0], True)
        self._host = (self._host[0], True)
        self._virtual_i_ps = (self._virtual_i_ps[0], True)
        self._discovered = (self._discovered[0], True)
        self._enabled = (self._enabled[0], True)

    def is_dirty(self):
        return any([self._cluster[1], self._host[1], self._virtual_i_ps[1], self._discovered[1], self._enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleClusterNode):
            return False
        return super(OracleClusterNode, self).__eq__(other) and \
               self.cluster == other.cluster and \
               self.host == other.host and \
               self.virtual_i_ps == other.virtual_i_ps and \
               self.discovered == other.discovered and \
               self.enabled == other.enabled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cluster(self):
        """
        The reference to the parent cluster environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._cluster[0]

    @cluster.setter
    def cluster(self, value):
        self._cluster = (value, True)

    @property
    def host(self):
        """
        The reference to the associated host object.

        :rtype: ``TEXT_TYPE``
        """
        return self._host[0]

    @host.setter
    def host(self, value):
        self._host = (value, True)

    @property
    def virtual_i_ps(self):
        """
        The list of virtual IPs belonging to this node.

        :rtype: ``list`` of :py:class:`delphixpy.web.vo.OracleVirtualIP`
        """
        return self._virtual_i_ps[0]

    @virtual_i_ps.setter
    def virtual_i_ps(self, value):
        self._virtual_i_ps = (value, True)

    @property
    def discovered(self):
        """
        Indicates whether the node is discovered.

        :rtype: ``bool``
        """
        return self._discovered[0]

    @discovered.setter
    def discovered(self, value):
        self._discovered = (value, True)

    @property
    def enabled(self):
        """
        Indicates whether the node is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

