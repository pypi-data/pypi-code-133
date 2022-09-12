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
#     /delphix-x500-distinguished-name-composite.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.X500DistinguishedName import X500DistinguishedName
from delphixpy import common

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

class X500DistinguishedNameComposite(X500DistinguishedName):
    """
    *(extends* :py:class:`delphixpy.web.vo.X500DistinguishedName` *)* The
    representation of a composite X.500 Distinguished Name.
    """
    def __init__(self, undef_enabled=True):
        super(X500DistinguishedNameComposite, self).__init__()
        self._type = ("X500DistinguishedNameComposite", True)
        self._dname = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(X500DistinguishedNameComposite, cls).from_dict(data, dirty, undef_enabled)
        obj._dname = (data.get("dname", obj.__undef__), dirty)
        if obj._dname[0] is not None and obj._dname[0] is not obj.__undef__:
            assert isinstance(obj._dname[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._dname[0], type(obj._dname[0])))
            common.validate_format(obj._dname[0], "None", 1, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(X500DistinguishedNameComposite, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "dname" == "type" or (self.dname is not self.__undef__ and (not (dirty and not self._dname[1]) or isinstance(self.dname, list) or belongs_to_parent)):
            dct["dname"] = dictify(self.dname)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._dname = (self._dname[0], True)

    def is_dirty(self):
        return any([self._dname[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, X500DistinguishedNameComposite):
            return False
        return super(X500DistinguishedNameComposite, self).__eq__(other) and \
               self.dname == other.dname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def dname(self):
        """
        The composite Distinguished Name.

        :rtype: ``TEXT_TYPE``
        """
        return self._dname[0]

    @dname.setter
    def dname(self, value):
        self._dname = (value, True)

