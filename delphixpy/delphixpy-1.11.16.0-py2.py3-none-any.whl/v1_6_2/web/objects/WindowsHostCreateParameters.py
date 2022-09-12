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
#     /delphix-windows-host-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_2.web.objects.HostCreateParameters import HostCreateParameters
from delphixpy.v1_6_2 import common

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

class WindowsHostCreateParameters(HostCreateParameters):
    """
    *(extends* :py:class:`v1_6_2.web.vo.HostCreateParameters` *)* The
    parameters used for the add Windows host operation.
    """
    def __init__(self, undef_enabled=True):
        super(WindowsHostCreateParameters, self).__init__()
        self._type = ("WindowsHostCreateParameters", True)
        self._connector_certificate_password = (self.__undef__, True)
        self._connector_keystore = (self.__undef__, True)
        self._connector_keystore_password = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(WindowsHostCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._connector_certificate_password = (data.get("connectorCertificatePassword", obj.__undef__), dirty)
        if obj._connector_certificate_password[0] is not None and obj._connector_certificate_password[0] is not obj.__undef__:
            assert isinstance(obj._connector_certificate_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connector_certificate_password[0], type(obj._connector_certificate_password[0])))
            common.validate_format(obj._connector_certificate_password[0], "None", None, None)
        obj._connector_keystore = (data.get("connectorKeystore", obj.__undef__), dirty)
        if obj._connector_keystore[0] is not None and obj._connector_keystore[0] is not obj.__undef__:
            assert isinstance(obj._connector_keystore[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connector_keystore[0], type(obj._connector_keystore[0])))
            common.validate_format(obj._connector_keystore[0], "None", None, None)
        obj._connector_keystore_password = (data.get("connectorKeystorePassword", obj.__undef__), dirty)
        if obj._connector_keystore_password[0] is not None and obj._connector_keystore_password[0] is not obj.__undef__:
            assert isinstance(obj._connector_keystore_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connector_keystore_password[0], type(obj._connector_keystore_password[0])))
            common.validate_format(obj._connector_keystore_password[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(WindowsHostCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "connector_certificate_password" == "type" or (self.connector_certificate_password is not self.__undef__ and (not (dirty and not self._connector_certificate_password[1]) or isinstance(self.connector_certificate_password, list) or belongs_to_parent)):
            dct["connectorCertificatePassword"] = dictify(self.connector_certificate_password)
        if "connector_keystore" == "type" or (self.connector_keystore is not self.__undef__ and (not (dirty and not self._connector_keystore[1]) or isinstance(self.connector_keystore, list) or belongs_to_parent)):
            dct["connectorKeystore"] = dictify(self.connector_keystore)
        if "connector_keystore_password" == "type" or (self.connector_keystore_password is not self.__undef__ and (not (dirty and not self._connector_keystore_password[1]) or isinstance(self.connector_keystore_password, list) or belongs_to_parent)):
            dct["connectorKeystorePassword"] = dictify(self.connector_keystore_password)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._connector_certificate_password = (self._connector_certificate_password[0], True)
        self._connector_keystore = (self._connector_keystore[0], True)
        self._connector_keystore_password = (self._connector_keystore_password[0], True)

    def is_dirty(self):
        return any([self._connector_certificate_password[1], self._connector_keystore[1], self._connector_keystore_password[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, WindowsHostCreateParameters):
            return False
        return super(WindowsHostCreateParameters, self).__eq__(other) and \
               self.connector_certificate_password == other.connector_certificate_password and \
               self.connector_keystore == other.connector_keystore and \
               self.connector_keystore_password == other.connector_keystore_password

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def connector_certificate_password(self):
        """
        Password for the certificate in the Java Keystore.

        :rtype: ``TEXT_TYPE``
        """
        return self._connector_certificate_password[0]

    @connector_certificate_password.setter
    def connector_certificate_password(self, value):
        self._connector_certificate_password = (value, True)

    @property
    def connector_keystore(self):
        """
        Byte array of the Java Keystore data.

        :rtype: ``TEXT_TYPE``
        """
        return self._connector_keystore[0]

    @connector_keystore.setter
    def connector_keystore(self, value):
        self._connector_keystore = (value, True)

    @property
    def connector_keystore_password(self):
        """
        Password for the Java Keystore data.

        :rtype: ``TEXT_TYPE``
        """
        return self._connector_keystore_password[0]

    @connector_keystore_password.setter
    def connector_keystore_password(self, value):
        self._connector_keystore_password = (value, True)

