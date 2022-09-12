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
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_7 import common

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

class LuaEventBundle(TypedObject):
    """
    *(extends* :py:class:`v1_11_7.web.vo.TypedObject` *)* An opaque type
    containing all information necessary to produce localized content from a
    toolkit.
    """
    def __init__(self, undef_enabled=True):
        super(LuaEventBundle, self).__init__()
        self._type = ("LuaEventBundle", True)
        self._toolkit_name = (self.__undef__, True)
        self._message_id = (self.__undef__, True)
        self._params = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(LuaEventBundle, cls).from_dict(data, dirty, undef_enabled)
        if "toolkitName" not in data:
            raise ValueError("Missing required property \"toolkitName\".")
        obj._toolkit_name = (data.get("toolkitName", obj.__undef__), dirty)
        if obj._toolkit_name[0] is not None and obj._toolkit_name[0] is not obj.__undef__:
            assert isinstance(obj._toolkit_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._toolkit_name[0], type(obj._toolkit_name[0])))
            common.validate_format(obj._toolkit_name[0], "None", None, None)
        if "messageId" not in data:
            raise ValueError("Missing required property \"messageId\".")
        obj._message_id = (data.get("messageId", obj.__undef__), dirty)
        if obj._message_id[0] is not None and obj._message_id[0] is not obj.__undef__:
            assert isinstance(obj._message_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._message_id[0], type(obj._message_id[0])))
            common.validate_format(obj._message_id[0], "None", None, None)
        if "params" not in data:
            raise ValueError("Missing required property \"params\".")
        obj._params = []
        for item in data.get("params") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._params.append(item)
        obj._params = (obj._params, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(LuaEventBundle, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "toolkit_name" == "type" or (self.toolkit_name is not self.__undef__ and (not (dirty and not self._toolkit_name[1]) or isinstance(self.toolkit_name, list) or belongs_to_parent)):
            dct["toolkitName"] = dictify(self.toolkit_name)
        if "message_id" == "type" or (self.message_id is not self.__undef__ and (not (dirty and not self._message_id[1]) or isinstance(self.message_id, list) or belongs_to_parent)):
            dct["messageId"] = dictify(self.message_id)
        if "params" == "type" or (self.params is not self.__undef__ and (not (dirty and not self._params[1]) or isinstance(self.params, list) or belongs_to_parent)):
            dct["params"] = dictify(self.params, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._toolkit_name = (self._toolkit_name[0], True)
        self._message_id = (self._message_id[0], True)
        self._params = (self._params[0], True)

    def is_dirty(self):
        return any([self._toolkit_name[1], self._message_id[1], self._params[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, LuaEventBundle):
            return False
        return super(LuaEventBundle, self).__eq__(other) and \
               self.toolkit_name == other.toolkit_name and \
               self.message_id == other.message_id and \
               self.params == other.params

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def toolkit_name(self):
        """
        The name of the toolkit that generated this event bundle.

        :rtype: ``TEXT_TYPE``
        """
        return self._toolkit_name[0]

    @toolkit_name.setter
    def toolkit_name(self, value):
        self._toolkit_name = (value, True)

    @property
    def message_id(self):
        """
        The unique identifier of the message in this event bundle.

        :rtype: ``TEXT_TYPE``
        """
        return self._message_id[0]

    @message_id.setter
    def message_id(self, value):
        self._message_id = (value, True)

    @property
    def params(self):
        """
        The parameter values to consume when this event bundle is localized.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._params[0]

    @params.setter
    def params(self, value):
        self._params = (value, True)

