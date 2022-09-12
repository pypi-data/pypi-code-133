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
#     /delphix-database-template.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_10_4 import common

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

class DatabaseTemplate(NamedUserObject):
    """
    *(extends* :py:class:`v1_10_4.web.vo.NamedUserObject` *)* Parameter
    configuration for virtual databases.
    """
    def __init__(self, undef_enabled=True):
        super(DatabaseTemplate, self).__init__()
        self._type = ("DatabaseTemplate", True)
        self._description = (self.__undef__, True)
        self._source_type = (self.__undef__, True)
        self._parameters = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DatabaseTemplate, cls).from_dict(data, dirty, undef_enabled)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, None)
        obj._source_type = (data.get("sourceType", obj.__undef__), dirty)
        if obj._source_type[0] is not None and obj._source_type[0] is not obj.__undef__:
            assert isinstance(obj._source_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_type[0], type(obj._source_type[0])))
            assert obj._source_type[0] in ['MySQLVirtualSource', 'OracleVirtualSource', 'MSSqlVirtualSource', 'MSSqlLinkedSource', 'PgSQLVirtualSource'], "Expected enum ['MySQLVirtualSource', 'OracleVirtualSource', 'MSSqlVirtualSource', 'MSSqlLinkedSource', 'PgSQLVirtualSource'] but got %s" % obj._source_type[0]
            common.validate_format(obj._source_type[0], "type", None, None)
        obj._parameters = (data.get("parameters", obj.__undef__), dirty)
        if obj._parameters[0] is not None and obj._parameters[0] is not obj.__undef__:
            assert isinstance(obj._parameters[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._parameters[0], type(obj._parameters[0])))
            common.validate_format(obj._parameters[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DatabaseTemplate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "source_type" == "type" or (self.source_type is not self.__undef__ and (not (dirty and not self._source_type[1]) or isinstance(self.source_type, list) or belongs_to_parent)):
            dct["sourceType"] = dictify(self.source_type)
        if "parameters" == "type" or (self.parameters is not self.__undef__ and (not (dirty and not self._parameters[1]) or isinstance(self.parameters, list) or belongs_to_parent)):
            dct["parameters"] = dictify(self.parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._description = (self._description[0], True)
        self._source_type = (self._source_type[0], True)
        self._parameters = (self._parameters[0], True)

    def is_dirty(self):
        return any([self._description[1], self._source_type[1], self._parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DatabaseTemplate):
            return False
        return super(DatabaseTemplate, self).__eq__(other) and \
               self.description == other.description and \
               self.source_type == other.source_type and \
               self.parameters == other.parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def description(self):
        """
        User provided description for this template.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def source_type(self):
        """
        The type of the source associated with the template. *(permitted
        values: MySQLVirtualSource, OracleVirtualSource, MSSqlVirtualSource,
        MSSqlLinkedSource, PgSQLVirtualSource)*

        :rtype: ``TEXT_TYPE``
        """
        return self._source_type[0]

    @source_type.setter
    def source_type(self, value):
        self._source_type = (value, True)

    @property
    def parameters(self):
        """
        A name/value map of string configuration parameters.

        :rtype: ``dict``
        """
        return self._parameters[0]

    @parameters.setter
    def parameters(self, value):
        self._parameters = (value, True)

