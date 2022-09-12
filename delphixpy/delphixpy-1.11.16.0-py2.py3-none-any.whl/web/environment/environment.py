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

"""
Package "environment"
"""
API_VERSION = "1.11.16"

from delphixpy.web.environment import oracle
from delphixpy.web.environment import user
from delphixpy.web.environment import windows
try:
    from urllib import urlencode 
except ImportError:
    from urllib.parse import urlencode 
from delphixpy import response_validator

def create(engine, source_environment_create_parameters):
    """
    Create a new SourceEnvironment object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param source_environment_create_parameters: Payload object.
    :type source_environment_create_parameters:
        :py:class:`delphixpy.web.vo.SourceEnvironmentCreateParameters`
    :rtype: ``TEXT_TYPE``
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment"
    response = engine.post(url, source_environment_create_parameters.to_dict(dirty=True) if source_environment_create_parameters else None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['TEXT_TYPE'], returns_list=False, raw_result=raw_result)

def get(engine, ref):
    """
    Retrieve the specified SourceEnvironment object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    :rtype: :py:class:`delphixpy.web.vo.SourceEnvironment`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s" % ref
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['SourceEnvironment'], returns_list=False, raw_result=raw_result)

def get_all(engine, type=None):
    """
    Returns the list of all source environments.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param type: Filter the results based on the type of environment.
        *(permitted values: WindowsHostEnvironment, UnixHostEnvironment,
        ASEUnixHostEnvironment, OracleCluster)*
    :type type: ``TEXT_TYPE``
    :rtype: ``list`` of :py:class:`delphixpy.web.vo.SourceEnvironment`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment"
    query_params = {"type": type}
    query_dct = {k: query_params[k] for k in query_params if query_params[k] is not None}
    if query_dct:
        url_params = urlencode(query_dct)
        url += "?%s" % url_params
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['SourceEnvironment'], returns_list=True, raw_result=raw_result)

def update(engine, ref, source_environment=None):
    """
    Update the specified SourceEnvironment object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    :param source_environment: Payload object.
    :type source_environment: :py:class:`delphixpy.web.vo.SourceEnvironment`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s" % ref
    response = engine.post(url, source_environment.to_dict(dirty=True) if source_environment else None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

def delete(engine, ref):
    """
    Delete the specified SourceEnvironment object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s/delete" % ref
    response = engine.post(url, None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

def refresh(engine, ref):
    """
    Refreshes the given environment.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s/refresh" % ref
    response = engine.post(url, None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

def enable(engine, ref):
    """
    Enables the given environment. This is only applicable for disabled
    environments.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s/enable" % ref
    response = engine.post(url, None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

def disable(engine, ref):
    """
    Disables the given environment.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s/disable" % ref
    response = engine.post(url, None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

def nfs_checks(engine, ref, host_nfs_checks_parameters):
    """
    Tests that the environment user can run mount and unmount successfully on
    the host.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.SourceEnvironment.SourceEnvironment`
        object
    :type ref: ``str``
    :param host_nfs_checks_parameters: Payload object.
    :type host_nfs_checks_parameters:
        :py:class:`delphixpy.web.vo.HostNfsChecksParameters`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/environment/%s/nfsChecks" % ref
    response = engine.post(url, host_nfs_checks_parameters.to_dict(dirty=True) if host_nfs_checks_parameters else None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

