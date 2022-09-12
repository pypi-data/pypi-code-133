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
#     /delphix-timeflow.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_6_0 import factory
from delphixpy.v1_6_0 import common

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

class Timeflow(NamedUserObject):
    """
    *(extends* :py:class:`v1_6_0.web.vo.NamedUserObject` *)* Data for a
    particular historical timeline within a database.
    """
    def __init__(self, undef_enabled=True):
        super(Timeflow, self).__init__()
        self._type = ("Timeflow", True)
        self._container = (self.__undef__, True)
        self._creation_type = (self.__undef__, True)
        self._parent_point = (self.__undef__, True)
        self._parent_snapshot = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Timeflow, cls).from_dict(data, dirty, undef_enabled)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._creation_type = (data.get("creationType", obj.__undef__), dirty)
        if obj._creation_type[0] is not None and obj._creation_type[0] is not obj.__undef__:
            assert isinstance(obj._creation_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._creation_type[0], type(obj._creation_type[0])))
            assert obj._creation_type[0] in ['INITIAL', 'INDETERMINATE', 'REFRESH', 'ROLLBACK', 'TEMPORARY', 'V2P', 'PDB_PLUG', 'WAREHOUSE', 'ORACLE_LIVE_SOURCE_RESYNC'], "Expected enum ['INITIAL', 'INDETERMINATE', 'REFRESH', 'ROLLBACK', 'TEMPORARY', 'V2P', 'PDB_PLUG', 'WAREHOUSE', 'ORACLE_LIVE_SOURCE_RESYNC'] but got %s" % obj._creation_type[0]
            common.validate_format(obj._creation_type[0], "None", None, None)
        if "parentPoint" in data and data["parentPoint"] is not None:
            obj._parent_point = (factory.create_object(data["parentPoint"], "TimeflowPoint"), dirty)
            factory.validate_type(obj._parent_point[0], "TimeflowPoint")
        else:
            obj._parent_point = (obj.__undef__, dirty)
        obj._parent_snapshot = (data.get("parentSnapshot", obj.__undef__), dirty)
        if obj._parent_snapshot[0] is not None and obj._parent_snapshot[0] is not obj.__undef__:
            assert isinstance(obj._parent_snapshot[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._parent_snapshot[0], type(obj._parent_snapshot[0])))
            common.validate_format(obj._parent_snapshot[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Timeflow, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]))):
            dct["container"] = dictify(self.container)
        if "creation_type" == "type" or (self.creation_type is not self.__undef__ and (not (dirty and not self._creation_type[1]))):
            dct["creationType"] = dictify(self.creation_type)
        if "parent_point" == "type" or (self.parent_point is not self.__undef__ and (not (dirty and not self._parent_point[1]))):
            dct["parentPoint"] = dictify(self.parent_point)
        if "parent_snapshot" == "type" or (self.parent_snapshot is not self.__undef__ and (not (dirty and not self._parent_snapshot[1]))):
            dct["parentSnapshot"] = dictify(self.parent_snapshot)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._creation_type = (self._creation_type[0], True)
        self._parent_point = (self._parent_point[0], True)
        self._parent_snapshot = (self._parent_snapshot[0], True)

    def is_dirty(self):
        return any([self._container[1], self._creation_type[1], self._parent_point[1], self._parent_snapshot[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Timeflow):
            return False
        return super(Timeflow, self).__eq__(other) and \
               self.container == other.container and \
               self.creation_type == other.creation_type and \
               self.parent_point == other.parent_point and \
               self.parent_snapshot == other.parent_snapshot

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        Reference to the data container (database) for this TimeFlow.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def creation_type(self):
        """
        The source action that created the TimeFlow. *(permitted values:
        INITIAL, INDETERMINATE, REFRESH, ROLLBACK, TEMPORARY, V2P, PDB_PLUG,
        WAREHOUSE, ORACLE_LIVE_SOURCE_RESYNC)*

        :rtype: ``TEXT_TYPE``
        """
        return self._creation_type[0]

    @creation_type.setter
    def creation_type(self, value):
        self._creation_type = (value, True)

    @property
    def parent_point(self):
        """
        The origin point on the parent TimeFlow from which this TimeFlow was
        provisioned. This will not be present for TimeFlows derived from linked
        sources.

        :rtype: :py:class:`v1_6_0.web.vo.TimeflowPoint`
        """
        return self._parent_point[0]

    @parent_point.setter
    def parent_point(self, value):
        self._parent_point = (value, True)

    @property
    def parent_snapshot(self):
        """
        Reference to the parent snapshot that serves as the provisioning base
        for this object. This may be different from the snapshot within the
        parent point, and is only present for virtual TimeFlows.

        :rtype: ``TEXT_TYPE``
        """
        return self._parent_snapshot[0]

    @parent_snapshot.setter
    def parent_snapshot(self, value):
        self._parent_snapshot = (value, True)

