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
#     /delphix-dns-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_2.web.objects.TypedObject import TypedObject
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

class DNSConfig(TypedObject):
    """
    *(extends* :py:class:`v1_6_2.web.vo.TypedObject` *)* DNS Client
    Configuration.
    """
    def __init__(self, undef_enabled=True):
        super(DNSConfig, self).__init__()
        self._type = ("DNSConfig", True)
        self._domain = (self.__undef__, True)
        self._servers = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DNSConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._domain = []
        for item in data.get("domain") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._domain.append(item)
        obj._domain = (obj._domain, dirty)
        obj._servers = []
        for item in data.get("servers") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "ipAddress", None, None)
            obj._servers.append(item)
        obj._servers = (obj._servers, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DNSConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "domain" == "type" or (self.domain is not self.__undef__ and (not (dirty and not self._domain[1]) or isinstance(self.domain, list) or belongs_to_parent)):
            dct["domain"] = dictify(self.domain, prop_is_list_or_vo=True)
        if "servers" == "type" or (self.servers is not self.__undef__ and (not (dirty and not self._servers[1]) or isinstance(self.servers, list) or belongs_to_parent)):
            dct["servers"] = dictify(self.servers, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._domain = (self._domain[0], True)
        self._servers = (self._servers[0], True)

    def is_dirty(self):
        return any([self._domain[1], self._servers[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DNSConfig):
            return False
        return super(DNSConfig, self).__eq__(other) and \
               self.domain == other.domain and \
               self.servers == other.servers

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def domain(self):
        """
        One of more DNS domain names.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._domain[0]

    @domain.setter
    def domain(self, value):
        self._domain = (value, True)

    @property
    def servers(self):
        """
        List of DNS servers.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._servers[0]

    @servers.setter
    def servers(self, value):
        self._servers = (value, True)

