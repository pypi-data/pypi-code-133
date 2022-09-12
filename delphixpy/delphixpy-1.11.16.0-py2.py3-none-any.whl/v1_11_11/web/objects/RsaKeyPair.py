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
#     /delphix-rsa-key-pair.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.KeyPair import KeyPair
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

class RsaKeyPair(KeyPair):
    """
    *(extends* :py:class:`v1_11_11.web.vo.KeyPair` *)* A key pair generated
    using the RSA algorithm.
    """
    def __init__(self, undef_enabled=True):
        super(RsaKeyPair, self).__init__()
        self._type = ("RsaKeyPair", True)
        self._key_size = (self.__undef__, True)
        self._signature_algorithm = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RsaKeyPair, cls).from_dict(data, dirty, undef_enabled)
        obj._key_size = (data.get("keySize", obj.__undef__), dirty)
        if obj._key_size[0] is not None and obj._key_size[0] is not obj.__undef__:
            assert isinstance(obj._key_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._key_size[0], type(obj._key_size[0])))
            common.validate_format(obj._key_size[0], "None", None, None)
        obj._signature_algorithm = (data.get("signatureAlgorithm", obj.__undef__), dirty)
        if obj._signature_algorithm[0] is not None and obj._signature_algorithm[0] is not obj.__undef__:
            assert isinstance(obj._signature_algorithm[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._signature_algorithm[0], type(obj._signature_algorithm[0])))
            assert obj._signature_algorithm[0] in ['SHA256withRSA', 'SHA384withRSA', 'SHA512withRSA'], "Expected enum ['SHA256withRSA', 'SHA384withRSA', 'SHA512withRSA'] but got %s" % obj._signature_algorithm[0]
            common.validate_format(obj._signature_algorithm[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RsaKeyPair, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "key_size" == "type" or (self.key_size is not self.__undef__ and (not (dirty and not self._key_size[1]) or isinstance(self.key_size, list) or belongs_to_parent)):
            dct["keySize"] = dictify(self.key_size)
        elif belongs_to_parent and self.key_size is self.__undef__:
            dct["keySize"] = 2048
        if "signature_algorithm" == "type" or (self.signature_algorithm is not self.__undef__ and (not (dirty and not self._signature_algorithm[1]) or isinstance(self.signature_algorithm, list) or belongs_to_parent)):
            dct["signatureAlgorithm"] = dictify(self.signature_algorithm)
        elif belongs_to_parent and self.signature_algorithm is self.__undef__:
            dct["signatureAlgorithm"] = "SHA256withRSA"
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._key_size = (self._key_size[0], True)
        self._signature_algorithm = (self._signature_algorithm[0], True)

    def is_dirty(self):
        return any([self._key_size[1], self._signature_algorithm[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RsaKeyPair):
            return False
        return super(RsaKeyPair, self).__eq__(other) and \
               self.key_size == other.key_size and \
               self.signature_algorithm == other.signature_algorithm

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def key_size(self):
        """
        *(default value: 2048)* The size of each key to be generated.

        :rtype: ``int``
        """
        return self._key_size[0]

    @key_size.setter
    def key_size(self, value):
        self._key_size = (value, True)

    @property
    def signature_algorithm(self):
        """
        *(default value: SHA256withRSA)* The signature algorithm this key pair
        will use to sign certificates and CSRs. *(permitted values:
        SHA256withRSA, SHA384withRSA, SHA512withRSA)*

        :rtype: ``TEXT_TYPE``
        """
        return self._signature_algorithm[0]

    @signature_algorithm.setter
    def signature_algorithm(self, value):
        self._signature_algorithm = (value, True)

