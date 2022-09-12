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
#     /delphix-mssql-file-mapping-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.FileMappingParameters import FileMappingParameters
from delphixpy.v1_11_15 import factory
from delphixpy.v1_11_15 import common

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

class MSSqlFileMappingParameters(FileMappingParameters):
    """
    *(extends* :py:class:`v1_11_15.web.vo.FileMappingParameters` *)* The
    parameters to use as input to provide File Mapping for MSSQL databases.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlFileMappingParameters, self).__init__()
        self._type = ("MSSqlFileMappingParameters", True)
        self._filesystem_layout = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlFileMappingParameters, cls).from_dict(data, dirty, undef_enabled)
        if "filesystemLayout" not in data:
            raise ValueError("Missing required property \"filesystemLayout\".")
        if "filesystemLayout" in data and data["filesystemLayout"] is not None:
            obj._filesystem_layout = (factory.create_object(data["filesystemLayout"], "MSSqlTimeflowFilesystemLayout"), dirty)
            factory.validate_type(obj._filesystem_layout[0], "MSSqlTimeflowFilesystemLayout")
        else:
            obj._filesystem_layout = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlFileMappingParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "filesystem_layout" == "type" or (self.filesystem_layout is not self.__undef__ and (not (dirty and not self._filesystem_layout[1]) or isinstance(self.filesystem_layout, list) or belongs_to_parent)):
            dct["filesystemLayout"] = dictify(self.filesystem_layout, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._filesystem_layout = (self._filesystem_layout[0], True)

    def is_dirty(self):
        return any([self._filesystem_layout[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlFileMappingParameters):
            return False
        return super(MSSqlFileMappingParameters, self).__eq__(other) and \
               self.filesystem_layout == other.filesystem_layout

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def filesystem_layout(self):
        """
        The filesystem configuration of the MSSQL database.

        :rtype: :py:class:`v1_11_15.web.vo.MSSqlTimeflowFilesystemLayout`
        """
        return self._filesystem_layout[0]

    @filesystem_layout.setter
    def filesystem_layout(self, value):
        self._filesystem_layout = (value, True)

