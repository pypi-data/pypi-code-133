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
#     /delphix-ase-instance.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.SourceRepository import SourceRepository
from delphixpy.v1_8_1 import factory
from delphixpy.v1_8_1 import common

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

class ASEInstance(SourceRepository):
    """
    *(extends* :py:class:`v1_8_1.web.vo.SourceRepository` *)* The SAP ASE
    source repository.
    """
    def __init__(self, undef_enabled=True):
        super(ASEInstance, self).__init__()
        self._type = ("ASEInstance", True)
        self._credentials = (self.__undef__, True)
        self._db_user = (self.__undef__, True)
        self._installation_path = (self.__undef__, True)
        self._instance_name = (self.__undef__, True)
        self._instance_owner = (self.__undef__, True)
        self._internal_version = (self.__undef__, True)
        self._page_size = (self.__undef__, True)
        self._ports = (self.__undef__, True)
        self._server_name = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASEInstance, cls).from_dict(data, dirty, undef_enabled)
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._credentials[0], "PasswordCredential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        obj._db_user = (data.get("dbUser", obj.__undef__), dirty)
        if obj._db_user[0] is not None and obj._db_user[0] is not obj.__undef__:
            assert isinstance(obj._db_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._db_user[0], type(obj._db_user[0])))
            common.validate_format(obj._db_user[0], "None", None, 256)
        obj._installation_path = (data.get("installationPath", obj.__undef__), dirty)
        if obj._installation_path[0] is not None and obj._installation_path[0] is not obj.__undef__:
            assert isinstance(obj._installation_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._installation_path[0], type(obj._installation_path[0])))
            common.validate_format(obj._installation_path[0], "None", None, None)
        obj._instance_name = (data.get("instanceName", obj.__undef__), dirty)
        if obj._instance_name[0] is not None and obj._instance_name[0] is not obj.__undef__:
            assert isinstance(obj._instance_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._instance_name[0], type(obj._instance_name[0])))
            common.validate_format(obj._instance_name[0], "None", None, None)
        obj._instance_owner = (data.get("instanceOwner", obj.__undef__), dirty)
        if obj._instance_owner[0] is not None and obj._instance_owner[0] is not obj.__undef__:
            assert isinstance(obj._instance_owner[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._instance_owner[0], type(obj._instance_owner[0])))
            common.validate_format(obj._instance_owner[0], "None", None, None)
        obj._internal_version = (data.get("internalVersion", obj.__undef__), dirty)
        if obj._internal_version[0] is not None and obj._internal_version[0] is not obj.__undef__:
            assert isinstance(obj._internal_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._internal_version[0], type(obj._internal_version[0])))
            common.validate_format(obj._internal_version[0], "None", None, None)
        obj._page_size = (data.get("pageSize", obj.__undef__), dirty)
        if obj._page_size[0] is not None and obj._page_size[0] is not obj.__undef__:
            assert isinstance(obj._page_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._page_size[0], type(obj._page_size[0])))
            common.validate_format(obj._page_size[0], "None", None, None)
        obj._ports = []
        for item in data.get("ports") or []:
            assert isinstance(item, int), ("Expected one of ['integer'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._ports.append(item)
        obj._ports = (obj._ports, dirty)
        obj._server_name = (data.get("serverName", obj.__undef__), dirty)
        if obj._server_name[0] is not None and obj._server_name[0] is not obj.__undef__:
            assert isinstance(obj._server_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._server_name[0], type(obj._server_name[0])))
            common.validate_format(obj._server_name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASEInstance, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials, prop_is_list_or_vo=True)
        if "db_user" == "type" or (self.db_user is not self.__undef__ and (not (dirty and not self._db_user[1]) or isinstance(self.db_user, list) or belongs_to_parent)):
            dct["dbUser"] = dictify(self.db_user)
        if "installation_path" == "type" or (self.installation_path is not self.__undef__ and (not (dirty and not self._installation_path[1]))):
            dct["installationPath"] = dictify(self.installation_path)
        if "instance_name" == "type" or (self.instance_name is not self.__undef__ and (not (dirty and not self._instance_name[1]))):
            dct["instanceName"] = dictify(self.instance_name)
        if "instance_owner" == "type" or (self.instance_owner is not self.__undef__ and (not (dirty and not self._instance_owner[1]))):
            dct["instanceOwner"] = dictify(self.instance_owner)
        if "internal_version" == "type" or (self.internal_version is not self.__undef__ and (not (dirty and not self._internal_version[1]))):
            dct["internalVersion"] = dictify(self.internal_version)
        if "page_size" == "type" or (self.page_size is not self.__undef__ and (not (dirty and not self._page_size[1]) or isinstance(self.page_size, list) or belongs_to_parent)):
            dct["pageSize"] = dictify(self.page_size)
        if "ports" == "type" or (self.ports is not self.__undef__ and (not (dirty and not self._ports[1]))):
            dct["ports"] = dictify(self.ports)
        if "server_name" == "type" or (self.server_name is not self.__undef__ and (not (dirty and not self._server_name[1]))):
            dct["serverName"] = dictify(self.server_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._credentials = (self._credentials[0], True)
        self._db_user = (self._db_user[0], True)
        self._installation_path = (self._installation_path[0], True)
        self._instance_name = (self._instance_name[0], True)
        self._instance_owner = (self._instance_owner[0], True)
        self._internal_version = (self._internal_version[0], True)
        self._page_size = (self._page_size[0], True)
        self._ports = (self._ports[0], True)
        self._server_name = (self._server_name[0], True)

    def is_dirty(self):
        return any([self._credentials[1], self._db_user[1], self._installation_path[1], self._instance_name[1], self._instance_owner[1], self._internal_version[1], self._page_size[1], self._ports[1], self._server_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASEInstance):
            return False
        return super(ASEInstance, self).__eq__(other) and \
               self.credentials == other.credentials and \
               self.db_user == other.db_user and \
               self.installation_path == other.installation_path and \
               self.instance_name == other.instance_name and \
               self.instance_owner == other.instance_owner and \
               self.internal_version == other.internal_version and \
               self.page_size == other.page_size and \
               self.ports == other.ports and \
               self.server_name == other.server_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def credentials(self):
        """
        The password of the database user.

        :rtype: :py:class:`v1_8_1.web.vo.PasswordCredential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

    @property
    def db_user(self):
        """
        The username of the database user.

        :rtype: ``TEXT_TYPE``
        """
        return self._db_user[0]

    @db_user.setter
    def db_user(self, value):
        self._db_user = (value, True)

    @property
    def installation_path(self):
        """
        The SAP ASE instance home.

        :rtype: ``TEXT_TYPE``
        """
        return self._installation_path[0]

    @installation_path.setter
    def installation_path(self, value):
        self._installation_path = (value, True)

    @property
    def instance_name(self):
        """
        The name of the SAP ASE instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._instance_name[0]

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = (value, True)

    @property
    def instance_owner(self):
        """
        Account the SAP ASE instance is running as.

        :rtype: ``TEXT_TYPE``
        """
        return self._instance_owner[0]

    @instance_owner.setter
    def instance_owner(self, value):
        self._instance_owner = (value, True)

    @property
    def internal_version(self):
        """
        Internal version of the SAP ASE instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._internal_version[0]

    @internal_version.setter
    def internal_version(self, value):
        self._internal_version = (value, True)

    @property
    def page_size(self):
        """
        Database page size for the SAP ASE instance.

        :rtype: ``int``
        """
        return self._page_size[0]

    @page_size.setter
    def page_size(self, value):
        self._page_size = (value, True)

    @property
    def ports(self):
        """
        The network ports for connecting to the SAP ASE instance.

        :rtype: ``list`` of ``int``
        """
        return self._ports[0]

    @ports.setter
    def ports(self, value):
        self._ports = (value, True)

    @property
    def server_name(self):
        """
        The server name of the SAP ASE instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._server_name[0]

    @server_name.setter
    def server_name(self, value):
        self._server_name = (value, True)

