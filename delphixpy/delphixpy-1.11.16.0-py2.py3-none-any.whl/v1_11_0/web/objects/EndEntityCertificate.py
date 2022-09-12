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
#     /delphix-end-entity-certificate.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_0.web.objects.Certificate import Certificate
from delphixpy.v1_11_0 import factory
from delphixpy.v1_11_0 import common

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

class EndEntityCertificate(Certificate):
    """
    *(extends* :py:class:`v1_11_0.web.vo.Certificate` *)* An End-Entity Public
    Key Certificate.
    """
    def __init__(self, undef_enabled=True):
        super(EndEntityCertificate, self).__init__()
        self._type = ("EndEntityCertificate", True)
        self._end_entity = (self.__undef__, True)

    API_VERSION = "1.11.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(EndEntityCertificate, cls).from_dict(data, dirty, undef_enabled)
        if "endEntity" in data and data["endEntity"] is not None:
            obj._end_entity = (factory.create_object(data["endEntity"], "EndEntity"), dirty)
            factory.validate_type(obj._end_entity[0], "EndEntity")
        else:
            obj._end_entity = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(EndEntityCertificate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "end_entity" == "type" or (self.end_entity is not self.__undef__ and (not (dirty and not self._end_entity[1]))):
            dct["endEntity"] = dictify(self.end_entity)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._end_entity = (self._end_entity[0], True)

    def is_dirty(self):
        return any([self._end_entity[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, EndEntityCertificate):
            return False
        return super(EndEntityCertificate, self).__eq__(other) and \
               self.end_entity == other.end_entity

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def end_entity(self):
        """
        The specific TLS service this certificate is used for.

        :rtype: :py:class:`v1_11_0.web.vo.EndEntity`
        """
        return self._end_entity[0]

    @end_entity.setter
    def end_entity(self, value):
        self._end_entity = (value, True)

