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
#     /delphix-database-template-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_8_1 import common

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

class DatabaseTemplateConfig(TypedObject):
    """
    *(extends* :py:class:`v1_8_1.web.vo.TypedObject` *)* Static template
    configuration information for a given source type.
    """
    def __init__(self, undef_enabled=True):
        super(DatabaseTemplateConfig, self).__init__()
        self._type = ("DatabaseTemplateConfig", True)
        self._reserved = (self.__undef__, True)
        self._source_type = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DatabaseTemplateConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._reserved = []
        for item in data.get("reserved") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._reserved.append(item)
        obj._reserved = (obj._reserved, dirty)
        obj._source_type = (data.get("sourceType", obj.__undef__), dirty)
        if obj._source_type[0] is not None and obj._source_type[0] is not obj.__undef__:
            assert isinstance(obj._source_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_type[0], type(obj._source_type[0])))
            common.validate_format(obj._source_type[0], "type", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DatabaseTemplateConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "reserved" == "type" or (self.reserved is not self.__undef__ and (not (dirty and not self._reserved[1]))):
            dct["reserved"] = dictify(self.reserved)
        if "source_type" == "type" or (self.source_type is not self.__undef__ and (not (dirty and not self._source_type[1]))):
            dct["sourceType"] = dictify(self.source_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._reserved = (self._reserved[0], True)
        self._source_type = (self._source_type[0], True)

    def is_dirty(self):
        return any([self._reserved[1], self._source_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DatabaseTemplateConfig):
            return False
        return super(DatabaseTemplateConfig, self).__eq__(other) and \
               self.reserved == other.reserved and \
               self.source_type == other.source_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def reserved(self):
        """
        A list of reserved parameters names that cannot be used in the
        template.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._reserved[0]

    @reserved.setter
    def reserved(self, value):
        self._reserved = (value, True)

    @property
    def source_type(self):
        """
        The object type for sources to which this template is applicable.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_type[0]

    @source_type.setter
    def source_type(self, value):
        self._source_type = (value, True)

