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
#     /delphix-with-control-node-initialization-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.SystemInitializationParameters import SystemInitializationParameters
from delphixpy.v1_7_1 import common

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

class WithControlNodeInitializationParameters(SystemInitializationParameters):
    """
    *(extends* :py:class:`v1_7_1.web.vo.SystemInitializationParameters` *)*
    Parameters used for creating a domain.
    """
    def __init__(self, undef_enabled=True):
        super(WithControlNodeInitializationParameters, self).__init__()
        self._type = ("WithControlNodeInitializationParameters", True)
        self._default_password = (self.__undef__, True)
        self._default_user = (self.__undef__, True)
        self._devices = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(WithControlNodeInitializationParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._default_password = (data.get("defaultPassword", obj.__undef__), dirty)
        if obj._default_password[0] is not None and obj._default_password[0] is not obj.__undef__:
            assert isinstance(obj._default_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._default_password[0], type(obj._default_password[0])))
            common.validate_format(obj._default_password[0], "password", None, None)
        obj._default_user = (data.get("defaultUser", obj.__undef__), dirty)
        if obj._default_user[0] is not None and obj._default_user[0] is not obj.__undef__:
            assert isinstance(obj._default_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._default_user[0], type(obj._default_user[0])))
            common.validate_format(obj._default_user[0], "None", 1, 256)
        obj._devices = []
        for item in data.get("devices") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._devices.append(item)
        obj._devices = (obj._devices, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(WithControlNodeInitializationParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "default_password" == "type" or (self.default_password is not self.__undef__ and (not (dirty and not self._default_password[1]) or isinstance(self.default_password, list) or belongs_to_parent)):
            dct["defaultPassword"] = dictify(self.default_password)
        elif belongs_to_parent and self.default_password is self.__undef__:
            dct["defaultPassword"] = "delphix"
        if "default_user" == "type" or (self.default_user is not self.__undef__ and (not (dirty and not self._default_user[1]) or isinstance(self.default_user, list) or belongs_to_parent)):
            dct["defaultUser"] = dictify(self.default_user)
        elif belongs_to_parent and self.default_user is self.__undef__:
            dct["defaultUser"] = "delphix_admin"
        if "devices" == "type" or (self.devices is not self.__undef__ and (not (dirty and not self._devices[1]) or isinstance(self.devices, list) or belongs_to_parent)):
            dct["devices"] = dictify(self.devices, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._default_password = (self._default_password[0], True)
        self._default_user = (self._default_user[0], True)
        self._devices = (self._devices[0], True)

    def is_dirty(self):
        return any([self._default_password[1], self._default_user[1], self._devices[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, WithControlNodeInitializationParameters):
            return False
        return super(WithControlNodeInitializationParameters, self).__eq__(other) and \
               self.default_password == other.default_password and \
               self.default_user == other.default_user and \
               self.devices == other.devices

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def default_password(self):
        """
        *(default value: delphix)* Password to use for the default domain
        administrator.

        :rtype: ``TEXT_TYPE``
        """
        return self._default_password[0]

    @default_password.setter
    def default_password(self, value):
        self._default_password = (value, True)

    @property
    def default_user(self):
        """
        *(default value: delphix_admin)* Name of the default domain
        administrator to create.

        :rtype: ``TEXT_TYPE``
        """
        return self._default_user[0]

    @default_user.setter
    def default_user(self, value):
        self._default_user = (value, True)

    @property
    def devices(self):
        """
        List of storage devices to use for the node which is being initialized.
        In unified enginedeployment model the storage devices will be used for
        both applications/databases data and forthe Delphix Engine metadata.
        For grid control nodes, the storage devices will be usedexclusively to
        store metadata as applications/databases data is stored on grid data
        nodes.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._devices[0]

    @devices.setter
    def devices(self, value):
        self._devices = (value, True)

