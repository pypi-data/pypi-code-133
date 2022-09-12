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
#     /delphix-source-repository-template.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_9.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_11_9 import common

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

class SourceRepositoryTemplate(NamedUserObject):
    """
    *(extends* :py:class:`v1_11_9.web.vo.NamedUserObject` *)* The
    representation of a repository template object.
    """
    def __init__(self, undef_enabled=True):
        super(SourceRepositoryTemplate, self).__init__()
        self._type = ("SourceRepositoryTemplate", True)
        self._repository = (self.__undef__, True)
        self._container = (self.__undef__, True)
        self._template = (self.__undef__, True)

    API_VERSION = "1.11.9"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourceRepositoryTemplate, cls).from_dict(data, dirty, undef_enabled)
        obj._repository = (data.get("repository", obj.__undef__), dirty)
        if obj._repository[0] is not None and obj._repository[0] is not obj.__undef__:
            assert isinstance(obj._repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._repository[0], type(obj._repository[0])))
            common.validate_format(obj._repository[0], "objectReference", None, None)
        obj._container = (data.get("container", obj.__undef__), dirty)
        if obj._container[0] is not None and obj._container[0] is not obj.__undef__:
            assert isinstance(obj._container[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._container[0], type(obj._container[0])))
            common.validate_format(obj._container[0], "objectReference", None, None)
        obj._template = (data.get("template", obj.__undef__), dirty)
        if obj._template[0] is not None and obj._template[0] is not obj.__undef__:
            assert isinstance(obj._template[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._template[0], type(obj._template[0])))
            common.validate_format(obj._template[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourceRepositoryTemplate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "repository" == "type" or (self.repository is not self.__undef__ and (not (dirty and not self._repository[1]) or isinstance(self.repository, list) or belongs_to_parent)):
            dct["repository"] = dictify(self.repository)
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container)
        if "template" == "type" or (self.template is not self.__undef__ and (not (dirty and not self._template[1]) or isinstance(self.template, list) or belongs_to_parent)):
            dct["template"] = dictify(self.template)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._repository = (self._repository[0], True)
        self._container = (self._container[0], True)
        self._template = (self._template[0], True)

    def is_dirty(self):
        return any([self._repository[1], self._container[1], self._template[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourceRepositoryTemplate):
            return False
        return super(SourceRepositoryTemplate, self).__eq__(other) and \
               self.repository == other.repository and \
               self.container == other.container and \
               self.template == other.template

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def repository(self):
        """
        The reference to the target repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._repository[0]

    @repository.setter
    def repository(self, value):
        self._repository = (value, True)

    @property
    def container(self):
        """
        The reference to the database container.

        :rtype: ``TEXT_TYPE``
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def template(self):
        """
        The reference to the associated template.

        :rtype: ``TEXT_TYPE``
        """
        return self._template[0]

    @template.setter
    def template(self, value):
        self._template = (value, True)

