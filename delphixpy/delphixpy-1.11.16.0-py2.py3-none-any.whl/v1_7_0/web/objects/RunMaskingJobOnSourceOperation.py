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
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_0.web.objects.SourceOperation import SourceOperation
from delphixpy.v1_7_0 import common

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

class RunMaskingJobOnSourceOperation(SourceOperation):
    """
    *(extends* :py:class:`v1_7_0.web.vo.SourceOperation` *)* An operation that
    runs a Masking Job on the local Delphix Masking Engine instance.
    """
    def __init__(self, undef_enabled=True):
        super(RunMaskingJobOnSourceOperation, self).__init__()
        self._type = ("RunMaskingJobOnSourceOperation", True)
        self._application_id = (self.__undef__, True)
        self._masking_job_id = (self.__undef__, True)
        self._name = (self.__undef__, True)

    API_VERSION = "1.7.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(RunMaskingJobOnSourceOperation, cls).from_dict(data, dirty, undef_enabled)
        obj._application_id = (data.get("applicationId", obj.__undef__), dirty)
        if obj._application_id[0] is not None and obj._application_id[0] is not obj.__undef__:
            assert isinstance(obj._application_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._application_id[0], type(obj._application_id[0])))
            common.validate_format(obj._application_id[0], "None", None, None)
        obj._masking_job_id = (data.get("maskingJobId", obj.__undef__), dirty)
        if obj._masking_job_id[0] is not None and obj._masking_job_id[0] is not obj.__undef__:
            assert isinstance(obj._masking_job_id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._masking_job_id[0], type(obj._masking_job_id[0])))
            common.validate_format(obj._masking_job_id[0], "None", None, None)
        obj._name = (data.get("name", obj.__undef__), dirty)
        if obj._name[0] is not None and obj._name[0] is not obj.__undef__:
            assert isinstance(obj._name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._name[0], type(obj._name[0])))
            common.validate_format(obj._name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(RunMaskingJobOnSourceOperation, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "application_id" == "type" or (self.application_id is not self.__undef__ and (not (dirty and not self._application_id[1]) or isinstance(self.application_id, list) or belongs_to_parent)):
            dct["applicationId"] = dictify(self.application_id)
        if "masking_job_id" == "type" or (self.masking_job_id is not self.__undef__ and (not (dirty and not self._masking_job_id[1]) or isinstance(self.masking_job_id, list) or belongs_to_parent)):
            dct["maskingJobId"] = dictify(self.masking_job_id)
        if "name" == "type" or (self.name is not self.__undef__ and (not (dirty and not self._name[1]) or isinstance(self.name, list) or belongs_to_parent)):
            dct["name"] = dictify(self.name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._application_id = (self._application_id[0], True)
        self._masking_job_id = (self._masking_job_id[0], True)
        self._name = (self._name[0], True)

    def is_dirty(self):
        return any([self._application_id[1], self._masking_job_id[1], self._name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, RunMaskingJobOnSourceOperation):
            return False
        return super(RunMaskingJobOnSourceOperation, self).__eq__(other) and \
               self.application_id == other.application_id and \
               self.masking_job_id == other.masking_job_id and \
               self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def application_id(self):
        """
        The application ID of the Masking Job to be executed.

        :rtype: ``TEXT_TYPE``
        """
        return self._application_id[0]

    @application_id.setter
    def application_id(self, value):
        self._application_id = (value, True)

    @property
    def masking_job_id(self):
        """
        The Masking Job ID of the Masking Job to be executed.

        :rtype: ``TEXT_TYPE``
        """
        return self._masking_job_id[0]

    @masking_job_id.setter
    def masking_job_id(self, value):
        self._masking_job_id = (value, True)

    @property
    def name(self):
        """
        The name of the Masking Job to be executed.

        :rtype: ``TEXT_TYPE``
        """
        return self._name[0]

    @name.setter
    def name(self, value):
        self._name = (value, True)

