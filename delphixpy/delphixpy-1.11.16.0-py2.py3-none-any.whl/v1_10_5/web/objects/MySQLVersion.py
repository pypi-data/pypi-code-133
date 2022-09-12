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
#     /delphix-mysql-version.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_5 import common

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

class MySQLVersion(TypedObject):
    """
    *(extends* :py:class:`v1_10_5.web.vo.TypedObject` *)* Version of a MySQL
    installation.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLVersion, self).__init__()
        self._type = ("MySQLVersion", True)
        self._version = (self.__undef__, True)
        self._variant = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLVersion, cls).from_dict(data, dirty, undef_enabled)
        obj._version = (data.get("version", obj.__undef__), dirty)
        if obj._version[0] is not None and obj._version[0] is not obj.__undef__:
            assert isinstance(obj._version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._version[0], type(obj._version[0])))
            common.validate_format(obj._version[0], "mysqlVersion", None, None)
        obj._variant = (data.get("variant", obj.__undef__), dirty)
        if obj._variant[0] is not None and obj._variant[0] is not obj.__undef__:
            assert isinstance(obj._variant[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._variant[0], type(obj._variant[0])))
            assert obj._variant[0] in ['CommunityServer', 'MariaDB'], "Expected enum ['CommunityServer', 'MariaDB'] but got %s" % obj._variant[0]
            common.validate_format(obj._variant[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLVersion, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "version" == "type" or (self.version is not self.__undef__ and (not (dirty and not self._version[1]))):
            dct["version"] = dictify(self.version)
        if "variant" == "type" or (self.variant is not self.__undef__ and (not (dirty and not self._variant[1]))):
            dct["variant"] = dictify(self.variant)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._version = (self._version[0], True)
        self._variant = (self._variant[0], True)

    def is_dirty(self):
        return any([self._version[1], self._variant[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLVersion):
            return False
        return super(MySQLVersion, self).__eq__(other) and \
               self.version == other.version and \
               self.variant == other.variant

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def version(self):
        """
        Version of the MySQL installation.

        :rtype: ``TEXT_TYPE``
        """
        return self._version[0]

    @version.setter
    def version(self, value):
        self._version = (value, True)

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

