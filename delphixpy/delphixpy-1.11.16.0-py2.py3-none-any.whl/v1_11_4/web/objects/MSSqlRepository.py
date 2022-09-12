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
#     /delphix-mssql-repository.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_4.web.objects.SourceRepository import SourceRepository
from delphixpy.v1_11_4 import common

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

class MSSqlRepository(SourceRepository):
    """
    *(extends* :py:class:`v1_11_4.web.vo.SourceRepository` *)* The SQL Server
    source repository.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlRepository, self).__init__()
        self._type = ("MSSqlRepository", True)
        self._internal_version = (self.__undef__, True)
        self._fulltext_installed = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlRepository, cls).from_dict(data, dirty, undef_enabled)
        obj._internal_version = (data.get("internalVersion", obj.__undef__), dirty)
        if obj._internal_version[0] is not None and obj._internal_version[0] is not obj.__undef__:
            assert isinstance(obj._internal_version[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._internal_version[0], type(obj._internal_version[0])))
            common.validate_format(obj._internal_version[0], "None", None, None)
        obj._fulltext_installed = (data.get("fulltextInstalled", obj.__undef__), dirty)
        if obj._fulltext_installed[0] is not None and obj._fulltext_installed[0] is not obj.__undef__:
            assert isinstance(obj._fulltext_installed[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._fulltext_installed[0], type(obj._fulltext_installed[0])))
            common.validate_format(obj._fulltext_installed[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlRepository, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "internal_version" == "type" or (self.internal_version is not self.__undef__ and (not (dirty and not self._internal_version[1]))):
            dct["internalVersion"] = dictify(self.internal_version)
        if dirty and "internalVersion" in dct:
            del dct["internalVersion"]
        if "fulltext_installed" == "type" or (self.fulltext_installed is not self.__undef__ and (not (dirty and not self._fulltext_installed[1]) or isinstance(self.fulltext_installed, list) or belongs_to_parent)):
            dct["fulltextInstalled"] = dictify(self.fulltext_installed)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._internal_version = (self._internal_version[0], True)
        self._fulltext_installed = (self._fulltext_installed[0], True)

    def is_dirty(self):
        return any([self._internal_version[1], self._fulltext_installed[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlRepository):
            return False
        return super(MSSqlRepository, self).__eq__(other) and \
               self.internal_version == other.internal_version and \
               self.fulltext_installed == other.fulltext_installed

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def internal_version(self):
        """
        Internal version of the SQL Server instance.

        :rtype: ``int``
        """
        return self._internal_version[0]

    @property
    def fulltext_installed(self):
        """
        Represents Full-text search and semantic search feature.

        :rtype: ``bool``
        """
        return self._fulltext_installed[0]

    @fulltext_installed.setter
    def fulltext_installed(self, value):
        self._fulltext_installed = (value, True)

