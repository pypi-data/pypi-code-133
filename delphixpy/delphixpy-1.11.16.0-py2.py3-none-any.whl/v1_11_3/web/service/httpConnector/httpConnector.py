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
Package "service.httpConnector"
"""
API_VERSION = "1.11.3"

from delphixpy.v1_11_3 import response_validator

def get(engine):
    """
    Retrieve the specified HttpConnectorConfig object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.v1_11_3.delphix_engine.DelphixEngine`
    :rtype: :py:class:`v1_11_3.web.vo.HttpConnectorConfig`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/service/httpConnector"
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['HttpConnectorConfig'], returns_list=False, raw_result=raw_result)

def set(engine, http_connector_config=None):
    """
    Update the specified HttpConnectorConfig object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.v1_11_3.delphix_engine.DelphixEngine`
    :param http_connector_config: Payload object.
    :type http_connector_config: :py:class:`v1_11_3.web.vo.HttpConnectorConfig`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/service/httpConnector"
    response = engine.post(url, http_connector_config.to_dict(dirty=True) if http_connector_config else None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

