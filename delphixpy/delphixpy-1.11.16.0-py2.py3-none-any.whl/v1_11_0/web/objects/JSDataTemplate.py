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
#     /delphix-js-data-template.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.JSDataLayout import JSDataLayout
from delphixpy.v1_11_0 import common

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

class JSDataTemplate(JSDataLayout):
    """
    *(extends* :py:class:`v1_11_0.web.vo.JSDataLayout` *)* A data template is a
    collection of data sources and configuration representing a data layout
    that can be provisioned to Self-Service users.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataTemplate, self).__init__()
        self._type = ("JSDataTemplate", True)
        self._confirm_time_consuming_operations = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataTemplate, cls).from_dict(data, dirty, undef_enabled)
        obj._confirm_time_consuming_operations = (data.get("confirmTimeConsumingOperations", obj.__undef__), dirty)
        if obj._confirm_time_consuming_operations[0] is not None and obj._confirm_time_consuming_operations[0] is not obj.__undef__:
            assert isinstance(obj._confirm_time_consuming_operations[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._confirm_time_consuming_operations[0], type(obj._confirm_time_consuming_operations[0])))
            common.validate_format(obj._confirm_time_consuming_operations[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataTemplate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "confirm_time_consuming_operations" == "type" or (self.confirm_time_consuming_operations is not self.__undef__ and (not (dirty and not self._confirm_time_consuming_operations[1]) or isinstance(self.confirm_time_consuming_operations, list) or belongs_to_parent)):
            dct["confirmTimeConsumingOperations"] = dictify(self.confirm_time_consuming_operations)
        elif belongs_to_parent and self.confirm_time_consuming_operations is self.__undef__:
            dct["confirmTimeConsumingOperations"] = True
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._confirm_time_consuming_operations = (self._confirm_time_consuming_operations[0], True)

    def is_dirty(self):
        return any([self._confirm_time_consuming_operations[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataTemplate):
            return False
        return super(JSDataTemplate, self).__eq__(other) and \
               self.confirm_time_consuming_operations == other.confirm_time_consuming_operations

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def confirm_time_consuming_operations(self):
        """
        *(default value: True)* A client should consider warning the user
        before performing an operation which may take a long time, if this is
        true.

        :rtype: ``bool``
        """
        return self._confirm_time_consuming_operations[0]

    @confirm_time_consuming_operations.setter
    def confirm_time_consuming_operations(self, value):
        self._confirm_time_consuming_operations = (value, True)

