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
#     /delphix-mssql-availability-group-listener.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.MSSqlBaseClusterListener import MSSqlBaseClusterListener
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

class MSSqlAvailabilityGroupListener(MSSqlBaseClusterListener):
    """
    *(extends* :py:class:`v1_7_1.web.vo.MSSqlBaseClusterListener` *)* The
    representation of a SQL Server Availability Group Listener.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlAvailabilityGroupListener, self).__init__()
        self._type = ("MSSqlAvailabilityGroupListener", True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlAvailabilityGroupListener, cls).from_dict(data, dirty, undef_enabled)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlAvailabilityGroupListener, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        pass

    def is_dirty(self):
        return False

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlAvailabilityGroupListener):
            return False
        return super(MSSqlAvailabilityGroupListener, self).__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

