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
#     /delphix-upgrade-compatibility-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_0.web.objects.CompatibleRepositoriesParameters import CompatibleRepositoriesParameters
from delphixpy.v1_4_0 import common

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

class UpgradeCompatibilityParameters(CompatibleRepositoriesParameters):
    """
    *(extends* :py:class:`v1_4_0.web.vo.CompatibleRepositoriesParameters` *)*
    The criteria necessary to select valid repositories for upgrading.
    """
    def __init__(self, undef_enabled=True):
        super(UpgradeCompatibilityParameters, self).__init__()
        self._type = ("UpgradeCompatibilityParameters", True)
        self._source_repository = (self.__undef__, True)

    API_VERSION = "1.4.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(UpgradeCompatibilityParameters, cls).from_dict(data, dirty, undef_enabled)
        if "sourceRepository" not in data:
            raise ValueError("Missing required property \"sourceRepository\".")
        obj._source_repository = (data.get("sourceRepository", obj.__undef__), dirty)
        if obj._source_repository[0] is not None and obj._source_repository[0] is not obj.__undef__:
            assert isinstance(obj._source_repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_repository[0], type(obj._source_repository[0])))
            common.validate_format(obj._source_repository[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(UpgradeCompatibilityParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "source_repository" == "type" or (self.source_repository is not self.__undef__ and (not (dirty and not self._source_repository[1]) or isinstance(self.source_repository, list) or belongs_to_parent)):
            dct["sourceRepository"] = dictify(self.source_repository)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._source_repository = (self._source_repository[0], True)

    def is_dirty(self):
        return any([self._source_repository[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, UpgradeCompatibilityParameters):
            return False
        return super(UpgradeCompatibilityParameters, self).__eq__(other) and \
               self.source_repository == other.source_repository

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def source_repository(self):
        """
        The repository to use as a source of compatibility information.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_repository[0]

    @source_repository.setter
    def source_repository(self, value):
        self._source_repository = (value, True)

