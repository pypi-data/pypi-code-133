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
#     /delphix-appdata-source-repository.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.SourceRepository import SourceRepository
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

class AppDataRepository(SourceRepository):
    """
    *(extends* :py:class:`v1_6_0.web.vo.SourceRepository` *)* An AppData
    repository.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataRepository, self).__init__()
        self._type = ("AppDataRepository", True)
        self._parameters = (self.__undef__, True)
        self._toolkit = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataRepository, cls).from_dict(data, dirty, undef_enabled)
        obj._parameters = []
        for item in data.get("parameters") or []:
            obj._parameters.append(factory.create_object(item))
            factory.validate_type(obj._parameters[-1], "DynamicParameterValue")
        obj._parameters = (obj._parameters, dirty)
        obj._toolkit = (data.get("toolkit", obj.__undef__), dirty)
        if obj._toolkit[0] is not None and obj._toolkit[0] is not obj.__undef__:
            assert isinstance(obj._toolkit[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._toolkit[0], type(obj._toolkit[0])))
            common.validate_format(obj._toolkit[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataRepository, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "parameters" == "type" or (self.parameters is not self.__undef__ and (not (dirty and not self._parameters[1]) or isinstance(self.parameters, list) or belongs_to_parent)):
            dct["parameters"] = dictify(self.parameters, prop_is_list_or_vo=True)
        if "toolkit" == "type" or (self.toolkit is not self.__undef__ and (not (dirty and not self._toolkit[1]) or isinstance(self.toolkit, list) or belongs_to_parent)):
            dct["toolkit"] = dictify(self.toolkit)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._parameters = (self._parameters[0], True)
        self._toolkit = (self._toolkit[0], True)

    def is_dirty(self):
        return any([self._parameters[1], self._toolkit[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataRepository):
            return False
        return super(AppDataRepository, self).__eq__(other) and \
               self.parameters == other.parameters and \
               self.toolkit == other.toolkit

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def parameters(self):
        """
        The list of parameters specified by the repository schema in the
        toolkit. If no schema is specified, this list is empty.

        :rtype: ``list`` of :py:class:`v1_6_0.web.vo.DynamicParameterValue`
        """
        return self._parameters[0]

    @parameters.setter
    def parameters(self, value):
        self._parameters = (value, True)

    @property
    def toolkit(self):
        """
        The toolkit associated with this repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._toolkit[0]

    @toolkit.setter
    def toolkit(self, value):
        self._toolkit = (value, True)

