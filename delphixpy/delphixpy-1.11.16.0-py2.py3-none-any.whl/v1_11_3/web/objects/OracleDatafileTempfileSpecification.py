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
#     /delphix-oracle-datafile-tempfile-specification.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.OracleFileSpecification import OracleFileSpecification
from delphixpy.v1_11_3 import common

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

class OracleDatafileTempfileSpecification(OracleFileSpecification):
    """
    *(extends* :py:class:`v1_11_3.web.vo.OracleFileSpecification` *)* Describes
    an Oracle datafile or tempfile for use when creating or altering
    controlfiles, databases, or tablespaces.
    """
    def __init__(self, undef_enabled=True):
        super(OracleDatafileTempfileSpecification, self).__init__()
        self._type = ("OracleDatafileTempfileSpecification", True)
        self._auto_extend = (self.__undef__, True)
        self._auto_extend_increment = (self.__undef__, True)
        self._max_size = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleDatafileTempfileSpecification, cls).from_dict(data, dirty, undef_enabled)
        obj._auto_extend = (data.get("autoExtend", obj.__undef__), dirty)
        if obj._auto_extend[0] is not None and obj._auto_extend[0] is not obj.__undef__:
            assert isinstance(obj._auto_extend[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._auto_extend[0], type(obj._auto_extend[0])))
            common.validate_format(obj._auto_extend[0], "None", None, None)
        obj._auto_extend_increment = (data.get("autoExtendIncrement", obj.__undef__), dirty)
        if obj._auto_extend_increment[0] is not None and obj._auto_extend_increment[0] is not obj.__undef__:
            assert isinstance(obj._auto_extend_increment[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._auto_extend_increment[0], type(obj._auto_extend_increment[0])))
            common.validate_format(obj._auto_extend_increment[0], "None", None, None)
        obj._max_size = (data.get("maxSize", obj.__undef__), dirty)
        if obj._max_size[0] is not None and obj._max_size[0] is not obj.__undef__:
            assert isinstance(obj._max_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._max_size[0], type(obj._max_size[0])))
            common.validate_format(obj._max_size[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleDatafileTempfileSpecification, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "auto_extend" == "type" or (self.auto_extend is not self.__undef__ and (not (dirty and not self._auto_extend[1]) or isinstance(self.auto_extend, list) or belongs_to_parent)):
            dct["autoExtend"] = dictify(self.auto_extend)
        elif belongs_to_parent and self.auto_extend is self.__undef__:
            dct["autoExtend"] = True
        if "auto_extend_increment" == "type" or (self.auto_extend_increment is not self.__undef__ and (not (dirty and not self._auto_extend_increment[1]) or isinstance(self.auto_extend_increment, list) or belongs_to_parent)):
            dct["autoExtendIncrement"] = dictify(self.auto_extend_increment)
        if "max_size" == "type" or (self.max_size is not self.__undef__ and (not (dirty and not self._max_size[1]) or isinstance(self.max_size, list) or belongs_to_parent)):
            dct["maxSize"] = dictify(self.max_size)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._auto_extend = (self._auto_extend[0], True)
        self._auto_extend_increment = (self._auto_extend_increment[0], True)
        self._max_size = (self._max_size[0], True)

    def is_dirty(self):
        return any([self._auto_extend[1], self._auto_extend_increment[1], self._max_size[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleDatafileTempfileSpecification):
            return False
        return super(OracleDatafileTempfileSpecification, self).__eq__(other) and \
               self.auto_extend == other.auto_extend and \
               self.auto_extend_increment == other.auto_extend_increment and \
               self.max_size == other.max_size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def auto_extend(self):
        """
        *(default value: True)* Enable or disable the automatic extension of a
        new or existing datafile or tempfile.

        :rtype: ``bool``
        """
        return self._auto_extend[0]

    @auto_extend.setter
    def auto_extend(self, value):
        self._auto_extend = (value, True)

    @property
    def auto_extend_increment(self):
        """
        The size in MB of the next increment of disk space to be allocated
        automatically when more extents are required. The default is the size
        of one data block.

        :rtype: ``int``
        """
        return self._auto_extend_increment[0]

    @auto_extend_increment.setter
    def auto_extend_increment(self, value):
        self._auto_extend_increment = (value, True)

    @property
    def max_size(self):
        """
        The maximum disk space allowed for automatic extension of the datafile.
        Omit this if you do not want to limit the disk space that Oracle can
        allocate to the datafile or tempfile.

        :rtype: ``int``
        """
        return self._max_size[0]

    @max_size.setter
    def max_size(self, value):
        self._max_size = (value, True)

