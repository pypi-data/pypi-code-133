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
#     /delphix-oracle-listener.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_0.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_5_0 import common

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

class OracleListener(NamedUserObject):
    """
    *(extends* :py:class:`v1_5_0.web.vo.NamedUserObject` *)* An Oracle
    listener.
    """
    def __init__(self, undef_enabled=True):
        super(OracleListener, self).__init__()
        self._type = ("OracleListener", True)
        self._discovered = (self.__undef__, True)
        self._end_points = (self.__undef__, True)
        self._environment = (self.__undef__, True)

    API_VERSION = "1.5.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleListener, cls).from_dict(data, dirty, undef_enabled)
        obj._discovered = (data.get("discovered", obj.__undef__), dirty)
        if obj._discovered[0] is not None and obj._discovered[0] is not obj.__undef__:
            assert isinstance(obj._discovered[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._discovered[0], type(obj._discovered[0])))
            common.validate_format(obj._discovered[0], "None", None, None)
        obj._end_points = []
        for item in data.get("endPoints") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "hostnameAndPort", None, None)
            obj._end_points.append(item)
        obj._end_points = (obj._end_points, dirty)
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleListener, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "discovered" == "type" or (self.discovered is not self.__undef__ and (not (dirty and not self._discovered[1]))):
            dct["discovered"] = dictify(self.discovered)
        if "end_points" == "type" or (self.end_points is not self.__undef__ and (not (dirty and not self._end_points[1]) or isinstance(self.end_points, list) or belongs_to_parent)):
            dct["endPoints"] = dictify(self.end_points, prop_is_list_or_vo=True)
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]) or isinstance(self.environment, list) or belongs_to_parent)):
            dct["environment"] = dictify(self.environment)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._discovered = (self._discovered[0], True)
        self._end_points = (self._end_points[0], True)
        self._environment = (self._environment[0], True)

    def is_dirty(self):
        return any([self._discovered[1], self._end_points[1], self._environment[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleListener):
            return False
        return super(OracleListener, self).__eq__(other) and \
               self.discovered == other.discovered and \
               self.end_points == other.end_points and \
               self.environment == other.environment

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def discovered(self):
        """
        Whether this listener was automatically discovered.

        :rtype: ``bool``
        """
        return self._discovered[0]

    @discovered.setter
    def discovered(self, value):
        self._discovered = (value, True)

    @property
    def end_points(self):
        """
        The list of end points for this listener.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._end_points[0]

    @end_points.setter
    def end_points(self, value):
        self._end_points = (value, True)

    @property
    def environment(self):
        """
        Reference to the environment this listener is associated with.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

