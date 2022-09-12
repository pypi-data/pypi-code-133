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
#     /delphix-certificate-signing-request-create-parameters.json
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

class CertificateSigningRequestCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.TypedObject` *)* The parameters used
    to create a certificate signing request (CSR).
    """
    def __init__(self, undef_enabled=True):
        super(CertificateSigningRequestCreateParameters, self).__init__()
        self._type = ("CertificateSigningRequestCreateParameters", True)
        self._end_entity = (self.__undef__, True)
        self._dname = (self.__undef__, True)
        self._force_replace = (self.__undef__, True)
        self._key_pair = (self.__undef__, True)
        self._subject_alternative_names = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CertificateSigningRequestCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "endEntity" in data and data["endEntity"] is not None:
            obj._end_entity = (factory.create_object(data["endEntity"], "EndEntity"), dirty)
            factory.validate_type(obj._end_entity[0], "EndEntity")
        else:
            obj._end_entity = (obj.__undef__, dirty)
        if "dname" in data and data["dname"] is not None:
            obj._dname = (factory.create_object(data["dname"], "X500DistinguishedName"), dirty)
            factory.validate_type(obj._dname[0], "X500DistinguishedName")
        else:
            obj._dname = (obj.__undef__, dirty)
        obj._force_replace = (data.get("forceReplace", obj.__undef__), dirty)
        if obj._force_replace[0] is not None and obj._force_replace[0] is not obj.__undef__:
            assert isinstance(obj._force_replace[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._force_replace[0], type(obj._force_replace[0])))
            common.validate_format(obj._force_replace[0], "None", None, None)
        if "keyPair" in data and data["keyPair"] is not None:
            obj._key_pair = (factory.create_object(data["keyPair"], "KeyPair"), dirty)
            factory.validate_type(obj._key_pair[0], "KeyPair")
        else:
            obj._key_pair = (obj.__undef__, dirty)
        obj._subject_alternative_names = []
        for item in data.get("subjectAlternativeNames") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "host", None, None)
            obj._subject_alternative_names.append(item)
        obj._subject_alternative_names = (obj._subject_alternative_names, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CertificateSigningRequestCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "end_entity" == "type" or (self.end_entity is not self.__undef__ and (not (dirty and not self._end_entity[1]) or isinstance(self.end_entity, list) or belongs_to_parent)):
            dct["endEntity"] = dictify(self.end_entity, prop_is_list_or_vo=True)
        if "dname" == "type" or (self.dname is not self.__undef__ and (not (dirty and not self._dname[1]) or isinstance(self.dname, list) or belongs_to_parent)):
            dct["dname"] = dictify(self.dname, prop_is_list_or_vo=True)
        if "force_replace" == "type" or (self.force_replace is not self.__undef__ and (not (dirty and not self._force_replace[1]) or isinstance(self.force_replace, list) or belongs_to_parent)):
            dct["forceReplace"] = dictify(self.force_replace)
        elif belongs_to_parent and self.force_replace is self.__undef__:
            dct["forceReplace"] = False
        if "key_pair" == "type" or (self.key_pair is not self.__undef__ and (not (dirty and not self._key_pair[1]) or isinstance(self.key_pair, list) or belongs_to_parent)):
            dct["keyPair"] = dictify(self.key_pair, prop_is_list_or_vo=True)
        if "subject_alternative_names" == "type" or (self.subject_alternative_names is not self.__undef__ and (not (dirty and not self._subject_alternative_names[1]) or isinstance(self.subject_alternative_names, list) or belongs_to_parent)):
            dct["subjectAlternativeNames"] = dictify(self.subject_alternative_names, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._end_entity = (self._end_entity[0], True)
        self._dname = (self._dname[0], True)
        self._force_replace = (self._force_replace[0], True)
        self._key_pair = (self._key_pair[0], True)
        self._subject_alternative_names = (self._subject_alternative_names[0], True)

    def is_dirty(self):
        return any([self._end_entity[1], self._dname[1], self._force_replace[1], self._key_pair[1], self._subject_alternative_names[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CertificateSigningRequestCreateParameters):
            return False
        return super(CertificateSigningRequestCreateParameters, self).__eq__(other) and \
               self.end_entity == other.end_entity and \
               self.dname == other.dname and \
               self.force_replace == other.force_replace and \
               self.key_pair == other.key_pair and \
               self.subject_alternative_names == other.subject_alternative_names

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def end_entity(self):
        """
        The specific TLS service to generate the CSR for.

        :rtype: :py:class:`v1_11_9.web.vo.EndEntity`
        """
        return self._end_entity[0]

    @end_entity.setter
    def end_entity(self, value):
        self._end_entity = (value, True)

    @property
    def dname(self):
        """
        The Distinguished Name to use.

        :rtype: :py:class:`v1_11_9.web.vo.X500DistinguishedName`
        """
        return self._dname[0]

    @dname.setter
    def dname(self, value):
        self._dname = (value, True)

    @property
    def force_replace(self):
        """
        Force replace the active keypair and certificate with this newly
        generated one.

        :rtype: ``bool``
        """
        return self._force_replace[0]

    @force_replace.setter
    def force_replace(self, value):
        self._force_replace = (value, True)

    @property
    def key_pair(self):
        """
        The backing key pair and signature algorithm it will use.

        :rtype: :py:class:`v1_11_9.web.vo.KeyPair`
        """
        return self._key_pair[0]

    @key_pair.setter
    def key_pair(self, value):
        self._key_pair = (value, True)

    @property
    def subject_alternative_names(self):
        """
        The subject alternative names associated with this certificate.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._subject_alternative_names[0]

    @subject_alternative_names.setter
    def subject_alternative_names(self, value):
        self._subject_alternative_names = (value, True)

