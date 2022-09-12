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
#     /delphix-ase-staging-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_10.web.objects.ASESource import ASESource
from delphixpy.v1_11_10 import factory
from delphixpy.v1_11_10 import common

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

class ASEStagingSource(ASESource):
    """
    *(extends* :py:class:`v1_11_10.web.vo.ASESource` *)* An SAP ASE staging
    source used for validated sync..
    """
    def __init__(self, undef_enabled=True):
        super(ASEStagingSource, self).__init__()
        self._type = ("ASEStagingSource", True)
        self._mount_base = (self.__undef__, True)
        self._pre_script = (self.__undef__, True)
        self._post_script = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._runtime_mount_information = (self.__undef__, True)

    API_VERSION = "1.11.10"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASEStagingSource, cls).from_dict(data, dirty, undef_enabled)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "None", None, 87)
        obj._pre_script = (data.get("preScript", obj.__undef__), dirty)
        if obj._pre_script[0] is not None and obj._pre_script[0] is not obj.__undef__:
            assert isinstance(obj._pre_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pre_script[0], type(obj._pre_script[0])))
            common.validate_format(obj._pre_script[0], "None", None, 1024)
        obj._post_script = (data.get("postScript", obj.__undef__), dirty)
        if obj._post_script[0] is not None and obj._post_script[0] is not obj.__undef__:
            assert isinstance(obj._post_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._post_script[0], type(obj._post_script[0])))
            common.validate_format(obj._post_script[0], "None", None, 1024)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "StagingSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "StagingSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        if "runtimeMountInformation" in data and data["runtimeMountInformation"] is not None:
            obj._runtime_mount_information = (factory.create_object(data["runtimeMountInformation"], "RuntimeMountInformation"), dirty)
            factory.validate_type(obj._runtime_mount_information[0], "RuntimeMountInformation")
        else:
            obj._runtime_mount_information = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASEStagingSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]) or isinstance(self.mount_base, list) or belongs_to_parent)):
            dct["mountBase"] = dictify(self.mount_base)
        if "pre_script" == "type" or (self.pre_script is not self.__undef__ and (not (dirty and not self._pre_script[1]) or isinstance(self.pre_script, list) or belongs_to_parent)):
            dct["preScript"] = dictify(self.pre_script)
        if "post_script" == "type" or (self.post_script is not self.__undef__ and (not (dirty and not self._post_script[1]) or isinstance(self.post_script, list) or belongs_to_parent)):
            dct["postScript"] = dictify(self.post_script)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "runtime_mount_information" == "type" or (self.runtime_mount_information is not self.__undef__ and (not (dirty and not self._runtime_mount_information[1]))):
            dct["runtimeMountInformation"] = dictify(self.runtime_mount_information)
        if dirty and "runtimeMountInformation" in dct:
            del dct["runtimeMountInformation"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._mount_base = (self._mount_base[0], True)
        self._pre_script = (self._pre_script[0], True)
        self._post_script = (self._post_script[0], True)
        self._operations = (self._operations[0], True)
        self._runtime_mount_information = (self._runtime_mount_information[0], True)

    def is_dirty(self):
        return any([self._mount_base[1], self._pre_script[1], self._post_script[1], self._operations[1], self._runtime_mount_information[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASEStagingSource):
            return False
        return super(ASEStagingSource, self).__eq__(other) and \
               self.mount_base == other.mount_base and \
               self.pre_script == other.pre_script and \
               self.post_script == other.post_script and \
               self.operations == other.operations and \
               self.runtime_mount_information == other.runtime_mount_information

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def mount_base(self):
        """
        The base mount point for the NFS mounts.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_base[0]

    @mount_base.setter
    def mount_base(self, value):
        self._mount_base = (value, True)

    @property
    def pre_script(self):
        """
        The path to a user-provided script or executable to run on the staging
        host prior to restoring from a backup during validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._pre_script[0]

    @pre_script.setter
    def pre_script(self, value):
        self._pre_script = (value, True)

    @property
    def post_script(self):
        """
        The path to a user-provided shell script or executable to run on the
        staging host after restoring from a backup during validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._post_script[0]

    @post_script.setter
    def post_script(self, value):
        self._post_script = (value, True)

    @property
    def operations(self):
        """
        User-specified hook operations for this staging source.

        :rtype: :py:class:`v1_11_10.web.vo.StagingSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def runtime_mount_information(self):
        """
        The representation of runtime mount information.

        :rtype: :py:class:`v1_11_10.web.vo.RuntimeMountInformation`
        """
        return self._runtime_mount_information[0]

