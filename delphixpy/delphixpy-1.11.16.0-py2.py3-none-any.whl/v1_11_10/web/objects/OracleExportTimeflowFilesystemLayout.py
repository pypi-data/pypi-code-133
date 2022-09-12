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
#     /delphix-oracle-export-timeflow-filesystem-layout.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_10.web.objects.TimeflowFilesystemLayout import TimeflowFilesystemLayout
from delphixpy.v1_11_10 import common

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

class OracleExportTimeflowFilesystemLayout(TimeflowFilesystemLayout):
    """
    *(extends* :py:class:`v1_11_10.web.vo.TimeflowFilesystemLayout` *)* A
    filesystem layout that matches the filesystem of a Delphix Oracle TimeFlow
    for use in database export.
    """
    def __init__(self, undef_enabled=True):
        super(OracleExportTimeflowFilesystemLayout, self).__init__()
        self._type = ("OracleExportTimeflowFilesystemLayout", True)
        self._use_absolute_path_for_data_files = (self.__undef__, True)

    API_VERSION = "1.11.10"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleExportTimeflowFilesystemLayout, cls).from_dict(data, dirty, undef_enabled)
        obj._use_absolute_path_for_data_files = (data.get("useAbsolutePathForDataFiles", obj.__undef__), dirty)
        if obj._use_absolute_path_for_data_files[0] is not None and obj._use_absolute_path_for_data_files[0] is not obj.__undef__:
            assert isinstance(obj._use_absolute_path_for_data_files[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._use_absolute_path_for_data_files[0], type(obj._use_absolute_path_for_data_files[0])))
            common.validate_format(obj._use_absolute_path_for_data_files[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleExportTimeflowFilesystemLayout, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "use_absolute_path_for_data_files" == "type" or (self.use_absolute_path_for_data_files is not self.__undef__ and (not (dirty and not self._use_absolute_path_for_data_files[1]) or isinstance(self.use_absolute_path_for_data_files, list) or belongs_to_parent)):
            dct["useAbsolutePathForDataFiles"] = dictify(self.use_absolute_path_for_data_files)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._use_absolute_path_for_data_files = (self._use_absolute_path_for_data_files[0], True)

    def is_dirty(self):
        return any([self._use_absolute_path_for_data_files[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleExportTimeflowFilesystemLayout):
            return False
        return super(OracleExportTimeflowFilesystemLayout, self).__eq__(other) and \
               self.use_absolute_path_for_data_files == other.use_absolute_path_for_data_files

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def use_absolute_path_for_data_files(self):
        """
        Use absolute path for data files.

        :rtype: ``bool``
        """
        return self._use_absolute_path_for_data_files[0]

    @use_absolute_path_for_data_files.setter
    def use_absolute_path_for_data_files(self, value):
        self._use_absolute_path_for_data_files = (value, True)

