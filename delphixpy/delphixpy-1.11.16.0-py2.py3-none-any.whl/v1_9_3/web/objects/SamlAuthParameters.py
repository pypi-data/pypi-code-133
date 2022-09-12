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
#     /delphix-saml-auth-parameters.json
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

class SamlAuthParameters(TypedObject):
    """
    *(extends* :py:class:`v1_9_3.web.vo.TypedObject` *)* The parameter to use
    as input to determine whether to encode a SAML authentication request.
    """
    def __init__(self, undef_enabled=True):
        super(SamlAuthParameters, self).__init__()
        self._type = ("SamlAuthParameters", True)
        self._encode_request = (self.__undef__, True)

    API_VERSION = "1.9.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SamlAuthParameters, cls).from_dict(data, dirty, undef_enabled)
        if "encodeRequest" not in data:
            raise ValueError("Missing required property \"encodeRequest\".")
        obj._encode_request = (data.get("encodeRequest", obj.__undef__), dirty)
        if obj._encode_request[0] is not None and obj._encode_request[0] is not obj.__undef__:
            assert isinstance(obj._encode_request[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._encode_request[0], type(obj._encode_request[0])))
            common.validate_format(obj._encode_request[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SamlAuthParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "encode_request" == "type" or (self.encode_request is not self.__undef__ and (not (dirty and not self._encode_request[1]) or isinstance(self.encode_request, list) or belongs_to_parent)):
            dct["encodeRequest"] = dictify(self.encode_request)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._encode_request = (self._encode_request[0], True)

    def is_dirty(self):
        return any([self._encode_request[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SamlAuthParameters):
            return False
        return super(SamlAuthParameters, self).__eq__(other) and \
               self.encode_request == other.encode_request

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def encode_request(self):
        """
        *(default value: True)* Set to true to encode SAML authentication
        requests.

        :rtype: ``bool``
        """
        return self._encode_request[0]

    @encode_request.setter
    def encode_request(self, value):
        self._encode_request = (value, True)

