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
#     /delphix-system-initialization-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_16.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_16 import factory
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

class SystemInitializationParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_16.web.vo.TypedObject` *)* Parameters used for
    intializing an engine.
    """
    def __init__(self, undef_enabled=True):
        super(SystemInitializationParameters, self).__init__()
        self._type = ("SystemInitializationParameters", True)
        self._default_user = (self.__undef__, True)
        self._default_password = (self.__undef__, True)
        self._default_email = (self.__undef__, True)
        self._devices = (self.__undef__, True)
        self._object_store = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SystemInitializationParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._default_user = (data.get("defaultUser", obj.__undef__), dirty)
        if obj._default_user[0] is not None and obj._default_user[0] is not obj.__undef__:
            assert isinstance(obj._default_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._default_user[0], type(obj._default_user[0])))
            common.validate_format(obj._default_user[0], "None", 1, 256)
        obj._default_password = (data.get("defaultPassword", obj.__undef__), dirty)
        if obj._default_password[0] is not None and obj._default_password[0] is not obj.__undef__:
            assert isinstance(obj._default_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._default_password[0], type(obj._default_password[0])))
            common.validate_format(obj._default_password[0], "password", None, None)
        obj._default_email = (data.get("defaultEmail", obj.__undef__), dirty)
        if obj._default_email[0] is not None and obj._default_email[0] is not obj.__undef__:
            assert isinstance(obj._default_email[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._default_email[0], type(obj._default_email[0])))
            common.validate_format(obj._default_email[0], "email", None, None)
        obj._devices = []
        for item in data.get("devices") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._devices.append(item)
        obj._devices = (obj._devices, dirty)
        if "objectStore" in data and data["objectStore"] is not None:
            obj._object_store = (factory.create_object(data["objectStore"], "ObjectStore"), dirty)
            factory.validate_type(obj._object_store[0], "ObjectStore")
        else:
            obj._object_store = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SystemInitializationParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "default_user" == "type" or (self.default_user is not self.__undef__ and (not (dirty and not self._default_user[1]) or isinstance(self.default_user, list) or belongs_to_parent)):
            dct["defaultUser"] = dictify(self.default_user)
        elif belongs_to_parent and self.default_user is self.__undef__:
            dct["defaultUser"] = "admin"
        if "default_password" == "type" or (self.default_password is not self.__undef__ and (not (dirty and not self._default_password[1]) or isinstance(self.default_password, list) or belongs_to_parent)):
            dct["defaultPassword"] = dictify(self.default_password)
        if "default_email" == "type" or (self.default_email is not self.__undef__ and (not (dirty and not self._default_email[1]) or isinstance(self.default_email, list) or belongs_to_parent)):
            dct["defaultEmail"] = dictify(self.default_email)
        if "devices" == "type" or (self.devices is not self.__undef__ and (not (dirty and not self._devices[1]) or isinstance(self.devices, list) or belongs_to_parent)):
            dct["devices"] = dictify(self.devices, prop_is_list_or_vo=True)
        if "object_store" == "type" or (self.object_store is not self.__undef__ and (not (dirty and not self._object_store[1]) or isinstance(self.object_store, list) or belongs_to_parent)):
            dct["objectStore"] = dictify(self.object_store, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._default_user = (self._default_user[0], True)
        self._default_password = (self._default_password[0], True)
        self._default_email = (self._default_email[0], True)
        self._devices = (self._devices[0], True)
        self._object_store = (self._object_store[0], True)

    def is_dirty(self):
        return any([self._default_user[1], self._default_password[1], self._default_email[1], self._devices[1], self._object_store[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SystemInitializationParameters):
            return False
        return super(SystemInitializationParameters, self).__eq__(other) and \
               self.default_user == other.default_user and \
               self.default_password == other.default_password and \
               self.default_email == other.default_email and \
               self.devices == other.devices and \
               self.object_store == other.object_store

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def default_user(self):
        """
        *(default value: admin)* Name of the default domain administrator to
        create.

        :rtype: ``TEXT_TYPE``
        """
        return self._default_user[0]

    @default_user.setter
    def default_user(self, value):
        self._default_user = (value, True)

    @property
    def default_password(self):
        """
        Password to use for the default domain administrator.

        :rtype: ``TEXT_TYPE``
        """
        return self._default_password[0]

    @default_password.setter
    def default_password(self, value):
        self._default_password = (value, True)

    @property
    def default_email(self):
        """
        Email of the default domain administrator.

        :rtype: ``TEXT_TYPE``
        """
        return self._default_email[0]

    @default_email.setter
    def default_email(self, value):
        self._default_email = (value, True)

    @property
    def devices(self):
        """
        List of storage devices to use.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._devices[0]

    @devices.setter
    def devices(self, value):
        self._devices = (value, True)

    @property
    def object_store(self):
        """
        Object storage.

        :rtype: :py:class:`v1_11_16.web.vo.ObjectStore`
        """
        return self._object_store[0]

    @object_store.setter
    def object_store(self, value):
        self._object_store = (value, True)

