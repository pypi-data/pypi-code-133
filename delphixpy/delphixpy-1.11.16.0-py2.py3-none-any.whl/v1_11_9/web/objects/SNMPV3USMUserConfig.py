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
#     /delphix-snmp-v3-usm-user-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.PersistentObject import PersistentObject
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

class SNMPV3USMUserConfig(PersistentObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.PersistentObject` *)* SNMP USM User
    configuration.
    """
    def __init__(self, undef_enabled=True):
        super(SNMPV3USMUserConfig, self).__init__()
        self._type = ("SNMPV3USMUserConfig", True)
        self._username = (self.__undef__, True)
        self._authentication_protocol = (self.__undef__, True)
        self._authentication_passphrase = (self.__undef__, True)
        self._privacy_protocol = (self.__undef__, True)
        self._privacy_passphrase = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SNMPV3USMUserConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "None", 1, None)
        obj._authentication_protocol = (data.get("authenticationProtocol", obj.__undef__), dirty)
        if obj._authentication_protocol[0] is not None and obj._authentication_protocol[0] is not obj.__undef__:
            assert isinstance(obj._authentication_protocol[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._authentication_protocol[0], type(obj._authentication_protocol[0])))
            assert obj._authentication_protocol[0] in ['SHA', 'MD5'], "Expected enum ['SHA', 'MD5'] but got %s" % obj._authentication_protocol[0]
            common.validate_format(obj._authentication_protocol[0], "None", None, None)
        obj._authentication_passphrase = (data.get("authenticationPassphrase", obj.__undef__), dirty)
        if obj._authentication_passphrase[0] is not None and obj._authentication_passphrase[0] is not obj.__undef__:
            assert isinstance(obj._authentication_passphrase[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._authentication_passphrase[0], type(obj._authentication_passphrase[0])))
            common.validate_format(obj._authentication_passphrase[0], "password", 8, None)
        obj._privacy_protocol = (data.get("privacyProtocol", obj.__undef__), dirty)
        if obj._privacy_protocol[0] is not None and obj._privacy_protocol[0] is not obj.__undef__:
            assert isinstance(obj._privacy_protocol[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._privacy_protocol[0], type(obj._privacy_protocol[0])))
            assert obj._privacy_protocol[0] in ['AES', 'DES'], "Expected enum ['AES', 'DES'] but got %s" % obj._privacy_protocol[0]
            common.validate_format(obj._privacy_protocol[0], "None", None, None)
        obj._privacy_passphrase = (data.get("privacyPassphrase", obj.__undef__), dirty)
        if obj._privacy_passphrase[0] is not None and obj._privacy_passphrase[0] is not obj.__undef__:
            assert isinstance(obj._privacy_passphrase[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._privacy_passphrase[0], type(obj._privacy_passphrase[0])))
            common.validate_format(obj._privacy_passphrase[0], "password", 8, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SNMPV3USMUserConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]) or isinstance(self.username, list) or belongs_to_parent)):
            dct["username"] = dictify(self.username)
        if "authentication_protocol" == "type" or (self.authentication_protocol is not self.__undef__ and (not (dirty and not self._authentication_protocol[1]) or isinstance(self.authentication_protocol, list) or belongs_to_parent)):
            dct["authenticationProtocol"] = dictify(self.authentication_protocol)
        if "authentication_passphrase" == "type" or (self.authentication_passphrase is not self.__undef__ and (not (dirty and not self._authentication_passphrase[1]) or isinstance(self.authentication_passphrase, list) or belongs_to_parent)):
            dct["authenticationPassphrase"] = dictify(self.authentication_passphrase)
        if "privacy_protocol" == "type" or (self.privacy_protocol is not self.__undef__ and (not (dirty and not self._privacy_protocol[1]) or isinstance(self.privacy_protocol, list) or belongs_to_parent)):
            dct["privacyProtocol"] = dictify(self.privacy_protocol)
        if "privacy_passphrase" == "type" or (self.privacy_passphrase is not self.__undef__ and (not (dirty and not self._privacy_passphrase[1]) or isinstance(self.privacy_passphrase, list) or belongs_to_parent)):
            dct["privacyPassphrase"] = dictify(self.privacy_passphrase)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._username = (self._username[0], True)
        self._authentication_protocol = (self._authentication_protocol[0], True)
        self._authentication_passphrase = (self._authentication_passphrase[0], True)
        self._privacy_protocol = (self._privacy_protocol[0], True)
        self._privacy_passphrase = (self._privacy_passphrase[0], True)

    def is_dirty(self):
        return any([self._username[1], self._authentication_protocol[1], self._authentication_passphrase[1], self._privacy_protocol[1], self._privacy_passphrase[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SNMPV3USMUserConfig):
            return False
        return super(SNMPV3USMUserConfig, self).__eq__(other) and \
               self.username == other.username and \
               self.authentication_protocol == other.authentication_protocol and \
               self.authentication_passphrase == other.authentication_passphrase and \
               self.privacy_protocol == other.privacy_protocol and \
               self.privacy_passphrase == other.privacy_passphrase

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def username(self):
        """
        The name of user.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

    @property
    def authentication_protocol(self):
        """
        The protocol to use for authenticating with the user. *(permitted
        values: SHA, MD5)*

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._authentication_protocol[0]

    @authentication_protocol.setter
    def authentication_protocol(self, value):
        self._authentication_protocol = (value, True)

    @property
    def authentication_passphrase(self):
        """
        The passphrase to use for authentication.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._authentication_passphrase[0]

    @authentication_passphrase.setter
    def authentication_passphrase(self, value):
        self._authentication_passphrase = (value, True)

    @property
    def privacy_protocol(self):
        """
        The protocol to use for encrypting the SNMP payload. *(permitted
        values: AES, DES)*

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._privacy_protocol[0]

    @privacy_protocol.setter
    def privacy_protocol(self, value):
        self._privacy_protocol = (value, True)

    @property
    def privacy_passphrase(self):
        """
        The passphrase to use for encrypting the SNMP payload.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._privacy_passphrase[0]

    @privacy_passphrase.setter
    def privacy_passphrase(self, value):
        self._privacy_passphrase = (value, True)

