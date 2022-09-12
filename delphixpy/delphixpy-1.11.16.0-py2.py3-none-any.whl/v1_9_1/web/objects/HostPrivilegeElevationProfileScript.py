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
#     /delphix-host-privilege-elevation-profile-script.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_1.web.objects.PersistentObject import PersistentObject
from delphixpy.v1_9_1 import common

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

class HostPrivilegeElevationProfileScript(PersistentObject):
    """
    *(extends* :py:class:`v1_9_1.web.vo.PersistentObject` *)* A script that is
    part of a profile for elevating user privileges on a host.
    """
    def __init__(self, undef_enabled=True):
        super(HostPrivilegeElevationProfileScript, self).__init__()
        self._type = ("HostPrivilegeElevationProfileScript", True)
        self._name = (self.__undef__, True)
        self._contents = (self.__undef__, True)
        self._profile = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HostPrivilegeElevationProfileScript, cls).from_dict(data, dirty, undef_enabled)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        obj._contents = (data.get("contents", obj.__undef__), dirty)
        if obj._contents[0] is not None and obj._contents[0] is not obj.__undef__:
            assert isinstance(obj._contents[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._contents[0], type(obj._contents[0])))
            common.validate_format(obj._contents[0], "None", None, None)
        obj._profile = (data.get("profile", obj.__undef__), dirty)
        if obj._profile[0] is not None and obj._profile[0] is not obj.__undef__:
            assert isinstance(obj._profile[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._profile[0], type(obj._profile[0])))
            common.validate_format(obj._profile[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(HostPrivilegeElevationProfileScript, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "contents" == "type" or (self.contents is not self.__undef__ and (not (dirty and not self._contents[1]) or isinstance(self.contents, list) or belongs_to_parent)):
            dct["contents"] = dictify(self.contents)
        if "profile" == "type" or (self.profile is not self.__undef__ and (not (dirty and not self._profile[1]) or isinstance(self.profile, list) or belongs_to_parent)):
            dct["profile"] = dictify(self.profile)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._name = (self._name[0], True)
        self._contents = (self._contents[0], True)
        self._profile = (self._profile[0], True)

    def is_dirty(self):
        return any([self._name[1], self._contents[1], self._profile[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HostPrivilegeElevationProfileScript):
            return False
        return super(HostPrivilegeElevationProfileScript, self).__eq__(other) and \
               self.name == other.name and \
               self.contents == other.contents and \
               self.profile == other.profile

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def name(self):
        """
        The privilege elevation profile script name.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def contents(self):
        """
        The contents of the privilege elevation profile script.

        :rtype: ``TEXT_TYPE``
        """
        return self._contents[0]

    @contents.setter
    def contents(self, value):
        self._contents = (value, True)

    @property
    def profile(self):
        """
        The privilege elevation profile to which this script belongs.

        :rtype: ``TEXT_TYPE``
        """
        return self._profile[0]

    @profile.setter
    def profile(self, value):
        self._profile = (value, True)

