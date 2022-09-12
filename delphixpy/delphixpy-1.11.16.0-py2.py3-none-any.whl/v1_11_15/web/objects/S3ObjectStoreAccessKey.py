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
#     /delphix-s3-object-store-access-key.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.S3ObjectStoreAccess import S3ObjectStoreAccess
from delphixpy.v1_11_15 import common

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

class S3ObjectStoreAccessKey(S3ObjectStoreAccess):
    """
    *(extends* :py:class:`v1_11_15.web.vo.S3ObjectStoreAccess` *)* S3 object
    store access key.
    """
    def __init__(self, undef_enabled=True):
        super(S3ObjectStoreAccessKey, self).__init__()
        self._type = ("S3ObjectStoreAccessKey", True)
        self._access_id = (self.__undef__, True)
        self._access_key = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(S3ObjectStoreAccessKey, cls).from_dict(data, dirty, undef_enabled)
        obj._access_id = (data.get("accessId", obj.__undef__), dirty)
        if obj._access_id[0] is not None and obj._access_id[0] is not obj.__undef__:
            assert isinstance(obj._access_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._access_id[0], type(obj._access_id[0])))
            common.validate_format(obj._access_id[0], "None", None, None)
        obj._access_key = (data.get("accessKey", obj.__undef__), dirty)
        if obj._access_key[0] is not None and obj._access_key[0] is not obj.__undef__:
            assert isinstance(obj._access_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._access_key[0], type(obj._access_key[0])))
            common.validate_format(obj._access_key[0], "password", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(S3ObjectStoreAccessKey, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "access_id" == "type" or (self.access_id is not self.__undef__ and (not (dirty and not self._access_id[1]) or isinstance(self.access_id, list) or belongs_to_parent)):
            dct["accessId"] = dictify(self.access_id)
        if "access_key" == "type" or (self.access_key is not self.__undef__ and (not (dirty and not self._access_key[1]) or isinstance(self.access_key, list) or belongs_to_parent)):
            dct["accessKey"] = dictify(self.access_key)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._access_id = (self._access_id[0], True)
        self._access_key = (self._access_key[0], True)

    def is_dirty(self):
        return any([self._access_id[1], self._access_key[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, S3ObjectStoreAccessKey):
            return False
        return super(S3ObjectStoreAccessKey, self).__eq__(other) and \
               self.access_id == other.access_id and \
               self.access_key == other.access_key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def access_id(self):
        """
        Access ID for the object store.

        :rtype: ``TEXT_TYPE``
        """
        return self._access_id[0]

    @access_id.setter
    def access_id(self, value):
        self._access_id = (value, True)

    @property
    def access_key(self):
        """
        Access key for the object store.

        :rtype: ``TEXT_TYPE``
        """
        return self._access_key[0]

    @access_key.setter
    def access_key(self, value):
        self._access_key = (value, True)

