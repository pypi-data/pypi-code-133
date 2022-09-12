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
#     /delphix-end-entity-certificate-replace-chain-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.EndEntityCertificateReplaceParameters import EndEntityCertificateReplaceParameters
from delphixpy.v1_11_11 import factory
from delphixpy.v1_11_11 import common

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

class EndEntityCertificateReplaceChainParameters(EndEntityCertificateReplaceParameters):
    """
    *(extends*
    :py:class:`v1_11_11.web.vo.EndEntityCertificateReplaceParameters` *)* The
    parameters for replacing an end-entity certificate with a PEM certificate
    chain.
    """
    def __init__(self, undef_enabled=True):
        super(EndEntityCertificateReplaceChainParameters, self).__init__()
        self._type = ("EndEntityCertificateReplaceChainParameters", True)
        self._chain = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(EndEntityCertificateReplaceChainParameters, cls).from_dict(data, dirty, undef_enabled)
        if "chain" not in data:
            raise ValueError("Missing required property \"chain\".")
        if "chain" in data and data["chain"] is not None:
            obj._chain = (factory.create_object(data["chain"], "PemCertificateChain"), dirty)
            factory.validate_type(obj._chain[0], "PemCertificateChain")
        else:
            obj._chain = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(EndEntityCertificateReplaceChainParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "chain" == "type" or (self.chain is not self.__undef__ and (not (dirty and not self._chain[1]) or isinstance(self.chain, list) or belongs_to_parent)):
            dct["chain"] = dictify(self.chain, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._chain = (self._chain[0], True)

    def is_dirty(self):
        return any([self._chain[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, EndEntityCertificateReplaceChainParameters):
            return False
        return super(EndEntityCertificateReplaceChainParameters, self).__eq__(other) and \
               self.chain == other.chain

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def chain(self):
        """
        The PEM certificate chain.

        :rtype: :py:class:`v1_11_11.web.vo.PemCertificateChain`
        """
        return self._chain[0]

    @chain.setter
    def chain(self, value):
        self._chain = (value, True)

