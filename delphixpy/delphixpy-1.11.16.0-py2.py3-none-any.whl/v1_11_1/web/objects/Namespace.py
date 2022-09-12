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
#     /delphix-namespace.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_1.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_11_1 import common

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

class Namespace(NamedUserObject):
    """
    *(extends* :py:class:`v1_11_1.web.vo.NamedUserObject` *)* Object namespace
    for target-side replication.
    """
    def __init__(self, undef_enabled=True):
        super(Namespace, self).__init__()
        self._type = ("Namespace", True)
        self._namespace_type = (self.__undef__, True)
        self._description = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._tag = (self.__undef__, True)
        self._secure_namespace = (self.__undef__, True)
        self._failed_over = (self.__undef__, True)
        self._failover_report = (self.__undef__, True)

    API_VERSION = "1.11.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Namespace, cls).from_dict(data, dirty, undef_enabled)
        obj._namespace_type = (data.get("namespaceType", obj.__undef__), dirty)
        if obj._namespace_type[0] is not None and obj._namespace_type[0] is not obj.__undef__:
            assert isinstance(obj._namespace_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._namespace_type[0], type(obj._namespace_type[0])))
            assert obj._namespace_type[0] in ['REPLICATION'], "Expected enum ['REPLICATION'] but got %s" % obj._namespace_type[0]
            common.validate_format(obj._namespace_type[0], "None", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, 4096)
        obj._source = (data.get("source", obj.__undef__), dirty)
        if obj._source[0] is not None and obj._source[0] is not obj.__undef__:
            assert isinstance(obj._source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source[0], type(obj._source[0])))
            common.validate_format(obj._source[0], "None", None, None)
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", None, None)
        obj._secure_namespace = (data.get("secureNamespace", obj.__undef__), dirty)
        if obj._secure_namespace[0] is not None and obj._secure_namespace[0] is not obj.__undef__:
            assert isinstance(obj._secure_namespace[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._secure_namespace[0], type(obj._secure_namespace[0])))
            common.validate_format(obj._secure_namespace[0], "None", None, None)
        obj._failed_over = (data.get("failedOver", obj.__undef__), dirty)
        if obj._failed_over[0] is not None and obj._failed_over[0] is not obj.__undef__:
            assert isinstance(obj._failed_over[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._failed_over[0], type(obj._failed_over[0])))
            common.validate_format(obj._failed_over[0], "None", None, None)
        obj._failover_report = (data.get("failoverReport", obj.__undef__), dirty)
        if obj._failover_report[0] is not None and obj._failover_report[0] is not obj.__undef__:
            assert isinstance(obj._failover_report[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._failover_report[0], type(obj._failover_report[0])))
            common.validate_format(obj._failover_report[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Namespace, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "namespace_type" == "type" or (self.namespace_type is not self.__undef__ and (not (dirty and not self._namespace_type[1]))):
            dct["namespaceType"] = dictify(self.namespace_type)
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]))):
            dct["source"] = dictify(self.source)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]))):
            dct["tag"] = dictify(self.tag)
        if "secure_namespace" == "type" or (self.secure_namespace is not self.__undef__ and (not (dirty and not self._secure_namespace[1]))):
            dct["secureNamespace"] = dictify(self.secure_namespace)
        if "failed_over" == "type" or (self.failed_over is not self.__undef__ and (not (dirty and not self._failed_over[1]))):
            dct["failedOver"] = dictify(self.failed_over)
        if "failover_report" == "type" or (self.failover_report is not self.__undef__ and (not (dirty and not self._failover_report[1]))):
            dct["failoverReport"] = dictify(self.failover_report)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._namespace_type = (self._namespace_type[0], True)
        self._description = (self._description[0], True)
        self._source = (self._source[0], True)
        self._tag = (self._tag[0], True)
        self._secure_namespace = (self._secure_namespace[0], True)
        self._failed_over = (self._failed_over[0], True)
        self._failover_report = (self._failover_report[0], True)

    def is_dirty(self):
        return any([self._namespace_type[1], self._description[1], self._source[1], self._tag[1], self._secure_namespace[1], self._failed_over[1], self._failover_report[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Namespace):
            return False
        return super(Namespace, self).__eq__(other) and \
               self.namespace_type == other.namespace_type and \
               self.description == other.description and \
               self.source == other.source and \
               self.tag == other.tag and \
               self.secure_namespace == other.secure_namespace and \
               self.failed_over == other.failed_over and \
               self.failover_report == other.failover_report

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def namespace_type(self):
        """
        Type of object namespace. *(permitted values: REPLICATION)*

        :rtype: ``TEXT_TYPE``
        """
        return self._namespace_type[0]

    @namespace_type.setter
    def namespace_type(self, value):
        self._namespace_type = (value, True)

    @property
    def description(self):
        """
        Description of this namespace.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def source(self):
        """
        For replication, the source host IP address.

        :rtype: ``TEXT_TYPE``
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def tag(self):
        """
        A unique identifier for the source data stream.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

    @property
    def secure_namespace(self):
        """
        True if the source data stream was generated from a secure replication
        spec.

        :rtype: ``bool``
        """
        return self._secure_namespace[0]

    @secure_namespace.setter
    def secure_namespace(self, value):
        self._secure_namespace = (value, True)

    @property
    def failed_over(self):
        """
        Indicates the namespace has been failed over into the live environment.

        :rtype: ``bool``
        """
        return self._failed_over[0]

    @failed_over.setter
    def failed_over(self, value):
        self._failed_over = (value, True)

    @property
    def failover_report(self):
        """
        If failedOver is true, contains a report concern objects affected
        during failover.

        :rtype: ``TEXT_TYPE``
        """
        return self._failover_report[0]

    @failover_report.setter
    def failover_report(self, value):
        self._failover_report = (value, True)

