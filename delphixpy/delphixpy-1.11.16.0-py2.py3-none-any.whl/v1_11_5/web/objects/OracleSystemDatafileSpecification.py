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
#     /delphix-oracle-system-datafile-specification.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_5.web.objects.OracleDatafileTempfileSpecification import OracleDatafileTempfileSpecification
from delphixpy.v1_11_5 import common

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

class OracleSystemDatafileSpecification(OracleDatafileTempfileSpecification):
    """
    *(extends* :py:class:`v1_11_5.web.vo.OracleDatafileTempfileSpecification`
    *)* Describes an Oracle datafile in the SYSTEM tablespace.
    """
    def __init__(self, undef_enabled=True):
        super(OracleSystemDatafileSpecification, self).__init__()
        self._type = ("OracleSystemDatafileSpecification", True)
        self._size = (self.__undef__, True)

    API_VERSION = "1.11.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleSystemDatafileSpecification, cls).from_dict(data, dirty, undef_enabled)
        obj._size = (data.get("size", obj.__undef__), dirty)
        if obj._size[0] is not None and obj._size[0] is not obj.__undef__:
            assert isinstance(obj._size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._size[0], type(obj._size[0])))
            common.validate_format(obj._size[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleSystemDatafileSpecification, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "size" == "type" or (self.size is not self.__undef__ and (not (dirty and not self._size[1]) or isinstance(self.size, list) or belongs_to_parent)):
            dct["size"] = dictify(self.size)
        elif belongs_to_parent and self.size is self.__undef__:
            dct["size"] = 700
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._size = (self._size[0], True)

    def is_dirty(self):
        return any([self._size[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleSystemDatafileSpecification):
            return False
        return super(OracleSystemDatafileSpecification, self).__eq__(other) and \
               self.size == other.size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def size(self):
        """
        *(default value: 700)* The size of the file in MB.

        :rtype: ``int``
        """
        return self._size[0]

    @size.setter
    def size(self, value):
        self._size = (value, True)

