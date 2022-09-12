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
#     /delphix-oracle-link-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.OracleBaseLinkParameters import OracleBaseLinkParameters
from delphixpy.v1_4_3 import factory
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

class OracleLinkParameters(OracleBaseLinkParameters):
    """
    *(extends* :py:class:`v1_4_3.web.vo.OracleBaseLinkParameters` *)*
    Represents parameters to link non-pluggable Oracle databases.
    """
    def __init__(self, undef_enabled=True):
        super(OracleLinkParameters, self).__init__()
        self._type = ("OracleLinkParameters", True)
        self._non_sys_credentials = (self.__undef__, True)
        self._non_sys_user = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleLinkParameters, cls).from_dict(data, dirty, undef_enabled)
        if "nonSysCredentials" in data and data["nonSysCredentials"] is not None:
            obj._non_sys_credentials = (factory.create_object(data["nonSysCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._non_sys_credentials[0], "PasswordCredential")
        else:
            obj._non_sys_credentials = (obj.__undef__, dirty)
        obj._non_sys_user = (data.get("nonSysUser", obj.__undef__), dirty)
        if obj._non_sys_user[0] is not None and obj._non_sys_user[0] is not obj.__undef__:
            assert isinstance(obj._non_sys_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._non_sys_user[0], type(obj._non_sys_user[0])))
            common.validate_format(obj._non_sys_user[0], "None", None, 30)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleLinkParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "non_sys_credentials" == "type" or (self.non_sys_credentials is not self.__undef__ and (not (dirty and not self._non_sys_credentials[1]) or isinstance(self.non_sys_credentials, list) or belongs_to_parent)):
            dct["nonSysCredentials"] = dictify(self.non_sys_credentials, prop_is_list_or_vo=True)
        if "non_sys_user" == "type" or (self.non_sys_user is not self.__undef__ and (not (dirty and not self._non_sys_user[1]) or isinstance(self.non_sys_user, list) or belongs_to_parent)):
            dct["nonSysUser"] = dictify(self.non_sys_user)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._non_sys_credentials = (self._non_sys_credentials[0], True)
        self._non_sys_user = (self._non_sys_user[0], True)

    def is_dirty(self):
        return any([self._non_sys_credentials[1], self._non_sys_user[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleLinkParameters):
            return False
        return super(OracleLinkParameters, self).__eq__(other) and \
               self.non_sys_credentials == other.non_sys_credentials and \
               self.non_sys_user == other.non_sys_user

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def non_sys_credentials(self):
        """
        Non-SYS database credentials to access this database.

        :rtype: :py:class:`v1_4_3.web.vo.PasswordCredential`
        """
        return self._non_sys_credentials[0]

    @non_sys_credentials.setter
    def non_sys_credentials(self, value):
        self._non_sys_credentials = (value, True)

    @property
    def non_sys_user(self):
        """
        Non-SYS database user to access this database.

        :rtype: ``TEXT_TYPE``
        """
        return self._non_sys_user[0]

    @non_sys_user.setter
    def non_sys_user(self, value):
        self._non_sys_user = (value, True)

