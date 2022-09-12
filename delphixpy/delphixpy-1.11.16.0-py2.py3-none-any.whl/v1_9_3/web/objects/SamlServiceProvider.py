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
#     /delphix-saml-service-provider.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_3.web.objects.ReadonlyNamedUserObject import ReadonlyNamedUserObject
from delphixpy.v1_9_3 import common

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

class SamlServiceProvider(ReadonlyNamedUserObject):
    """
    *(extends* :py:class:`v1_9_3.web.vo.ReadonlyNamedUserObject` *)* SAML
    service provider configuration.
    """
    def __init__(self, undef_enabled=True):
        super(SamlServiceProvider, self).__init__()
        self._type = ("SamlServiceProvider", True)
        self._entity_id = (self.__undef__, True)
        self._base_url = (self.__undef__, True)
        self._hash_alg_url = (self.__undef__, True)
        self._destination = (self.__undef__, True)
        self._issuer_id = (self.__undef__, True)
        self._signing_key = (self.__undef__, True)
        self._decrypting_key = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SamlServiceProvider, cls).from_dict(data, dirty, undef_enabled)
        if "entityId" not in data:
            raise ValueError("Missing required property \"entityId\".")
        obj._entity_id = (data.get("entityId", obj.__undef__), dirty)
        if obj._entity_id[0] is not None and obj._entity_id[0] is not obj.__undef__:
            assert isinstance(obj._entity_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._entity_id[0], type(obj._entity_id[0])))
            common.validate_format(obj._entity_id[0], "None", None, None)
        if "baseUrl" not in data:
            raise ValueError("Missing required property \"baseUrl\".")
        obj._base_url = (data.get("baseUrl", obj.__undef__), dirty)
        if obj._base_url[0] is not None and obj._base_url[0] is not obj.__undef__:
            assert isinstance(obj._base_url[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._base_url[0], type(obj._base_url[0])))
            common.validate_format(obj._base_url[0], "None", None, None)
        if "hashAlgUrl" not in data:
            raise ValueError("Missing required property \"hashAlgUrl\".")
        obj._hash_alg_url = (data.get("hashAlgUrl", obj.__undef__), dirty)
        if obj._hash_alg_url[0] is not None and obj._hash_alg_url[0] is not obj.__undef__:
            assert isinstance(obj._hash_alg_url[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._hash_alg_url[0], type(obj._hash_alg_url[0])))
            common.validate_format(obj._hash_alg_url[0], "None", None, None)
        if "destination" not in data:
            raise ValueError("Missing required property \"destination\".")
        obj._destination = (data.get("destination", obj.__undef__), dirty)
        if obj._destination[0] is not None and obj._destination[0] is not obj.__undef__:
            assert isinstance(obj._destination[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._destination[0], type(obj._destination[0])))
            common.validate_format(obj._destination[0], "None", None, None)
        if "issuerId" not in data:
            raise ValueError("Missing required property \"issuerId\".")
        obj._issuer_id = (data.get("issuerId", obj.__undef__), dirty)
        if obj._issuer_id[0] is not None and obj._issuer_id[0] is not obj.__undef__:
            assert isinstance(obj._issuer_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._issuer_id[0], type(obj._issuer_id[0])))
            common.validate_format(obj._issuer_id[0], "None", None, None)
        obj._signing_key = (data.get("signingKey", obj.__undef__), dirty)
        if obj._signing_key[0] is not None and obj._signing_key[0] is not obj.__undef__:
            assert isinstance(obj._signing_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._signing_key[0], type(obj._signing_key[0])))
            common.validate_format(obj._signing_key[0], "None", None, None)
        obj._decrypting_key = (data.get("decryptingKey", obj.__undef__), dirty)
        if obj._decrypting_key[0] is not None and obj._decrypting_key[0] is not obj.__undef__:
            assert isinstance(obj._decrypting_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._decrypting_key[0], type(obj._decrypting_key[0])))
            common.validate_format(obj._decrypting_key[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SamlServiceProvider, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "entity_id" == "type" or (self.entity_id is not self.__undef__ and (not (dirty and not self._entity_id[1]) or isinstance(self.entity_id, list) or belongs_to_parent)):
            dct["entityId"] = dictify(self.entity_id)
        if "base_url" == "type" or (self.base_url is not self.__undef__ and (not (dirty and not self._base_url[1]) or isinstance(self.base_url, list) or belongs_to_parent)):
            dct["baseUrl"] = dictify(self.base_url)
        if "hash_alg_url" == "type" or (self.hash_alg_url is not self.__undef__ and (not (dirty and not self._hash_alg_url[1]) or isinstance(self.hash_alg_url, list) or belongs_to_parent)):
            dct["hashAlgUrl"] = dictify(self.hash_alg_url)
        if "destination" == "type" or (self.destination is not self.__undef__ and (not (dirty and not self._destination[1]) or isinstance(self.destination, list) or belongs_to_parent)):
            dct["destination"] = dictify(self.destination)
        if "issuer_id" == "type" or (self.issuer_id is not self.__undef__ and (not (dirty and not self._issuer_id[1]) or isinstance(self.issuer_id, list) or belongs_to_parent)):
            dct["issuerId"] = dictify(self.issuer_id)
        if "signing_key" == "type" or (self.signing_key is not self.__undef__ and (not (dirty and not self._signing_key[1]) or isinstance(self.signing_key, list) or belongs_to_parent)):
            dct["signingKey"] = dictify(self.signing_key)
        if "decrypting_key" == "type" or (self.decrypting_key is not self.__undef__ and (not (dirty and not self._decrypting_key[1]) or isinstance(self.decrypting_key, list) or belongs_to_parent)):
            dct["decryptingKey"] = dictify(self.decrypting_key)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._entity_id = (self._entity_id[0], True)
        self._base_url = (self._base_url[0], True)
        self._hash_alg_url = (self._hash_alg_url[0], True)
        self._destination = (self._destination[0], True)
        self._issuer_id = (self._issuer_id[0], True)
        self._signing_key = (self._signing_key[0], True)
        self._decrypting_key = (self._decrypting_key[0], True)

    def is_dirty(self):
        return any([self._entity_id[1], self._base_url[1], self._hash_alg_url[1], self._destination[1], self._issuer_id[1], self._signing_key[1], self._decrypting_key[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SamlServiceProvider):
            return False
        return super(SamlServiceProvider, self).__eq__(other) and \
               self.entity_id == other.entity_id and \
               self.base_url == other.base_url and \
               self.hash_alg_url == other.hash_alg_url and \
               self.destination == other.destination and \
               self.issuer_id == other.issuer_id and \
               self.signing_key == other.signing_key and \
               self.decrypting_key == other.decrypting_key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def entity_id(self):
        """
        Unique name of service provider.

        :rtype: ``TEXT_TYPE``
        """
        return self._entity_id[0]

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = (value, True)

    @property
    def base_url(self):
        """
        The public URL the Delphix Engine will be accessed at.

        :rtype: ``TEXT_TYPE``
        """
        return self._base_url[0]

    @base_url.setter
    def base_url(self, value):
        self._base_url = (value, True)

    @property
    def hash_alg_url(self):
        """
        Algorithm used for creation of digital signature on metadata.

        :rtype: ``TEXT_TYPE``
        """
        return self._hash_alg_url[0]

    @hash_alg_url.setter
    def hash_alg_url(self, value):
        self._hash_alg_url = (value, True)

    @property
    def destination(self):
        """
        URL to which the SAML authentication request will be sent.

        :rtype: ``TEXT_TYPE``
        """
        return self._destination[0]

    @destination.setter
    def destination(self, value):
        self._destination = (value, True)

    @property
    def issuer_id(self):
        """
        A unique identifier that is provided by the identity provider to ensure
        we are a valid service provider.

        :rtype: ``TEXT_TYPE``
        """
        return self._issuer_id[0]

    @issuer_id.setter
    def issuer_id(self, value):
        self._issuer_id = (value, True)

    @property
    def signing_key(self):
        """
        The signing (public) key that will be used to verify SAML signatures.
        Leave empty if responses will not be signed.

        :rtype: ``TEXT_TYPE``
        """
        return self._signing_key[0]

    @signing_key.setter
    def signing_key(self, value):
        self._signing_key = (value, True)

    @property
    def decrypting_key(self):
        """
        The decryption (private) key that will be used to decrypt SAML
        assertions. Leave empty if response will not be encrypted. This key
        MUST be a PKCS8 key.

        :rtype: ``TEXT_TYPE``
        """
        return self._decrypting_key[0]

    @decrypting_key.setter
    def decrypting_key(self, value):
        self._decrypting_key = (value, True)

