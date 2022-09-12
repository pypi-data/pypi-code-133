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
#     /delphix-toolkit-linked-direct-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_1.web.objects.ToolkitLinkedSource import ToolkitLinkedSource
from delphixpy.v1_5_1 import common

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

class ToolkitLinkedDirectSource(ToolkitLinkedSource):
    """
    *(extends* :py:class:`v1_5_1.web.vo.ToolkitLinkedSource` *)* A linked
    source definition for toolkits that perform linking using direct file sync.
    """
    def __init__(self, undef_enabled=True):
        super(ToolkitLinkedDirectSource, self).__init__()
        self._type = ("ToolkitLinkedDirectSource", True)
        self._post_sync = (self.__undef__, True)
        self._pre_sync = (self.__undef__, True)

    API_VERSION = "1.5.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ToolkitLinkedDirectSource, cls).from_dict(data, dirty, undef_enabled)
        if "postSync" not in data:
            raise ValueError("Missing required property \"postSync\".")
        obj._post_sync = (data.get("postSync", obj.__undef__), dirty)
        if obj._post_sync[0] is not None and obj._post_sync[0] is not obj.__undef__:
            assert isinstance(obj._post_sync[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._post_sync[0], type(obj._post_sync[0])))
            common.validate_format(obj._post_sync[0], "None", None, None)
        if "preSync" not in data:
            raise ValueError("Missing required property \"preSync\".")
        obj._pre_sync = (data.get("preSync", obj.__undef__), dirty)
        if obj._pre_sync[0] is not None and obj._pre_sync[0] is not obj.__undef__:
            assert isinstance(obj._pre_sync[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pre_sync[0], type(obj._pre_sync[0])))
            common.validate_format(obj._pre_sync[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ToolkitLinkedDirectSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "post_sync" == "type" or (self.post_sync is not self.__undef__ and (not (dirty and not self._post_sync[1]) or isinstance(self.post_sync, list) or belongs_to_parent)):
            dct["postSync"] = dictify(self.post_sync)
        if "pre_sync" == "type" or (self.pre_sync is not self.__undef__ and (not (dirty and not self._pre_sync[1]) or isinstance(self.pre_sync, list) or belongs_to_parent)):
            dct["preSync"] = dictify(self.pre_sync)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._post_sync = (self._post_sync[0], True)
        self._pre_sync = (self._pre_sync[0], True)

    def is_dirty(self):
        return any([self._post_sync[1], self._pre_sync[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ToolkitLinkedDirectSource):
            return False
        return super(ToolkitLinkedDirectSource, self).__eq__(other) and \
               self.post_sync == other.post_sync and \
               self.pre_sync == other.pre_sync

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def post_sync(self):
        """
        A workflow script to run after syncing source files.

        :rtype: ``TEXT_TYPE``
        """
        return self._post_sync[0]

    @post_sync.setter
    def post_sync(self, value):
        self._post_sync = (value, True)

    @property
    def pre_sync(self):
        """
        A workflow script to run before syncing source files.

        :rtype: ``TEXT_TYPE``
        """
        return self._pre_sync[0]

    @pre_sync.setter
    def pre_sync(self, value):
        self._pre_sync = (value, True)

