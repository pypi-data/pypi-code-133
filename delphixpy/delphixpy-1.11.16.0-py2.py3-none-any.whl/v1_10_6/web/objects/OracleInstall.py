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
#     /delphix-oracle-install.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.SourceRepository import SourceRepository
from delphixpy.v1_10_6 import common

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

class OracleInstall(SourceRepository):
    """
    *(extends* :py:class:`v1_10_6.web.vo.SourceRepository` *)* The Oracle
    source repository.
    """
    def __init__(self, undef_enabled=True):
        super(OracleInstall, self).__init__()
        self._type = ("OracleInstall", True)
        self._installation_home = (self.__undef__, True)
        self._oracle_base = (self.__undef__, True)
        self._version = (self.__undef__, True)
        self._group_name = (self.__undef__, True)
        self._group_id = (self.__undef__, True)
        self._user_name = (self.__undef__, True)
        self._user_id = (self.__undef__, True)
        self._bits = (self.__undef__, True)
        self._rac = (self.__undef__, True)
        self._discovered = (self.__undef__, True)
        self._logsync_possible = (self.__undef__, True)
        self._applied_patches = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleInstall, cls).from_dict(data, dirty, undef_enabled)
        obj._installation_home = (data.get("installationHome", obj.__undef__), dirty)
        if obj._installation_home[0] is not None and obj._installation_home[0] is not obj.__undef__:
            assert isinstance(obj._installation_home[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._installation_home[0], type(obj._installation_home[0])))
            common.validate_format(obj._installation_home[0], "None", None, 256)
        obj._oracle_base = (data.get("oracleBase", obj.__undef__), dirty)
        if obj._oracle_base[0] is not None and obj._oracle_base[0] is not obj.__undef__:
            assert isinstance(obj._oracle_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._oracle_base[0], type(obj._oracle_base[0])))
            common.validate_format(obj._oracle_base[0], "None", None, 256)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "oracleVersion", None, None)
        obj._group_name = (data.get("groupName", obj.__undef__), dirty)
        if obj._group_name[0] is not None and obj._group_name[0] is not obj.__undef__:
            assert isinstance(obj._group_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._group_name[0], type(obj._group_name[0])))
            common.validate_format(obj._group_name[0], "None", None, None)
        obj._group_id = (data.get("groupId", obj.__undef__), dirty)
        if obj._group_id[0] is not None and obj._group_id[0] is not obj.__undef__:
            assert isinstance(obj._group_id[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._group_id[0], type(obj._group_id[0])))
            common.validate_format(obj._group_id[0], "None", None, None)
        obj._user_name = (data.get("userName", obj.__undef__), dirty)
        if obj._user_name[0] is not None and obj._user_name[0] is not obj.__undef__:
            assert isinstance(obj._user_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user_name[0], type(obj._user_name[0])))
            common.validate_format(obj._user_name[0], "None", None, None)
        obj._user_id = (data.get("userId", obj.__undef__), dirty)
        if obj._user_id[0] is not None and obj._user_id[0] is not obj.__undef__:
            assert isinstance(obj._user_id[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._user_id[0], type(obj._user_id[0])))
            common.validate_format(obj._user_id[0], "None", None, None)
        obj._bits = (data.get("bits", obj.__undef__), dirty)
        if obj._bits[0] is not None and obj._bits[0] is not obj.__undef__:
            assert isinstance(obj._bits[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._bits[0], type(obj._bits[0])))
            assert obj._bits[0] in [32, 64], "Expected enum [32, 64] but got %s" % obj._bits[0]
            common.validate_format(obj._bits[0], "None", None, None)
        obj._rac = (data.get("rac", obj.__undef__), dirty)
        if obj._rac[0] is not None and obj._rac[0] is not obj.__undef__:
            assert isinstance(obj._rac[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._rac[0], type(obj._rac[0])))
            common.validate_format(obj._rac[0], "None", None, None)
        obj._discovered = (data.get("discovered", obj.__undef__), dirty)
        if obj._discovered[0] is not None and obj._discovered[0] is not obj.__undef__:
            assert isinstance(obj._discovered[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._discovered[0], type(obj._discovered[0])))
            common.validate_format(obj._discovered[0], "None", None, None)
        obj._logsync_possible = (data.get("logsyncPossible", obj.__undef__), dirty)
        if obj._logsync_possible[0] is not None and obj._logsync_possible[0] is not obj.__undef__:
            assert isinstance(obj._logsync_possible[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._logsync_possible[0], type(obj._logsync_possible[0])))
            common.validate_format(obj._logsync_possible[0], "None", None, None)
        obj._applied_patches = []
        for item in data.get("appliedPatches") or []:
            assert isinstance(item, int), ("Expected one of ['integer'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._applied_patches.append(item)
        obj._applied_patches = (obj._applied_patches, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleInstall, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "installation_home" == "type" or (self.installation_home is not self.__undef__ and (not (dirty and not self._installation_home[1]) or isinstance(self.installation_home, list) or belongs_to_parent)):
            dct["installationHome"] = dictify(self.installation_home)
        if "oracle_base" == "type" or (self.oracle_base is not self.__undef__ and (not (dirty and not self._oracle_base[1]) or isinstance(self.oracle_base, list) or belongs_to_parent)):
            dct["oracleBase"] = dictify(self.oracle_base)
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]) or isinstance(self.version, list) or belongs_to_parent)):
            dct["version"] = dictify(self.version)
        if "group_name" == "type" or (self.group_name is not self.__undef__ and (not (dirty and not self._group_name[1]))):
            dct["groupName"] = dictify(self.group_name)
        if "group_id" == "type" or (self.group_id is not self.__undef__ and (not (dirty and not self._group_id[1]))):
            dct["groupId"] = dictify(self.group_id)
        if "user_name" == "type" or (self.user_name is not self.__undef__ and (not (dirty and not self._user_name[1]))):
            dct["userName"] = dictify(self.user_name)
        if "user_id" == "type" or (self.user_id is not self.__undef__ and (not (dirty and not self._user_id[1]))):
            dct["userId"] = dictify(self.user_id)
        if "bits" == "type" or (self.bits is not self.__undef__ and (not (dirty and not self._bits[1]) or isinstance(self.bits, list) or belongs_to_parent)):
            dct["bits"] = dictify(self.bits)
        if "rac" == "type" or (self.rac is not self.__undef__ and (not (dirty and not self._rac[1]))):
            dct["rac"] = dictify(self.rac)
        if "discovered" == "type" or (self.discovered is not self.__undef__ and (not (dirty and not self._discovered[1]))):
            dct["discovered"] = dictify(self.discovered)
        if "logsync_possible" == "type" or (self.logsync_possible is not self.__undef__ and (not (dirty and not self._logsync_possible[1]))):
            dct["logsyncPossible"] = dictify(self.logsync_possible)
        if "applied_patches" == "type" or (self.applied_patches is not self.__undef__ and (not (dirty and not self._applied_patches[1]) or isinstance(self.applied_patches, list) or belongs_to_parent)):
            dct["appliedPatches"] = dictify(self.applied_patches, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._installation_home = (self._installation_home[0], True)
        self._oracle_base = (self._oracle_base[0], True)
        self._version = (self._version[0], True)
        self._group_name = (self._group_name[0], True)
        self._group_id = (self._group_id[0], True)
        self._user_name = (self._user_name[0], True)
        self._user_id = (self._user_id[0], True)
        self._bits = (self._bits[0], True)
        self._rac = (self._rac[0], True)
        self._discovered = (self._discovered[0], True)
        self._logsync_possible = (self._logsync_possible[0], True)
        self._applied_patches = (self._applied_patches[0], True)

    def is_dirty(self):
        return any([self._installation_home[1], self._oracle_base[1], self._version[1], self._group_name[1], self._group_id[1], self._user_name[1], self._user_id[1], self._bits[1], self._rac[1], self._discovered[1], self._logsync_possible[1], self._applied_patches[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleInstall):
            return False
        return super(OracleInstall, self).__eq__(other) and \
               self.installation_home == other.installation_home and \
               self.oracle_base == other.oracle_base and \
               self.version == other.version and \
               self.group_name == other.group_name and \
               self.group_id == other.group_id and \
               self.user_name == other.user_name and \
               self.user_id == other.user_id and \
               self.bits == other.bits and \
               self.rac == other.rac and \
               self.discovered == other.discovered and \
               self.logsync_possible == other.logsync_possible and \
               self.applied_patches == other.applied_patches

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def installation_home(self):
        """
        The Oracle install home.

        :rtype: ``TEXT_TYPE``
        """
        return self._installation_home[0]

    @installation_home.setter
    def installation_home(self, value):
        self._installation_home = (value, True)

    @property
    def oracle_base(self):
        """
        The Oracle base where database binaries are located.

        :rtype: ``TEXT_TYPE``
        """
        return self._oracle_base[0]

    @oracle_base.setter
    def oracle_base(self, value):
        self._oracle_base = (value, True)

    @property
    def version(self):
        """
        Version of the repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

    @property
    def group_name(self):
        """
        Group name of the user that owns the install.

        :rtype: ``TEXT_TYPE``
        """
        return self._group_name[0]

    @group_name.setter
    def group_name(self, value):
        self._group_name = (value, True)

    @property
    def group_id(self):
        """
        Group ID of the user that owns the install.

        :rtype: ``int``
        """
        return self._group_id[0]

    @group_id.setter
    def group_id(self, value):
        self._group_id = (value, True)

    @property
    def user_name(self):
        """
        User name of the user that owns the install.

        :rtype: ``TEXT_TYPE``
        """
        return self._user_name[0]

    @user_name.setter
    def user_name(self, value):
        self._user_name = (value, True)

    @property
    def user_id(self):
        """
        User ID of the user that owns the install.

        :rtype: ``int``
        """
        return self._user_id[0]

    @user_id.setter
    def user_id(self, value):
        self._user_id = (value, True)

    @property
    def bits(self):
        """
        32 or 64 bits. *(permitted values: 32, 64)*

        :rtype: ``int``
        """
        return self._bits[0]

    @bits.setter
    def bits(self, value):
        self._bits = (value, True)

    @property
    def rac(self):
        """
        Flag indicating whether the install supports Oracle RAC.

        :rtype: ``bool``
        """
        return self._rac[0]

    @rac.setter
    def rac(self, value):
        self._rac = (value, True)

    @property
    def discovered(self):
        """
        Flag indicating whether the install was discovered or manually entered.

        :rtype: ``bool``
        """
        return self._discovered[0]

    @discovered.setter
    def discovered(self, value):
        self._discovered = (value, True)

    @property
    def logsync_possible(self):
        """
        Flag indicating whether this repository can use LogSync.

        :rtype: ``bool``
        """
        return self._logsync_possible[0]

    @logsync_possible.setter
    def logsync_possible(self, value):
        self._logsync_possible = (value, True)

    @property
    def applied_patches(self):
        """
        List of Oracle patches that have been applied to this Oracle Home.

        :rtype: ``list`` of ``int``
        """
        return self._applied_patches[0]

    @applied_patches.setter
    def applied_patches(self, value):
        self._applied_patches = (value, True)

