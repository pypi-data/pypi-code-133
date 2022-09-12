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
#     /delphix-js-data-container-create-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.JSDataLayoutCreateParameters import JSDataLayoutCreateParameters
from delphixpy.v1_10_4 import common

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

class JSDataContainerCreateParameters(JSDataLayoutCreateParameters):
    """
    *(extends* :py:class:`v1_10_4.web.vo.JSDataLayoutCreateParameters` *)* The
    parameters used to create a data container.
    """
    def __init__(self, undef_enabled=True):
        super(JSDataContainerCreateParameters, self).__init__()
        self._type = ("JSDataContainerCreateParameters", True)
        self._template = (self.__undef__, True)
        self._owners = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSDataContainerCreateParameters, cls).from_dict(data, dirty, undef_enabled)
        if "template" not in data:
            raise ValueError("Missing required property \"template\".")
        obj._template = (data.get("template", obj.__undef__), dirty)
        if obj._template[0] is not None and obj._template[0] is not obj.__undef__:
            assert isinstance(obj._template[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._template[0], type(obj._template[0])))
            common.validate_format(obj._template[0], "objectReference", None, None)
        obj._owners = []
        for item in data.get("owners") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._owners.append(item)
        obj._owners = (obj._owners, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSDataContainerCreateParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "template" == "type" or (self.template is not self.__undef__ and (not (dirty and not self._template[1]) or isinstance(self.template, list) or belongs_to_parent)):
            dct["template"] = dictify(self.template)
        if "owners" == "type" or (self.owners is not self.__undef__ and (not (dirty and not self._owners[1]) or isinstance(self.owners, list) or belongs_to_parent)):
            dct["owners"] = dictify(self.owners, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._template = (self._template[0], True)
        self._owners = (self._owners[0], True)

    def is_dirty(self):
        return any([self._template[1], self._owners[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSDataContainerCreateParameters):
            return False
        return super(JSDataContainerCreateParameters, self).__eq__(other) and \
               self.template == other.template and \
               self.owners == other.owners

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def template(self):
        """
        A reference to the template that this data container is provisioned
        from.

        :rtype: ``TEXT_TYPE``
        """
        return self._template[0]

    @template.setter
    def template(self, value):
        self._template = (value, True)

    @property
    def owners(self):
        """
        A reference to the list of users that own this data container.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._owners[0]

    @owners.setter
    def owners(self, value):
        self._owners = (value, True)

