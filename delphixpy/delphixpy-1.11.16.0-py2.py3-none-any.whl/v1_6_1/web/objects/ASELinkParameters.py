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
#     /delphix-ase-link-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.LinkParameters import LinkParameters
from delphixpy.v1_6_1 import factory
from delphixpy.v1_6_1 import common

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

class ASELinkParameters(LinkParameters):
    """
    *(extends* :py:class:`v1_6_1.web.vo.LinkParameters` *)* SAP ASE specific
    parameters for a link request.
    """
    def __init__(self, undef_enabled=True):
        super(ASELinkParameters, self).__init__()
        self._type = ("ASELinkParameters", True)
        self._container = (self.__undef__, True)
        self._db_credentials = (self.__undef__, True)
        self._db_user = (self.__undef__, True)
        self._source = (self.__undef__, True)
        self._source_host_user = (self.__undef__, True)
        self._staging_host_user = (self.__undef__, True)
        self._staging_post_script = (self.__undef__, True)
        self._staging_pre_script = (self.__undef__, True)
        self._staging_repository = (self.__undef__, True)
        self._sync_parameters = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASELinkParameters, cls).from_dict(data, dirty, undef_enabled)
        if "container" not in data:
            raise ValueError("Missing required property \"container\".")
        if "container" in data and data["container"] is not None:
            obj._container = (factory.create_object(data["container"], "ASEDBContainer"), dirty)
            factory.validate_type(obj._container[0], "ASEDBContainer")
        else:
            obj._container = (obj.__undef__, dirty)
        if "dbCredentials" in data and data["dbCredentials"] is not None:
            obj._db_credentials = (factory.create_object(data["dbCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._db_credentials[0], "PasswordCredential")
        else:
            obj._db_credentials = (obj.__undef__, dirty)
        obj._db_user = (data.get("dbUser", obj.__undef__), dirty)
        if obj._db_user[0] is not None and obj._db_user[0] is not obj.__undef__:
            assert isinstance(obj._db_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._db_user[0], type(obj._db_user[0])))
            common.validate_format(obj._db_user[0], "None", None, None)
        if "source" not in data:
            raise ValueError("Missing required property \"source\".")
        if "source" in data and data["source"] is not None:
            obj._source = (factory.create_object(data["source"], "ASELinkedSource"), dirty)
            factory.validate_type(obj._source[0], "ASELinkedSource")
        else:
            obj._source = (obj.__undef__, dirty)
        obj._source_host_user = (data.get("sourceHostUser", obj.__undef__), dirty)
        if obj._source_host_user[0] is not None and obj._source_host_user[0] is not obj.__undef__:
            assert isinstance(obj._source_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_host_user[0], type(obj._source_host_user[0])))
            common.validate_format(obj._source_host_user[0], "objectReference", None, None)
        obj._staging_host_user = (data.get("stagingHostUser", obj.__undef__), dirty)
        if obj._staging_host_user[0] is not None and obj._staging_host_user[0] is not obj.__undef__:
            assert isinstance(obj._staging_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_host_user[0], type(obj._staging_host_user[0])))
            common.validate_format(obj._staging_host_user[0], "objectReference", None, None)
        obj._staging_post_script = (data.get("stagingPostScript", obj.__undef__), dirty)
        if obj._staging_post_script[0] is not None and obj._staging_post_script[0] is not obj.__undef__:
            assert isinstance(obj._staging_post_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_post_script[0], type(obj._staging_post_script[0])))
            common.validate_format(obj._staging_post_script[0], "None", None, 1024)
        obj._staging_pre_script = (data.get("stagingPreScript", obj.__undef__), dirty)
        if obj._staging_pre_script[0] is not None and obj._staging_pre_script[0] is not obj.__undef__:
            assert isinstance(obj._staging_pre_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_pre_script[0], type(obj._staging_pre_script[0])))
            common.validate_format(obj._staging_pre_script[0], "None", None, 1024)
        obj._staging_repository = (data.get("stagingRepository", obj.__undef__), dirty)
        if obj._staging_repository[0] is not None and obj._staging_repository[0] is not obj.__undef__:
            assert isinstance(obj._staging_repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_repository[0], type(obj._staging_repository[0])))
            common.validate_format(obj._staging_repository[0], "objectReference", None, None)
        if "syncParameters" in data and data["syncParameters"] is not None:
            obj._sync_parameters = (factory.create_object(data["syncParameters"], "ASESyncParameters"), dirty)
            factory.validate_type(obj._sync_parameters[0], "ASESyncParameters")
        else:
            obj._sync_parameters = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASELinkParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "container" == "type" or (self.container is not self.__undef__ and (not (dirty and not self._container[1]) or isinstance(self.container, list) or belongs_to_parent)):
            dct["container"] = dictify(self.container, prop_is_list_or_vo=True)
        if "db_credentials" == "type" or (self.db_credentials is not self.__undef__ and (not (dirty and not self._db_credentials[1]) or isinstance(self.db_credentials, list) or belongs_to_parent)):
            dct["dbCredentials"] = dictify(self.db_credentials, prop_is_list_or_vo=True)
        if "db_user" == "type" or (self.db_user is not self.__undef__ and (not (dirty and not self._db_user[1]) or isinstance(self.db_user, list) or belongs_to_parent)):
            dct["dbUser"] = dictify(self.db_user)
        if "source" == "type" or (self.source is not self.__undef__ and (not (dirty and not self._source[1]) or isinstance(self.source, list) or belongs_to_parent)):
            dct["source"] = dictify(self.source, prop_is_list_or_vo=True)
        if "source_host_user" == "type" or (self.source_host_user is not self.__undef__ and (not (dirty and not self._source_host_user[1]) or isinstance(self.source_host_user, list) or belongs_to_parent)):
            dct["sourceHostUser"] = dictify(self.source_host_user)
        if "staging_host_user" == "type" or (self.staging_host_user is not self.__undef__ and (not (dirty and not self._staging_host_user[1]) or isinstance(self.staging_host_user, list) or belongs_to_parent)):
            dct["stagingHostUser"] = dictify(self.staging_host_user)
        if "staging_post_script" == "type" or (self.staging_post_script is not self.__undef__ and (not (dirty and not self._staging_post_script[1]) or isinstance(self.staging_post_script, list) or belongs_to_parent)):
            dct["stagingPostScript"] = dictify(self.staging_post_script)
        if "staging_pre_script" == "type" or (self.staging_pre_script is not self.__undef__ and (not (dirty and not self._staging_pre_script[1]) or isinstance(self.staging_pre_script, list) or belongs_to_parent)):
            dct["stagingPreScript"] = dictify(self.staging_pre_script)
        if "staging_repository" == "type" or (self.staging_repository is not self.__undef__ and (not (dirty and not self._staging_repository[1]) or isinstance(self.staging_repository, list) or belongs_to_parent)):
            dct["stagingRepository"] = dictify(self.staging_repository)
        if "sync_parameters" == "type" or (self.sync_parameters is not self.__undef__ and (not (dirty and not self._sync_parameters[1]) or isinstance(self.sync_parameters, list) or belongs_to_parent)):
            dct["syncParameters"] = dictify(self.sync_parameters, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._container = (self._container[0], True)
        self._db_credentials = (self._db_credentials[0], True)
        self._db_user = (self._db_user[0], True)
        self._source = (self._source[0], True)
        self._source_host_user = (self._source_host_user[0], True)
        self._staging_host_user = (self._staging_host_user[0], True)
        self._staging_post_script = (self._staging_post_script[0], True)
        self._staging_pre_script = (self._staging_pre_script[0], True)
        self._staging_repository = (self._staging_repository[0], True)
        self._sync_parameters = (self._sync_parameters[0], True)

    def is_dirty(self):
        return any([self._container[1], self._db_credentials[1], self._db_user[1], self._source[1], self._source_host_user[1], self._staging_host_user[1], self._staging_post_script[1], self._staging_pre_script[1], self._staging_repository[1], self._sync_parameters[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASELinkParameters):
            return False
        return super(ASELinkParameters, self).__eq__(other) and \
               self.container == other.container and \
               self.db_credentials == other.db_credentials and \
               self.db_user == other.db_user and \
               self.source == other.source and \
               self.source_host_user == other.source_host_user and \
               self.staging_host_user == other.staging_host_user and \
               self.staging_post_script == other.staging_post_script and \
               self.staging_pre_script == other.staging_pre_script and \
               self.staging_repository == other.staging_repository and \
               self.sync_parameters == other.sync_parameters

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def container(self):
        """
        Container to create as part of the linking process.

        :rtype: :py:class:`v1_6_1.web.vo.ASEDBContainer`
        """
        return self._container[0]

    @container.setter
    def container(self, value):
        self._container = (value, True)

    @property
    def db_credentials(self):
        """
        The credential for the source DB user.

        :rtype: :py:class:`v1_6_1.web.vo.PasswordCredential`
        """
        return self._db_credentials[0]

    @db_credentials.setter
    def db_credentials(self, value):
        self._db_credentials = (value, True)

    @property
    def db_user(self):
        """
        The user name for the source DB user.

        :rtype: ``TEXT_TYPE``
        """
        return self._db_user[0]

    @db_user.setter
    def db_user(self, value):
        self._db_user = (value, True)

    @property
    def source(self):
        """
        Source to link the container to. This must reference an existing source
        config.

        :rtype: :py:class:`v1_6_1.web.vo.ASELinkedSource`
        """
        return self._source[0]

    @source.setter
    def source(self, value):
        self._source = (value, True)

    @property
    def source_host_user(self):
        """
        Information about the host OS user on the source to use for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_host_user[0]

    @source_host_user.setter
    def source_host_user(self, value):
        self._source_host_user = (value, True)

    @property
    def staging_host_user(self):
        """
        Information about the host OS user on the staging environment to use
        for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_host_user[0]

    @staging_host_user.setter
    def staging_host_user(self, value):
        self._staging_host_user = (value, True)

    @property
    def staging_post_script(self):
        """
        A user-provided shell script or executable to run after restoring from
        a backup during validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_post_script[0]

    @staging_post_script.setter
    def staging_post_script(self, value):
        self._staging_post_script = (value, True)

    @property
    def staging_pre_script(self):
        """
        A user-provided shell script or executable to run prior to restoring
        from a backup during validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_pre_script[0]

    @staging_pre_script.setter
    def staging_pre_script(self, value):
        self._staging_pre_script = (value, True)

    @property
    def staging_repository(self):
        """
        The SAP ASE instance on the staging environment that we want to use for
        validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_repository[0]

    @staging_repository.setter
    def staging_repository(self, value):
        self._staging_repository = (value, True)

    @property
    def sync_parameters(self):
        """
        Sync parameters for the container.

        :rtype: :py:class:`v1_6_1.web.vo.ASESyncParameters`
        """
        return self._sync_parameters[0]

    @sync_parameters.setter
    def sync_parameters(self, value):
        self._sync_parameters = (value, True)

