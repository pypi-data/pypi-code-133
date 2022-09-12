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
#     /delphix-timeflow-filesystem-layout.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.FilesystemLayout import FilesystemLayout
from delphixpy.v1_11_13 import common

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

class TimeflowFilesystemLayout(FilesystemLayout):
    """
    *(extends* :py:class:`v1_11_13.web.vo.FilesystemLayout` *)* A filesystem
    layout that matches the filesystem of a Delphix TimeFlow.
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowFilesystemLayout, self).__init__()
        self._type = ("TimeflowFilesystemLayout", True)
        self._target_directory = (self.__undef__, True)
        self._data_directory = (self.__undef__, True)
        self._archive_directory = (self.__undef__, True)
        self._external_directory = (self.__undef__, True)
        self._temp_directory = (self.__undef__, True)
        self._script_directory = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowFilesystemLayout, cls).from_dict(data, dirty, undef_enabled)
        obj._target_directory = (data.get("targetDirectory", obj.__undef__), dirty)
        if obj._target_directory[0] is not None and obj._target_directory[0] is not obj.__undef__:
            assert isinstance(obj._target_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_directory[0], type(obj._target_directory[0])))
            common.validate_format(obj._target_directory[0], "None", None, None)
        obj._data_directory = (data.get("dataDirectory", obj.__undef__), dirty)
        if obj._data_directory[0] is not None and obj._data_directory[0] is not obj.__undef__:
            assert isinstance(obj._data_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_directory[0], type(obj._data_directory[0])))
            common.validate_format(obj._data_directory[0], "None", None, None)
        obj._archive_directory = (data.get("archiveDirectory", obj.__undef__), dirty)
        if obj._archive_directory[0] is not None and obj._archive_directory[0] is not obj.__undef__:
            assert isinstance(obj._archive_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._archive_directory[0], type(obj._archive_directory[0])))
            common.validate_format(obj._archive_directory[0], "None", None, None)
        obj._external_directory = (data.get("externalDirectory", obj.__undef__), dirty)
        if obj._external_directory[0] is not None and obj._external_directory[0] is not obj.__undef__:
            assert isinstance(obj._external_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._external_directory[0], type(obj._external_directory[0])))
            common.validate_format(obj._external_directory[0], "None", None, None)
        obj._temp_directory = (data.get("tempDirectory", obj.__undef__), dirty)
        if obj._temp_directory[0] is not None and obj._temp_directory[0] is not obj.__undef__:
            assert isinstance(obj._temp_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._temp_directory[0], type(obj._temp_directory[0])))
            common.validate_format(obj._temp_directory[0], "None", None, None)
        obj._script_directory = (data.get("scriptDirectory", obj.__undef__), dirty)
        if obj._script_directory[0] is not None and obj._script_directory[0] is not obj.__undef__:
            assert isinstance(obj._script_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._script_directory[0], type(obj._script_directory[0])))
            common.validate_format(obj._script_directory[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowFilesystemLayout, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "target_directory" == "type" or (self.target_directory is not self.__undef__ and (not (dirty and not self._target_directory[1]) or isinstance(self.target_directory, list) or belongs_to_parent)):
            dct["targetDirectory"] = dictify(self.target_directory)
        if "data_directory" == "type" or (self.data_directory is not self.__undef__ and (not (dirty and not self._data_directory[1]) or isinstance(self.data_directory, list) or belongs_to_parent)):
            dct["dataDirectory"] = dictify(self.data_directory)
        if "archive_directory" == "type" or (self.archive_directory is not self.__undef__ and (not (dirty and not self._archive_directory[1]) or isinstance(self.archive_directory, list) or belongs_to_parent)):
            dct["archiveDirectory"] = dictify(self.archive_directory)
        if "external_directory" == "type" or (self.external_directory is not self.__undef__ and (not (dirty and not self._external_directory[1]) or isinstance(self.external_directory, list) or belongs_to_parent)):
            dct["externalDirectory"] = dictify(self.external_directory)
        if "temp_directory" == "type" or (self.temp_directory is not self.__undef__ and (not (dirty and not self._temp_directory[1]) or isinstance(self.temp_directory, list) or belongs_to_parent)):
            dct["tempDirectory"] = dictify(self.temp_directory)
        if "script_directory" == "type" or (self.script_directory is not self.__undef__ and (not (dirty and not self._script_directory[1]) or isinstance(self.script_directory, list) or belongs_to_parent)):
            dct["scriptDirectory"] = dictify(self.script_directory)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._target_directory = (self._target_directory[0], True)
        self._data_directory = (self._data_directory[0], True)
        self._archive_directory = (self._archive_directory[0], True)
        self._external_directory = (self._external_directory[0], True)
        self._temp_directory = (self._temp_directory[0], True)
        self._script_directory = (self._script_directory[0], True)

    def is_dirty(self):
        return any([self._target_directory[1], self._data_directory[1], self._archive_directory[1], self._external_directory[1], self._temp_directory[1], self._script_directory[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowFilesystemLayout):
            return False
        return super(TimeflowFilesystemLayout, self).__eq__(other) and \
               self.target_directory == other.target_directory and \
               self.data_directory == other.data_directory and \
               self.archive_directory == other.archive_directory and \
               self.external_directory == other.external_directory and \
               self.temp_directory == other.temp_directory and \
               self.script_directory == other.script_directory

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def target_directory(self):
        """
        The base directory to use for the exported database.

        :rtype: ``TEXT_TYPE``
        """
        return self._target_directory[0]

    @target_directory.setter
    def target_directory(self, value):
        self._target_directory = (value, True)

    @property
    def data_directory(self):
        """
        The directory for data files.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_directory[0]

    @data_directory.setter
    def data_directory(self, value):
        self._data_directory = (value, True)

    @property
    def archive_directory(self):
        """
        The directory for archive files.

        :rtype: ``TEXT_TYPE``
        """
        return self._archive_directory[0]

    @archive_directory.setter
    def archive_directory(self, value):
        self._archive_directory = (value, True)

    @property
    def external_directory(self):
        """
        The directory for external files.

        :rtype: ``TEXT_TYPE``
        """
        return self._external_directory[0]

    @external_directory.setter
    def external_directory(self, value):
        self._external_directory = (value, True)

    @property
    def temp_directory(self):
        """
        The directory for temporary files.

        :rtype: ``TEXT_TYPE``
        """
        return self._temp_directory[0]

    @temp_directory.setter
    def temp_directory(self, value):
        self._temp_directory = (value, True)

    @property
    def script_directory(self):
        """
        The directory for script files.

        :rtype: ``TEXT_TYPE``
        """
        return self._script_directory[0]

    @script_directory.setter
    def script_directory(self, value):
        self._script_directory = (value, True)

