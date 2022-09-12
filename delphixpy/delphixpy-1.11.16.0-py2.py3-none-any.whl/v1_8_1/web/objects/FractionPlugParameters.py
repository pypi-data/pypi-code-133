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
#     /delphix-fraction-plug-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_8_1 import factory
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

class FractionPlugParameters(TypedObject):
    """
    *(extends* :py:class:`v1_8_1.web.vo.TypedObject` *)* The parameters to use
    as input when transporting a transportable tablespace.
    """
    def __init__(self, undef_enabled=True):
        super(FractionPlugParameters, self).__init__()
        self._type = ("FractionPlugParameters", True)
        self._schemas_prefix = (self.__undef__, True)
        self._tablespaces_prefix = (self.__undef__, True)
        self._timeflow_point_parameters = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(FractionPlugParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._schemas_prefix = (data.get("schemasPrefix", obj.__undef__), dirty)
        if obj._schemas_prefix[0] is not None and obj._schemas_prefix[0] is not obj.__undef__:
            assert isinstance(obj._schemas_prefix[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._schemas_prefix[0], type(obj._schemas_prefix[0])))
            common.validate_format(obj._schemas_prefix[0], "None", None, 28)
        obj._tablespaces_prefix = (data.get("tablespacesPrefix", obj.__undef__), dirty)
        if obj._tablespaces_prefix[0] is not None and obj._tablespaces_prefix[0] is not obj.__undef__:
            assert isinstance(obj._tablespaces_prefix[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tablespaces_prefix[0], type(obj._tablespaces_prefix[0])))
            common.validate_format(obj._tablespaces_prefix[0], "None", None, 28)
        if "timeflowPointParameters" not in data:
            raise ValueError("Missing required property \"timeflowPointParameters\".")
        if "timeflowPointParameters" in data and data["timeflowPointParameters"] is not None:
            obj._timeflow_point_parameters = (factory.create_object(data["timeflowPointParameters"], "TimeflowPointParameters"), dirty)
            factory.validate_type(obj._timeflow_point_parameters[0], "TimeflowPointParameters")
        else:
            obj._timeflow_point_parameters = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(FractionPlugParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "schemas_prefix" == "type" or (self.schemas_prefix is not self.__undef__ and (not (dirty and not self._schemas_prefix[1]) or isinstance(self.schemas_prefix, list) or belongs_to_parent)):
            dct["schemasPrefix"] = dictify(self.schemas_prefix)
        if "tablespaces_prefix" == "type" or (self.tablespaces_prefix is not self.__undef__ and (not (dirty and not self._tablespaces_prefix[1]) or isinstance(self.tablespaces_prefix, list) or belongs_to_parent)):
            dct["tablespacesPrefix"] = dictify(self.tablespaces_prefix)
        if "timeflow_point_parameters" == "type" or (self.timeflow_point_parameters is not self.__undef__ and (not (dirty and not self._timeflow_point_parameters[1]) or isinstance(self.timeflow_point_parameters, list) or belongs_to_parent)):
            dct["timeflowPointParameters"] = dictify(self.timeflow_point_parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._schemas_prefix = (self._schemas_prefix[0], True)
        self._tablespaces_prefix = (self._tablespaces_prefix[0], True)
        self._timeflow_point_parameters = (self._timeflow_point_parameters[0], True)

    def is_dirty(self):
        return any([self._schemas_prefix[1], self._tablespaces_prefix[1], self._timeflow_point_parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, FractionPlugParameters):
            return False
        return super(FractionPlugParameters, self).__eq__(other) and \
               self.schemas_prefix == other.schemas_prefix and \
               self.tablespaces_prefix == other.tablespaces_prefix and \
               self.timeflow_point_parameters == other.timeflow_point_parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def schemas_prefix(self):
        """
        Optional prefix to add to schemas being moved into warehouse.

        :rtype: ``TEXT_TYPE``
        """
        return self._schemas_prefix[0]

    @schemas_prefix.setter
    def schemas_prefix(self, value):
        self._schemas_prefix = (value, True)

    @property
    def tablespaces_prefix(self):
        """
        Optional prefix to add to tablespaces being moved into warehouse.

        :rtype: ``TEXT_TYPE``
        """
        return self._tablespaces_prefix[0]

    @tablespaces_prefix.setter
    def tablespaces_prefix(self, value):
        self._tablespaces_prefix = (value, True)

    @property
    def timeflow_point_parameters(self):
        """
        The TimeFlow point, bookmark, or semantic location to base provisioning
        on.

        :rtype: :py:class:`v1_8_1.web.vo.TimeflowPointParameters`
        """
        return self._timeflow_point_parameters[0]

    @timeflow_point_parameters.setter
    def timeflow_point_parameters(self, value):
        self._timeflow_point_parameters = (value, True)

