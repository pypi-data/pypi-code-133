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
#     /delphix-certificate.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_3.web.objects.UserObject import UserObject
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

class Certificate(UserObject):
    """
    *(extends* :py:class:`v1_9_3.web.vo.UserObject` *)* Public Key Certificate.
    """
    def __init__(self, undef_enabled=True):
        super(Certificate, self).__init__()
        self._type = ("Certificate", True)
        self._name = (self.__undef__, True)
        self._issued_by_dn = (self.__undef__, True)
        self._issuer = (self.__undef__, True)
        self._serial_number = (self.__undef__, True)
        self._not_before = (self.__undef__, True)
        self._not_after = (self.__undef__, True)
        self._sha1_fingerprint = (self.__undef__, True)
        self._md5_fingerprint = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Certificate, cls).from_dict(data, dirty, undef_enabled)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "objectName", None, None)
        obj._issued_by_dn = (data.get("issuedByDN", obj.__undef__), dirty)
        if obj._issued_by_dn[0] is not None and obj._issued_by_dn[0] is not obj.__undef__:
            assert isinstance(obj._issued_by_dn[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._issued_by_dn[0], type(obj._issued_by_dn[0])))
            common.validate_format(obj._issued_by_dn[0], "None", None, None)
        obj._issuer = (data.get("issuer", obj.__undef__), dirty)
        if obj._issuer[0] is not None and obj._issuer[0] is not obj.__undef__:
            assert isinstance(obj._issuer[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._issuer[0], type(obj._issuer[0])))
            common.validate_format(obj._issuer[0], "objectReference", None, None)
        obj._serial_number = (data.get("serialNumber", obj.__undef__), dirty)
        if obj._serial_number[0] is not None and obj._serial_number[0] is not obj.__undef__:
            assert isinstance(obj._serial_number[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._serial_number[0], type(obj._serial_number[0])))
            common.validate_format(obj._serial_number[0], "None", None, None)
        obj._not_before = (data.get("notBefore", obj.__undef__), dirty)
        if obj._not_before[0] is not None and obj._not_before[0] is not obj.__undef__:
            assert isinstance(obj._not_before[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._not_before[0], type(obj._not_before[0])))
            common.validate_format(obj._not_before[0], "date", None, None)
        obj._not_after = (data.get("notAfter", obj.__undef__), dirty)
        if obj._not_after[0] is not None and obj._not_after[0] is not obj.__undef__:
            assert isinstance(obj._not_after[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._not_after[0], type(obj._not_after[0])))
            common.validate_format(obj._not_after[0], "date", None, None)
        obj._sha1_fingerprint = (data.get("sha1Fingerprint", obj.__undef__), dirty)
        if obj._sha1_fingerprint[0] is not None and obj._sha1_fingerprint[0] is not obj.__undef__:
            assert isinstance(obj._sha1_fingerprint[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._sha1_fingerprint[0], type(obj._sha1_fingerprint[0])))
            common.validate_format(obj._sha1_fingerprint[0], "None", None, None)
        obj._md5_fingerprint = (data.get("md5Fingerprint", obj.__undef__), dirty)
        if obj._md5_fingerprint[0] is not None and obj._md5_fingerprint[0] is not obj.__undef__:
            assert isinstance(obj._md5_fingerprint[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._md5_fingerprint[0], type(obj._md5_fingerprint[0])))
            common.validate_format(obj._md5_fingerprint[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Certificate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]))):
            dct["name"] = dictify(self.name)
        if "issued_by_dn" == "type" or (self.issued_by_dn is not self.__undef__ and (not (dirty and not self._issued_by_dn[1]))):
            dct["issuedByDN"] = dictify(self.issued_by_dn)
        if "issuer" == "type" or (self.issuer is not self.__undef__ and (not (dirty and not self._issuer[1]))):
            dct["issuer"] = dictify(self.issuer)
        if "serial_number" == "type" or (self.serial_number is not self.__undef__ and (not (dirty and not self._serial_number[1]))):
            dct["serialNumber"] = dictify(self.serial_number)
        if "not_before" == "type" or (self.not_before is not self.__undef__ and (not (dirty and not self._not_before[1]))):
            dct["notBefore"] = dictify(self.not_before)
        if "not_after" == "type" or (self.not_after is not self.__undef__ and (not (dirty and not self._not_after[1]))):
            dct["notAfter"] = dictify(self.not_after)
        if "sha1_fingerprint" == "type" or (self.sha1_fingerprint is not self.__undef__ and (not (dirty and not self._sha1_fingerprint[1]))):
            dct["sha1Fingerprint"] = dictify(self.sha1_fingerprint)
        if "md5_fingerprint" == "type" or (self.md5_fingerprint is not self.__undef__ and (not (dirty and not self._md5_fingerprint[1]))):
            dct["md5Fingerprint"] = dictify(self.md5_fingerprint)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._name = (self._name[0], True)
        self._issued_by_dn = (self._issued_by_dn[0], True)
        self._issuer = (self._issuer[0], True)
        self._serial_number = (self._serial_number[0], True)
        self._not_before = (self._not_before[0], True)
        self._not_after = (self._not_after[0], True)
        self._sha1_fingerprint = (self._sha1_fingerprint[0], True)
        self._md5_fingerprint = (self._md5_fingerprint[0], True)

    def is_dirty(self):
        return any([self._name[1], self._issued_by_dn[1], self._issuer[1], self._serial_number[1], self._not_before[1], self._not_after[1], self._sha1_fingerprint[1], self._md5_fingerprint[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Certificate):
            return False
        return super(Certificate, self).__eq__(other) and \
               self.name == other.name and \
               self.issued_by_dn == other.issued_by_dn and \
               self.issuer == other.issuer and \
               self.serial_number == other.serial_number and \
               self.not_before == other.not_before and \
               self.not_after == other.not_after and \
               self.sha1_fingerprint == other.sha1_fingerprint and \
               self.md5_fingerprint == other.md5_fingerprint

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def name(self):
        """
        The Distinguished Name of this certificate.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def issued_by_dn(self):
        """
        Issuer of this certificate.

        :rtype: ``TEXT_TYPE``
        """
        return self._issued_by_dn[0]

    @issued_by_dn.setter
    def issued_by_dn(self, value):
        self._issued_by_dn = (value, True)

    @property
    def issuer(self):
        """
        A reference to the certificate that issued this certificate. Null if
        this is a root CA.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._issuer[0]

    @issuer.setter
    def issuer(self, value):
        self._issuer = (value, True)

    @property
    def serial_number(self):
        """
        Certificate serial number.

        :rtype: ``TEXT_TYPE``
        """
        return self._serial_number[0]

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = (value, True)

    @property
    def not_before(self):
        """
        Start of validity.

        :rtype: ``TEXT_TYPE``
        """
        return self._not_before[0]

    @not_before.setter
    def not_before(self, value):
        self._not_before = (value, True)

    @property
    def not_after(self):
        """
        End of validity.

        :rtype: ``TEXT_TYPE``
        """
        return self._not_after[0]

    @not_after.setter
    def not_after(self, value):
        self._not_after = (value, True)

    @property
    def sha1_fingerprint(self):
        """
        SHA-1 fingerprint.

        :rtype: ``TEXT_TYPE``
        """
        return self._sha1_fingerprint[0]

    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value):
        self._sha1_fingerprint = (value, True)

    @property
    def md5_fingerprint(self):
        """
        MD5 fingerprint.

        :rtype: ``TEXT_TYPE``
        """
        return self._md5_fingerprint[0]

    @md5_fingerprint.setter
    def md5_fingerprint(self, value):
        self._md5_fingerprint = (value, True)

