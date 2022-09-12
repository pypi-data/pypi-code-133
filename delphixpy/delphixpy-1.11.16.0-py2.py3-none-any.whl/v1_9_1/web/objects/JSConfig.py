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
#     /delphix-js-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_1 import common

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

class JSConfig(TypedObject):
    """
    *(extends* :py:class:`v1_9_1.web.vo.TypedObject` *)* Jet Stream
    configuration.
    """
    def __init__(self, undef_enabled=True):
        super(JSConfig, self).__init__()
        self._type = ("JSConfig", True)
        self._default_bookmark_expiration = (self.__undef__, True)
        self._retry_attempts = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._default_bookmark_expiration = (data.get("defaultBookmarkExpiration", obj.__undef__), dirty)
        if obj._default_bookmark_expiration[0] is not None and obj._default_bookmark_expiration[0] is not obj.__undef__:
            assert isinstance(obj._default_bookmark_expiration[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._default_bookmark_expiration[0], type(obj._default_bookmark_expiration[0])))
            common.validate_format(obj._default_bookmark_expiration[0], "None", None, None)
        obj._retry_attempts = (data.get("retryAttempts", obj.__undef__), dirty)
        if obj._retry_attempts[0] is not None and obj._retry_attempts[0] is not obj.__undef__:
            assert isinstance(obj._retry_attempts[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._retry_attempts[0], type(obj._retry_attempts[0])))
            common.validate_format(obj._retry_attempts[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "default_bookmark_expiration" == "type" or (self.default_bookmark_expiration is not self.__undef__ and (not (dirty and not self._default_bookmark_expiration[1]) or isinstance(self.default_bookmark_expiration, list) or belongs_to_parent)):
            dct["defaultBookmarkExpiration"] = dictify(self.default_bookmark_expiration)
        if "retry_attempts" == "type" or (self.retry_attempts is not self.__undef__ and (not (dirty and not self._retry_attempts[1]) or isinstance(self.retry_attempts, list) or belongs_to_parent)):
            dct["retryAttempts"] = dictify(self.retry_attempts)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._default_bookmark_expiration = (self._default_bookmark_expiration[0], True)
        self._retry_attempts = (self._retry_attempts[0], True)

    def is_dirty(self):
        return any([self._default_bookmark_expiration[1], self._retry_attempts[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSConfig):
            return False
        return super(JSConfig, self).__eq__(other) and \
               self.default_bookmark_expiration == other.default_bookmark_expiration and \
               self.retry_attempts == other.retry_attempts

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def default_bookmark_expiration(self):
        """
        Default expiration for bookmarks created through the GUI, in days. If
        value is 0, bookmarks will default to no expiration.

        :rtype: ``int``
        """
        return self._default_bookmark_expiration[0]

    @default_bookmark_expiration.setter
    def default_bookmark_expiration(self, value):
        self._default_bookmark_expiration = (value, True)

    @property
    def retry_attempts(self):
        """
        The number of times to retry failed sources during Jet Stream data
        operations.

        :rtype: ``int``
        """
        return self._retry_attempts[0]

    @retry_attempts.setter
    def retry_attempts(self, value):
        self._retry_attempts = (value, True)

