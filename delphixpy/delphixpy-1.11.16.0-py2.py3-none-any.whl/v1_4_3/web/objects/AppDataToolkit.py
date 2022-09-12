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
#     /delphix-appdata-toolkit.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_3.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_4_3 import factory
from delphixpy.v1_4_3 import common

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

class AppDataToolkit(NamedUserObject):
    """
    *(extends* :py:class:`v1_4_3.web.vo.NamedUserObject` *)* An installed
    AppData toolkit.
    """
    def __init__(self, undef_enabled=True):
        super(AppDataToolkit, self).__init__()
        self._type = ("AppDataToolkit", True)
        self._name = (self.__undef__, True)
        self._pretty_name = (self.__undef__, True)
        self._provision = (self.__undef__, True)
        self._provision_parameters = (self.__undef__, True)
        self._snapshot = (self.__undef__, True)
        self._start = (self.__undef__, True)
        self._status_script = (self.__undef__, True)
        self._stop = (self.__undef__, True)

    API_VERSION = "1.4.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AppDataToolkit, cls).from_dict(data, dirty, undef_enabled)
        if "name" not in data:
            raise ValueError("Missing required property \"name\".")
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, 256)
        if "prettyName" not in data:
            raise ValueError("Missing required property \"prettyName\".")
        obj._pretty_name = (data.get("prettyName", obj.__undef__), dirty)
        if obj._pretty_name[0] is not None and obj._pretty_name[0] is not obj.__undef__:
            assert isinstance(obj._pretty_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pretty_name[0], type(obj._pretty_name[0])))
            common.validate_format(obj._pretty_name[0], "None", None, 256)
        obj._provision = []
        for item in data.get("provision") or []:
            obj._provision.append(factory.create_object(item))
            factory.validate_type(obj._provision[-1], "Operation")
        obj._provision = (obj._provision, dirty)
        obj._provision_parameters = []
        for item in data.get("provisionParameters") or []:
            obj._provision_parameters.append(factory.create_object(item))
            factory.validate_type(obj._provision_parameters[-1], "AppDataParameter")
        obj._provision_parameters = (obj._provision_parameters, dirty)
        obj._snapshot = []
        for item in data.get("snapshot") or []:
            obj._snapshot.append(factory.create_object(item))
            factory.validate_type(obj._snapshot[-1], "Operation")
        obj._snapshot = (obj._snapshot, dirty)
        obj._start = []
        for item in data.get("start") or []:
            obj._start.append(factory.create_object(item))
            factory.validate_type(obj._start[-1], "Operation")
        obj._start = (obj._start, dirty)
        obj._status_script = (data.get("statusScript", obj.__undef__), dirty)
        if obj._status_script[0] is not None and obj._status_script[0] is not obj.__undef__:
            assert isinstance(obj._status_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._status_script[0], type(obj._status_script[0])))
            common.validate_format(obj._status_script[0], "None", None, None)
        obj._stop = []
        for item in data.get("stop") or []:
            obj._stop.append(factory.create_object(item))
            factory.validate_type(obj._stop[-1], "Operation")
        obj._stop = (obj._stop, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AppDataToolkit, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        if "pretty_name" == "type" or (self.pretty_name is not self.__undef__ and (not (dirty and not self._pretty_name[1]) or isinstance(self.pretty_name, list) or belongs_to_parent)):
            dct["prettyName"] = dictify(self.pretty_name)
        if "provision" == "type" or (self.provision is not self.__undef__ and (not (dirty and not self._provision[1]))):
            dct["provision"] = dictify(self.provision)
        if "provision_parameters" == "type" or (self.provision_parameters is not self.__undef__ and (not (dirty and not self._provision_parameters[1]))):
            dct["provisionParameters"] = dictify(self.provision_parameters)
        if "snapshot" == "type" or (self.snapshot is not self.__undef__ and (not (dirty and not self._snapshot[1]))):
            dct["snapshot"] = dictify(self.snapshot)
        if "start" == "type" or (self.start is not self.__undef__ and (not (dirty and not self._start[1]))):
            dct["start"] = dictify(self.start)
        if "status_script" == "type" or (self.status_script is not self.__undef__ and (not (dirty and not self._status_script[1]))):
            dct["statusScript"] = dictify(self.status_script)
        if "stop" == "type" or (self.stop is not self.__undef__ and (not (dirty and not self._stop[1]))):
            dct["stop"] = dictify(self.stop)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._name = (self._name[0], True)
        self._pretty_name = (self._pretty_name[0], True)
        self._provision = (self._provision[0], True)
        self._provision_parameters = (self._provision_parameters[0], True)
        self._snapshot = (self._snapshot[0], True)
        self._start = (self._start[0], True)
        self._status_script = (self._status_script[0], True)
        self._stop = (self._stop[0], True)

    def is_dirty(self):
        return any([self._name[1], self._pretty_name[1], self._provision[1], self._provision_parameters[1], self._snapshot[1], self._start[1], self._status_script[1], self._stop[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AppDataToolkit):
            return False
        return super(AppDataToolkit, self).__eq__(other) and \
               self.name == other.name and \
               self.pretty_name == other.pretty_name and \
               self.provision == other.provision and \
               self.provision_parameters == other.provision_parameters and \
               self.snapshot == other.snapshot and \
               self.start == other.start and \
               self.status_script == other.status_script and \
               self.stop == other.stop

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def name(self):
        """
        A unique and descriptive name for the toolkit.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

    @property
    def pretty_name(self):
        """
        A human readable name for the toolkit.

        :rtype: ``TEXT_TYPE``
        """
        return self._pretty_name[0]

    @pretty_name.setter
    def pretty_name(self, value):
        self._pretty_name = (value, True)

    @property
    def provision(self):
        """
        A list of operations to run when provisioning a virtual copy of the
        application. The environment for all operations will contain the
        provision parameters.

        :rtype: ``list`` of :py:class:`v1_4_3.web.vo.Operation`
        """
        return self._provision[0]

    @provision.setter
    def provision(self, value):
        self._provision = (value, True)

    @property
    def provision_parameters(self):
        """
        Dynamic parameters the user must enter as input when provisioning a
        virtual copy of this AppData type.

        :rtype: ``list`` of :py:class:`v1_4_3.web.vo.AppDataParameter`
        """
        return self._provision_parameters[0]

    @provision_parameters.setter
    def provision_parameters(self, value):
        self._provision_parameters = (value, True)

    @property
    def snapshot(self):
        """
        A list of operations to run before taking a snapshot of a virtual copy
        of the application. The environment for all operations will contain the
        provision parameters.

        :rtype: ``list`` of :py:class:`v1_4_3.web.vo.Operation`
        """
        return self._snapshot[0]

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = (value, True)

    @property
    def start(self):
        """
        A list of operations to run when starting a virtual copy of the
        application. The environment for all operations will contain the
        provision parameters.

        :rtype: ``list`` of :py:class:`v1_4_3.web.vo.Operation`
        """
        return self._start[0]

    @start.setter
    def start(self, value):
        self._start = (value, True)

    @property
    def status_script(self):
        """
        The script to run to determine if a virtual copy of the application is
        running. The script should exit with exit code of 0 if the application
        is running, 128 if the application is not running, and any other exit
        code if the script encounters an unexpected error. The script is passed
        the provision parameters as input.

        :rtype: ``TEXT_TYPE``
        """
        return self._status_script[0]

    @status_script.setter
    def status_script(self, value):
        self._status_script = (value, True)

    @property
    def stop(self):
        """
        A list of operations to run when stopping a virtual copy of the
        application. The environment for all operations will contain the
        provision parameters.

        :rtype: ``list`` of :py:class:`v1_4_3.web.vo.Operation`
        """
        return self._stop[0]

    @stop.setter
    def stop(self, value):
        self._stop = (value, True)

