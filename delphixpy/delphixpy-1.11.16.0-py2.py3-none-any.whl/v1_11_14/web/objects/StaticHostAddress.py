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
#     /delphix-static-host-address.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_14.web.objects.UserObject import UserObject
from delphixpy.v1_11_14 import common

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

class StaticHostAddress(UserObject):
    """
    *(extends* :py:class:`v1_11_14.web.vo.UserObject` *)* Static mapping of
    hostname to IP address.
    """
    def __init__(self, undef_enabled=True):
        super(StaticHostAddress, self).__init__()
        self._type = ("StaticHostAddress", True)
        self._hostname = (self.__undef__, True)
        self._addresses = (self.__undef__, True)

    API_VERSION = "1.11.14"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(StaticHostAddress, cls).from_dict(data, dirty, undef_enabled)
        obj._hostname = (data.get("hostname", obj.__undef__), dirty)
        if obj._hostname[0] is not None and obj._hostname[0] is not obj.__undef__:
            assert isinstance(obj._hostname[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._hostname[0], type(obj._hostname[0])))
            common.validate_format(obj._hostname[0], "hostname", None, None)
        obj._addresses = []
        for item in data.get("addresses") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "ipAddress", None, None)
            obj._addresses.append(item)
        obj._addresses = (obj._addresses, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(StaticHostAddress, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "hostname" == "type" or (self.hostname is not self.__undef__ and (not (dirty and not self._hostname[1]) or isinstance(self.hostname, list) or belongs_to_parent)):
            dct["hostname"] = dictify(self.hostname)
        if "addresses" == "type" or (self.addresses is not self.__undef__ and (not (dirty and not self._addresses[1]) or isinstance(self.addresses, list) or belongs_to_parent)):
            dct["addresses"] = dictify(self.addresses, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._hostname = (self._hostname[0], True)
        self._addresses = (self._addresses[0], True)

    def is_dirty(self):
        return any([self._hostname[1], self._addresses[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, StaticHostAddress):
            return False
        return super(StaticHostAddress, self).__eq__(other) and \
               self.hostname == other.hostname and \
               self.addresses == other.addresses

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def hostname(self):
        """
        The hostname to resolve.

        :rtype: ``TEXT_TYPE``
        """
        return self._hostname[0]

    @hostname.setter
    def hostname(self, value):
        self._hostname = (value, True)

    @property
    def addresses(self):
        """
        List of IP addresses to assign to the hostname.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._addresses[0]

    @addresses.setter
    def addresses(self, value):
        self._addresses = (value, True)

