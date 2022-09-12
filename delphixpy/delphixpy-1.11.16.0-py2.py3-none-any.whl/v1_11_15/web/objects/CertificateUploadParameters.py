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
#     /delphix-certificate-upload-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_15 import common

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

class CertificateUploadParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_15.web.vo.TypedObject` *)* The parameters for
    uploading a keystore which include the credentials needed to access it.
    """
    def __init__(self, undef_enabled=True):
        super(CertificateUploadParameters, self).__init__()
        self._type = ("CertificateUploadParameters", True)
        self._alias = (self.__undef__, True)
        self._storepass = (self.__undef__, True)
        self._keypass = (self.__undef__, True)
        self._keystore_type = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CertificateUploadParameters, cls).from_dict(data, dirty, undef_enabled)
        if "alias" not in data:
            raise ValueError("Missing required property \"alias\".")
        obj._alias = (data.get("alias", obj.__undef__), dirty)
        if obj._alias[0] is not None and obj._alias[0] is not obj.__undef__:
            assert isinstance(obj._alias[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._alias[0], type(obj._alias[0])))
            common.validate_format(obj._alias[0], "None", None, None)
        if "storepass" not in data:
            raise ValueError("Missing required property \"storepass\".")
        obj._storepass = (data.get("storepass", obj.__undef__), dirty)
        if obj._storepass[0] is not None and obj._storepass[0] is not obj.__undef__:
            assert isinstance(obj._storepass[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._storepass[0], type(obj._storepass[0])))
            common.validate_format(obj._storepass[0], "password", None, None)
        obj._keypass = (data.get("keypass", obj.__undef__), dirty)
        if obj._keypass[0] is not None and obj._keypass[0] is not obj.__undef__:
            assert isinstance(obj._keypass[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._keypass[0], type(obj._keypass[0])))
            common.validate_format(obj._keypass[0], "password", None, None)
        if "keystoreType" not in data:
            raise ValueError("Missing required property \"keystoreType\".")
        obj._keystore_type = (data.get("keystoreType", obj.__undef__), dirty)
        if obj._keystore_type[0] is not None and obj._keystore_type[0] is not obj.__undef__:
            assert isinstance(obj._keystore_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._keystore_type[0], type(obj._keystore_type[0])))
            assert obj._keystore_type[0] in ['JKS', 'PKCS12'], "Expected enum ['JKS', 'PKCS12'] but got %s" % obj._keystore_type[0]
            common.validate_format(obj._keystore_type[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CertificateUploadParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "alias" == "type" or (self.alias is not self.__undef__ and (not (dirty and not self._alias[1]) or isinstance(self.alias, list) or belongs_to_parent)):
            dct["alias"] = dictify(self.alias)
        if "storepass" == "type" or (self.storepass is not self.__undef__ and (not (dirty and not self._storepass[1]) or isinstance(self.storepass, list) or belongs_to_parent)):
            dct["storepass"] = dictify(self.storepass)
        if "keypass" == "type" or (self.keypass is not self.__undef__ and (not (dirty and not self._keypass[1]))):
            dct["keypass"] = dictify(self.keypass)
        if "keystore_type" == "type" or (self.keystore_type is not self.__undef__ and (not (dirty and not self._keystore_type[1]) or isinstance(self.keystore_type, list) or belongs_to_parent)):
            dct["keystoreType"] = dictify(self.keystore_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._alias = (self._alias[0], True)
        self._storepass = (self._storepass[0], True)
        self._keypass = (self._keypass[0], True)
        self._keystore_type = (self._keystore_type[0], True)

    def is_dirty(self):
        return any([self._alias[1], self._storepass[1], self._keypass[1], self._keystore_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CertificateUploadParameters):
            return False
        return super(CertificateUploadParameters, self).__eq__(other) and \
               self.alias == other.alias and \
               self.storepass == other.storepass and \
               self.keypass == other.keypass and \
               self.keystore_type == other.keystore_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def alias(self):
        """
        The lowercase alias for the certificate and key pair to use.

        :rtype: ``TEXT_TYPE``
        """
        return self._alias[0]

    @alias.setter
    def alias(self, value):
        self._alias = (value, True)

    @property
    def storepass(self):
        """
        The password for the keystore.

        :rtype: ``TEXT_TYPE``
        """
        return self._storepass[0]

    @storepass.setter
    def storepass(self, value):
        self._storepass = (value, True)

    @property
    def keypass(self):
        """
        The password for the key pair. If not provided, then the storepass is
        used.

        :rtype: ``TEXT_TYPE``
        """
        return self._keypass[0]

    @keypass.setter
    def keypass(self, value):
        self._keypass = (value, True)

    @property
    def keystore_type(self):
        """
        *(default value: JKS)* The format of the keystore. *(permitted values:
        JKS, PKCS12)*

        :rtype: ``TEXT_TYPE``
        """
        return self._keystore_type[0]

    @keystore_type.setter
    def keystore_type(self, value):
        self._keystore_type = (value, True)

