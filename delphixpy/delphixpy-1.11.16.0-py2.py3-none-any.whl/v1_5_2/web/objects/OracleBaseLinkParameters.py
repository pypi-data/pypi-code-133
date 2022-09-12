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
#     /delphix-oracle-base-link-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_2.web.objects.LinkParameters import LinkParameters
from delphixpy.v1_5_2 import factory
from delphixpy.v1_5_2 import common

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

class OracleBaseLinkParameters(LinkParameters):
    """
    *(extends* :py:class:`v1_5_2.web.vo.LinkParameters` *)* Represents common
    parameters to link all Oracle databases.
    """
    def __init__(self, undef_enabled=True):
        super(OracleBaseLinkParameters, self).__init__()
        self._type = ("OracleBaseLinkParameters", True)
        self._container = (self.__undef__, True)
        self._db_credentials = (self.__undef__, True)
        self._db_user = (self.__undef__, True)
        self._environment_user = (self.__undef__, True)
        self._link_now = (self.__undef__, True)
        self._source = (self.__undef__, True)

    API_VERSION = "1.5.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleBaseLinkParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "OracleDatabaseContainer"), dirty)
            factory.validate_type(obj._container[0], "OracleDatabaseContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "dbCredentials" not in data:
            raise ValueError("Missing required property \"dbCredentials\".")
        if "dbCredentials" in data and data["dbCredentials"] is not None:
            obj._db_credentials = (factory.create_object(data["dbCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._db_credentials[0], "PasswordCredential")
        else:
            obj._db_credentials = (obj.__undef__, dirty)
        if "dbUser" not in data:
            raise ValueError("Missing required property \"dbUser\".")
        obj._db_user = (data.get("dbUser", obj.__undef__), dirty)
        if obj._db_user[0] is not None and obj._db_user[0] is not obj.__undef__:
            assert isinstance(obj._db_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._db_user[0], type(obj._db_user[0])))
            common.validate_format(obj._db_user[0], "None", None, None)
        if "environmentUser" not in data:
            raise ValueError("Missing required property \"environmentUser\".")
        obj._environment_user = (data.get("environmentUser", obj.__undef__), dirty)
        if obj._environment_user[0] is not None and obj._environment_user[0] is not obj.__undef__:
            assert isinstance(obj._environment_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment_user[0], type(obj._environment_user[0])))
            common.validate_format(obj._environment_user[0], "objectReference", None, None)
        obj._link_now = (data.get("linkNow", obj.__undef__), dirty)
        if obj._link_now[0] is not None and obj._link_now[0] is not obj.__undef__:
            assert isinstance(obj._link_now[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._link_now[0], type(obj._link_now[0])))
            common.validate_format(obj._link_now[0], "None", None, None)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "OracleLinkedSource"), dirty)
            factory.validate_type(obj._source[0], "OracleLinkedSource")
        else:
            obj._source = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleBaseLinkParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "db_credentials" == "type" or (self.db_credentials is not self.__undef__ and (not (dirty and not self._db_credentials[1]) or isinstance(self.db_credentials, list) or belongs_to_parent)):
            dct["dbCredentials"] = dictify(self.db_credentials, prop_is_list_or_vo=True)
        if "db_user" == "type" or (self.db_user is not self.__undef__ and (not (dirty and not self._db_user[1]) or isinstance(self.db_user, list) or belongs_to_parent)):
            dct["dbUser"] = dictify(self.db_user)
        if "environment_user" == "type" or (self.environment_user is not self.__undef__ and (not (dirty and not self._environment_user[1]) or isinstance(self.environment_user, list) or belongs_to_parent)):
            dct["environmentUser"] = dictify(self.environment_user)
        if "link_now" == "type" or (self.link_now is not self.__undef__ and (not (dirty and not self._link_now[1]) or isinstance(self.link_now, list) or belongs_to_parent)):
            dct["linkNow"] = dictify(self.link_now)
        elif belongs_to_parent and self.link_now is self.__undef__:
            dct["linkNow"] = False
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._db_credentials = (self._db_credentials[0], True)
        self._db_user = (self._db_user[0], True)
        self._environment_user = (self._environment_user[0], True)
        self._link_now = (self._link_now[0], True)
        self._source = (self._source[0], True)

    def is_dirty(self):
        return any([self._container[1], self._db_credentials[1], self._db_user[1], self._environment_user[1], self._link_now[1], self._source[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleBaseLinkParameters):
            return False
        return super(OracleBaseLinkParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.db_credentials == other.db_credentials and \
               self.db_user == other.db_user and \
               self.environment_user == other.environment_user and \
               self.link_now == other.link_now and \
               self.source == other.source

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        Container to create as part of the linking process.

        :rtype: :py:class:`v1_5_2.web.vo.OracleDatabaseContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def db_credentials(self):
        """
        The password for the DB user.

        :rtype: :py:class:`v1_5_2.web.vo.PasswordCredential`
        """
        return self._db_credentials[0]

    @db_credentials.setter
    def db_credentials(self, value):
        self._db_credentials = (value, True)

    @property
    def db_user(self):
        """
        The name of the DB user.

        :rtype: ``TEXT_TYPE``
        """
        return self._db_user[0]

    @db_user.setter
    def db_user(self, value):
        self._db_user = (value, True)

    @property
    def environment_user(self):
        """
        Information about the OS user to use for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment_user[0]

    @environment_user.setter
    def environment_user(self, value):
        self._environment_user = (value, True)

    @property
    def link_now(self):
        """
        True if initial load should be done immediately.

        :rtype: ``bool``
        """
        return self._link_now[0]

    @link_now.setter
    def link_now(self, value):
        self._link_now = (value, True)

    @property
    def source(self):
        """
        Source to link the container to. This must reference an existing linked
        source config.

        :rtype: :py:class:`v1_5_2.web.vo.OracleLinkedSource`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

