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
#     /delphix-alert-action-email-list.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_1.web.objects.AlertActionEmail import AlertActionEmail
from delphixpy.v1_10_1 import common

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

class AlertActionEmailList(AlertActionEmail):
    """
    *(extends* :py:class:`v1_10_1.web.vo.AlertActionEmail` *)* Alert action to
    email a list of users in response to an alert.
    """
    def __init__(self, undef_enabled=True):
        super(AlertActionEmailList, self).__init__()
        self._type = ("AlertActionEmailList", True)
        self._addresses = (self.__undef__, True)

    API_VERSION = "1.10.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AlertActionEmailList, cls).from_dict(data, dirty, undef_enabled)
        if "addresses" not in data:
            raise ValueError("Missing required property \"addresses\".")
        obj._addresses = []
        for item in data.get("addresses") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "email", None, None)
            obj._addresses.append(item)
        obj._addresses = (obj._addresses, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AlertActionEmailList, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "addresses" == "type" or (self.addresses is not self.__undef__ and (not (dirty and not self._addresses[1]) or isinstance(self.addresses, list) or belongs_to_parent)):
            dct["addresses"] = dictify(self.addresses, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._addresses = (self._addresses[0], True)

    def is_dirty(self):
        return any([self._addresses[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AlertActionEmailList):
            return False
        return super(AlertActionEmailList, self).__eq__(other) and \
               self.addresses == other.addresses

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def addresses(self):
        """
        List of email addresses to send mail to.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._addresses[0]

    @addresses.setter
    def addresses(self, value):
        self._addresses = (value, True)

