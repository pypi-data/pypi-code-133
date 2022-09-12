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
#     /delphix-ok-result.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_0.web.objects.CallResult import CallResult
from delphixpy.v1_5_0 import common

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

class OKResult(CallResult):
    """
    *(extends* :py:class:`v1_5_0.web.vo.CallResult` *)* Result of a successful
    API call.
    """
    def __init__(self, undef_enabled=True):
        super(OKResult, self).__init__()
        self._type = ("OKResult", True)
        self._action = (self.__undef__, True)
        self._job = (self.__undef__, True)
        self._result = (self.__undef__, True)

    API_VERSION = "1.5.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OKResult, cls).from_dict(data, dirty, undef_enabled)
        obj._action = (data.get("action", obj.__undef__), dirty)
        if obj._action[0] is not None and obj._action[0] is not obj.__undef__:
            assert isinstance(obj._action[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._action[0], type(obj._action[0])))
            common.validate_format(obj._action[0], "objectReference", None, None)
        obj._job = (data.get("job", obj.__undef__), dirty)
        if obj._job[0] is not None and obj._job[0] is not obj.__undef__:
            assert isinstance(obj._job[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._job[0], type(obj._job[0])))
            common.validate_format(obj._job[0], "objectReference", None, None)
        obj._result = (data.get("result", obj.__undef__), dirty)
        if obj._result[0] is not None and obj._result[0] is not obj.__undef__:
            assert isinstance(obj._result[0], dict) or isinstance(obj._result[0], list) or isinstance(obj._result[0], TEXT_TYPE), ("Expected one of ['object', 'array', 'string'], but got %s of type %s" % (obj._result[0], type(obj._result[0])))
            common.validate_format(obj._result[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OKResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "action" == "type" or (self.action is not self.__undef__ and (not (dirty and not self._action[1]))):
            dct["action"] = dictify(self.action)
        if "job" == "type" or (self.job is not self.__undef__ and (not (dirty and not self._job[1]))):
            dct["job"] = dictify(self.job)
        if "result" == "type" or (self.result is not self.__undef__ and (not (dirty and not self._result[1]))):
            dct["result"] = dictify(self.result)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._action = (self._action[0], True)
        self._job = (self._job[0], True)
        self._result = (self._result[0], True)

    def is_dirty(self):
        return any([self._action[1], self._job[1], self._result[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OKResult):
            return False
        return super(OKResult, self).__eq__(other) and \
               self.action == other.action and \
               self.job == other.job and \
               self.result == other.result

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def action(self):
        """
        Reference to the action associated with the operation, if any.

        :rtype: ``TEXT_TYPE``
        """
        return self._action[0]

    @action.setter
    def action(self, value):
        self._action = (value, True)

    @property
    def job(self):
        """
        Reference to the job started by the operation, if any.

        :rtype: ``TEXT_TYPE``
        """
        return self._job[0]

    @job.setter
    def job(self, value):
        self._job = (value, True)

    @property
    def result(self):
        """
        Result of the operation. This will be specific to the API being
        invoked.

        :rtype: ``dict`` *or* ``list`` *or* ``TEXT_TYPE``
        """
        return self._result[0]

    @result.setter
    def result(self, value):
        self._result = (value, True)

