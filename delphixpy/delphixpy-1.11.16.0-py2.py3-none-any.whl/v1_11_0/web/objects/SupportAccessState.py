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
#     /delphix-supportaccessstate.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_0 import common

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

class SupportAccessState(TypedObject):
    """
    *(extends* :py:class:`v1_11_0.web.vo.TypedObject` *)* The state of the
    access to the support shell.
    """
    def __init__(self, undef_enabled=True):
        super(SupportAccessState, self).__init__()
        self._type = ("SupportAccessState", True)
        self._access_type = (self.__undef__, True)
        self._start_time = (self.__undef__, True)
        self._end_time = (self.__undef__, True)
        self._token = (self.__undef__, True)
        self._authentication_method = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SupportAccessState, cls).from_dict(data, dirty, undef_enabled)
        obj._access_type = (data.get("accessType", obj.__undef__), dirty)
        if obj._access_type[0] is not None and obj._access_type[0] is not obj.__undef__:
            assert isinstance(obj._access_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._access_type[0], type(obj._access_type[0])))
            assert obj._access_type[0] in ['DISABLED', 'ENABLED_NO_TOKEN', 'ENABLED_WITH_TOKEN'], "Expected enum ['DISABLED', 'ENABLED_NO_TOKEN', 'ENABLED_WITH_TOKEN'] but got %s" % obj._access_type[0]
            common.validate_format(obj._access_type[0], "None", None, None)
        obj._start_time = (data.get("startTime", obj.__undef__), dirty)
        if obj._start_time[0] is not None and obj._start_time[0] is not obj.__undef__:
            assert isinstance(obj._start_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._start_time[0], type(obj._start_time[0])))
            common.validate_format(obj._start_time[0], "date", None, None)
        obj._end_time = (data.get("endTime", obj.__undef__), dirty)
        if obj._end_time[0] is not None and obj._end_time[0] is not obj.__undef__:
            assert isinstance(obj._end_time[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._end_time[0], type(obj._end_time[0])))
            common.validate_format(obj._end_time[0], "date", None, None)
        obj._token = (data.get("token", obj.__undef__), dirty)
        if obj._token[0] is not None and obj._token[0] is not obj.__undef__:
            assert isinstance(obj._token[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._token[0], type(obj._token[0])))
            common.validate_format(obj._token[0], "None", None, None)
        obj._authentication_method = (data.get("authenticationMethod", obj.__undef__), dirty)
        if obj._authentication_method[0] is not None and obj._authentication_method[0] is not obj.__undef__:
            assert isinstance(obj._authentication_method[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._authentication_method[0], type(obj._authentication_method[0])))
            assert obj._authentication_method[0] in ['USERNAME_AND_PASSWORD', 'CHALLENGE_RESPONSE'], "Expected enum ['USERNAME_AND_PASSWORD', 'CHALLENGE_RESPONSE'] but got %s" % obj._authentication_method[0]
            common.validate_format(obj._authentication_method[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SupportAccessState, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "access_type" == "type" or (self.access_type is not self.__undef__ and (not (dirty and not self._access_type[1]) or isinstance(self.access_type, list) or belongs_to_parent)):
            dct["accessType"] = dictify(self.access_type)
        if "start_time" == "type" or (self.start_time is not self.__undef__ and (not (dirty and not self._start_time[1]) or isinstance(self.start_time, list) or belongs_to_parent)):
            dct["startTime"] = dictify(self.start_time)
        if "end_time" == "type" or (self.end_time is not self.__undef__ and (not (dirty and not self._end_time[1]) or isinstance(self.end_time, list) or belongs_to_parent)):
            dct["endTime"] = dictify(self.end_time)
        if "token" == "type" or (self.token is not self.__undef__ and (not (dirty and not self._token[1]) or isinstance(self.token, list) or belongs_to_parent)):
            dct["token"] = dictify(self.token)
        if "authentication_method" == "type" or (self.authentication_method is not self.__undef__ and (not (dirty and not self._authentication_method[1]))):
            dct["authenticationMethod"] = dictify(self.authentication_method)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._access_type = (self._access_type[0], True)
        self._start_time = (self._start_time[0], True)
        self._end_time = (self._end_time[0], True)
        self._token = (self._token[0], True)
        self._authentication_method = (self._authentication_method[0], True)

    def is_dirty(self):
        return any([self._access_type[1], self._start_time[1], self._end_time[1], self._token[1], self._authentication_method[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SupportAccessState):
            return False
        return super(SupportAccessState, self).__eq__(other) and \
               self.access_type == other.access_type and \
               self.start_time == other.start_time and \
               self.end_time == other.end_time and \
               self.token == other.token and \
               self.authentication_method == other.authentication_method

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def access_type(self):
        """
        How the support shell can be accessed. *(permitted values: DISABLED,
        ENABLED_NO_TOKEN, ENABLED_WITH_TOKEN)*

        :rtype: ``TEXT_TYPE``
        """
        return self._access_type[0]

    @access_type.setter
    def access_type(self, value):
        self._access_type = (value, True)

    @property
    def start_time(self):
        """
        If ENABLED_WITH_TOKEN, the time that the token will be valid.

        :rtype: ``TEXT_TYPE``
        """
        return self._start_time[0]

    @start_time.setter
    def start_time(self, value):
        self._start_time = (value, True)

    @property
    def end_time(self):
        """
        If ENABLED_WITH_TOKEN, time that the token will no longer be valid.

        :rtype: ``TEXT_TYPE``
        """
        return self._end_time[0]

    @end_time.setter
    def end_time(self, value):
        self._end_time = (value, True)

    @property
    def token(self):
        """
        If ENABLED_WITH_TOKEN, the token that must be supplied to login.

        :rtype: ``TEXT_TYPE``
        """
        return self._token[0]

    @token.setter
    def token(self, value):
        self._token = (value, True)

    @property
    def authentication_method(self):
        """
        Authentication method for the support shell. *(permitted values:
        USERNAME_AND_PASSWORD, CHALLENGE_RESPONSE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._authentication_method[0]

    @authentication_method.setter
    def authentication_method(self, value):
        self._authentication_method = (value, True)

