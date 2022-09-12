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
#     /delphix-ca-certificate.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.Certificate import Certificate
from delphixpy.v1_11_11 import common

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

class CaCertificate(Certificate):
    """
    *(extends* :py:class:`v1_11_11.web.vo.Certificate` *)* Public Key
    Certificate that is a Certificate Authority.
    """
    def __init__(self, undef_enabled=True):
        super(CaCertificate, self).__init__()
        self._type = ("CaCertificate", True)
        self._accepted = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(CaCertificate, cls).from_dict(data, dirty, undef_enabled)
        obj._accepted = (data.get("accepted", obj.__undef__), dirty)
        if obj._accepted[0] is not None and obj._accepted[0] is not obj.__undef__:
            assert isinstance(obj._accepted[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._accepted[0], type(obj._accepted[0])))
            common.validate_format(obj._accepted[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(CaCertificate, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "accepted" == "type" or (self.accepted is not self.__undef__ and (not (dirty and not self._accepted[1]))):
            dct["accepted"] = dictify(self.accepted)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._accepted = (self._accepted[0], True)

    def is_dirty(self):
        return any([self._accepted[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, CaCertificate):
            return False
        return super(CaCertificate, self).__eq__(other) and \
               self.accepted == other.accepted

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def accepted(self):
        """
        Delphix trusts this certificate .

        :rtype: ``bool``
        """
        return self._accepted[0]

    @accepted.setter
    def accepted(self, value):
        self._accepted = (value, True)

