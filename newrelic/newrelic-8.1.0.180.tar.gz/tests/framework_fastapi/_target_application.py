# Copyright 2010 New Relic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fastapi import FastAPI

from newrelic.api.transaction import current_transaction
from testing_support.asgi_testing import AsgiTest

app = FastAPI()


@app.get("/sync")
def sync():
    assert current_transaction() is not None
    return {}


@app.get("/async")
async def non_sync():
    assert current_transaction() is not None
    return {}


target_application = AsgiTest(app)
