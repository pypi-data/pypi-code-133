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
#     /delphix-ssh-verify-raw-key.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.SshVerifyBase import SshVerifyBase
from delphixpy.v1_11_0 import common

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

class SshVerifyRawKey(SshVerifyBase):
    """
    *(extends* :py:class:`v1_11_0.web.vo.SshVerifyBase` *)* SSH verification
    strategy based on a known per-host key.
    """
    def __init__(self, undef_enabled=True):
        super(SshVerifyRawKey, self).__init__()
        self._type = ("SshVerifyRawKey", True)
        self._raw_key = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SshVerifyRawKey, cls).from_dict(data, dirty, undef_enabled)
        if "rawKey" not in data:
            raise ValueError("Missing required property \"rawKey\".")
        obj._raw_key = (data.get("rawKey", obj.__undef__), dirty)
        if obj._raw_key[0] is not None and obj._raw_key[0] is not obj.__undef__:
            assert isinstance(obj._raw_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._raw_key[0], type(obj._raw_key[0])))
            common.validate_format(obj._raw_key[0], "hostKey", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SshVerifyRawKey, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "raw_key" == "type" or (self.raw_key is not self.__undef__ and (not (dirty and not self._raw_key[1]) or isinstance(self.raw_key, list) or belongs_to_parent)):
            dct["rawKey"] = dictify(self.raw_key)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._raw_key = (self._raw_key[0], True)

    def is_dirty(self):
        return any([self._raw_key[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SshVerifyRawKey):
            return False
        return super(SshVerifyRawKey, self).__eq__(other) and \
               self.raw_key == other.raw_key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def raw_key(self):
        """
        Base64-encoded ssh key of the host.

        :rtype: ``TEXT_TYPE``
        """
        return self._raw_key[0]

    @raw_key.setter
    def raw_key(self, value):
        self._raw_key = (value, True)

