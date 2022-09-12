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
#     /delphix-js-timeline-point-latest-time-input.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.JSTimelinePointTimeParameters import JSTimelinePointTimeParameters
from delphixpy.v1_6_1 import common

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

class JSTimelinePointLatestTimeInput(JSTimelinePointTimeParameters):
    """
    *(extends* :py:class:`v1_6_1.web.vo.JSTimelinePointTimeParameters` *)*
    Specifies the use of the latest available data from the given data layout.
    """
    def __init__(self, undef_enabled=True):
        super(JSTimelinePointLatestTimeInput, self).__init__()
        self._type = ("JSTimelinePointLatestTimeInput", True)
        self._source_data_layout = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSTimelinePointLatestTimeInput, cls).from_dict(data, dirty, undef_enabled)
        if "sourceDataLayout" not in data:
            raise ValueError("Missing required property \"sourceDataLayout\".")
        obj._source_data_layout = (data.get("sourceDataLayout", obj.__undef__), dirty)
        if obj._source_data_layout[0] is not None and obj._source_data_layout[0] is not obj.__undef__:
            assert isinstance(obj._source_data_layout[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_data_layout[0], type(obj._source_data_layout[0])))
            common.validate_format(obj._source_data_layout[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSTimelinePointLatestTimeInput, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source_data_layout" == "type" or (self.source_data_layout is not self.__undef__ and (not (dirty and not self._source_data_layout[1]) or isinstance(self.source_data_layout, list) or belongs_to_parent)):
            dct["sourceDataLayout"] = dictify(self.source_data_layout)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source_data_layout = (self._source_data_layout[0], True)

    def is_dirty(self):
        return any([self._source_data_layout[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSTimelinePointLatestTimeInput):
            return False
        return super(JSTimelinePointLatestTimeInput, self).__eq__(other) and \
               self.source_data_layout == other.source_data_layout

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source_data_layout(self):
        """
        The reference to the data layout used for this operation.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_data_layout[0]

    @source_data_layout.setter
    def source_data_layout(self, value):
        self._source_data_layout = (value, True)

