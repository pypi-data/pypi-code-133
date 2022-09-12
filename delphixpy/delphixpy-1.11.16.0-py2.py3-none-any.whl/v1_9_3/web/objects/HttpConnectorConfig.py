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
#     /delphix-http-connector-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_3.web.objects.TypedObject import TypedObject
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

class HttpConnectorConfig(TypedObject):
    """
    *(extends* :py:class:`v1_9_3.web.vo.TypedObject` *)* Configuration for the
    HTTP and HTTPS connector of this application.
    """
    def __init__(self, undef_enabled=True):
        super(HttpConnectorConfig, self).__init__()
        self._type = ("HttpConnectorConfig", True)
        self._http_mode = (self.__undef__, True)
        self._tls_versions = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HttpConnectorConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._http_mode = (data.get("httpMode", obj.__undef__), dirty)
        if obj._http_mode[0] is not None and obj._http_mode[0] is not obj.__undef__:
            assert isinstance(obj._http_mode[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._http_mode[0], type(obj._http_mode[0])))
            assert obj._http_mode[0] in ['HTTP_ONLY', 'HTTPS_ONLY', 'HTTP_REDIRECT', 'BOTH'], "Expected enum ['HTTP_ONLY', 'HTTPS_ONLY', 'HTTP_REDIRECT', 'BOTH'] but got %s" % obj._http_mode[0]
            common.validate_format(obj._http_mode[0], "None", None, None)
        obj._tls_versions = []
        for item in data.get("tlsVersions") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            assert item in ['SSLv3', 'TLSv1', 'TLSv1_1', 'TLSv1_2'], "Expected enum ['SSLv3', 'TLSv1', 'TLSv1_1', 'TLSv1_2'] but got %s" % item
            common.validate_format(item, "None", None, None)
            obj._tls_versions.append(item)
        obj._tls_versions = (obj._tls_versions, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(HttpConnectorConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "http_mode" == "type" or (self.http_mode is not self.__undef__ and (not (dirty and not self._http_mode[1]) or isinstance(self.http_mode, list) or belongs_to_parent)):
            dct["httpMode"] = dictify(self.http_mode)
        elif belongs_to_parent and self.http_mode is self.__undef__:
            dct["httpMode"] = "BOTH"
        if "tls_versions" == "type" or (self.tls_versions is not self.__undef__ and (not (dirty and not self._tls_versions[1]) or isinstance(self.tls_versions, list) or belongs_to_parent)):
            dct["tlsVersions"] = dictify(self.tls_versions, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._http_mode = (self._http_mode[0], True)
        self._tls_versions = (self._tls_versions[0], True)

    def is_dirty(self):
        return any([self._http_mode[1], self._tls_versions[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HttpConnectorConfig):
            return False
        return super(HttpConnectorConfig, self).__eq__(other) and \
               self.http_mode == other.http_mode and \
               self.tls_versions == other.tls_versions

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def http_mode(self):
        """
        *(default value: BOTH)* Controls the HTTP(s) protocol configuration of
        this appliance. *(permitted values: HTTP_ONLY, HTTPS_ONLY,
        HTTP_REDIRECT, BOTH)*

        :rtype: ``TEXT_TYPE``
        """
        return self._http_mode[0]

    @http_mode.setter
    def http_mode(self, value):
        self._http_mode = (value, True)

    @property
    def tls_versions(self):
        """
        Version of TLS (transport layer security) enabled on this appliance.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._tls_versions[0]

    @tls_versions.setter
    def tls_versions(self, value):
        self._tls_versions = (value, True)

