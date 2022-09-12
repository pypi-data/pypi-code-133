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
#     /delphix-certificate-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_6 import common

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

class CertificateConfig(TypedObject):
    """
    *(extends* :py:class:`v1_10_6.web.vo.TypedObject` *)* Configuration for the
    use of custom CA signed certificates.
    """
    def __init__(self, undef_enabled=True):
        super(CertificateConfig, self).__init__()
        self._type = ("CertificateConfig", True)
        self._validate_windows_connector_certificate = (self.__undef__, True)
        self._enable_user_managed_server_auth_for_network_throughput_tests = (self.__undef__, True)
        self._enable_user_managed_client_auth_for_network_throughput_tests = (self.__undef__, True)
        self._enable_user_managed_server_auth_for_replication = (self.__undef__, True)
        self._enable_user_managed_client_auth_for_replication = (self.__undef__, True)
        self._enable_user_managed_server_auth_for_engine_to_host_dsp = (self.__undef__, True)
        self._enable_user_managed_client_auth_for_engine_to_host_dsp = (self.__undef__, True)
        self._certificate_expiration_warning_threshold = (self.__undef__, True)
        self._certificate_expiration_critical_threshold = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CertificateConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._validate_windows_connector_certificate = (data.get("validateWindowsConnectorCertificate", obj.__undef__), dirty)
        if obj._validate_windows_connector_certificate[0] is not None and obj._validate_windows_connector_certificate[0] is not obj.__undef__:
            assert isinstance(obj._validate_windows_connector_certificate[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._validate_windows_connector_certificate[0], type(obj._validate_windows_connector_certificate[0])))
            common.validate_format(obj._validate_windows_connector_certificate[0], "None", None, None)
        obj._enable_user_managed_server_auth_for_network_throughput_tests = (data.get("enableUserManagedServerAuthForNetworkThroughputTests", obj.__undef__), dirty)
        if obj._enable_user_managed_server_auth_for_network_throughput_tests[0] is not None and obj._enable_user_managed_server_auth_for_network_throughput_tests[0] is not obj.__undef__:
            assert isinstance(obj._enable_user_managed_server_auth_for_network_throughput_tests[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_user_managed_server_auth_for_network_throughput_tests[0], type(obj._enable_user_managed_server_auth_for_network_throughput_tests[0])))
            common.validate_format(obj._enable_user_managed_server_auth_for_network_throughput_tests[0], "None", None, None)
        obj._enable_user_managed_client_auth_for_network_throughput_tests = (data.get("enableUserManagedClientAuthForNetworkThroughputTests", obj.__undef__), dirty)
        if obj._enable_user_managed_client_auth_for_network_throughput_tests[0] is not None and obj._enable_user_managed_client_auth_for_network_throughput_tests[0] is not obj.__undef__:
            assert isinstance(obj._enable_user_managed_client_auth_for_network_throughput_tests[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_user_managed_client_auth_for_network_throughput_tests[0], type(obj._enable_user_managed_client_auth_for_network_throughput_tests[0])))
            common.validate_format(obj._enable_user_managed_client_auth_for_network_throughput_tests[0], "None", None, None)
        obj._enable_user_managed_server_auth_for_replication = (data.get("enableUserManagedServerAuthForReplication", obj.__undef__), dirty)
        if obj._enable_user_managed_server_auth_for_replication[0] is not None and obj._enable_user_managed_server_auth_for_replication[0] is not obj.__undef__:
            assert isinstance(obj._enable_user_managed_server_auth_for_replication[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_user_managed_server_auth_for_replication[0], type(obj._enable_user_managed_server_auth_for_replication[0])))
            common.validate_format(obj._enable_user_managed_server_auth_for_replication[0], "None", None, None)
        obj._enable_user_managed_client_auth_for_replication = (data.get("enableUserManagedClientAuthForReplication", obj.__undef__), dirty)
        if obj._enable_user_managed_client_auth_for_replication[0] is not None and obj._enable_user_managed_client_auth_for_replication[0] is not obj.__undef__:
            assert isinstance(obj._enable_user_managed_client_auth_for_replication[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_user_managed_client_auth_for_replication[0], type(obj._enable_user_managed_client_auth_for_replication[0])))
            common.validate_format(obj._enable_user_managed_client_auth_for_replication[0], "None", None, None)
        obj._enable_user_managed_server_auth_for_engine_to_host_dsp = (data.get("enableUserManagedServerAuthForEngineToHostDsp", obj.__undef__), dirty)
        if obj._enable_user_managed_server_auth_for_engine_to_host_dsp[0] is not None and obj._enable_user_managed_server_auth_for_engine_to_host_dsp[0] is not obj.__undef__:
            assert isinstance(obj._enable_user_managed_server_auth_for_engine_to_host_dsp[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_user_managed_server_auth_for_engine_to_host_dsp[0], type(obj._enable_user_managed_server_auth_for_engine_to_host_dsp[0])))
            common.validate_format(obj._enable_user_managed_server_auth_for_engine_to_host_dsp[0], "None", None, None)
        obj._enable_user_managed_client_auth_for_engine_to_host_dsp = (data.get("enableUserManagedClientAuthForEngineToHostDsp", obj.__undef__), dirty)
        if obj._enable_user_managed_client_auth_for_engine_to_host_dsp[0] is not None and obj._enable_user_managed_client_auth_for_engine_to_host_dsp[0] is not obj.__undef__:
            assert isinstance(obj._enable_user_managed_client_auth_for_engine_to_host_dsp[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enable_user_managed_client_auth_for_engine_to_host_dsp[0], type(obj._enable_user_managed_client_auth_for_engine_to_host_dsp[0])))
            common.validate_format(obj._enable_user_managed_client_auth_for_engine_to_host_dsp[0], "None", None, None)
        obj._certificate_expiration_warning_threshold = (data.get("certificateExpirationWarningThreshold", obj.__undef__), dirty)
        if obj._certificate_expiration_warning_threshold[0] is not None and obj._certificate_expiration_warning_threshold[0] is not obj.__undef__:
            assert isinstance(obj._certificate_expiration_warning_threshold[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._certificate_expiration_warning_threshold[0], type(obj._certificate_expiration_warning_threshold[0])))
            common.validate_format(obj._certificate_expiration_warning_threshold[0], "None", None, None)
        obj._certificate_expiration_critical_threshold = (data.get("certificateExpirationCriticalThreshold", obj.__undef__), dirty)
        if obj._certificate_expiration_critical_threshold[0] is not None and obj._certificate_expiration_critical_threshold[0] is not obj.__undef__:
            assert isinstance(obj._certificate_expiration_critical_threshold[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._certificate_expiration_critical_threshold[0], type(obj._certificate_expiration_critical_threshold[0])))
            common.validate_format(obj._certificate_expiration_critical_threshold[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CertificateConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "validate_windows_connector_certificate" == "type" or (self.validate_windows_connector_certificate is not self.__undef__ and (not (dirty and not self._validate_windows_connector_certificate[1]) or isinstance(self.validate_windows_connector_certificate, list) or belongs_to_parent)):
            dct["validateWindowsConnectorCertificate"] = dictify(self.validate_windows_connector_certificate)
        if "enable_user_managed_server_auth_for_network_throughput_tests" == "type" or (self.enable_user_managed_server_auth_for_network_throughput_tests is not self.__undef__ and (not (dirty and not self._enable_user_managed_server_auth_for_network_throughput_tests[1]) or isinstance(self.enable_user_managed_server_auth_for_network_throughput_tests, list) or belongs_to_parent)):
            dct["enableUserManagedServerAuthForNetworkThroughputTests"] = dictify(self.enable_user_managed_server_auth_for_network_throughput_tests)
        if "enable_user_managed_client_auth_for_network_throughput_tests" == "type" or (self.enable_user_managed_client_auth_for_network_throughput_tests is not self.__undef__ and (not (dirty and not self._enable_user_managed_client_auth_for_network_throughput_tests[1]) or isinstance(self.enable_user_managed_client_auth_for_network_throughput_tests, list) or belongs_to_parent)):
            dct["enableUserManagedClientAuthForNetworkThroughputTests"] = dictify(self.enable_user_managed_client_auth_for_network_throughput_tests)
        if "enable_user_managed_server_auth_for_replication" == "type" or (self.enable_user_managed_server_auth_for_replication is not self.__undef__ and (not (dirty and not self._enable_user_managed_server_auth_for_replication[1]) or isinstance(self.enable_user_managed_server_auth_for_replication, list) or belongs_to_parent)):
            dct["enableUserManagedServerAuthForReplication"] = dictify(self.enable_user_managed_server_auth_for_replication)
        if "enable_user_managed_client_auth_for_replication" == "type" or (self.enable_user_managed_client_auth_for_replication is not self.__undef__ and (not (dirty and not self._enable_user_managed_client_auth_for_replication[1]) or isinstance(self.enable_user_managed_client_auth_for_replication, list) or belongs_to_parent)):
            dct["enableUserManagedClientAuthForReplication"] = dictify(self.enable_user_managed_client_auth_for_replication)
        if "enable_user_managed_server_auth_for_engine_to_host_dsp" == "type" or (self.enable_user_managed_server_auth_for_engine_to_host_dsp is not self.__undef__ and (not (dirty and not self._enable_user_managed_server_auth_for_engine_to_host_dsp[1]) or isinstance(self.enable_user_managed_server_auth_for_engine_to_host_dsp, list) or belongs_to_parent)):
            dct["enableUserManagedServerAuthForEngineToHostDsp"] = dictify(self.enable_user_managed_server_auth_for_engine_to_host_dsp)
        if "enable_user_managed_client_auth_for_engine_to_host_dsp" == "type" or (self.enable_user_managed_client_auth_for_engine_to_host_dsp is not self.__undef__ and (not (dirty and not self._enable_user_managed_client_auth_for_engine_to_host_dsp[1]) or isinstance(self.enable_user_managed_client_auth_for_engine_to_host_dsp, list) or belongs_to_parent)):
            dct["enableUserManagedClientAuthForEngineToHostDsp"] = dictify(self.enable_user_managed_client_auth_for_engine_to_host_dsp)
        if "certificate_expiration_warning_threshold" == "type" or (self.certificate_expiration_warning_threshold is not self.__undef__ and (not (dirty and not self._certificate_expiration_warning_threshold[1]) or isinstance(self.certificate_expiration_warning_threshold, list) or belongs_to_parent)):
            dct["certificateExpirationWarningThreshold"] = dictify(self.certificate_expiration_warning_threshold)
        if "certificate_expiration_critical_threshold" == "type" or (self.certificate_expiration_critical_threshold is not self.__undef__ and (not (dirty and not self._certificate_expiration_critical_threshold[1]) or isinstance(self.certificate_expiration_critical_threshold, list) or belongs_to_parent)):
            dct["certificateExpirationCriticalThreshold"] = dictify(self.certificate_expiration_critical_threshold)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._validate_windows_connector_certificate = (self._validate_windows_connector_certificate[0], True)
        self._enable_user_managed_server_auth_for_network_throughput_tests = (self._enable_user_managed_server_auth_for_network_throughput_tests[0], True)
        self._enable_user_managed_client_auth_for_network_throughput_tests = (self._enable_user_managed_client_auth_for_network_throughput_tests[0], True)
        self._enable_user_managed_server_auth_for_replication = (self._enable_user_managed_server_auth_for_replication[0], True)
        self._enable_user_managed_client_auth_for_replication = (self._enable_user_managed_client_auth_for_replication[0], True)
        self._enable_user_managed_server_auth_for_engine_to_host_dsp = (self._enable_user_managed_server_auth_for_engine_to_host_dsp[0], True)
        self._enable_user_managed_client_auth_for_engine_to_host_dsp = (self._enable_user_managed_client_auth_for_engine_to_host_dsp[0], True)
        self._certificate_expiration_warning_threshold = (self._certificate_expiration_warning_threshold[0], True)
        self._certificate_expiration_critical_threshold = (self._certificate_expiration_critical_threshold[0], True)

    def is_dirty(self):
        return any([self._validate_windows_connector_certificate[1], self._enable_user_managed_server_auth_for_network_throughput_tests[1], self._enable_user_managed_client_auth_for_network_throughput_tests[1], self._enable_user_managed_server_auth_for_replication[1], self._enable_user_managed_client_auth_for_replication[1], self._enable_user_managed_server_auth_for_engine_to_host_dsp[1], self._enable_user_managed_client_auth_for_engine_to_host_dsp[1], self._certificate_expiration_warning_threshold[1], self._certificate_expiration_critical_threshold[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CertificateConfig):
            return False
        return super(CertificateConfig, self).__eq__(other) and \
               self.validate_windows_connector_certificate == other.validate_windows_connector_certificate and \
               self.enable_user_managed_server_auth_for_network_throughput_tests == other.enable_user_managed_server_auth_for_network_throughput_tests and \
               self.enable_user_managed_client_auth_for_network_throughput_tests == other.enable_user_managed_client_auth_for_network_throughput_tests and \
               self.enable_user_managed_server_auth_for_replication == other.enable_user_managed_server_auth_for_replication and \
               self.enable_user_managed_client_auth_for_replication == other.enable_user_managed_client_auth_for_replication and \
               self.enable_user_managed_server_auth_for_engine_to_host_dsp == other.enable_user_managed_server_auth_for_engine_to_host_dsp and \
               self.enable_user_managed_client_auth_for_engine_to_host_dsp == other.enable_user_managed_client_auth_for_engine_to_host_dsp and \
               self.certificate_expiration_warning_threshold == other.certificate_expiration_warning_threshold and \
               self.certificate_expiration_critical_threshold == other.certificate_expiration_critical_threshold

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def validate_windows_connector_certificate(self):
        """
        Whether or not the engine will validate custom Windows Connector
        certificates.

        :rtype: ``bool``
        """
        return self._validate_windows_connector_certificate[0]

    @validate_windows_connector_certificate.setter
    def validate_windows_connector_certificate(self, value):
        self._validate_windows_connector_certificate = (value, True)

    @property
    def enable_user_managed_server_auth_for_network_throughput_tests(self):
        """
        Whether or not the engine will use the user managed DSP key for server
        authentication during network throughput tests. Requires a stack
        restart to take effect. Note that if doing an engine to engine test,
        this flag will need to be true for the other Delphix Engine too.

        :rtype: ``bool``
        """
        return self._enable_user_managed_server_auth_for_network_throughput_tests[0]

    @enable_user_managed_server_auth_for_network_throughput_tests.setter
    def enable_user_managed_server_auth_for_network_throughput_tests(self, value):
        self._enable_user_managed_server_auth_for_network_throughput_tests = (value, True)

    @property
    def enable_user_managed_client_auth_for_network_throughput_tests(self):
        """
        Whether or not the engine will use the user managed DSP key for client
        authentication during network throughput tests. This will use the user
        managed DSP key on the host environment or source Delphix Engine,
        depending on if an engine to host, or engine to engine test is
        executed, respectively. Requires server auth to be enabled, and a stack
        restart to take effect. Note that if doing an engine to engine test,
        this flag will need to be true for the other Delphix Engine too.

        :rtype: ``bool``
        """
        return self._enable_user_managed_client_auth_for_network_throughput_tests[0]

    @enable_user_managed_client_auth_for_network_throughput_tests.setter
    def enable_user_managed_client_auth_for_network_throughput_tests(self, value):
        self._enable_user_managed_client_auth_for_network_throughput_tests = (value, True)

    @property
    def enable_user_managed_server_auth_for_replication(self):
        """
        Whether or not the engine will use the user managed DSP key for server
        authentication during replication. Requires a stack restart to take
        effect. Note that this flag will need to be true for the other engine
        too.

        :rtype: ``bool``
        """
        return self._enable_user_managed_server_auth_for_replication[0]

    @enable_user_managed_server_auth_for_replication.setter
    def enable_user_managed_server_auth_for_replication(self, value):
        self._enable_user_managed_server_auth_for_replication = (value, True)

    @property
    def enable_user_managed_client_auth_for_replication(self):
        """
        Whether or not the engine will use the user managed DSP key for client
        authentication during replication. This will use the user managed DSP
        key on the source Delphix Engine. Requires server auth to be enabled,
        and a stack restart to take effect. Note that this flag will need to be
        true for the other Delphix Engine too.

        :rtype: ``bool``
        """
        return self._enable_user_managed_client_auth_for_replication[0]

    @enable_user_managed_client_auth_for_replication.setter
    def enable_user_managed_client_auth_for_replication(self, value):
        self._enable_user_managed_client_auth_for_replication = (value, True)

    @property
    def enable_user_managed_server_auth_for_engine_to_host_dsp(self):
        """
        Whether or not the engine will use the user managed DSP key for server
        authentication for engine to host apps. Requires a stack restart to
        take effect.

        :rtype: ``bool``
        """
        return self._enable_user_managed_server_auth_for_engine_to_host_dsp[0]

    @enable_user_managed_server_auth_for_engine_to_host_dsp.setter
    def enable_user_managed_server_auth_for_engine_to_host_dsp(self, value):
        self._enable_user_managed_server_auth_for_engine_to_host_dsp = (value, True)

    @property
    def enable_user_managed_client_auth_for_engine_to_host_dsp(self):
        """
        Whether or not the engine will use the user managed DSP key for client
        authentication for engine to host apps. This will use the user managed
        DSP key on the host environment. Requires server auth to be enabled,
        and a stack restart to take effect.

        :rtype: ``bool``
        """
        return self._enable_user_managed_client_auth_for_engine_to_host_dsp[0]

    @enable_user_managed_client_auth_for_engine_to_host_dsp.setter
    def enable_user_managed_client_auth_for_engine_to_host_dsp(self, value):
        self._enable_user_managed_client_auth_for_engine_to_host_dsp = (value, True)

    @property
    def certificate_expiration_warning_threshold(self):
        """
        A warning fault will be thrown if any end entity certificates will
        expire within this duration (in days). Must be greater than the
        critical threshold.

        :rtype: ``int``
        """
        return self._certificate_expiration_warning_threshold[0]

    @certificate_expiration_warning_threshold.setter
    def certificate_expiration_warning_threshold(self, value):
        self._certificate_expiration_warning_threshold = (value, True)

    @property
    def certificate_expiration_critical_threshold(self):
        """
        A critical fault will be thrown if any end entity certificates will
        expire within this duration (in days). Must be less than the warning
        threshold.

        :rtype: ``int``
        """
        return self._certificate_expiration_critical_threshold[0]

    @certificate_expiration_critical_threshold.setter
    def certificate_expiration_critical_threshold(self, value):
        self._certificate_expiration_critical_threshold = (value, True)

