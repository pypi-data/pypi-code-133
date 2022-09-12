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
#     /delphix-mysql-db-container.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.DatabaseContainer import DatabaseContainer
from delphixpy.v1_8_1 import factory
from delphixpy.v1_8_1 import common

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

class MySQLDatabaseContainer(DatabaseContainer):
    """
    *(extends* :py:class:`v1_8_1.web.vo.DatabaseContainer` *)* A MySQL Database
    Container.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLDatabaseContainer, self).__init__()
        self._type = ("MySQLDatabaseContainer", True)
        self._runtime = (self.__undef__, True)
        self._variant = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLDatabaseContainer, cls).from_dict(data, dirty, undef_enabled)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "MySQLDBContainerRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "MySQLDBContainerRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        obj._variant = (data.get("variant", obj.__undef__), dirty)
        if obj._variant[0] is not None and obj._variant[0] is not obj.__undef__:
            assert isinstance(obj._variant[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._variant[0], type(obj._variant[0])))
            assert obj._variant[0] in ['CommunityServer', 'MariaDB'], "Expected enum ['CommunityServer', 'MariaDB'] but got %s" % obj._variant[0]
            common.validate_format(obj._variant[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLDatabaseContainer, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "variant" == "type" or (self.variant is not self.__undef__ and (not (dirty and not self._variant[1]))):
            dct["variant"] = dictify(self.variant)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._runtime = (self._runtime[0], True)
        self._variant = (self._variant[0], True)

    def is_dirty(self):
        return any([self._runtime[1], self._variant[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLDatabaseContainer):
            return False
        return super(MySQLDatabaseContainer, self).__eq__(other) and \
               self.runtime == other.runtime and \
               self.variant == other.variant

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def runtime(self):
        """
        Runtime properties of this container.

        :rtype: :py:class:`v1_8_1.web.vo.MySQLDBContainerRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def variant(self):
        """
        Variant of the MySQL installation. *(permitted values: CommunityServer,
        MariaDB)*

        :rtype: ``TEXT_TYPE``
        """
        return self._variant[0]

    @variant.setter
    def variant(self, value):
        self._variant = (value, True)

