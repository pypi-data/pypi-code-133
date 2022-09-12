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
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.SourceConnectionInfo import SourceConnectionInfo
from delphixpy.v1_6_1 import common

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

class VMwareSourceConnectionInfo(SourceConnectionInfo):
    """
    *(extends* :py:class:`v1_6_1.web.vo.SourceConnectionInfo` *)* Contains
    information that can be used to connect to the VM.
    """
    def __init__(self, undef_enabled=True):
        super(VMwareSourceConnectionInfo, self).__init__()
        self._type = ("VMwareSourceConnectionInfo", True)
        self._ip_address = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(VMwareSourceConnectionInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._ip_address = (data.get("ipAddress", obj.__undef__), dirty)
        if obj._ip_address[0] is not None and obj._ip_address[0] is not obj.__undef__:
            assert isinstance(obj._ip_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._ip_address[0], type(obj._ip_address[0])))
            common.validate_format(obj._ip_address[0], "ipAddress", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(VMwareSourceConnectionInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "ip_address" == "type" or (self.ip_address is not self.__undef__ and (not (dirty and not self._ip_address[1]))):
            dct["ipAddress"] = dictify(self.ip_address)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._ip_address = (self._ip_address[0], True)

    def is_dirty(self):
        return any([self._ip_address[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, VMwareSourceConnectionInfo):
            return False
        return super(VMwareSourceConnectionInfo, self).__eq__(other) and \
               self.ip_address == other.ip_address

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def ip_address(self):
        """
        The IP address used to connect to the VM.

        :rtype: ``TEXT_TYPE``
        """
        return self._ip_address[0]

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = (value, True)

