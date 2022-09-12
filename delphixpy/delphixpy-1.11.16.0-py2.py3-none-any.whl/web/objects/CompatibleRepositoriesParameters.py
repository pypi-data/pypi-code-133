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
#     /delphix-compatible-repositories-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.TypedObject import TypedObject
from delphixpy import common

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

class CompatibleRepositoriesParameters(TypedObject):
    """
    *(extends* :py:class:`delphixpy.web.vo.TypedObject` *)* The compatibility
    parameters to use for filtering the list of available repositories.
    """
    def __init__(self, undef_enabled=True):
        super(CompatibleRepositoriesParameters, self).__init__()
        self._type = ("CompatibleRepositoriesParameters", True)
        self._environment = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CompatibleRepositoriesParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._environment = (data.get("environment", obj.__undef__), dirty)
        if obj._environment[0] is not None and obj._environment[0] is not obj.__undef__:
            assert isinstance(obj._environment[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment[0], type(obj._environment[0])))
            common.validate_format(obj._environment[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CompatibleRepositoriesParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "environment" == "type" or (self.environment is not self.__undef__ and (not (dirty and not self._environment[1]) or isinstance(self.environment, list) or belongs_to_parent)):
            dct["environment"] = dictify(self.environment)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._environment = (self._environment[0], True)

    def is_dirty(self):
        return any([self._environment[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CompatibleRepositoriesParameters):
            return False
        return super(CompatibleRepositoriesParameters, self).__eq__(other) and \
               self.environment == other.environment

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def environment(self):
        """
        Restrict returned repositories to this environment.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment[0]

    @environment.setter
    def environment(self, value):
        self._environment = (value, True)

