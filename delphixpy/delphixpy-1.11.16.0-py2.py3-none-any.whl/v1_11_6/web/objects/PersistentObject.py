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
#     /delphix-persistent-object.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_6.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_6 import common

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

class PersistentObject(TypedObject):
    """
    *(extends* :py:class:`v1_11_6.web.vo.TypedObject` *)* Super schema for all
    typed schemas with a reference property.
    """
    def __init__(self, undef_enabled=True):
        super(PersistentObject, self).__init__()
        self._type = ("PersistentObject", True)
        self._reference = (self.__undef__, True)
        self._namespace = (self.__undef__, True)

    API_VERSION = "1.11.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PersistentObject, cls).from_dict(data, dirty, undef_enabled)
        obj._reference = (data.get("reference", obj.__undef__), dirty)
        if obj._reference[0] is not None and obj._reference[0] is not obj.__undef__:
            assert isinstance(obj._reference[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._reference[0], type(obj._reference[0])))
            common.validate_format(obj._reference[0], "objectReference", None, None)
        obj._namespace = (data.get("namespace", obj.__undef__), dirty)
        if obj._namespace[0] is not None and obj._namespace[0] is not obj.__undef__:
            assert isinstance(obj._namespace[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._namespace[0], type(obj._namespace[0])))
            common.validate_format(obj._namespace[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PersistentObject, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "reference" == "type" or (self.reference is not self.__undef__ and (not (dirty and not self._reference[1]))):
            dct["reference"] = dictify(self.reference)
        if "namespace" == "type" or (self.namespace is not self.__undef__ and (not (dirty and not self._namespace[1]))):
            dct["namespace"] = dictify(self.namespace)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._reference = (self._reference[0], True)
        self._namespace = (self._namespace[0], True)

    def is_dirty(self):
        return any([self._reference[1], self._namespace[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PersistentObject):
            return False
        return super(PersistentObject, self).__eq__(other) and \
               self.reference == other.reference and \
               self.namespace == other.namespace

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def reference(self):
        """
        The object reference.

        :rtype: ``TEXT_TYPE``
        """
        return self._reference[0]

    @reference.setter
    def reference(self, value):
        self._reference = (value, True)

    @property
    def namespace(self):
        """
        Alternate namespace for this object, for replicated and restored
        objects.

        :rtype: ``TEXT_TYPE``
        """
        return self._namespace[0]

    @namespace.setter
    def namespace(self, value):
        self._namespace = (value, True)

