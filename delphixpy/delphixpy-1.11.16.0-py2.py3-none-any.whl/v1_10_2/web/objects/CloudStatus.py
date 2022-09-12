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
#     /delphix-cloud.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_2 import factory
from delphixpy.v1_10_2 import common

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

class CloudStatus(TypedObject):
    """
    *(extends* :py:class:`v1_10_2.web.vo.TypedObject` *)* Delphix Cloud
    facilities.
    """
    def __init__(self, undef_enabled=True):
        super(CloudStatus, self).__init__()
        self._type = ("CloudStatus", True)
        self._delphix_data_services_component_status = (self.__undef__, True)
        self._delphix_data_services_component_info = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CloudStatus, cls).from_dict(data, dirty, undef_enabled)
        obj._delphix_data_services_component_status = (data.get("delphixDataServicesComponentStatus", obj.__undef__), dirty)
        if obj._delphix_data_services_component_status[0] is not None and obj._delphix_data_services_component_status[0] is not obj.__undef__:
            assert isinstance(obj._delphix_data_services_component_status[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._delphix_data_services_component_status[0], type(obj._delphix_data_services_component_status[0])))
            assert obj._delphix_data_services_component_status[0] in ['ONLINE', 'MAINTENANCE', 'DISABLED', 'STARTING', 'UNKNOWN', 'ENABLING'], "Expected enum ['ONLINE', 'MAINTENANCE', 'DISABLED', 'STARTING', 'UNKNOWN', 'ENABLING'] but got %s" % obj._delphix_data_services_component_status[0]
            common.validate_format(obj._delphix_data_services_component_status[0], "None", None, None)
        if "delphixDataServicesComponentInfo" in data and data["delphixDataServicesComponentInfo"] is not None:
            obj._delphix_data_services_component_info = (factory.create_object(data["delphixDataServicesComponentInfo"], "DelphixDataServicesComponentInfo"), dirty)
            factory.validate_type(obj._delphix_data_services_component_info[0], "DelphixDataServicesComponentInfo")
        else:
            obj._delphix_data_services_component_info = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CloudStatus, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "delphix_data_services_component_status" == "type" or (self.delphix_data_services_component_status is not self.__undef__ and (not (dirty and not self._delphix_data_services_component_status[1]))):
            dct["delphixDataServicesComponentStatus"] = dictify(self.delphix_data_services_component_status)
        if "delphix_data_services_component_info" == "type" or (self.delphix_data_services_component_info is not self.__undef__ and (not (dirty and not self._delphix_data_services_component_info[1]))):
            dct["delphixDataServicesComponentInfo"] = dictify(self.delphix_data_services_component_info)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._delphix_data_services_component_status = (self._delphix_data_services_component_status[0], True)
        self._delphix_data_services_component_info = (self._delphix_data_services_component_info[0], True)

    def is_dirty(self):
        return any([self._delphix_data_services_component_status[1], self._delphix_data_services_component_info[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CloudStatus):
            return False
        return super(CloudStatus, self).__eq__(other) and \
               self.delphix_data_services_component_status == other.delphix_data_services_component_status and \
               self.delphix_data_services_component_info == other.delphix_data_services_component_info

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def delphix_data_services_component_status(self):
        """
        Indicates the current status of the Delphix Data Services Component.
        *(permitted values: ONLINE, MAINTENANCE, DISABLED, STARTING, UNKNOWN,
        ENABLING)*

        :rtype: ``TEXT_TYPE``
        """
        return self._delphix_data_services_component_status[0]

    @delphix_data_services_component_status.setter
    def delphix_data_services_component_status(self, value):
        self._delphix_data_services_component_status = (value, True)

    @property
    def delphix_data_services_component_info(self):
        """
        Provides information about the Delphix Data Services Component.

        :rtype: :py:class:`v1_10_2.web.vo.DelphixDataServicesComponentInfo`
        """
        return self._delphix_data_services_component_info[0]

    @delphix_data_services_component_info.setter
    def delphix_data_services_component_info(self, value):
        self._delphix_data_services_component_info = (value, True)

