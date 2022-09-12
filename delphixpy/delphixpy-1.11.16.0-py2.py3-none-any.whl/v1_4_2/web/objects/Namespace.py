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
#     /delphix-namespace.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_2.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_4_2 import common

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

class Namespace(NamedUserObject):
    """
    *(extends* :py:class:`v1_4_2.web.vo.NamedUserObject` *)* Object namespace
    for target-side replication.
    """
    def __init__(self, undef_enabled=True):
        super(Namespace, self).__init__()
        self._type = ("Namespace", True)
        self._namespace_type = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._tag = (self.__undef__, True)

    API_VERSION = "1.4.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Namespace, cls).from_dict(data, dirty, undef_enabled)
        obj._namespace_type = (data.get("namespaceType", obj.__undef__), dirty)
        if obj._namespace_type[0] is not None and obj._namespace_type[0] is not obj.__undef__:
            assert isinstance(obj._namespace_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._namespace_type[0], type(obj._namespace_type[0])))
            assert obj._namespace_type[0] in ['REPLICATION'], "Expected enum ['REPLICATION'] but got %s" % obj._namespace_type[0]
            common.validate_format(obj._namespace_type[0], "None", None, None)
        obj._source = (data.get("source", obj.__undef__), dirty)
        if obj._source[0] is not None and obj._source[0] is not obj.__undef__:
            assert isinstance(obj._source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source[0], type(obj._source[0])))
            common.validate_format(obj._source[0], "None", None, None)
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Namespace, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "namespace_type" == "type" or (self.namespace_type is not self.__undef__ and (not (dirty and not self._namespace_type[1]))):
            dct["namespaceType"] = dictify(self.namespace_type)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]))):
            dct["source"] = dictify(self.source)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]))):
            dct["tag"] = dictify(self.tag)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._namespace_type = (self._namespace_type[0], True)
        self._source = (self._source[0], True)
        self._tag = (self._tag[0], True)

    def is_dirty(self):
        return any([self._namespace_type[1], self._source[1], self._tag[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Namespace):
            return False
        return super(Namespace, self).__eq__(other) and \
               self.namespace_type == other.namespace_type and \
               self.source == other.source and \
               self.tag == other.tag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def namespace_type(self):
        """
        Type of object namespace. *(permitted values: REPLICATION)*

        :rtype: ``TEXT_TYPE``
        """
        return self._namespace_type[0]

    @namespace_type.setter
    def namespace_type(self, value):
        self._namespace_type = (value, True)

    @property
    def source(self):
        """
        For replication, the source host IP address.

        :rtype: ``TEXT_TYPE``
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def tag(self):
        """
        A unique identifier for the source data stream.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

