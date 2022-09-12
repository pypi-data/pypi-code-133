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
#     /delphix-commvault-connectivity-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_12.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_12 import common

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

class CommvaultConnectivityParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_12.web.vo.TypedObject` *)* Parameters needed to
    test Commvault connectivity on an environment.
    """
    def __init__(self, undef_enabled=True):
        super(CommvaultConnectivityParameters, self).__init__()
        self._type = ("CommvaultConnectivityParameters", True)
        self._environment = (self.__undef__, True)
        self._environment_user = (self.__undef__, True)
        self._commserve_host_name = (self.__undef__, True)
        self._source_client_name = (self.__undef__, True)
        self._staging_client_name = (self.__undef__, True)

    API_VERSION = "1.11.12"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CommvaultConnectivityParameters, cls).from_dict(data, dirty, undef_enabled)
        if "environment" not in data:
            raise ValueError("Missing required property \"environment\".")
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        if "environmentUser" not in data:
            raise ValueError("Missing required property \"environmentUser\".")
        obj._environment_user = (data.get("environmentUser", obj.__undef__), dirty)
        if obj._environment_user[0] is not None and obj._environment_user[0] is not obj.__undef__:
            assert isinstance(obj._environment_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment_user[0], type(obj._environment_user[0])))
            common.validate_format(obj._environment_user[0], "objectReference", None, None)
        if "commserveHostName" not in data:
            raise ValueError("Missing required property \"commserveHostName\".")
        obj._commserve_host_name = (data.get("commserveHostName", obj.__undef__), dirty)
        if obj._commserve_host_name[0] is not None and obj._commserve_host_name[0] is not obj.__undef__:
            assert isinstance(obj._commserve_host_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._commserve_host_name[0], type(obj._commserve_host_name[0])))
            common.validate_format(obj._commserve_host_name[0], "None", None, None)
        if "sourceClientName" not in data:
            raise ValueError("Missing required property \"sourceClientName\".")
        obj._source_client_name = (data.get("sourceClientName", obj.__undef__), dirty)
        if obj._source_client_name[0] is not None and obj._source_client_name[0] is not obj.__undef__:
            assert isinstance(obj._source_client_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_client_name[0], type(obj._source_client_name[0])))
            common.validate_format(obj._source_client_name[0], "None", None, None)
        if "stagingClientName" not in data:
            raise ValueError("Missing required property \"stagingClientName\".")
        obj._staging_client_name = (data.get("stagingClientName", obj.__undef__), dirty)
        if obj._staging_client_name[0] is not None and obj._staging_client_name[0] is not obj.__undef__:
            assert isinstance(obj._staging_client_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_client_name[0], type(obj._staging_client_name[0])))
            common.validate_format(obj._staging_client_name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CommvaultConnectivityParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]) or isinstance(self.environment, list) or belongs_to_parent)):
            dct["environment"] = dictify(self.environment)
        if "environment_user" == "type" or (self.environment_user is not self.__undef__ and (not (dirty and not self._environment_user[1]) or isinstance(self.environment_user, list) or belongs_to_parent)):
            dct["environmentUser"] = dictify(self.environment_user)
        if "commserve_host_name" == "type" or (self.commserve_host_name is not self.__undef__ and (not (dirty and not self._commserve_host_name[1]) or isinstance(self.commserve_host_name, list) or belongs_to_parent)):
            dct["commserveHostName"] = dictify(self.commserve_host_name)
        if "source_client_name" == "type" or (self.source_client_name is not self.__undef__ and (not (dirty and not self._source_client_name[1]) or isinstance(self.source_client_name, list) or belongs_to_parent)):
            dct["sourceClientName"] = dictify(self.source_client_name)
        if "staging_client_name" == "type" or (self.staging_client_name is not self.__undef__ and (not (dirty and not self._staging_client_name[1]) or isinstance(self.staging_client_name, list) or belongs_to_parent)):
            dct["stagingClientName"] = dictify(self.staging_client_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._environment = (self._environment[0], True)
        self._environment_user = (self._environment_user[0], True)
        self._commserve_host_name = (self._commserve_host_name[0], True)
        self._source_client_name = (self._source_client_name[0], True)
        self._staging_client_name = (self._staging_client_name[0], True)

    def is_dirty(self):
        return any([self._environment[1], self._environment_user[1], self._commserve_host_name[1], self._source_client_name[1], self._staging_client_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CommvaultConnectivityParameters):
            return False
        return super(CommvaultConnectivityParameters, self).__eq__(other) and \
               self.environment == other.environment and \
               self.environment_user == other.environment_user and \
               self.commserve_host_name == other.commserve_host_name and \
               self.source_client_name == other.source_client_name and \
               self.staging_client_name == other.staging_client_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def environment(self):
        """
        Target environment to test Commvault connectivity from.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

    @property
    def environment_user(self):
        """
        The environment user required to connect to the target environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment_user[0]

    @environment_user.setter
    def environment_user(self, value):
        self._environment_user = (value, True)

    @property
    def commserve_host_name(self):
        """
        The hostname of the CommServe server to connect to.

        :rtype: ``TEXT_TYPE``
        """
        return self._commserve_host_name[0]

    @commserve_host_name.setter
    def commserve_host_name(self, value):
        self._commserve_host_name = (value, True)

    @property
    def source_client_name(self):
        """
        The name of the Source Client in CommServe.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_client_name[0]

    @source_client_name.setter
    def source_client_name(self, value):
        self._source_client_name = (value, True)

    @property
    def staging_client_name(self):
        """
        The name of the Staging Client in CommServe.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_client_name[0]

    @staging_client_name.setter
    def staging_client_name(self, value):
        self._staging_client_name = (value, True)

