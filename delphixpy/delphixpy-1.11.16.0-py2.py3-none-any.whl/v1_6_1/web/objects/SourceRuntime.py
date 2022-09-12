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
#     /delphix-source-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_1 import common

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

class SourceRuntime(TypedObject):
    """
    *(extends* :py:class:`v1_6_1.web.vo.TypedObject` *)* Runtime properties of
    a linked or virtual source database.
    """
    def __init__(self, undef_enabled=True):
        super(SourceRuntime, self).__init__()
        self._type = ("SourceRuntime", True)
        self._accessible = (self.__undef__, True)
        self._database_size = (self.__undef__, True)
        self._enabled = (self.__undef__, True)
        self._not_accessible_reason = (self.__undef__, True)
        self._status = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._accessible = (data.get("accessible", obj.__undef__), dirty)
        if obj._accessible[0] is not None and obj._accessible[0] is not obj.__undef__:
            assert isinstance(obj._accessible[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._accessible[0], type(obj._accessible[0])))
            common.validate_format(obj._accessible[0], "None", None, None)
        obj._database_size = (data.get("databaseSize", obj.__undef__), dirty)
        if obj._database_size[0] is not None and obj._database_size[0] is not obj.__undef__:
            assert isinstance(obj._database_size[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._database_size[0], type(obj._database_size[0])))
            common.validate_format(obj._database_size[0], "None", None, None)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            assert obj._enabled[0] in ['ENABLED', 'PARTIAL', 'DISABLED'], "Expected enum ['ENABLED', 'PARTIAL', 'DISABLED'] but got %s" % obj._enabled[0]
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._not_accessible_reason = (data.get("notAccessibleReason", obj.__undef__), dirty)
        if obj._not_accessible_reason[0] is not None and obj._not_accessible_reason[0] is not obj.__undef__:
            assert isinstance(obj._not_accessible_reason[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._not_accessible_reason[0], type(obj._not_accessible_reason[0])))
            common.validate_format(obj._not_accessible_reason[0], "None", None, None)
        obj._status = (data.get("status", obj.__undef__), dirty)
        if obj._status[0] is not None and obj._status[0] is not obj.__undef__:
            assert isinstance(obj._status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status[0], type(obj._status[0])))
            assert obj._status[0] in ['RUNNING', 'INACTIVE', 'PENDING', 'CANCELED', 'FAILED', 'CHECKING', 'UNKNOWN'], "Expected enum ['RUNNING', 'INACTIVE', 'PENDING', 'CANCELED', 'FAILED', 'CHECKING', 'UNKNOWN'] but got %s" % obj._status[0]
            common.validate_format(obj._status[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "accessible" == "type" or (self.accessible is not self.__undef__ and (not (dirty and not self._accessible[1]))):
            dct["accessible"] = dictify(self.accessible)
        if "database_size" == "type" or (self.database_size is not self.__undef__ and (not (dirty and not self._database_size[1]))):
            dct["databaseSize"] = dictify(self.database_size)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]))):
            dct["enabled"] = dictify(self.enabled)
        if "not_accessible_reason" == "type" or (self.not_accessible_reason is not self.__undef__ and (not (dirty and not self._not_accessible_reason[1]))):
            dct["notAccessibleReason"] = dictify(self.not_accessible_reason)
        if "status" == "type" or (self.status is not self.__undef__ and (not (dirty and not self._status[1]))):
            dct["status"] = dictify(self.status)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._accessible = (self._accessible[0], True)
        self._database_size = (self._database_size[0], True)
        self._enabled = (self._enabled[0], True)
        self._not_accessible_reason = (self._not_accessible_reason[0], True)
        self._status = (self._status[0], True)

    def is_dirty(self):
        return any([self._accessible[1], self._database_size[1], self._enabled[1], self._not_accessible_reason[1], self._status[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceRuntime):
            return False
        return super(SourceRuntime, self).__eq__(other) and \
               self.accessible == other.accessible and \
               self.database_size == other.database_size and \
               self.enabled == other.enabled and \
               self.not_accessible_reason == other.not_accessible_reason and \
               self.status == other.status

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def accessible(self):
        """
        True if the source is JDBC accessible. If false then no properties can
        be retrieved.

        :rtype: ``bool``
        """
        return self._accessible[0]

    @accessible.setter
    def accessible(self, value):
        self._accessible = (value, True)

    @property
    def database_size(self):
        """
        Size of the database in bytes.

        :rtype: ``float``
        """
        return self._database_size[0]

    @database_size.setter
    def database_size(self, value):
        self._database_size = (value, True)

    @property
    def enabled(self):
        """
        Status indicating whether the source is enabled. A source has a
        'PARTIAL' status if its sub-sources are not all enabled. *(permitted
        values: ENABLED, PARTIAL, DISABLED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def not_accessible_reason(self):
        """
        The reason why the source is not JDBC accessible.

        :rtype: ``TEXT_TYPE``
        """
        return self._not_accessible_reason[0]

    @not_accessible_reason.setter
    def not_accessible_reason(self, value):
        self._not_accessible_reason = (value, True)

    @property
    def status(self):
        """
        Status of the source. 'Unknown' if all attempts to connect to the
        source failed. *(permitted values: RUNNING, INACTIVE, PENDING,
        CANCELED, FAILED, CHECKING, UNKNOWN)*

        :rtype: ``TEXT_TYPE``
        """
        return self._status[0]

    @status.setter
    def status(self, value):
        self._status = (value, True)

