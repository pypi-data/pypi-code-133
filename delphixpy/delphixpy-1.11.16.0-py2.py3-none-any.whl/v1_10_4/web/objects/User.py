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
#     /delphix-user.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_10_4 import factory
from delphixpy.v1_10_4 import common

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

class User(NamedUserObject):
    """
    *(extends* :py:class:`v1_10_4.web.vo.NamedUserObject` *)* Delphix users.
    """
    def __init__(self, undef_enabled=True):
        super(User, self).__init__()
        self._type = ("User", True)
        self._user_type = (self.__undef__, True)
        self._email_address = (self.__undef__, True)
        self._enabled = (self.__undef__, True)
        self._first_name = (self.__undef__, True)
        self._last_name = (self.__undef__, True)
        self._password_update_request = (self.__undef__, True)
        self._is_default = (self.__undef__, True)
        self._mobile_phone_number = (self.__undef__, True)
        self._work_phone_number = (self.__undef__, True)
        self._home_phone_number = (self.__undef__, True)
        self._authentication_type = (self.__undef__, True)
        self._principal = (self.__undef__, True)
        self._credential = (self.__undef__, True)
        self._public_key = (self.__undef__, True)
        self._session_timeout = (self.__undef__, True)
        self._locale = (self.__undef__, True)
        self._api_user = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(User, cls).from_dict(data, dirty, undef_enabled)
        obj._user_type = (data.get("userType", obj.__undef__), dirty)
        if obj._user_type[0] is not None and obj._user_type[0] is not obj.__undef__:
            assert isinstance(obj._user_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user_type[0], type(obj._user_type[0])))
            assert obj._user_type[0] in ['SYSTEM', 'DOMAIN'], "Expected enum ['SYSTEM', 'DOMAIN'] but got %s" % obj._user_type[0]
            common.validate_format(obj._user_type[0], "None", None, None)
        obj._email_address = (data.get("emailAddress", obj.__undef__), dirty)
        if obj._email_address[0] is not None and obj._email_address[0] is not obj.__undef__:
            assert isinstance(obj._email_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._email_address[0], type(obj._email_address[0])))
            common.validate_format(obj._email_address[0], "email", None, 256)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._first_name = (data.get("firstName", obj.__undef__), dirty)
        if obj._first_name[0] is not None and obj._first_name[0] is not obj.__undef__:
            assert isinstance(obj._first_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._first_name[0], type(obj._first_name[0])))
            common.validate_format(obj._first_name[0], "None", None, 64)
        obj._last_name = (data.get("lastName", obj.__undef__), dirty)
        if obj._last_name[0] is not None and obj._last_name[0] is not obj.__undef__:
            assert isinstance(obj._last_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_name[0], type(obj._last_name[0])))
            common.validate_format(obj._last_name[0], "None", None, 64)
        obj._password_update_request = (data.get("passwordUpdateRequest", obj.__undef__), dirty)
        if obj._password_update_request[0] is not None and obj._password_update_request[0] is not obj.__undef__:
            assert isinstance(obj._password_update_request[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._password_update_request[0], type(obj._password_update_request[0])))
            assert obj._password_update_request[0] in ['NONE', 'FIRST_LOGIN', 'ADMIN_REQUEST', 'PASSWORD_POLICY'], "Expected enum ['NONE', 'FIRST_LOGIN', 'ADMIN_REQUEST', 'PASSWORD_POLICY'] but got %s" % obj._password_update_request[0]
            common.validate_format(obj._password_update_request[0], "None", None, None)
        obj._is_default = (data.get("isDefault", obj.__undef__), dirty)
        if obj._is_default[0] is not None and obj._is_default[0] is not obj.__undef__:
            assert isinstance(obj._is_default[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._is_default[0], type(obj._is_default[0])))
            common.validate_format(obj._is_default[0], "None", None, None)
        obj._mobile_phone_number = (data.get("mobilePhoneNumber", obj.__undef__), dirty)
        if obj._mobile_phone_number[0] is not None and obj._mobile_phone_number[0] is not obj.__undef__:
            assert isinstance(obj._mobile_phone_number[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mobile_phone_number[0], type(obj._mobile_phone_number[0])))
            common.validate_format(obj._mobile_phone_number[0], "None", None, 32)
        obj._work_phone_number = (data.get("workPhoneNumber", obj.__undef__), dirty)
        if obj._work_phone_number[0] is not None and obj._work_phone_number[0] is not obj.__undef__:
            assert isinstance(obj._work_phone_number[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._work_phone_number[0], type(obj._work_phone_number[0])))
            common.validate_format(obj._work_phone_number[0], "None", None, 32)
        obj._home_phone_number = (data.get("homePhoneNumber", obj.__undef__), dirty)
        if obj._home_phone_number[0] is not None and obj._home_phone_number[0] is not obj.__undef__:
            assert isinstance(obj._home_phone_number[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._home_phone_number[0], type(obj._home_phone_number[0])))
            common.validate_format(obj._home_phone_number[0], "None", None, 32)
        obj._authentication_type = (data.get("authenticationType", obj.__undef__), dirty)
        if obj._authentication_type[0] is not None and obj._authentication_type[0] is not obj.__undef__:
            assert isinstance(obj._authentication_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._authentication_type[0], type(obj._authentication_type[0])))
            assert obj._authentication_type[0] in ['LDAP', 'NATIVE', 'SAML'], "Expected enum ['LDAP', 'NATIVE', 'SAML'] but got %s" % obj._authentication_type[0]
            common.validate_format(obj._authentication_type[0], "None", None, None)
        obj._principal = (data.get("principal", obj.__undef__), dirty)
        if obj._principal[0] is not None and obj._principal[0] is not obj.__undef__:
            assert isinstance(obj._principal[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._principal[0], type(obj._principal[0])))
            common.validate_format(obj._principal[0], "None", None, None)
        if "credential" in data and data["credential"] is not None:
            obj._credential = (factory.create_object(data["credential"], "PasswordCredential"), dirty)
            factory.validate_type(obj._credential[0], "PasswordCredential")
        else:
            obj._credential = (obj.__undef__, dirty)
        obj._public_key = []
        for item in data.get("publicKey") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "hostKey", None, None)
            obj._public_key.append(item)
        obj._public_key = (obj._public_key, dirty)
        obj._session_timeout = (data.get("sessionTimeout", obj.__undef__), dirty)
        if obj._session_timeout[0] is not None and obj._session_timeout[0] is not obj.__undef__:
            assert isinstance(obj._session_timeout[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._session_timeout[0], type(obj._session_timeout[0])))
            common.validate_format(obj._session_timeout[0], "None", None, None)
        obj._locale = (data.get("locale", obj.__undef__), dirty)
        if obj._locale[0] is not None and obj._locale[0] is not obj.__undef__:
            assert isinstance(obj._locale[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._locale[0], type(obj._locale[0])))
            common.validate_format(obj._locale[0], "locale", None, 16)
        obj._api_user = (data.get("apiUser", obj.__undef__), dirty)
        if obj._api_user[0] is not None and obj._api_user[0] is not obj.__undef__:
            assert isinstance(obj._api_user[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._api_user[0], type(obj._api_user[0])))
            common.validate_format(obj._api_user[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(User, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "user_type" == "type" or (self.user_type is not self.__undef__ and (not (dirty and not self._user_type[1]) or isinstance(self.user_type, list) or belongs_to_parent)):
            dct["userType"] = dictify(self.user_type)
        elif belongs_to_parent and self.user_type is self.__undef__:
            dct["userType"] = "DOMAIN"
        if "email_address" == "type" or (self.email_address is not self.__undef__ and (not (dirty and not self._email_address[1]) or isinstance(self.email_address, list) or belongs_to_parent)):
            dct["emailAddress"] = dictify(self.email_address)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]) or isinstance(self.enabled, list) or belongs_to_parent)):
            dct["enabled"] = dictify(self.enabled)
        elif belongs_to_parent and self.enabled is self.__undef__:
            dct["enabled"] = True
        if "first_name" == "type" or (self.first_name is not self.__undef__ and (not (dirty and not self._first_name[1]) or isinstance(self.first_name, list) or belongs_to_parent)):
            dct["firstName"] = dictify(self.first_name)
        if "last_name" == "type" or (self.last_name is not self.__undef__ and (not (dirty and not self._last_name[1]) or isinstance(self.last_name, list) or belongs_to_parent)):
            dct["lastName"] = dictify(self.last_name)
        if "password_update_request" == "type" or (self.password_update_request is not self.__undef__ and (not (dirty and not self._password_update_request[1]) or isinstance(self.password_update_request, list) or belongs_to_parent)):
            dct["passwordUpdateRequest"] = dictify(self.password_update_request)
        elif belongs_to_parent and self.password_update_request is self.__undef__:
            dct["passwordUpdateRequest"] = "NONE"
        if "is_default" == "type" or (self.is_default is not self.__undef__ and (not (dirty and not self._is_default[1]) or isinstance(self.is_default, list) or belongs_to_parent)):
            dct["isDefault"] = dictify(self.is_default)
        if "mobile_phone_number" == "type" or (self.mobile_phone_number is not self.__undef__ and (not (dirty and not self._mobile_phone_number[1]) or isinstance(self.mobile_phone_number, list) or belongs_to_parent)):
            dct["mobilePhoneNumber"] = dictify(self.mobile_phone_number)
        if "work_phone_number" == "type" or (self.work_phone_number is not self.__undef__ and (not (dirty and not self._work_phone_number[1]) or isinstance(self.work_phone_number, list) or belongs_to_parent)):
            dct["workPhoneNumber"] = dictify(self.work_phone_number)
        if "home_phone_number" == "type" or (self.home_phone_number is not self.__undef__ and (not (dirty and not self._home_phone_number[1]) or isinstance(self.home_phone_number, list) or belongs_to_parent)):
            dct["homePhoneNumber"] = dictify(self.home_phone_number)
        if "authentication_type" == "type" or (self.authentication_type is not self.__undef__ and (not (dirty and not self._authentication_type[1]) or isinstance(self.authentication_type, list) or belongs_to_parent)):
            dct["authenticationType"] = dictify(self.authentication_type)
        if "principal" == "type" or (self.principal is not self.__undef__ and (not (dirty and not self._principal[1]) or isinstance(self.principal, list) or belongs_to_parent)):
            dct["principal"] = dictify(self.principal)
        if "credential" == "type" or (self.credential is not self.__undef__ and (not (dirty and not self._credential[1]) or isinstance(self.credential, list) or belongs_to_parent)):
            dct["credential"] = dictify(self.credential, prop_is_list_or_vo=True)
        if "public_key" == "type" or (self.public_key is not self.__undef__ and (not (dirty and not self._public_key[1]) or isinstance(self.public_key, list) or belongs_to_parent)):
            dct["publicKey"] = dictify(self.public_key, prop_is_list_or_vo=True)
        if "session_timeout" == "type" or (self.session_timeout is not self.__undef__ and (not (dirty and not self._session_timeout[1]) or isinstance(self.session_timeout, list) or belongs_to_parent)):
            dct["sessionTimeout"] = dictify(self.session_timeout)
        elif belongs_to_parent and self.session_timeout is self.__undef__:
            dct["sessionTimeout"] = 30
        if "locale" == "type" or (self.locale is not self.__undef__ and (not (dirty and not self._locale[1]) or isinstance(self.locale, list) or belongs_to_parent)):
            dct["locale"] = dictify(self.locale)
        elif belongs_to_parent and self.locale is self.__undef__:
            dct["locale"] = "en-US"
        if "api_user" == "type" or (self.api_user is not self.__undef__ and (not (dirty and not self._api_user[1]) or isinstance(self.api_user, list) or belongs_to_parent)):
            dct["apiUser"] = dictify(self.api_user)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._user_type = (self._user_type[0], True)
        self._email_address = (self._email_address[0], True)
        self._enabled = (self._enabled[0], True)
        self._first_name = (self._first_name[0], True)
        self._last_name = (self._last_name[0], True)
        self._password_update_request = (self._password_update_request[0], True)
        self._is_default = (self._is_default[0], True)
        self._mobile_phone_number = (self._mobile_phone_number[0], True)
        self._work_phone_number = (self._work_phone_number[0], True)
        self._home_phone_number = (self._home_phone_number[0], True)
        self._authentication_type = (self._authentication_type[0], True)
        self._principal = (self._principal[0], True)
        self._credential = (self._credential[0], True)
        self._public_key = (self._public_key[0], True)
        self._session_timeout = (self._session_timeout[0], True)
        self._locale = (self._locale[0], True)
        self._api_user = (self._api_user[0], True)

    def is_dirty(self):
        return any([self._user_type[1], self._email_address[1], self._enabled[1], self._first_name[1], self._last_name[1], self._password_update_request[1], self._is_default[1], self._mobile_phone_number[1], self._work_phone_number[1], self._home_phone_number[1], self._authentication_type[1], self._principal[1], self._credential[1], self._public_key[1], self._session_timeout[1], self._locale[1], self._api_user[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, User):
            return False
        return super(User, self).__eq__(other) and \
               self.user_type == other.user_type and \
               self.email_address == other.email_address and \
               self.enabled == other.enabled and \
               self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.password_update_request == other.password_update_request and \
               self.is_default == other.is_default and \
               self.mobile_phone_number == other.mobile_phone_number and \
               self.work_phone_number == other.work_phone_number and \
               self.home_phone_number == other.home_phone_number and \
               self.authentication_type == other.authentication_type and \
               self.principal == other.principal and \
               self.credential == other.credential and \
               self.public_key == other.public_key and \
               self.session_timeout == other.session_timeout and \
               self.locale == other.locale and \
               self.api_user == other.api_user

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def user_type(self):
        """
        *(default value: DOMAIN)* Type of user. *(permitted values: SYSTEM,
        DOMAIN)*

        :rtype: ``TEXT_TYPE``
        """
        return self._user_type[0]

    @user_type.setter
    def user_type(self, value):
        self._user_type = (value, True)

    @property
    def email_address(self):
        """
        Email address for the user.

        :rtype: ``TEXT_TYPE``
        """
        return self._email_address[0]

    @email_address.setter
    def email_address(self, value):
        self._email_address = (value, True)

    @property
    def enabled(self):
        """
        *(default value: True)* True if the user is currently enabled and can
        log into the system.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def first_name(self):
        """
        First name of user.

        :rtype: ``TEXT_TYPE``
        """
        return self._first_name[0]

    @first_name.setter
    def first_name(self, value):
        self._first_name = (value, True)

    @property
    def last_name(self):
        """
        Last name of user.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_name[0]

    @last_name.setter
    def last_name(self, value):
        self._last_name = (value, True)

    @property
    def password_update_request(self):
        """
        *(default value: NONE)* Whether the user's password should be updated
        and why. *(permitted values: NONE, FIRST_LOGIN, ADMIN_REQUEST,
        PASSWORD_POLICY)*

        :rtype: ``TEXT_TYPE``
        """
        return self._password_update_request[0]

    @password_update_request.setter
    def password_update_request(self, value):
        self._password_update_request = (value, True)

    @property
    def is_default(self):
        """
        True if this is the default user and cannot be deleted.

        :rtype: ``bool``
        """
        return self._is_default[0]

    @is_default.setter
    def is_default(self, value):
        self._is_default = (value, True)

    @property
    def mobile_phone_number(self):
        """
        Mobile phone number of user.

        :rtype: ``TEXT_TYPE``
        """
        return self._mobile_phone_number[0]

    @mobile_phone_number.setter
    def mobile_phone_number(self, value):
        self._mobile_phone_number = (value, True)

    @property
    def work_phone_number(self):
        """
        Work phone number of user.

        :rtype: ``TEXT_TYPE``
        """
        return self._work_phone_number[0]

    @work_phone_number.setter
    def work_phone_number(self, value):
        self._work_phone_number = (value, True)

    @property
    def home_phone_number(self):
        """
        Home phone number of user.

        :rtype: ``TEXT_TYPE``
        """
        return self._home_phone_number[0]

    @home_phone_number.setter
    def home_phone_number(self, value):
        self._home_phone_number = (value, True)

    @property
    def authentication_type(self):
        """
        User authentication type. *(permitted values: LDAP, NATIVE, SAML)*

        :rtype: ``TEXT_TYPE``
        """
        return self._authentication_type[0]

    @authentication_type.setter
    def authentication_type(self, value):
        self._authentication_type = (value, True)

    @property
    def principal(self):
        """
        Principal name used for authentication.

        :rtype: ``TEXT_TYPE``
        """
        return self._principal[0]

    @principal.setter
    def principal(self, value):
        self._principal = (value, True)

    @property
    def credential(self):
        """
        Credential used for authentication.

        :rtype: :py:class:`v1_10_4.web.vo.PasswordCredential`
        """
        return self._credential[0]

    @credential.setter
    def credential(self, value):
        self._credential = (value, True)

    @property
    def public_key(self):
        """
        Public key used for authentication.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._public_key[0]

    @public_key.setter
    def public_key(self, value):
        self._public_key = (value, True)

    @property
    def session_timeout(self):
        """
        *(default value: 30)* Session timeout in minutes.

        :rtype: ``int``
        """
        return self._session_timeout[0]

    @session_timeout.setter
    def session_timeout(self, value):
        self._session_timeout = (value, True)

    @property
    def locale(self):
        """
        *(default value: en-US)* Preferred locale as an IETF BCP 47 language
        tag, defaults to 'en-US'.

        :rtype: ``TEXT_TYPE``
        """
        return self._locale[0]

    @locale.setter
    def locale(self, value):
        self._locale = (value, True)

    @property
    def api_user(self):
        """
        If the Delphix Engine has been configured for SSO, only users with this
        property set can authenticate with a username and password for API or
        CLI access.

        :rtype: ``bool``
        """
        return self._api_user[0]

    @api_user.setter
    def api_user(self, value):
        self._api_user = (value, True)

