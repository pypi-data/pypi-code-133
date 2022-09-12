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
#     /delphix-oracle-start-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_2.web.objects.SourceStartParameters import SourceStartParameters
from delphixpy.v1_5_2 import factory
from delphixpy.v1_5_2 import common

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

class OracleStartParameters(SourceStartParameters):
    """
    *(extends* :py:class:`v1_5_2.web.vo.SourceStartParameters` *)* The
    parameters to use as input to start oracle sources.
    """
    def __init__(self, undef_enabled=True):
        super(OracleStartParameters, self).__init__()
        self._type = ("OracleStartParameters", True)
        self._credential = (self.__undef__, True)
        self._instances = (self.__undef__, True)
        self._username = (self.__undef__, True)

    API_VERSION = "1.5.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleStartParameters, cls).from_dict(data, dirty, undef_enabled)
        if "credential" in data and data["credential"] is not None:
            obj._credential = (factory.create_object(data["credential"], "Credential"), dirty)
            factory.validate_type(obj._credential[0], "Credential")
        else:
            obj._credential = (obj.__undef__, dirty)
        obj._instances = []
        for item in data.get("instances") or []:
            assert isinstance(item, float), ("Expected one of ['number'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._instances.append(item)
        obj._instances = (obj._instances, dirty)
        obj._username = (data.get("username", obj.__undef__), dirty)
        if obj._username[0] is not None and obj._username[0] is not obj.__undef__:
            assert isinstance(obj._username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._username[0], type(obj._username[0])))
            common.validate_format(obj._username[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleStartParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "credential" == "type" or (self.credential is not self.__undef__ and (not (dirty and not self._credential[1]))):
            dct["credential"] = dictify(self.credential)
        if "instances" == "type" or (self.instances is not self.__undef__ and (not (dirty and not self._instances[1]))):
            dct["instances"] = dictify(self.instances)
        if "username" == "type" or (self.username is not self.__undef__ and (not (dirty and not self._username[1]))):
            dct["username"] = dictify(self.username)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._credential = (self._credential[0], True)
        self._instances = (self._instances[0], True)
        self._username = (self._username[0], True)

    def is_dirty(self):
        return any([self._credential[1], self._instances[1], self._username[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleStartParameters):
            return False
        return super(OracleStartParameters, self).__eq__(other) and \
               self.credential == other.credential and \
               self.instances == other.instances and \
               self.username == other.username

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def credential(self):
        """
        The security credential of the privileged user to run the provision
        operation as.

        :rtype: :py:class:`v1_5_2.web.vo.Credential`
        """
        return self._credential[0]

    @credential.setter
    def credential(self, value):
        self._credential = (value, True)

    @property
    def instances(self):
        """
        List of specific Oracle instances to start.

        :rtype: ``list`` of ``float``
        """
        return self._instances[0]

    @instances.setter
    def instances(self, value):
        self._instances = (value, True)

    @property
    def username(self):
        """
        The name of the privileged user to run the provision operation as.

        :rtype: ``TEXT_TYPE``
        """
        return self._username[0]

    @username.setter
    def username(self, value):
        self._username = (value, True)

