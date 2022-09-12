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
#     /delphix-host-os.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_16 import common

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

class HostOS(TypedObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.TypedObject` *)* The operating system
    information for the host.
    """
    def __init__(self, undef_enabled=True):
        super(HostOS, self).__init__()
        self._type = ("HostOS", True)
        self._name = (self.__undef__, True)
        self._kernel = (self.__undef__, True)
        self._release = (self.__undef__, True)
        self._version = (self.__undef__, True)
        self._timezone = (self.__undef__, True)
        self._distribution = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HostOS, cls).from_dict(data, dirty, undef_enabled)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        obj._kernel = (data.get("kernel", obj.__undef__), dirty)
        if obj._kernel[0] is not None and obj._kernel[0] is not obj.__undef__:
            assert isinstance(obj._kernel[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._kernel[0], type(obj._kernel[0])))
            common.validate_format(obj._kernel[0], "None", None, None)
        obj._release = (data.get("release", obj.__undef__), dirty)
        if obj._release[0] is not None and obj._release[0] is not obj.__undef__:
            assert isinstance(obj._release[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._release[0], type(obj._release[0])))
            common.validate_format(obj._release[0], "None", None, None)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "None", None, None)
        obj._timezone = (data.get("timezone", obj.__undef__), dirty)
        if obj._timezone[0] is not None and obj._timezone[0] is not obj.__undef__:
            assert isinstance(obj._timezone[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timezone[0], type(obj._timezone[0])))
            common.validate_format(obj._timezone[0], "None", None, None)
        obj._distribution = (data.get("distribution", obj.__undef__), dirty)
        if obj._distribution[0] is not None and obj._distribution[0] is not obj.__undef__:
            assert isinstance(obj._distribution[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._distribution[0], type(obj._distribution[0])))
            common.validate_format(obj._distribution[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(HostOS, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]))):
            dct["name"] = dictify(self.name)
        if "kernel" == "type" or (self.kernel is not self.__undef__ and (not (dirty and not self._kernel[1]))):
            dct["kernel"] = dictify(self.kernel)
        if "release" == "type" or (self.release is not self.__undef__ and (not (dirty and not self._release[1]))):
            dct["release"] = dictify(self.release)
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]))):
            dct["version"] = dictify(self.version)
        if "timezone" == "type" or (self.timezone is not self.__undef__ and (not (dirty and not self._timezone[1]))):
            dct["timezone"] = dictify(self.timezone)
        if "distribution" == "type" or (self.distribution is not self.__undef__ and (not (dirty and not self._distribution[1]))):
            dct["distribution"] = dictify(self.distribution)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._name = (self._name[0], True)
        self._kernel = (self._kernel[0], True)
        self._release = (self._release[0], True)
        self._version = (self._version[0], True)
        self._timezone = (self._timezone[0], True)
        self._distribution = (self._distribution[0], True)

    def is_dirty(self):
        return any([self._name[1], self._kernel[1], self._release[1], self._version[1], self._timezone[1], self._distribution[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HostOS):
            return False
        return super(HostOS, self).__eq__(other) and \
               self.name == other.name and \
               self.kernel == other.kernel and \
               self.release == other.release and \
               self.version == other.version and \
               self.timezone == other.timezone and \
               self.distribution == other.distribution

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def name(self):
        """
        The OS name.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def kernel(self):
        """
        The OS kernel.

        :rtype: ``TEXT_TYPE``
        """
        return self._kernel[0]

    @kernel.setter
    def kernel(self, value):
        self._kernel = (value, True)

    @property
    def release(self):
        """
        The OS release.

        :rtype: ``TEXT_TYPE``
        """
        return self._release[0]

    @release.setter
    def release(self, value):
        self._release = (value, True)

    @property
    def version(self):
        """
        The OS version.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

    @property
    def timezone(self):
        """
        The OS timezone.

        :rtype: ``TEXT_TYPE``
        """
        return self._timezone[0]

    @timezone.setter
    def timezone(self, value):
        self._timezone = (value, True)

    @property
    def distribution(self):
        """
        The OS distribution.

        :rtype: ``TEXT_TYPE``
        """
        return self._distribution[0]

    @distribution.setter
    def distribution(self, value):
        self._distribution = (value, True)

