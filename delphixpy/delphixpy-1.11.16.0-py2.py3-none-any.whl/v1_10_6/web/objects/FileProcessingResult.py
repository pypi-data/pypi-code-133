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
#     /delphix-file-processing-result.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_6 import common

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

class FileProcessingResult(TypedObject):
    """
    *(extends* :py:class:`v1_10_6.web.vo.TypedObject` *)* Result of a file
    processing request (upload or download).
    """
    def __init__(self, undef_enabled=True):
        super(FileProcessingResult, self).__init__()
        self._type = ("FileProcessingResult", True)
        self._url = (self.__undef__, True)
        self._token = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(FileProcessingResult, cls).from_dict(data, dirty, undef_enabled)
        obj._url = (data.get("url", obj.__undef__), dirty)
        if obj._url[0] is not None and obj._url[0] is not obj.__undef__:
            assert isinstance(obj._url[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._url[0], type(obj._url[0])))
            common.validate_format(obj._url[0], "None", None, None)
        obj._token = (data.get("token", obj.__undef__), dirty)
        if obj._token[0] is not None and obj._token[0] is not obj.__undef__:
            assert isinstance(obj._token[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._token[0], type(obj._token[0])))
            common.validate_format(obj._token[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(FileProcessingResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "url" == "type" or (self.url is not self.__undef__ and (not (dirty and not self._url[1]))):
            dct["url"] = dictify(self.url)
        if "token" == "type" or (self.token is not self.__undef__ and (not (dirty and not self._token[1]))):
            dct["token"] = dictify(self.token)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._url = (self._url[0], True)
        self._token = (self._token[0], True)

    def is_dirty(self):
        return any([self._url[1], self._token[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, FileProcessingResult):
            return False
        return super(FileProcessingResult, self).__eq__(other) and \
               self.url == other.url and \
               self.token == other.token

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def url(self):
        """
        URL to download from or upload to.

        :rtype: ``TEXT_TYPE``
        """
        return self._url[0]

    @url.setter
    def url(self, value):
        self._url = (value, True)

    @property
    def token(self):
        """
        Token to pass as parameter to identify the file.

        :rtype: ``TEXT_TYPE``
        """
        return self._token[0]

    @token.setter
    def token(self, value):
        self._token = (value, True)

