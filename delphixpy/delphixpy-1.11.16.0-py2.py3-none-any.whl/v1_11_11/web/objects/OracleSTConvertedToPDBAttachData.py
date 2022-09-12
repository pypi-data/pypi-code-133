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
#     /delphix-oracle-st-converted-to-pdb-attach-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.OraclePDBAttachData import OraclePDBAttachData
from delphixpy.v1_11_11 import common

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

class OracleSTConvertedToPDBAttachData(OraclePDBAttachData):
    """
    *(extends* :py:class:`v1_11_11.web.vo.OraclePDBAttachData` *)* Represents
    parameters necessary to attach a single-tenant dSource that has been
    converted (migrated from non-mt) to an Oracle PDB.
    """
    def __init__(self, undef_enabled=True):
        super(OracleSTConvertedToPDBAttachData, self).__init__()
        self._type = ("OracleSTConvertedToPDBAttachData", True)
        self._new_pdb_container_name = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleSTConvertedToPDBAttachData, cls).from_dict(data, dirty, undef_enabled)
        obj._new_pdb_container_name = (data.get("newPdbContainerName", obj.__undef__), dirty)
        if obj._new_pdb_container_name[0] is not None and obj._new_pdb_container_name[0] is not obj.__undef__:
            assert isinstance(obj._new_pdb_container_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._new_pdb_container_name[0], type(obj._new_pdb_container_name[0])))
            common.validate_format(obj._new_pdb_container_name[0], "None", None, 256)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleSTConvertedToPDBAttachData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "new_pdb_container_name" == "type" or (self.new_pdb_container_name is not self.__undef__ and (not (dirty and not self._new_pdb_container_name[1]) or isinstance(self.new_pdb_container_name, list) or belongs_to_parent)):
            dct["newPdbContainerName"] = dictify(self.new_pdb_container_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._new_pdb_container_name = (self._new_pdb_container_name[0], True)

    def is_dirty(self):
        return any([self._new_pdb_container_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleSTConvertedToPDBAttachData):
            return False
        return super(OracleSTConvertedToPDBAttachData, self).__eq__(other) and \
               self.new_pdb_container_name == other.new_pdb_container_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def new_pdb_container_name(self):
        """
        If provided it will be used to name the new container, otherwise the
        name of the single tenant container will be used.

        :rtype: ``TEXT_TYPE``
        """
        return self._new_pdb_container_name[0]

    @new_pdb_container_name.setter
    def new_pdb_container_name(self, value):
        self._new_pdb_container_name = (value, True)

