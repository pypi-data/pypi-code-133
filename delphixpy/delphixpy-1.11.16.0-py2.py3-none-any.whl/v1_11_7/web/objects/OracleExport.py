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
#     /delphix-oracle-export.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_7 import factory
from delphixpy.v1_11_7 import common

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

class OracleExport(TypedObject):
    """
    *(extends* :py:class:`v1_11_7.web.vo.TypedObject` *)* The mutable state of
    an Oracle database export.
    """
    def __init__(self, undef_enabled=True):
        super(OracleExport, self).__init__()
        self._type = ("OracleExport", True)
        self._file_parallelism = (self.__undef__, True)
        self._dsp_options = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleExport, cls).from_dict(data, dirty, undef_enabled)
        obj._file_parallelism = (data.get("fileParallelism", obj.__undef__), dirty)
        if obj._file_parallelism[0] is not None and obj._file_parallelism[0] is not obj.__undef__:
            assert isinstance(obj._file_parallelism[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._file_parallelism[0], type(obj._file_parallelism[0])))
            common.validate_format(obj._file_parallelism[0], "None", None, None)
        if "dspOptions" in data and data["dspOptions"] is not None:
            obj._dsp_options = (factory.create_object(data["dspOptions"], "DSPOptions"), dirty)
            factory.validate_type(obj._dsp_options[0], "DSPOptions")
        else:
            obj._dsp_options = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleExport, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "file_parallelism" == "type" or (self.file_parallelism is not self.__undef__ and (not (dirty and not self._file_parallelism[1]))):
            dct["fileParallelism"] = dictify(self.file_parallelism)
        if "dsp_options" == "type" or (self.dsp_options is not self.__undef__ and (not (dirty and not self._dsp_options[1]))):
            dct["dspOptions"] = dictify(self.dsp_options)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._file_parallelism = (self._file_parallelism[0], True)
        self._dsp_options = (self._dsp_options[0], True)

    def is_dirty(self):
        return any([self._file_parallelism[1], self._dsp_options[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleExport):
            return False
        return super(OracleExport, self).__eq__(other) and \
               self.file_parallelism == other.file_parallelism and \
               self.dsp_options == other.dsp_options

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def file_parallelism(self):
        """
        *(default value: 3)* Number of files to stream in parallel across the
        network.

        :rtype: ``int``
        """
        return self._file_parallelism[0]

    @file_parallelism.setter
    def file_parallelism(self, value):
        self._file_parallelism = (value, True)

    @property
    def dsp_options(self):
        """
        DSP options for export.

        :rtype: :py:class:`v1_11_7.web.vo.DSPOptions`
        """
        return self._dsp_options[0]

    @dsp_options.setter
    def dsp_options(self, value):
        self._dsp_options = (value, True)

