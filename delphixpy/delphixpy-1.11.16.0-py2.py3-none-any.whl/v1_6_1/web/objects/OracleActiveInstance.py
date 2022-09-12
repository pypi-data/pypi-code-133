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
#     /delphix-oracle-active-instance.json
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

class OracleActiveInstance(TypedObject):
    """
    *(extends* :py:class:`v1_6_1.web.vo.TypedObject` *)* Active instance
    information for an Oracle database.
    """
    def __init__(self, undef_enabled=True):
        super(OracleActiveInstance, self).__init__()
        self._type = ("OracleActiveInstance", True)
        self._host_name = (self.__undef__, True)
        self._instance_name = (self.__undef__, True)
        self._instance_number = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleActiveInstance, cls).from_dict(data, dirty, undef_enabled)
        obj._host_name = (data.get("hostName", obj.__undef__), dirty)
        if obj._host_name[0] is not None and obj._host_name[0] is not obj.__undef__:
            assert isinstance(obj._host_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._host_name[0], type(obj._host_name[0])))
            common.validate_format(obj._host_name[0], "None", None, None)
        obj._instance_name = (data.get("instanceName", obj.__undef__), dirty)
        if obj._instance_name[0] is not None and obj._instance_name[0] is not obj.__undef__:
            assert isinstance(obj._instance_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._instance_name[0], type(obj._instance_name[0])))
            common.validate_format(obj._instance_name[0], "None", None, None)
        obj._instance_number = (data.get("instanceNumber", obj.__undef__), dirty)
        if obj._instance_number[0] is not None and obj._instance_number[0] is not obj.__undef__:
            assert isinstance(obj._instance_number[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._instance_number[0], type(obj._instance_number[0])))
            common.validate_format(obj._instance_number[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleActiveInstance, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "host_name" == "type" or (self.host_name is not self.__undef__ and (not (dirty and not self._host_name[1]))):
            dct["hostName"] = dictify(self.host_name)
        if "instance_name" == "type" or (self.instance_name is not self.__undef__ and (not (dirty and not self._instance_name[1]))):
            dct["instanceName"] = dictify(self.instance_name)
        if "instance_number" == "type" or (self.instance_number is not self.__undef__ and (not (dirty and not self._instance_number[1]))):
            dct["instanceNumber"] = dictify(self.instance_number)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._host_name = (self._host_name[0], True)
        self._instance_name = (self._instance_name[0], True)
        self._instance_number = (self._instance_number[0], True)

    def is_dirty(self):
        return any([self._host_name[1], self._instance_name[1], self._instance_number[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleActiveInstance):
            return False
        return super(OracleActiveInstance, self).__eq__(other) and \
               self.host_name == other.host_name and \
               self.instance_name == other.instance_name and \
               self.instance_number == other.instance_number

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def host_name(self):
        """
        The name of the host the instance runs on.

        :rtype: ``TEXT_TYPE``
        """
        return self._host_name[0]

    @host_name.setter
    def host_name(self, value):
        self._host_name = (value, True)

    @property
    def instance_name(self):
        """
        The name of the Oracle instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._instance_name[0]

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = (value, True)

    @property
    def instance_number(self):
        """
        The number of the Oracle instance.

        :rtype: ``int``
        """
        return self._instance_number[0]

    @instance_number.setter
    def instance_number(self, value):
        self._instance_number = (value, True)

