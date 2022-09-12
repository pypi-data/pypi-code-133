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
#     /delphix-source-environment-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_9 import factory
from delphixpy.v1_11_9 import common

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

class SourceEnvironmentCreateParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.TypedObject` *)* The parameters used
    for source environment create parameters.
    """
    def __init__(self, undef_enabled=True):
        super(SourceEnvironmentCreateParameters, self).__init__()
        self._type = ("SourceEnvironmentCreateParameters", True)
        self._primary_user = (self.__undef__, True)
        self._log_collection_enabled = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceEnvironmentCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "primaryUser" in data and data["primaryUser"] is not None:
            obj._primary_user = (factory.create_object(data["primaryUser"], "EnvironmentUser"), dirty)
            factory.validate_type(obj._primary_user[0], "EnvironmentUser")
        else:
            obj._primary_user = (obj.__undef__, dirty)
        obj._log_collection_enabled = (data.get("logCollectionEnabled", obj.__undef__), dirty)
        if obj._log_collection_enabled[0] is not None and obj._log_collection_enabled[0] is not obj.__undef__:
            assert isinstance(obj._log_collection_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._log_collection_enabled[0], type(obj._log_collection_enabled[0])))
            common.validate_format(obj._log_collection_enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceEnvironmentCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "primary_user" == "type" or (self.primary_user is not self.__undef__ and (not (dirty and not self._primary_user[1]) or isinstance(self.primary_user, list) or belongs_to_parent)):
            dct["primaryUser"] = dictify(self.primary_user, prop_is_list_or_vo=True)
        if "log_collection_enabled" == "type" or (self.log_collection_enabled is not self.__undef__ and (not (dirty and not self._log_collection_enabled[1]) or isinstance(self.log_collection_enabled, list) or belongs_to_parent)):
            dct["logCollectionEnabled"] = dictify(self.log_collection_enabled)
        elif belongs_to_parent and self.log_collection_enabled is self.__undef__:
            dct["logCollectionEnabled"] = False
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._primary_user = (self._primary_user[0], True)
        self._log_collection_enabled = (self._log_collection_enabled[0], True)

    def is_dirty(self):
        return any([self._primary_user[1], self._log_collection_enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceEnvironmentCreateParameters):
            return False
        return super(SourceEnvironmentCreateParameters, self).__eq__(other) and \
               self.primary_user == other.primary_user and \
               self.log_collection_enabled == other.log_collection_enabled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def primary_user(self):
        """
        The primary user associated with the environment.

        :rtype: :py:class:`v1_11_9.web.vo.EnvironmentUser`
        """
        return self._primary_user[0]

    @primary_user.setter
    def primary_user(self, value):
        self._primary_user = (value, True)

    @property
    def log_collection_enabled(self):
        """
        Flag indicating whether it is allowed to collect logs, potentially
        containing sensitive information, related to the created source
        environment.

        :rtype: ``bool``
        """
        return self._log_collection_enabled[0]

    @log_collection_enabled.setter
    def log_collection_enabled(self, value):
        self._log_collection_enabled = (value, True)

