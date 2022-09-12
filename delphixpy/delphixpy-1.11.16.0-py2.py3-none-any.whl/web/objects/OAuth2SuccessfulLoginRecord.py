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
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.LoginRecord import LoginRecord
from delphixpy import common

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

class OAuth2SuccessfulLoginRecord(LoginRecord):
    """
    *(extends* :py:class:`delphixpy.web.vo.LoginRecord` *)* Represents a
    successful OAuth2 login.
    """
    def __init__(self, undef_enabled=True):
        super(OAuth2SuccessfulLoginRecord, self).__init__()
        self._type = ("OAuth2SuccessfulLoginRecord", True)
        self._user_identity_claim_value = (self.__undef__, True)
        self._issuer = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OAuth2SuccessfulLoginRecord, cls).from_dict(data, dirty, undef_enabled)
        if "userIdentityClaimValue" not in data:
            raise ValueError("Missing required property \"userIdentityClaimValue\".")
        obj._user_identity_claim_value = (data.get("userIdentityClaimValue", obj.__undef__), dirty)
        if obj._user_identity_claim_value[0] is not None and obj._user_identity_claim_value[0] is not obj.__undef__:
            assert isinstance(obj._user_identity_claim_value[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user_identity_claim_value[0], type(obj._user_identity_claim_value[0])))
            common.validate_format(obj._user_identity_claim_value[0], "None", None, None)
        if "issuer" not in data:
            raise ValueError("Missing required property \"issuer\".")
        obj._issuer = (data.get("issuer", obj.__undef__), dirty)
        if obj._issuer[0] is not None and obj._issuer[0] is not obj.__undef__:
            assert isinstance(obj._issuer[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._issuer[0], type(obj._issuer[0])))
            common.validate_format(obj._issuer[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OAuth2SuccessfulLoginRecord, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "user_identity_claim_value" == "type" or (self.user_identity_claim_value is not self.__undef__ and (not (dirty and not self._user_identity_claim_value[1]) or isinstance(self.user_identity_claim_value, list) or belongs_to_parent)):
            dct["userIdentityClaimValue"] = dictify(self.user_identity_claim_value)
        if "issuer" == "type" or (self.issuer is not self.__undef__ and (not (dirty and not self._issuer[1]) or isinstance(self.issuer, list) or belongs_to_parent)):
            dct["issuer"] = dictify(self.issuer)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._user_identity_claim_value = (self._user_identity_claim_value[0], True)
        self._issuer = (self._issuer[0], True)

    def is_dirty(self):
        return any([self._user_identity_claim_value[1], self._issuer[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OAuth2SuccessfulLoginRecord):
            return False
        return super(OAuth2SuccessfulLoginRecord, self).__eq__(other) and \
               self.user_identity_claim_value == other.user_identity_claim_value and \
               self.issuer == other.issuer

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def user_identity_claim_value(self):
        """
        Value of the OAuth2 claim that identifies the user.

        :rtype: ``TEXT_TYPE``
        """
        return self._user_identity_claim_value[0]

    @user_identity_claim_value.setter
    def user_identity_claim_value(self, value):
        self._user_identity_claim_value = (value, True)

    @property
    def issuer(self):
        """
        Issuer of the access token.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._issuer[0]

    @issuer.setter
    def issuer(self, value):
        self._issuer = (value, True)

