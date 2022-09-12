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
#     /delphix-x509certificate.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_3.web.objects.UserObject import UserObject
from delphixpy.v1_5_3 import common

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

class X509Certificate(UserObject):
    """
    *(extends* :py:class:`v1_5_3.web.vo.UserObject` *)* X509 Certificate.
    """
    def __init__(self, undef_enabled=True):
        super(X509Certificate, self).__init__()
        self._type = ("X509Certificate", True)
        self._accepted = (self.__undef__, True)
        self._issued_by_dn = (self.__undef__, True)
        self._issued_to_dn = (self.__undef__, True)
        self._md5_fingerprint = (self.__undef__, True)
        self._serial_number = (self.__undef__, True)
        self._sha1_fingerprint = (self.__undef__, True)
        self._valid_from = (self.__undef__, True)
        self._valid_to = (self.__undef__, True)

    API_VERSION = "1.5.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(X509Certificate, cls).from_dict(data, dirty, undef_enabled)
        obj._accepted = (data.get("accepted", obj.__undef__), dirty)
        if obj._accepted[0] is not None and obj._accepted[0] is not obj.__undef__:
            assert isinstance(obj._accepted[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._accepted[0], type(obj._accepted[0])))
            common.validate_format(obj._accepted[0], "None", None, None)
        obj._issued_by_dn = (data.get("issuedByDN", obj.__undef__), dirty)
        if obj._issued_by_dn[0] is not None and obj._issued_by_dn[0] is not obj.__undef__:
            assert isinstance(obj._issued_by_dn[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._issued_by_dn[0], type(obj._issued_by_dn[0])))
            common.validate_format(obj._issued_by_dn[0], "None", None, None)
        obj._issued_to_dn = (data.get("issuedToDN", obj.__undef__), dirty)
        if obj._issued_to_dn[0] is not None and obj._issued_to_dn[0] is not obj.__undef__:
            assert isinstance(obj._issued_to_dn[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._issued_to_dn[0], type(obj._issued_to_dn[0])))
            common.validate_format(obj._issued_to_dn[0], "None", None, None)
        obj._md5_fingerprint = (data.get("md5Fingerprint", obj.__undef__), dirty)
        if obj._md5_fingerprint[0] is not None and obj._md5_fingerprint[0] is not obj.__undef__:
            assert isinstance(obj._md5_fingerprint[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._md5_fingerprint[0], type(obj._md5_fingerprint[0])))
            common.validate_format(obj._md5_fingerprint[0], "None", None, None)
        obj._serial_number = (data.get("serialNumber", obj.__undef__), dirty)
        if obj._serial_number[0] is not None and obj._serial_number[0] is not obj.__undef__:
            assert isinstance(obj._serial_number[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._serial_number[0], type(obj._serial_number[0])))
            common.validate_format(obj._serial_number[0], "None", None, None)
        obj._sha1_fingerprint = (data.get("sha1Fingerprint", obj.__undef__), dirty)
        if obj._sha1_fingerprint[0] is not None and obj._sha1_fingerprint[0] is not obj.__undef__:
            assert isinstance(obj._sha1_fingerprint[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._sha1_fingerprint[0], type(obj._sha1_fingerprint[0])))
            common.validate_format(obj._sha1_fingerprint[0], "None", None, None)
        obj._valid_from = (data.get("validFrom", obj.__undef__), dirty)
        if obj._valid_from[0] is not None and obj._valid_from[0] is not obj.__undef__:
            assert isinstance(obj._valid_from[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._valid_from[0], type(obj._valid_from[0])))
            common.validate_format(obj._valid_from[0], "None", None, None)
        obj._valid_to = (data.get("validTo", obj.__undef__), dirty)
        if obj._valid_to[0] is not None and obj._valid_to[0] is not obj.__undef__:
            assert isinstance(obj._valid_to[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._valid_to[0], type(obj._valid_to[0])))
            common.validate_format(obj._valid_to[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(X509Certificate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "accepted" == "type" or (self.accepted is not self.__undef__ and (not (dirty and not self._accepted[1]))):
            dct["accepted"] = dictify(self.accepted)
        if "issued_by_dn" == "type" or (self.issued_by_dn is not self.__undef__ and (not (dirty and not self._issued_by_dn[1]))):
            dct["issuedByDN"] = dictify(self.issued_by_dn)
        if "issued_to_dn" == "type" or (self.issued_to_dn is not self.__undef__ and (not (dirty and not self._issued_to_dn[1]))):
            dct["issuedToDN"] = dictify(self.issued_to_dn)
        if "md5_fingerprint" == "type" or (self.md5_fingerprint is not self.__undef__ and (not (dirty and not self._md5_fingerprint[1]))):
            dct["md5Fingerprint"] = dictify(self.md5_fingerprint)
        if "serial_number" == "type" or (self.serial_number is not self.__undef__ and (not (dirty and not self._serial_number[1]))):
            dct["serialNumber"] = dictify(self.serial_number)
        if "sha1_fingerprint" == "type" or (self.sha1_fingerprint is not self.__undef__ and (not (dirty and not self._sha1_fingerprint[1]))):
            dct["sha1Fingerprint"] = dictify(self.sha1_fingerprint)
        if "valid_from" == "type" or (self.valid_from is not self.__undef__ and (not (dirty and not self._valid_from[1]))):
            dct["validFrom"] = dictify(self.valid_from)
        if "valid_to" == "type" or (self.valid_to is not self.__undef__ and (not (dirty and not self._valid_to[1]))):
            dct["validTo"] = dictify(self.valid_to)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._accepted = (self._accepted[0], True)
        self._issued_by_dn = (self._issued_by_dn[0], True)
        self._issued_to_dn = (self._issued_to_dn[0], True)
        self._md5_fingerprint = (self._md5_fingerprint[0], True)
        self._serial_number = (self._serial_number[0], True)
        self._sha1_fingerprint = (self._sha1_fingerprint[0], True)
        self._valid_from = (self._valid_from[0], True)
        self._valid_to = (self._valid_to[0], True)

    def is_dirty(self):
        return any([self._accepted[1], self._issued_by_dn[1], self._issued_to_dn[1], self._md5_fingerprint[1], self._serial_number[1], self._sha1_fingerprint[1], self._valid_from[1], self._valid_to[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, X509Certificate):
            return False
        return super(X509Certificate, self).__eq__(other) and \
               self.accepted == other.accepted and \
               self.issued_by_dn == other.issued_by_dn and \
               self.issued_to_dn == other.issued_to_dn and \
               self.md5_fingerprint == other.md5_fingerprint and \
               self.serial_number == other.serial_number and \
               self.sha1_fingerprint == other.sha1_fingerprint and \
               self.valid_from == other.valid_from and \
               self.valid_to == other.valid_to

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def accepted(self):
        """
        Delphix trusts this certificate .

        :rtype: ``bool``
        """
        return self._accepted[0]

    @accepted.setter
    def accepted(self, value):
        self._accepted = (value, True)

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
    def issued_to_dn(self):
        """
        Distinguished name of subject of this certificate.

        :rtype: ``TEXT_TYPE``
        """
        return self._issued_to_dn[0]

    @issued_to_dn.setter
    def issued_to_dn(self, value):
        self._issued_to_dn = (value, True)

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
    def valid_from(self):
        """
        Start of validity.

        :rtype: ``TEXT_TYPE``
        """
        return self._valid_from[0]

    @valid_from.setter
    def valid_from(self, value):
        self._valid_from = (value, True)

    @property
    def valid_to(self):
        """
        End of validity.

        :rtype: ``TEXT_TYPE``
        """
        return self._valid_to[0]

    @valid_to.setter
    def valid_to(self, value):
        self._valid_to = (value, True)

