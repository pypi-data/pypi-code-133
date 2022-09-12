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
#     /delphix-toolkit-locale.json
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

class ToolkitLocale(TypedObject):
    """
    *(extends* :py:class:`v1_9_1.web.vo.TypedObject` *)* Contains a mapping
    from message IDs to messages for a locale.
    """
    def __init__(self, undef_enabled=True):
        super(ToolkitLocale, self).__init__()
        self._type = ("ToolkitLocale", True)
        self._locale_name = (self.__undef__, True)
        self._messages = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ToolkitLocale, cls).from_dict(data, dirty, undef_enabled)
        if "localeName" not in data:
            raise ValueError("Missing required property \"localeName\".")
        obj._locale_name = (data.get("localeName", obj.__undef__), dirty)
        if obj._locale_name[0] is not None and obj._locale_name[0] is not obj.__undef__:
            assert isinstance(obj._locale_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._locale_name[0], type(obj._locale_name[0])))
            common.validate_format(obj._locale_name[0], "locale", None, None)
        if "messages" not in data:
            raise ValueError("Missing required property \"messages\".")
        obj._messages = (data.get("messages", obj.__undef__), dirty)
        if obj._messages[0] is not None and obj._messages[0] is not obj.__undef__:
            assert isinstance(obj._messages[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._messages[0], type(obj._messages[0])))
            common.validate_format(obj._messages[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ToolkitLocale, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "locale_name" == "type" or (self.locale_name is not self.__undef__ and (not (dirty and not self._locale_name[1]) or isinstance(self.locale_name, list) or belongs_to_parent)):
            dct["localeName"] = dictify(self.locale_name)
        if "messages" == "type" or (self.messages is not self.__undef__ and (not (dirty and not self._messages[1]) or isinstance(self.messages, list) or belongs_to_parent)):
            dct["messages"] = dictify(self.messages, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._locale_name = (self._locale_name[0], True)
        self._messages = (self._messages[0], True)

    def is_dirty(self):
        return any([self._locale_name[1], self._messages[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ToolkitLocale):
            return False
        return super(ToolkitLocale, self).__eq__(other) and \
               self.locale_name == other.locale_name and \
               self.messages == other.messages

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def locale_name(self):
        """
        The name of this locale.

        :rtype: ``TEXT_TYPE``
        """
        return self._locale_name[0]

    @locale_name.setter
    def locale_name(self, value):
        self._locale_name = (value, True)

    @property
    def messages(self):
        """
        A mapping of message IDs to messages for this locale.

        :rtype: ``dict``
        """
        return self._messages[0]

    @messages.setter
    def messages(self, value):
        self._messages = (value, True)

