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
#     /delphix-js-data-container-delete-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.TypedObject import TypedObject
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

class JSDataContainerDeleteParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.TypedObject` *)* The parameters used
    to delete a data container.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataContainerDeleteParameters, self).__init__()
        self._type = ("JSDataContainerDeleteParameters", True)
        self._delete_data_sources = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataContainerDeleteParameters, cls).from_dict(data, dirty, undef_enabled)
        if "deleteDataSources" not in data:
            raise ValueError("Missing required property \"deleteDataSources\".")
        obj._delete_data_sources = (data.get("deleteDataSources", obj.__undef__), dirty)
        if obj._delete_data_sources[0] is not None and obj._delete_data_sources[0] is not obj.__undef__:
            assert isinstance(obj._delete_data_sources[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._delete_data_sources[0], type(obj._delete_data_sources[0])))
            common.validate_format(obj._delete_data_sources[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataContainerDeleteParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "delete_data_sources" == "type" or (self.delete_data_sources is not self.__undef__ and (not (dirty and not self._delete_data_sources[1]) or isinstance(self.delete_data_sources, list) or belongs_to_parent)):
            dct["deleteDataSources"] = dictify(self.delete_data_sources)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._delete_data_sources = (self._delete_data_sources[0], True)

    def is_dirty(self):
        return any([self._delete_data_sources[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataContainerDeleteParameters):
            return False
        return super(JSDataContainerDeleteParameters, self).__eq__(other) and \
               self.delete_data_sources == other.delete_data_sources

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def delete_data_sources(self):
        """
        *(default value: True)* If this value is true, then delete the
        underlying data from all data sources.

        :rtype: ``bool``
        """
        return self._delete_data_sources[0]

    @delete_data_sources.setter
    def delete_data_sources(self, value):
        self._delete_data_sources = (value, True)

