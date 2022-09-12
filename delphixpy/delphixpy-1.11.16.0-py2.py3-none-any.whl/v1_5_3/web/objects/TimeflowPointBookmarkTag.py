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
#     /delphix-timeflow-point-bookmark-tag.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_3.web.objects.TimeflowPointParameters import TimeflowPointParameters
from delphixpy.v1_5_3 import common

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

class TimeflowPointBookmarkTag(TimeflowPointParameters):
    """
    *(extends* :py:class:`v1_5_3.web.vo.TimeflowPointParameters` *)* TimeFlow
    point based on a TimeFlow bookmark tag.
    """
    def __init__(self, undef_enabled=True):
        super(TimeflowPointBookmarkTag, self).__init__()
        self._type = ("TimeflowPointBookmarkTag", True)
        self._container = (self.__undef__, True)
        self._tag = (self.__undef__, True)

    API_VERSION = "1.5.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeflowPointBookmarkTag, cls).from_dict(data, dirty, undef_enabled)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        if "tag" not in data:
            raise ValueError("Missing required property \"tag\".")
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeflowPointBookmarkTag, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]) or isinstance(self.tag, list) or belongs_to_parent)):
            dct["tag"] = dictify(self.tag)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._tag = (self._tag[0], True)

    def is_dirty(self):
        return any([self._container[1], self._tag[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeflowPointBookmarkTag):
            return False
        return super(TimeflowPointBookmarkTag, self).__eq__(other) and \
               self.container == other.container and \
               self.tag == other.tag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        Reference to the container.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def tag(self):
        """
        The name of the tag.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

