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

import os.path
THIS_DIR = os.path.dirname(__file__)

try:
    with open(os.path.join(THIS_DIR, 'version.txt'), 'r') as f:
        version = f.read()
except:
    version = '0.0.0.0'

version_info = list(map(int, version.split('.')))
