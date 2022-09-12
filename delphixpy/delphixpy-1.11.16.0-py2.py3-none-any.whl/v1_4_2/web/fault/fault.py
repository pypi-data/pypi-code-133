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
Package "fault"
"""
API_VERSION = "1.4.2"

from delphixpy.v1_4_2.web.fault import effect
try:
    from urllib import urlencode 
except ImportError:
    from urllib.parse import urlencode 
from delphixpy.v1_4_2 import response_validator

def get(engine, ref):
    """
    Retrieve the specified Fault object.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.v1_4_2.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.v1_4_2.web.objects.Fault.Fault` object
    :type ref: ``str``
    :rtype: :py:class:`v1_4_2.web.vo.Fault`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/fault/%s" % ref
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['Fault'], returns_list=False, raw_result=raw_result)

def get_all(engine, from_date=None, max_total=None, page_offset=None, page_size=None, severity=None, status=None, target=None, to_date=None):
    """
    Returns the list of all the faults that match the given criteria.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.v1_4_2.delphix_engine.DelphixEngine`
    :param from_date: Start date to use for the search.
    :type from_date: ``TEXT_TYPE``
    :param max_total: The upper bound for calculation of total alert count.
    :type max_total: ``int``
    :param page_offset: Offset within fault list, in units of pageSize chunks.
    :type page_offset: ``int``
    :param page_size: Limit the number of faults returned.
    :type page_size: ``int``
    :param severity: The impact of the fault on the system: CRITICAL or
        WARNING. *(permitted values: CRITICAL, WARNING)*
    :type severity: ``TEXT_TYPE``
    :param status: The status of the fault: ACTIVE or RESOLVED. *(permitted
        values: ACTIVE, RESOLVED)*
    :type status: ``TEXT_TYPE``
    :param target: The reference to the Delphix user-visible object associated
        with the fault.
    :type target: ``TEXT_TYPE``
    :param to_date: End date to use for the search.
    :type to_date: ``TEXT_TYPE``
    :rtype: ``list`` of :py:class:`v1_4_2.web.vo.Fault`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/fault"
    query_params = {"fromDate": from_date, "maxTotal": max_total, "pageOffset": page_offset, "pageSize": page_size, "severity": severity, "status": status, "target": target, "toDate": to_date}
    query_dct = {k: query_params[k] for k in query_params if query_params[k] is not None}
    if query_dct:
        url_params = urlencode(query_dct)
        url += "?%s" % url_params
    response = engine.get(url)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=['Fault'], returns_list=True, raw_result=raw_result)

def resolve(engine, ref, fault_resolve_parameters):
    """
    Marks the fault as resolved.

    :param engine: The Delphix Engine
    :type engine: :py:class:`delphixpy.v1_4_2.delphix_engine.DelphixEngine`
    :param ref: Reference to a
        :py:class:`delphixpy.v1_4_2.web.objects.Fault.Fault` object
    :type ref: ``str``
    :param fault_resolve_parameters: Payload object.
    :type fault_resolve_parameters:
        :py:class:`v1_4_2.web.vo.FaultResolveParameters`
    """
    assert API_VERSION == engine.API_VERSION, "Wrong API version (%s) for parameter 'engine' (%s)" % (API_VERSION, engine.API_VERSION)
    url = "/resources/json/delphix/fault/%s/resolve" % ref
    response = engine.post(url, fault_resolve_parameters.to_dict(dirty=True) if fault_resolve_parameters else None)
    result = response_validator.validate(response, engine)
    raw_result = getattr(engine, 'raw_result', False)
    return response_validator.parse_result(result, undef_enabled=True, return_types=None, returns_list=None, raw_result=raw_result)

