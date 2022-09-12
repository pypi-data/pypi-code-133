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
#     /delphix-create-transformation-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_10.web.objects.TypedObject import TypedObject
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

class CreateTransformationParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_10.web.vo.TypedObject` *)* Represents the
    parameters of a createTransformation request.
    """
    def __init__(self, undef_enabled=True):
        super(CreateTransformationParameters, self).__init__()
        self._type = ("CreateTransformationParameters", True)
        self._container = (self.__undef__, True)
        self._environment_user = (self.__undef__, True)
        self._repository = (self.__undef__, True)
        self._operations = (self.__undef__, True)

    API_VERSION = "1.11.10"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CreateTransformationParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "Container"), dirty)
            factory.validate_type(obj._container[0], "Container")
        else:
            obj._container = (obj.__undef__, dirty)
        obj._environment_user = (data.get("environmentUser", obj.__undef__), dirty)
        if obj._environment_user[0] is not None and obj._environment_user[0] is not obj.__undef__:
            assert isinstance(obj._environment_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._environment_user[0], type(obj._environment_user[0])))
            common.validate_format(obj._environment_user[0], "objectReference", None, None)
        obj._repository = (data.get("repository", obj.__undef__), dirty)
        if obj._repository[0] is not None and obj._repository[0] is not obj.__undef__:
            assert isinstance(obj._repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._repository[0], type(obj._repository[0])))
            common.validate_format(obj._repository[0], "objectReference", None, None)
        obj._operations = []
        for item in data.get("operations") or []:
            obj._operations.append(factory.create_object(item))
            factory.validate_type(obj._operations[-1], "SourceOperation")
        obj._operations = (obj._operations, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CreateTransformationParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "environment_user" == "type" or (self.environment_user is not self.__undef__ and (not (dirty and not self._environment_user[1]) or isinstance(self.environment_user, list) or belongs_to_parent)):
            dct["environmentUser"] = dictify(self.environment_user)
        if "repository" == "type" or (self.repository is not self.__undef__ and (not (dirty and not self._repository[1]) or isinstance(self.repository, list) or belongs_to_parent)):
            dct["repository"] = dictify(self.repository)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._environment_user = (self._environment_user[0], True)
        self._repository = (self._repository[0], True)
        self._operations = (self._operations[0], True)

    def is_dirty(self):
        return any([self._container[1], self._environment_user[1], self._repository[1], self._operations[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CreateTransformationParameters):
            return False
        return super(CreateTransformationParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.environment_user == other.environment_user and \
               self.repository == other.repository and \
               self.operations == other.operations

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        The container that will contain the transformed data associated with
        the newly created transformation; the "transformation container".

        :rtype: :py:class:`v1_11_10.web.vo.Container`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def environment_user(self):
        """
        Reference to the user used during application of the transformation.

        :rtype: ``TEXT_TYPE``
        """
        return self._environment_user[0]

    @environment_user.setter
    def environment_user(self, value):
        self._environment_user = (value, True)

    @property
    def repository(self):
        """
        Reference to the repository used during application of the
        transformation.

        :rtype: ``TEXT_TYPE``
        """
        return self._repository[0]

    @repository.setter
    def repository(self, value):
        self._repository = (value, True)

    @property
    def operations(self):
        """
        Operations to perform when this transformation is applied.

        :rtype: ``list`` of :py:class:`v1_11_10.web.vo.SourceOperation`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

