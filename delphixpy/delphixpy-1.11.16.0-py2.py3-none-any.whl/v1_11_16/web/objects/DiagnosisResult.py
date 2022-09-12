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
#     /delphix-diagnosis-result.json
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

class DiagnosisResult(TypedObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.TypedObject` *)* Details from a
    diagnosis check that was run due to a failed operation.
    """
    def __init__(self, undef_enabled=True):
        super(DiagnosisResult, self).__init__()
        self._type = ("DiagnosisResult", True)
        self._message_code = (self.__undef__, True)
        self._message = (self.__undef__, True)
        self._failure = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DiagnosisResult, cls).from_dict(data, dirty, undef_enabled)
        obj._message_code = (data.get("messageCode", obj.__undef__), dirty)
        if obj._message_code[0] is not None and obj._message_code[0] is not obj.__undef__:
            assert isinstance(obj._message_code[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message_code[0], type(obj._message_code[0])))
            common.validate_format(obj._message_code[0], "None", None, None)
        obj._message = (data.get("message", obj.__undef__), dirty)
        if obj._message[0] is not None and obj._message[0] is not obj.__undef__:
            assert isinstance(obj._message[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message[0], type(obj._message[0])))
            common.validate_format(obj._message[0], "None", None, None)
        obj._failure = (data.get("failure", obj.__undef__), dirty)
        if obj._failure[0] is not None and obj._failure[0] is not obj.__undef__:
            assert isinstance(obj._failure[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._failure[0], type(obj._failure[0])))
            common.validate_format(obj._failure[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DiagnosisResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "message_code" == "type" or (self.message_code is not self.__undef__ and (not (dirty and not self._message_code[1]))):
            dct["messageCode"] = dictify(self.message_code)
        if "message" == "type" or (self.message is not self.__undef__ and (not (dirty and not self._message[1]))):
            dct["message"] = dictify(self.message)
        if "failure" == "type" or (self.failure is not self.__undef__ and (not (dirty and not self._failure[1]))):
            dct["failure"] = dictify(self.failure)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._message_code = (self._message_code[0], True)
        self._message = (self._message[0], True)
        self._failure = (self._failure[0], True)

    def is_dirty(self):
        return any([self._message_code[1], self._message[1], self._failure[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DiagnosisResult):
            return False
        return super(DiagnosisResult, self).__eq__(other) and \
               self.message_code == other.message_code and \
               self.message == other.message and \
               self.failure == other.failure

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def message_code(self):
        """
        Message code associated with the event.

        :rtype: ``TEXT_TYPE``
        """
        return self._message_code[0]

    @message_code.setter
    def message_code(self, value):
        self._message_code = (value, True)

    @property
    def message(self):
        """
        Localized message.

        :rtype: ``TEXT_TYPE``
        """
        return self._message[0]

    @message.setter
    def message(self, value):
        self._message = (value, True)

    @property
    def failure(self):
        """
        True if this was a check that did not pass.

        :rtype: ``bool``
        """
        return self._failure[0]

    @failure.setter
    def failure(self, value):
        self._failure = (value, True)

