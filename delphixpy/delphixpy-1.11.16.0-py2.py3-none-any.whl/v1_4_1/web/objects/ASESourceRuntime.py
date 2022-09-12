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
#     /delphix-ase-source-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_1.web.objects.SourceRuntime import SourceRuntime
from delphixpy.v1_4_1 import common

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

class ASESourceRuntime(SourceRuntime):
    """
    *(extends* :py:class:`v1_4_1.web.vo.SourceRuntime` *)* Runtime (non-
    persistent) properties of a SAP ASE source.
    """
    def __init__(self, undef_enabled=True):
        super(ASESourceRuntime, self).__init__()
        self._type = ("ASESourceRuntime", True)
        self._durability_level = (self.__undef__, True)
        self._truncate_log_on_checkpoint = (self.__undef__, True)

    API_VERSION = "1.4.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASESourceRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._durability_level = (data.get("durabilityLevel", obj.__undef__), dirty)
        if obj._durability_level[0] is not None and obj._durability_level[0] is not obj.__undef__:
            assert isinstance(obj._durability_level[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._durability_level[0], type(obj._durability_level[0])))
            assert obj._durability_level[0] in ['FULL', 'AT_SHUTDOWN', 'NO_RECOVERY'], "Expected enum ['FULL', 'AT_SHUTDOWN', 'NO_RECOVERY'] but got %s" % obj._durability_level[0]
            common.validate_format(obj._durability_level[0], "None", None, None)
        obj._truncate_log_on_checkpoint = (data.get("truncateLogOnCheckpoint", obj.__undef__), dirty)
        if obj._truncate_log_on_checkpoint[0] is not None and obj._truncate_log_on_checkpoint[0] is not obj.__undef__:
            assert isinstance(obj._truncate_log_on_checkpoint[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._truncate_log_on_checkpoint[0], type(obj._truncate_log_on_checkpoint[0])))
            common.validate_format(obj._truncate_log_on_checkpoint[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASESourceRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "durability_level" == "type" or (self.durability_level is not self.__undef__ and (not (dirty and not self._durability_level[1]))):
            dct["durabilityLevel"] = dictify(self.durability_level)
        if "truncate_log_on_checkpoint" == "type" or (self.truncate_log_on_checkpoint is not self.__undef__ and (not (dirty and not self._truncate_log_on_checkpoint[1]))):
            dct["truncateLogOnCheckpoint"] = dictify(self.truncate_log_on_checkpoint)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._durability_level = (self._durability_level[0], True)
        self._truncate_log_on_checkpoint = (self._truncate_log_on_checkpoint[0], True)

    def is_dirty(self):
        return any([self._durability_level[1], self._truncate_log_on_checkpoint[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASESourceRuntime):
            return False
        return super(ASESourceRuntime, self).__eq__(other) and \
               self.durability_level == other.durability_level and \
               self.truncate_log_on_checkpoint == other.truncate_log_on_checkpoint

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def durability_level(self):
        """
        SAP ASE database durability level. *(permitted values: FULL,
        AT_SHUTDOWN, NO_RECOVERY)*

        :rtype: ``TEXT_TYPE``
        """
        return self._durability_level[0]

    @durability_level.setter
    def durability_level(self, value):
        self._durability_level = (value, True)

    @property
    def truncate_log_on_checkpoint(self):
        """
        True if configured to truncate log on checkpoint.

        :rtype: ``bool``
        """
        return self._truncate_log_on_checkpoint[0]

    @truncate_log_on_checkpoint.setter
    def truncate_log_on_checkpoint(self, value):
        self._truncate_log_on_checkpoint = (value, True)

