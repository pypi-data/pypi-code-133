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
#     /delphix-batch-snapshot-delete-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_0 import common

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

class BatchSnapshotDeleteParameters(TypedObject):
    """
    *(extends* :py:class:`v1_9_0.web.vo.TypedObject` *)* The parameters to use
    as input to TimeFlow snapshots batch delete requests.
    """
    def __init__(self, undef_enabled=True):
        super(BatchSnapshotDeleteParameters, self).__init__()
        self._type = ("BatchSnapshotDeleteParameters", True)
        self._snapshots = (self.__undef__, True)

    API_VERSION = "1.9.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(BatchSnapshotDeleteParameters, cls).from_dict(data, dirty, undef_enabled)
        if "snapshots" not in data:
            raise ValueError("Missing required property \"snapshots\".")
        obj._snapshots = []
        for item in data.get("snapshots") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._snapshots.append(item)
        obj._snapshots = (obj._snapshots, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(BatchSnapshotDeleteParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "snapshots" == "type" or (self.snapshots is not self.__undef__ and (not (dirty and not self._snapshots[1]) or isinstance(self.snapshots, list) or belongs_to_parent)):
            dct["snapshots"] = dictify(self.snapshots, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._snapshots = (self._snapshots[0], True)

    def is_dirty(self):
        return any([self._snapshots[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, BatchSnapshotDeleteParameters):
            return False
        return super(BatchSnapshotDeleteParameters, self).__eq__(other) and \
               self.snapshots == other.snapshots

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def snapshots(self):
        """
        TimeFlow snapshots to delete.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._snapshots[0]

    @snapshots.setter
    def snapshots(self, value):
        self._snapshots = (value, True)

