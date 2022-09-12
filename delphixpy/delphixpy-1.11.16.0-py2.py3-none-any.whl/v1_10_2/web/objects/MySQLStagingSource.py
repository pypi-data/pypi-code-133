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
#     /delphix-mysql-staging-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.MySQLSource import MySQLSource
from delphixpy.v1_10_2 import factory
from delphixpy.v1_10_2 import common

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

class MySQLStagingSource(MySQLSource):
    """
    *(extends* :py:class:`v1_10_2.web.vo.MySQLSource` *)* A MySQL staging
    source used for validated sync.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLStagingSource, self).__init__()
        self._type = ("MySQLStagingSource", True)
        self._mount_base = (self.__undef__, True)
        self._pre_script = (self.__undef__, True)
        self._post_script = (self.__undef__, True)
        self._runtime = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLStagingSource, cls).from_dict(data, dirty, undef_enabled)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "None", None, 256)
        obj._pre_script = (data.get("preScript", obj.__undef__), dirty)
        if obj._pre_script[0] is not None and obj._pre_script[0] is not obj.__undef__:
            assert isinstance(obj._pre_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pre_script[0], type(obj._pre_script[0])))
            common.validate_format(obj._pre_script[0], "None", None, None)
        obj._post_script = (data.get("postScript", obj.__undef__), dirty)
        if obj._post_script[0] is not None and obj._post_script[0] is not obj.__undef__:
            assert isinstance(obj._post_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._post_script[0], type(obj._post_script[0])))
            common.validate_format(obj._post_script[0], "None", None, None)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "MySQLSourceRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "MySQLSourceRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLStagingSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]))):
            dct["mountBase"] = dictify(self.mount_base)
        if "pre_script" == "type" or (self.pre_script is not self.__undef__ and (not (dirty and not self._pre_script[1]) or isinstance(self.pre_script, list) or belongs_to_parent)):
            dct["preScript"] = dictify(self.pre_script)
        if "post_script" == "type" or (self.post_script is not self.__undef__ and (not (dirty and not self._post_script[1]) or isinstance(self.post_script, list) or belongs_to_parent)):
            dct["postScript"] = dictify(self.post_script)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._mount_base = (self._mount_base[0], True)
        self._pre_script = (self._pre_script[0], True)
        self._post_script = (self._post_script[0], True)
        self._runtime = (self._runtime[0], True)

    def is_dirty(self):
        return any([self._mount_base[1], self._pre_script[1], self._post_script[1], self._runtime[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLStagingSource):
            return False
        return super(MySQLStagingSource, self).__eq__(other) and \
               self.mount_base == other.mount_base and \
               self.pre_script == other.pre_script and \
               self.post_script == other.post_script and \
               self.runtime == other.runtime

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def mount_base(self):
        """
        The base mount point for the NFS mounts on the staging host.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_base[0]

    @mount_base.setter
    def mount_base(self, value):
        self._mount_base = (value, True)

    @property
    def pre_script(self):
        """
        A user-provided script to run prior to taking a snapshot.

        :rtype: ``TEXT_TYPE``
        """
        return self._pre_script[0]

    @pre_script.setter
    def pre_script(self, value):
        self._pre_script = (value, True)

    @property
    def post_script(self):
        """
        A user-provided script to run after taking a snapshot.

        :rtype: ``TEXT_TYPE``
        """
        return self._post_script[0]

    @post_script.setter
    def post_script(self, value):
        self._post_script = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this source.

        :rtype: :py:class:`v1_10_2.web.vo.MySQLSourceRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

