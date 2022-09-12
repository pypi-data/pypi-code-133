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
#     /delphix-mssql-instance.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_3.web.objects.MSSqlRepository import MSSqlRepository
from delphixpy.v1_9_3 import common

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

class MSSqlInstance(MSSqlRepository):
    """
    *(extends* :py:class:`v1_9_3.web.vo.MSSqlRepository` *)* A SQL Server
    Instance.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlInstance, self).__init__()
        self._type = ("MSSqlInstance", True)
        self._instance_name = (self.__undef__, True)
        self._installation_path = (self.__undef__, True)
        self._server_name = (self.__undef__, True)
        self._port = (self.__undef__, True)
        self._instance_owner = (self.__undef__, True)
        self._version = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlInstance, cls).from_dict(data, dirty, undef_enabled)
        obj._instance_name = (data.get("instanceName", obj.__undef__), dirty)
        if obj._instance_name[0] is not None and obj._instance_name[0] is not obj.__undef__:
            assert isinstance(obj._instance_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._instance_name[0], type(obj._instance_name[0])))
            common.validate_format(obj._instance_name[0], "None", None, None)
        obj._installation_path = (data.get("installationPath", obj.__undef__), dirty)
        if obj._installation_path[0] is not None and obj._installation_path[0] is not obj.__undef__:
            assert isinstance(obj._installation_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._installation_path[0], type(obj._installation_path[0])))
            common.validate_format(obj._installation_path[0], "None", None, None)
        obj._server_name = (data.get("serverName", obj.__undef__), dirty)
        if obj._server_name[0] is not None and obj._server_name[0] is not obj.__undef__:
            assert isinstance(obj._server_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._server_name[0], type(obj._server_name[0])))
            common.validate_format(obj._server_name[0], "None", None, None)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        obj._instance_owner = (data.get("instanceOwner", obj.__undef__), dirty)
        if obj._instance_owner[0] is not None and obj._instance_owner[0] is not obj.__undef__:
            assert isinstance(obj._instance_owner[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._instance_owner[0], type(obj._instance_owner[0])))
            common.validate_format(obj._instance_owner[0], "None", None, None)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlInstance, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "instance_name" == "type" or (self.instance_name is not self.__undef__ and (not (dirty and not self._instance_name[1]))):
            dct["instanceName"] = dictify(self.instance_name)
        if "installation_path" == "type" or (self.installation_path is not self.__undef__ and (not (dirty and not self._installation_path[1]))):
            dct["installationPath"] = dictify(self.installation_path)
        if "server_name" == "type" or (self.server_name is not self.__undef__ and (not (dirty and not self._server_name[1]))):
            dct["serverName"] = dictify(self.server_name)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]))):
            dct["port"] = dictify(self.port)
        if "instance_owner" == "type" or (self.instance_owner is not self.__undef__ and (not (dirty and not self._instance_owner[1]))):
            dct["instanceOwner"] = dictify(self.instance_owner)
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]))):
            dct["version"] = dictify(self.version)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._instance_name = (self._instance_name[0], True)
        self._installation_path = (self._installation_path[0], True)
        self._server_name = (self._server_name[0], True)
        self._port = (self._port[0], True)
        self._instance_owner = (self._instance_owner[0], True)
        self._version = (self._version[0], True)

    def is_dirty(self):
        return any([self._instance_name[1], self._installation_path[1], self._server_name[1], self._port[1], self._instance_owner[1], self._version[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlInstance):
            return False
        return super(MSSqlInstance, self).__eq__(other) and \
               self.instance_name == other.instance_name and \
               self.installation_path == other.installation_path and \
               self.server_name == other.server_name and \
               self.port == other.port and \
               self.instance_owner == other.instance_owner and \
               self.version == other.version

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def instance_name(self):
        """
        The name of the SQL Server instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._instance_name[0]

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = (value, True)

    @property
    def installation_path(self):
        """
        The SQL Server instance home.

        :rtype: ``TEXT_TYPE``
        """
        return self._installation_path[0]

    @installation_path.setter
    def installation_path(self, value):
        self._installation_path = (value, True)

    @property
    def server_name(self):
        """
        The Servername of the SQL Server instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._server_name[0]

    @server_name.setter
    def server_name(self, value):
        self._server_name = (value, True)

    @property
    def port(self):
        """
        The network port for connecting to the SQL Server instance.

        :rtype: ``int``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

    @property
    def instance_owner(self):
        """
        Account the SQL Server instance is running as.

        :rtype: ``TEXT_TYPE``
        """
        return self._instance_owner[0]

    @instance_owner.setter
    def instance_owner(self, value):
        self._instance_owner = (value, True)

    @property
    def version(self):
        """
        The version of the SQL Server instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

