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
#     /delphix-named-keypair-credential.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.TypedObject import TypedObject
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

class NamedKeyPairCredential(TypedObject):
    """
    *(extends* :py:class:`delphixpy.web.vo.TypedObject` *)* Username and key-
    pair credential.
    """
    def __init__(self, undef_enabled=True):
        super(NamedKeyPairCredential, self).__init__()
        self._type = ("NamedKeyPairCredential", True)
        self._private_key = (self.__undef__, True)
        self._public_key = (self.__undef__, True)
        self._username = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NamedKeyPairCredential, cls).from_dict(data, dirty, undef_enabled)
        if "privateKey" not in data:
            raise ValueError("Missing required property \"privateKey\".")
        obj._private_key = (data.get("privateKey", obj.__undef__), dirty)
        if obj._private_key[0] is not None and obj._private_key[0] is not obj.__undef__:
            assert isinstance(obj._private_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._private_key[0], type(obj._private_key[0])))
            common.validate_format(obj._private_key[0], "password", None, None)
        if "publicKey" not in data:
            raise ValueError("Missing required property \"publicKey\".")
        obj._public_key = (data.get("publicKey", obj.__undef__), dirty)
        if obj._public_key[0] is not None and obj._public_key[0] is not obj.__undef__:
            assert isinstance(obj._public_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._public_key[0], type(obj._public_key[0])))
            common.validate_format(obj._public_key[0], "password", None, None)
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "objectName", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NamedKeyPairCredential, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "private_key" == "type" or (self.private_key is not self.__undef__ and (not (dirty and not self._private_key[1]) or isinstance(self.private_key, list) or belongs_to_parent)):
            dct["privateKey"] = dictify(self.private_key)
        if "public_key" == "type" or (self.public_key is not self.__undef__ and (not (dirty and not self._public_key[1]) or isinstance(self.public_key, list) or belongs_to_parent)):
            dct["publicKey"] = dictify(self.public_key)
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]) or isinstance(self.username, list) or belongs_to_parent)):
            dct["username"] = dictify(self.username)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._private_key = (self._private_key[0], True)
        self._public_key = (self._public_key[0], True)
        self._username = (self._username[0], True)

    def is_dirty(self):
        return any([self._private_key[1], self._public_key[1], self._username[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NamedKeyPairCredential):
            return False
        return super(NamedKeyPairCredential, self).__eq__(other) and \
               self.private_key == other.private_key and \
               self.public_key == other.public_key and \
               self.username == other.username

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def private_key(self):
        """
        The private key in the key pair.

        :rtype: ``TEXT_TYPE``
        """
        return self._private_key[0]

    @private_key.setter
    def private_key(self, value):
        self._private_key = (value, True)

    @property
    def public_key(self):
        """
        The public key in the key pair.

        :rtype: ``TEXT_TYPE``
        """
        return self._public_key[0]

    @public_key.setter
    def public_key(self, value):
        self._public_key = (value, True)

    @property
    def username(self):
        """
        The user name.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

