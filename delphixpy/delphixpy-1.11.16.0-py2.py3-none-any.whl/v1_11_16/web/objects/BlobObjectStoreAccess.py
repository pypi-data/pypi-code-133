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
#     /delphix-blob-object-store-access.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_16 import common

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

class BlobObjectStoreAccess(TypedObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.TypedObject` *)* Blob object store
    access.
    """
    def __init__(self, undef_enabled=True):
        super(BlobObjectStoreAccess, self).__init__()
        self._type = ("BlobObjectStoreAccess", True)
        self._azure_account = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(BlobObjectStoreAccess, cls).from_dict(data, dirty, undef_enabled)
        obj._azure_account = (data.get("azureAccount", obj.__undef__), dirty)
        if obj._azure_account[0] is not None and obj._azure_account[0] is not obj.__undef__:
            assert isinstance(obj._azure_account[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._azure_account[0], type(obj._azure_account[0])))
            common.validate_format(obj._azure_account[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(BlobObjectStoreAccess, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "azure_account" == "type" or (self.azure_account is not self.__undef__ and (not (dirty and not self._azure_account[1]) or isinstance(self.azure_account, list) or belongs_to_parent)):
            dct["azureAccount"] = dictify(self.azure_account)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._azure_account = (self._azure_account[0], True)

    def is_dirty(self):
        return any([self._azure_account[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, BlobObjectStoreAccess):
            return False
        return super(BlobObjectStoreAccess, self).__eq__(other) and \
               self.azure_account == other.azure_account

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def azure_account(self):
        """
        Azure account for the object store.

        :rtype: ``TEXT_TYPE``
        """
        return self._azure_account[0]

    @azure_account.setter
    def azure_account(self, value):
        self._azure_account = (value, True)

