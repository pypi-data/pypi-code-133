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
#     /delphix-appdata-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.Source import Source
from delphixpy.v1_11_2 import factory
from delphixpy.v1_11_2 import common

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

class AppDataSource(Source):
    """
    *(extends* :py:class:`v1_11_2.web.vo.Source` *)* An AppData source.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataSource, self).__init__()
        self._type = ("AppDataSource", True)
        self._toolkit = (self.__undef__, True)
        self._runtime = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataSource, cls).from_dict(data, dirty, undef_enabled)
        obj._toolkit = (data.get("toolkit", obj.__undef__), dirty)
        if obj._toolkit[0] is not None and obj._toolkit[0] is not obj.__undef__:
            assert isinstance(obj._toolkit[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._toolkit[0], type(obj._toolkit[0])))
            common.validate_format(obj._toolkit[0], "objectReference", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "AppDataSourceRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "AppDataSourceRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "toolkit" == "type" or (self.toolkit is not self.__undef__ and (not (dirty and not self._toolkit[1]))):
            dct["toolkit"] = dictify(self.toolkit)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._toolkit = (self._toolkit[0], True)
        self._runtime = (self._runtime[0], True)

    def is_dirty(self):
        return any([self._toolkit[1], self._runtime[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataSource):
            return False
        return super(AppDataSource, self).__eq__(other) and \
               self.toolkit == other.toolkit and \
               self.runtime == other.runtime

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def toolkit(self):
        """
        The toolkit associated with this source.

        :rtype: ``TEXT_TYPE``
        """
        return self._toolkit[0]

    @toolkit.setter
    def toolkit(self, value):
        self._toolkit = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this source.

        :rtype: :py:class:`v1_11_2.web.vo.AppDataSourceRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

