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
#     /delphix-oracle-custom-env-var-rac-file.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.OracleCustomEnvVarFile import OracleCustomEnvVarFile
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

class OracleCustomEnvVarRACFile(OracleCustomEnvVarFile):
    """
    *(extends* :py:class:`v1_11_0.web.vo.OracleCustomEnvVarFile` *)* Dictates
    an environment file to be sourced when the Delphix Engine administers an
    Oracle virtual database. This environment file must be available on the
    target environment. This type also includes parameters which will be passed
    to the environment file when it is sourced. For a RAC environment, the
    cluster node where the target environment file exists must also be
    specified.
    """
    def __init__(self, undef_enabled=True):
        super(OracleCustomEnvVarRACFile, self).__init__()
        self._type = ("OracleCustomEnvVarRACFile", True)
        self._cluster_node = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleCustomEnvVarRACFile, cls).from_dict(data, dirty, undef_enabled)
        if "clusterNode" not in data:
            raise ValueError("Missing required property \"clusterNode\".")
        obj._cluster_node = (data.get("clusterNode", obj.__undef__), dirty)
        if obj._cluster_node[0] is not None and obj._cluster_node[0] is not obj.__undef__:
            assert isinstance(obj._cluster_node[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cluster_node[0], type(obj._cluster_node[0])))
            common.validate_format(obj._cluster_node[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleCustomEnvVarRACFile, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cluster_node" == "type" or (self.cluster_node is not self.__undef__ and (not (dirty and not self._cluster_node[1]) or isinstance(self.cluster_node, list) or belongs_to_parent)):
            dct["clusterNode"] = dictify(self.cluster_node)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cluster_node = (self._cluster_node[0], True)

    def is_dirty(self):
        return any([self._cluster_node[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleCustomEnvVarRACFile):
            return False
        return super(OracleCustomEnvVarRACFile, self).__eq__(other) and \
               self.cluster_node == other.cluster_node

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cluster_node(self):
        """
        The cluster node on which the target environment file exists.

        :rtype: ``TEXT_TYPE``
        """
        return self._cluster_node[0]

    @cluster_node.setter
    def cluster_node(self, value):
        self._cluster_node = (value, True)

