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
#     /delphix-connectivity-dsp.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_2 import common

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

class DspConnectivity(TypedObject):
    """
    *(extends* :py:class:`v1_10_2.web.vo.TypedObject` *)* Mechanism to stress
    DSP connectivity to hosts that have been added to Delphix.
    """
    def __init__(self, undef_enabled=True):
        super(DspConnectivity, self).__init__()
        self._type = ("DspConnectivity", True)
        self._host = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._number_of_consecutive_connections = (self.__undef__, True)
        self._number_of_threads = (self.__undef__, True)
        self._number_of_seconds = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(DspConnectivity, cls).from_dict(data, dirty, undef_enabled)
        if "host" not in data:
            raise ValueError("Missing required property \"host\".")
        obj._host = (data.get("host", obj.__undef__), dirty)
        if obj._host[0] is not None and obj._host[0] is not obj.__undef__:
            assert isinstance(obj._host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._host[0], type(obj._host[0])))
            common.validate_format(obj._host[0], "objectReference", None, None)
        if "user" not in data:
            raise ValueError("Missing required property \"user\".")
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "objectReference", None, None)
        obj._number_of_consecutive_connections = (data.get("numberOfConsecutiveConnections", obj.__undef__), dirty)
        if obj._number_of_consecutive_connections[0] is not None and obj._number_of_consecutive_connections[0] is not obj.__undef__:
            assert isinstance(obj._number_of_consecutive_connections[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._number_of_consecutive_connections[0], type(obj._number_of_consecutive_connections[0])))
            common.validate_format(obj._number_of_consecutive_connections[0], "None", None, None)
        obj._number_of_threads = (data.get("numberOfThreads", obj.__undef__), dirty)
        if obj._number_of_threads[0] is not None and obj._number_of_threads[0] is not obj.__undef__:
            assert isinstance(obj._number_of_threads[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._number_of_threads[0], type(obj._number_of_threads[0])))
            common.validate_format(obj._number_of_threads[0], "None", None, None)
        obj._number_of_seconds = (data.get("numberOfSeconds", obj.__undef__), dirty)
        if obj._number_of_seconds[0] is not None and obj._number_of_seconds[0] is not obj.__undef__:
            assert isinstance(obj._number_of_seconds[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._number_of_seconds[0], type(obj._number_of_seconds[0])))
            common.validate_format(obj._number_of_seconds[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(DspConnectivity, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "host" == "type" or (self.host is not self.__undef__ and (not (dirty and not self._host[1]) or isinstance(self.host, list) or belongs_to_parent)):
            dct["host"] = dictify(self.host)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        if "number_of_consecutive_connections" == "type" or (self.number_of_consecutive_connections is not self.__undef__ and (not (dirty and not self._number_of_consecutive_connections[1]))):
            dct["numberOfConsecutiveConnections"] = dictify(self.number_of_consecutive_connections)
        if "number_of_threads" == "type" or (self.number_of_threads is not self.__undef__ and (not (dirty and not self._number_of_threads[1]))):
            dct["numberOfThreads"] = dictify(self.number_of_threads)
        if "number_of_seconds" == "type" or (self.number_of_seconds is not self.__undef__ and (not (dirty and not self._number_of_seconds[1]))):
            dct["numberOfSeconds"] = dictify(self.number_of_seconds)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._host = (self._host[0], True)
        self._user = (self._user[0], True)
        self._number_of_consecutive_connections = (self._number_of_consecutive_connections[0], True)
        self._number_of_threads = (self._number_of_threads[0], True)
        self._number_of_seconds = (self._number_of_seconds[0], True)

    def is_dirty(self):
        return any([self._host[1], self._user[1], self._number_of_consecutive_connections[1], self._number_of_threads[1], self._number_of_seconds[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, DspConnectivity):
            return False
        return super(DspConnectivity, self).__eq__(other) and \
               self.host == other.host and \
               self.user == other.user and \
               self.number_of_consecutive_connections == other.number_of_consecutive_connections and \
               self.number_of_threads == other.number_of_threads and \
               self.number_of_seconds == other.number_of_seconds

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def host(self):
        """
        The host to establish DSP connections on.

        :rtype: ``TEXT_TYPE``
        """
        return self._host[0]

    @host.setter
    def host(self, value):
        self._host = (value, True)

    @property
    def user(self):
        """
        The user associated with the environment to establish connections with.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def number_of_consecutive_connections(self):
        """
        *(default value: 100)* How many DSP connections we should consecutively
        create. This option will be ignored if numberOfSeconds is non-zero.

        :rtype: ``int``
        """
        return self._number_of_consecutive_connections[0]

    @number_of_consecutive_connections.setter
    def number_of_consecutive_connections(self, value):
        self._number_of_consecutive_connections = (value, True)

    @property
    def number_of_threads(self):
        """
        *(default value: 1)* The number of threads which will concurrently
        establish connections.

        :rtype: ``int``
        """
        return self._number_of_threads[0]

    @number_of_threads.setter
    def number_of_threads(self, value):
        self._number_of_threads = (value, True)

    @property
    def number_of_seconds(self):
        """
        The length of time that the test should run for.

        :rtype: ``int``
        """
        return self._number_of_seconds[0]

    @number_of_seconds.setter
    def number_of_seconds(self, value):
        self._number_of_seconds = (value, True)

