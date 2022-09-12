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
#     /delphix-run-bash-on-source-operation.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.SourceOperation import SourceOperation
from delphixpy.v1_10_5 import common

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

class RunBashOnSourceOperation(SourceOperation):
    """
    *(extends* :py:class:`v1_10_5.web.vo.SourceOperation` *)* A user-
    specifiable operation that runs a shell command on the target host using
    the Delphix supplied Bash shell.
    """
    def __init__(self, undef_enabled=True):
        super(RunBashOnSourceOperation, self).__init__()
        self._type = ("RunBashOnSourceOperation", True)
        self._command = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RunBashOnSourceOperation, cls).from_dict(data, dirty, undef_enabled)
        obj._command = (data.get("command", obj.__undef__), dirty)
        if obj._command[0] is not None and obj._command[0] is not obj.__undef__:
            assert isinstance(obj._command[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._command[0], type(obj._command[0])))
            common.validate_format(obj._command[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RunBashOnSourceOperation, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "command" == "type" or (self.command is not self.__undef__ and (not (dirty and not self._command[1]) or isinstance(self.command, list) or belongs_to_parent)):
            dct["command"] = dictify(self.command)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._command = (self._command[0], True)

    def is_dirty(self):
        return any([self._command[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RunBashOnSourceOperation):
            return False
        return super(RunBashOnSourceOperation, self).__eq__(other) and \
               self.command == other.command

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def command(self):
        """
        The shell command to execute on the target host.

        :rtype: ``TEXT_TYPE``
        """
        return self._command[0]

    @command.setter
    def command(self, value):
        self._command = (value, True)

