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
#     /delphix-credentials-env-vars.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_9 import factory
from delphixpy.v1_11_9 import common

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

class CredentialsEnvVars(TypedObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.TypedObject` *)* Credentials to be
    placed in environment variables for an operation.
    """
    def __init__(self, undef_enabled=True):
        super(CredentialsEnvVars, self).__init__()
        self._type = ("CredentialsEnvVars", True)
        self._base_var_name = (self.__undef__, True)
        self._credentials = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CredentialsEnvVars, cls).from_dict(data, dirty, undef_enabled)
        obj._base_var_name = (data.get("baseVarName", obj.__undef__), dirty)
        if obj._base_var_name[0] is not None and obj._base_var_name[0] is not obj.__undef__:
            assert isinstance(obj._base_var_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._base_var_name[0], type(obj._base_var_name[0])))
            common.validate_format(obj._base_var_name[0], "None", None, None)
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "Credential"), dirty)
            factory.validate_type(obj._credentials[0], "Credential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CredentialsEnvVars, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "base_var_name" == "type" or (self.base_var_name is not self.__undef__ and (not (dirty and not self._base_var_name[1]) or isinstance(self.base_var_name, list) or belongs_to_parent)):
            dct["baseVarName"] = dictify(self.base_var_name)
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._base_var_name = (self._base_var_name[0], True)
        self._credentials = (self._credentials[0], True)

    def is_dirty(self):
        return any([self._base_var_name[1], self._credentials[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CredentialsEnvVars):
            return False
        return super(CredentialsEnvVars, self).__eq__(other) and \
               self.base_var_name == other.base_var_name and \
               self.credentials == other.credentials

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def base_var_name(self):
        """
        Base name of the environment variables. Variables are named by
        appending '_USER', '_PASSWORD', '_PUBKEY' and '_PRIVKEY' to this base
        name, respectively. Variables whose values are not entered or are not
        present in the type of credential or vault selected, will not be set.

        :rtype: ``TEXT_TYPE``
        """
        return self._base_var_name[0]

    @base_var_name.setter
    def base_var_name(self, value):
        self._base_var_name = (value, True)

    @property
    def credentials(self):
        """
        The credentials to assign to the environment variables.

        :rtype: :py:class:`v1_11_9.web.vo.Credential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

