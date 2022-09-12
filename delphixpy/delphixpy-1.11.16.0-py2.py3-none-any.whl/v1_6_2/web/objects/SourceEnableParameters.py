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
#     /delphix-source-enable-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_2 import common

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

class SourceEnableParameters(TypedObject):
    """
    *(extends* :py:class:`v1_6_2.web.vo.TypedObject` *)* The parameters to use
    as input to enable a MSSQL, PostgreSQL, AppData, ASE or MySQL source.
    """
    def __init__(self, undef_enabled=True):
        super(SourceEnableParameters, self).__init__()
        self._type = ("SourceEnableParameters", True)
        self._attempt_start = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceEnableParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._attempt_start = (data.get("attemptStart", obj.__undef__), dirty)
        if obj._attempt_start[0] is not None and obj._attempt_start[0] is not obj.__undef__:
            assert isinstance(obj._attempt_start[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._attempt_start[0], type(obj._attempt_start[0])))
            common.validate_format(obj._attempt_start[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceEnableParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "attempt_start" == "type" or (self.attempt_start is not self.__undef__ and (not (dirty and not self._attempt_start[1]))):
            dct["attemptStart"] = dictify(self.attempt_start)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._attempt_start = (self._attempt_start[0], True)

    def is_dirty(self):
        return any([self._attempt_start[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceEnableParameters):
            return False
        return super(SourceEnableParameters, self).__eq__(other) and \
               self.attempt_start == other.attempt_start

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def attempt_start(self):
        """
        *(default value: True)* Whether to attempt a startup of the source
        after the enable.

        :rtype: ``bool``
        """
        return self._attempt_start[0]

    @attempt_start.setter
    def attempt_start(self, value):
        self._attempt_start = (value, True)

