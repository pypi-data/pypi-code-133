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

from delphixpy.v1_11_4.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_4 import factory
from delphixpy.v1_11_4 import common

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
    *(extends* :py:class:`v1_11_4.web.vo.TypedObject` *)* Configuration for the
    HTTP and HTTPS connector of this application.
    """
    def __init__(self, undef_enabled=True):
        super(HttpConnectorConfig, self).__init__()
        self._type = ("HttpConnectorConfig", True)
        self._http_mode = (self.__undef__, True)
        self._tls_versions = (self.__undef__, True)
        self._cipher_suites = (self.__undef__, True)
        self._http_port = (self.__undef__, True)
        self._https_port = (self.__undef__, True)
        self._masking_legacy_ports = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HttpConnectorConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._http_mode = (data.get("httpMode", obj.__undef__), dirty)
        if obj._http_mode[0] is not None and obj._http_mode[0] is not obj.__undef__:
            assert isinstance(obj._http_mode[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._http_mode[0], type(obj._http_mode[0])))
            assert obj._http_mode[0] in ['HTTP_ONLY', 'HTTPS_ONLY', 'HTTP_REDIRECT', 'BOTH', 'HTTP_REDIRECT_WITH_HSTS'], "Expected enum ['HTTP_ONLY', 'HTTPS_ONLY', 'HTTP_REDIRECT', 'BOTH', 'HTTP_REDIRECT_WITH_HSTS'] but got %s" % obj._http_mode[0]
            common.validate_format(obj._http_mode[0], "None", None, None)
        obj._tls_versions = []
        for item in data.get("tlsVersions") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            assert item in ['SSLv3', 'TLSv1', 'TLSv1_1', 'TLSv1_2'], "Expected enum ['SSLv3', 'TLSv1', 'TLSv1_1', 'TLSv1_2'] but got %s" % item
            common.validate_format(item, "None", None, None)
            obj._tls_versions.append(item)
        obj._tls_versions = (obj._tls_versions, dirty)
        obj._cipher_suites = []
        for item in data.get("cipherSuites") or []:
            obj._cipher_suites.append(factory.create_object(item))
            factory.validate_type(obj._cipher_suites[-1], "CipherSuite")
        obj._cipher_suites = (obj._cipher_suites, dirty)
        obj._http_port = (data.get("httpPort", obj.__undef__), dirty)
        if obj._http_port[0] is not None and obj._http_port[0] is not obj.__undef__:
            assert isinstance(obj._http_port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._http_port[0], type(obj._http_port[0])))
            common.validate_format(obj._http_port[0], "None", None, None)
        obj._https_port = (data.get("httpsPort", obj.__undef__), dirty)
        if obj._https_port[0] is not None and obj._https_port[0] is not obj.__undef__:
            assert isinstance(obj._https_port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._https_port[0], type(obj._https_port[0])))
            common.validate_format(obj._https_port[0], "None", None, None)
        obj._masking_legacy_ports = (data.get("maskingLegacyPorts", obj.__undef__), dirty)
        if obj._masking_legacy_ports[0] is not None and obj._masking_legacy_ports[0] is not obj.__undef__:
            assert isinstance(obj._masking_legacy_ports[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._masking_legacy_ports[0], type(obj._masking_legacy_ports[0])))
            common.validate_format(obj._masking_legacy_ports[0], "None", None, None)
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
        if "cipher_suites" == "type" or (self.cipher_suites is not self.__undef__ and (not (dirty and not self._cipher_suites[1]) or isinstance(self.cipher_suites, list) or belongs_to_parent)):
            dct["cipherSuites"] = dictify(self.cipher_suites, prop_is_list_or_vo=True)
        if "http_port" == "type" or (self.http_port is not self.__undef__ and (not (dirty and not self._http_port[1]) or isinstance(self.http_port, list) or belongs_to_parent)):
            dct["httpPort"] = dictify(self.http_port)
        elif belongs_to_parent and self.http_port is self.__undef__:
            dct["httpPort"] = 80
        if "https_port" == "type" or (self.https_port is not self.__undef__ and (not (dirty and not self._https_port[1]) or isinstance(self.https_port, list) or belongs_to_parent)):
            dct["httpsPort"] = dictify(self.https_port)
        elif belongs_to_parent and self.https_port is self.__undef__:
            dct["httpsPort"] = 443
        if "masking_legacy_ports" == "type" or (self.masking_legacy_ports is not self.__undef__ and (not (dirty and not self._masking_legacy_ports[1]) or isinstance(self.masking_legacy_ports, list) or belongs_to_parent)):
            dct["maskingLegacyPorts"] = dictify(self.masking_legacy_ports)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._http_mode = (self._http_mode[0], True)
        self._tls_versions = (self._tls_versions[0], True)
        self._cipher_suites = (self._cipher_suites[0], True)
        self._http_port = (self._http_port[0], True)
        self._https_port = (self._https_port[0], True)
        self._masking_legacy_ports = (self._masking_legacy_ports[0], True)

    def is_dirty(self):
        return any([self._http_mode[1], self._tls_versions[1], self._cipher_suites[1], self._http_port[1], self._https_port[1], self._masking_legacy_ports[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HttpConnectorConfig):
            return False
        return super(HttpConnectorConfig, self).__eq__(other) and \
               self.http_mode == other.http_mode and \
               self.tls_versions == other.tls_versions and \
               self.cipher_suites == other.cipher_suites and \
               self.http_port == other.http_port and \
               self.https_port == other.https_port and \
               self.masking_legacy_ports == other.masking_legacy_ports

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
        HTTP_REDIRECT, BOTH, HTTP_REDIRECT_WITH_HSTS)*

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

    @property
    def cipher_suites(self):
        """
        The TLS cipher suites enabled on this appliance for HTTPS.

        :rtype: ``list`` of :py:class:`v1_11_4.web.vo.CipherSuite`
        """
        return self._cipher_suites[0]

    @cipher_suites.setter
    def cipher_suites(self, value):
        self._cipher_suites = (value, True)

    @property
    def http_port(self):
        """
        *(default value: 80)* The HTTP port for the Delphix web UI.

        :rtype: ``int``
        """
        return self._http_port[0]

    @http_port.setter
    def http_port(self, value):
        self._http_port = (value, True)

    @property
    def https_port(self):
        """
        *(default value: 443)* The HTTPS port for the Delphix web UI.

        :rtype: ``int``
        """
        return self._https_port[0]

    @https_port.setter
    def https_port(self, value):
        self._https_port = (value, True)

    @property
    def masking_legacy_ports(self):
        """
        Enable legacy ports for the masking web UI (8282 for HTTP and 8443 for
        HTTPs).

        :rtype: ``bool``
        """
        return self._masking_legacy_ports[0]

    @masking_legacy_ports.setter
    def masking_legacy_ports(self, value):
        self._masking_legacy_ports = (value, True)

