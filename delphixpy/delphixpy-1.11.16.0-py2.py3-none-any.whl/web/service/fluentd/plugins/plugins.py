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
Package "service.fluentd.plugins"
"""
API_VERSION = "1.11.16"

from delphixpy import response_validator

def get(engine, ref):
    """
    Retrieve the specified FluentdPlugin object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.FluentdPlugin.FluentdPlugin` object
    :type ref: ``str``
    :rtype: :py:class:`delphixpy.web.vo.FluentdPlugin`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/service/fluentd/plugins/%s" % ref
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['FluentdPlugin'], returns_list=False, raw_result=raw_result)

def get_all(engine):
    """
    List FluentdPlugin objects on the system.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :rtype: ``list`` of :py:class:`delphixpy.web.vo.FluentdPlugin`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/service/fluentd/plugins"
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['FluentdPlugin'], returns_list=True, raw_result=raw_result)

def delete(engine, ref):
    """
    Delete the specified FluentdPlugin object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.web.objects.FluentdPlugin.FluentdPlugin` object
    :type ref: ``str``
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/service/fluentd/plugins/%s/delete" % ref
    response = engine.post(url, None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

def request_upload_token(engine):
    """
    Request fluentd plugin upload token.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.delphix_engine.DelphixEngine`
    :rtype: :py:class:`delphixpy.web.vo.FileUploadResult`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/service/fluentd/plugins/requestUploadToken"
    response = engine.post(url, None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['FileUploadResult'], returns_list=False, raw_result=raw_result)

