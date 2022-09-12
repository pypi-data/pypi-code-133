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
#     /delphix-oracle-base-db-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_1.web.objects.SourceConfig import SourceConfig
from delphixpy.v1_9_1 import factory
from delphixpy.v1_9_1 import common

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

class OracleBaseDBConfig(SourceConfig):
    """
    *(extends* :py:class:`v1_9_1.web.vo.SourceConfig` *)* The source config
    represents the dynamically discovered attributes of a base Oracle source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleBaseDBConfig, self).__init__()
        self._type = ("OracleBaseDBConfig", True)
        self._user = (self.__undef__, True)
        self._credentials = (self.__undef__, True)
        self._services = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleBaseDBConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "None", None, 30)
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._credentials[0], "PasswordCredential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        obj._services = []
        for item in data.get("services") or []:
            obj._services.append(factory.create_object(item))
            factory.validate_type(obj._services[-1], "OracleService")
        obj._services = (obj._services, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleBaseDBConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials, prop_is_list_or_vo=True)
        if "services" == "type" or (self.services is not self.__undef__ and (not (dirty and not self._services[1]) or isinstance(self.services, list) or belongs_to_parent)):
            dct["services"] = dictify(self.services, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._user = (self._user[0], True)
        self._credentials = (self._credentials[0], True)
        self._services = (self._services[0], True)

    def is_dirty(self):
        return any([self._user[1], self._credentials[1], self._services[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleBaseDBConfig):
            return False
        return super(OracleBaseDBConfig, self).__eq__(other) and \
               self.user == other.user and \
               self.credentials == other.credentials and \
               self.services == other.services

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def user(self):
        """
        The username of the database user.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def credentials(self):
        """
        The password of the database user. This must be a PasswordCredential
        instance.

        :rtype: :py:class:`v1_9_1.web.vo.PasswordCredential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

    @property
    def services(self):
        """
        The list of database services.

        :rtype: ``list`` of :py:class:`v1_9_1.web.vo.OracleService`
        """
        return self._services[0]

    @services.setter
    def services(self, value):
        self._services = (value, True)

