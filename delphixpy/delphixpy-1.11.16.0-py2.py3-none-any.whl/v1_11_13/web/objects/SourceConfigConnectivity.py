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
#     /delphix-connectivity-sourceconfig.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.AbstractSourceConfigConnectivity import AbstractSourceConfigConnectivity
from delphixpy.v1_11_13 import common

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

class SourceConfigConnectivity(AbstractSourceConfigConnectivity):
    """
    *(extends* :py:class:`v1_11_13.web.vo.AbstractSourceConfigConnectivity` *)*
    Mechanism to test JDBC connectivity to source configs.
    """
    def __init__(self, undef_enabled=True):
        super(SourceConfigConnectivity, self).__init__()
        self._type = ("SourceConfigConnectivity", True)
        self._username = (self.__undef__, True)
        self._password = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceConfigConnectivity, cls).from_dict(data, dirty, undef_enabled)
        if "username" not in data:
            raise ValueError("Missing required property \"username\".")
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "None", None, None)
        if "password" not in data:
            raise ValueError("Missing required property \"password\".")
        obj._password = (data.get("password", obj.__undef__), dirty)
        if obj._password[0] is not None and obj._password[0] is not obj.__undef__:
            assert isinstance(obj._password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._password[0], type(obj._password[0])))
            common.validate_format(obj._password[0], "password", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceConfigConnectivity, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]) or isinstance(self.username, list) or belongs_to_parent)):
            dct["username"] = dictify(self.username)
        if "password" == "type" or (self.password is not self.__undef__ and (not (dirty and not self._password[1]) or isinstance(self.password, list) or belongs_to_parent)):
            dct["password"] = dictify(self.password)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._username = (self._username[0], True)
        self._password = (self._password[0], True)

    def is_dirty(self):
        return any([self._username[1], self._password[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceConfigConnectivity):
            return False
        return super(SourceConfigConnectivity, self).__eq__(other) and \
               self.username == other.username and \
               self.password == other.password

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def username(self):
        """
        Database username.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

    @property
    def password(self):
        """
        Database password.

        :rtype: ``TEXT_TYPE``
        """
        return self._password[0]

    @password.setter
    def password(self, value):
        self._password = (value, True)

