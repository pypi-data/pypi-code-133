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
#     /delphix-certificate-import-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_0 import common

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

class CertificateImportParameters(TypedObject):
    """
    *(extends* :py:class:`v1_9_0.web.vo.TypedObject` *)* Parameters for
    importing a certificate.
    """
    def __init__(self, undef_enabled=True):
        super(CertificateImportParameters, self).__init__()
        self._type = ("CertificateImportParameters", True)
        self._certificate = (self.__undef__, True)
        self._alias = (self.__undef__, True)

    API_VERSION = "1.9.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CertificateImportParameters, cls).from_dict(data, dirty, undef_enabled)
        if "certificate" not in data:
            raise ValueError("Missing required property \"certificate\".")
        obj._certificate = (data.get("certificate", obj.__undef__), dirty)
        if obj._certificate[0] is not None and obj._certificate[0] is not obj.__undef__:
            assert isinstance(obj._certificate[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._certificate[0], type(obj._certificate[0])))
            common.validate_format(obj._certificate[0], "None", None, None)
        if "alias" not in data:
            raise ValueError("Missing required property \"alias\".")
        obj._alias = (data.get("alias", obj.__undef__), dirty)
        if obj._alias[0] is not None and obj._alias[0] is not obj.__undef__:
            assert isinstance(obj._alias[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._alias[0], type(obj._alias[0])))
            common.validate_format(obj._alias[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CertificateImportParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "certificate" == "type" or (self.certificate is not self.__undef__ and (not (dirty and not self._certificate[1]) or isinstance(self.certificate, list) or belongs_to_parent)):
            dct["certificate"] = dictify(self.certificate)
        if "alias" == "type" or (self.alias is not self.__undef__ and (not (dirty and not self._alias[1]) or isinstance(self.alias, list) or belongs_to_parent)):
            dct["alias"] = dictify(self.alias)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._certificate = (self._certificate[0], True)
        self._alias = (self._alias[0], True)

    def is_dirty(self):
        return any([self._certificate[1], self._alias[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CertificateImportParameters):
            return False
        return super(CertificateImportParameters, self).__eq__(other) and \
               self.certificate == other.certificate and \
               self.alias == other.alias

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def certificate(self):
        """
        Certificate contents.

        :rtype: ``TEXT_TYPE``
        """
        return self._certificate[0]

    @certificate.setter
    def certificate(self, value):
        self._certificate = (value, True)

    @property
    def alias(self):
        """
        The unique name for this certificate.

        :rtype: ``TEXT_TYPE``
        """
        return self._alias[0]

    @alias.setter
    def alias(self, value):
        self._alias = (value, True)

