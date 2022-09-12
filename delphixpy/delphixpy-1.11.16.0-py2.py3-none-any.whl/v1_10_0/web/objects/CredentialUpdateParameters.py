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
#     /delphix-credential-update-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_0 import factory
from delphixpy.v1_10_0 import common

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

class CredentialUpdateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_10_0.web.vo.TypedObject` *)* Parameters to update
    a Delphix user's password.
    """
    def __init__(self, undef_enabled=True):
        super(CredentialUpdateParameters, self).__init__()
        self._type = ("CredentialUpdateParameters", True)
        self._old_credential = (self.__undef__, True)
        self._new_credential = (self.__undef__, True)

    API_VERSION = "1.10.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CredentialUpdateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "oldCredential" in data and data["oldCredential"] is not None:
            obj._old_credential = (factory.create_object(data["oldCredential"], "PasswordCredential"), dirty)
            factory.validate_type(obj._old_credential[0], "PasswordCredential")
        else:
            obj._old_credential = (obj.__undef__, dirty)
        if "newCredential" in data and data["newCredential"] is not None:
            obj._new_credential = (factory.create_object(data["newCredential"], "PasswordCredential"), dirty)
            factory.validate_type(obj._new_credential[0], "PasswordCredential")
        else:
            obj._new_credential = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CredentialUpdateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "old_credential" == "type" or (self.old_credential is not self.__undef__ and (not (dirty and not self._old_credential[1]) or isinstance(self.old_credential, list) or belongs_to_parent)):
            dct["oldCredential"] = dictify(self.old_credential, prop_is_list_or_vo=True)
        if "new_credential" == "type" or (self.new_credential is not self.__undef__ and (not (dirty and not self._new_credential[1]) or isinstance(self.new_credential, list) or belongs_to_parent)):
            dct["newCredential"] = dictify(self.new_credential, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._old_credential = (self._old_credential[0], True)
        self._new_credential = (self._new_credential[0], True)

    def is_dirty(self):
        return any([self._old_credential[1], self._new_credential[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CredentialUpdateParameters):
            return False
        return super(CredentialUpdateParameters, self).__eq__(other) and \
               self.old_credential == other.old_credential and \
               self.new_credential == other.new_credential

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def old_credential(self):
        """
        The old credentials.

        :rtype: :py:class:`v1_10_0.web.vo.PasswordCredential`
        """
        return self._old_credential[0]

    @old_credential.setter
    def old_credential(self, value):
        self._old_credential = (value, True)

    @property
    def new_credential(self):
        """
        The new credentials.

        :rtype: :py:class:`v1_10_0.web.vo.PasswordCredential`
        """
        return self._new_credential[0]

    @new_credential.setter
    def new_credential(self, value):
        self._new_credential = (value, True)

