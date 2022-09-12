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
#     /delphix-rollback-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_5 import factory
from delphixpy.v1_10_5 import common

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

class RollbackParameters(TypedObject):
    """
    *(extends* :py:class:`v1_10_5.web.vo.TypedObject` *)* The parameters to use
    as input to rollback requests for MSSQL, PostgreSQL, AppData, ASE or MySQL.
    """
    def __init__(self, undef_enabled=True):
        super(RollbackParameters, self).__init__()
        self._type = ("RollbackParameters", True)
        self._timeflow_point_parameters = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RollbackParameters, cls).from_dict(data, dirty, undef_enabled)
        if "timeflowPointParameters" not in data:
            raise ValueError("Missing required property \"timeflowPointParameters\".")
        if "timeflowPointParameters" in data and data["timeflowPointParameters"] is not None:
            obj._timeflow_point_parameters = (factory.create_object(data["timeflowPointParameters"], "TimeflowPointParameters"), dirty)
            factory.validate_type(obj._timeflow_point_parameters[0], "TimeflowPointParameters")
        else:
            obj._timeflow_point_parameters = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RollbackParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "timeflow_point_parameters" == "type" or (self.timeflow_point_parameters is not self.__undef__ and (not (dirty and not self._timeflow_point_parameters[1]) or isinstance(self.timeflow_point_parameters, list) or belongs_to_parent)):
            dct["timeflowPointParameters"] = dictify(self.timeflow_point_parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._timeflow_point_parameters = (self._timeflow_point_parameters[0], True)

    def is_dirty(self):
        return any([self._timeflow_point_parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RollbackParameters):
            return False
        return super(RollbackParameters, self).__eq__(other) and \
               self.timeflow_point_parameters == other.timeflow_point_parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def timeflow_point_parameters(self):
        """
        The TimeFlow point, bookmark, or semantic location to roll the database
        back to.

        :rtype: :py:class:`v1_10_5.web.vo.TimeflowPointParameters`
        """
        return self._timeflow_point_parameters[0]

    @timeflow_point_parameters.setter
    def timeflow_point_parameters(self, value):
        self._timeflow_point_parameters = (value, True)

