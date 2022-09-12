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
#     /delphix-version-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_1 import common

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

class VersionInfo(TypedObject):
    """
    *(extends* :py:class:`v1_4_1.web.vo.TypedObject` *)* Representation of a
    Delphix software revision.
    """
    def __init__(self, undef_enabled=True):
        super(VersionInfo, self).__init__()
        self._type = ("VersionInfo", True)
        self._major = (self.__undef__, True)
        self._micro = (self.__undef__, True)
        self._minor = (self.__undef__, True)
        self._patch = (self.__undef__, True)

    API_VERSION = "1.4.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(VersionInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._major = (data.get("major", obj.__undef__), dirty)
        if obj._major[0] is not None and obj._major[0] is not obj.__undef__:
            assert isinstance(obj._major[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._major[0], type(obj._major[0])))
            common.validate_format(obj._major[0], "None", None, None)
        obj._micro = (data.get("micro", obj.__undef__), dirty)
        if obj._micro[0] is not None and obj._micro[0] is not obj.__undef__:
            assert isinstance(obj._micro[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._micro[0], type(obj._micro[0])))
            common.validate_format(obj._micro[0], "None", None, None)
        obj._minor = (data.get("minor", obj.__undef__), dirty)
        if obj._minor[0] is not None and obj._minor[0] is not obj.__undef__:
            assert isinstance(obj._minor[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._minor[0], type(obj._minor[0])))
            common.validate_format(obj._minor[0], "None", None, None)
        obj._patch = (data.get("patch", obj.__undef__), dirty)
        if obj._patch[0] is not None and obj._patch[0] is not obj.__undef__:
            assert isinstance(obj._patch[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._patch[0], type(obj._patch[0])))
            common.validate_format(obj._patch[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(VersionInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "major" == "type" or (self.major is not self.__undef__ and (not (dirty and not self._major[1]))):
            dct["major"] = dictify(self.major)
        if "micro" == "type" or (self.micro is not self.__undef__ and (not (dirty and not self._micro[1]))):
            dct["micro"] = dictify(self.micro)
        if "minor" == "type" or (self.minor is not self.__undef__ and (not (dirty and not self._minor[1]))):
            dct["minor"] = dictify(self.minor)
        if "patch" == "type" or (self.patch is not self.__undef__ and (not (dirty and not self._patch[1]))):
            dct["patch"] = dictify(self.patch)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._major = (self._major[0], True)
        self._micro = (self._micro[0], True)
        self._minor = (self._minor[0], True)
        self._patch = (self._patch[0], True)

    def is_dirty(self):
        return any([self._major[1], self._micro[1], self._minor[1], self._patch[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, VersionInfo):
            return False
        return super(VersionInfo, self).__eq__(other) and \
               self.major == other.major and \
               self.micro == other.micro and \
               self.minor == other.minor and \
               self.patch == other.patch

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def major(self):
        """
        Major version number.

        :rtype: ``int``
        """
        return self._major[0]

    @major.setter
    def major(self, value):
        self._major = (value, True)

    @property
    def micro(self):
        """
        Micro version number.

        :rtype: ``int``
        """
        return self._micro[0]

    @micro.setter
    def micro(self, value):
        self._micro = (value, True)

    @property
    def minor(self):
        """
        Minor version number.

        :rtype: ``int``
        """
        return self._minor[0]

    @minor.setter
    def minor(self, value):
        self._minor = (value, True)

    @property
    def patch(self):
        """
        Patch version number.

        :rtype: ``int``
        """
        return self._patch[0]

    @patch.setter
    def patch(self, value):
        self._patch = (value, True)

