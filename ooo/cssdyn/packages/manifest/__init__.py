# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ....dyn.packages.manifest.manifest_reader import ManifestReader as ManifestReader
except ImportError:
    pass
try:
    from ....dyn.packages.manifest.manifest_writer import ManifestWriter as ManifestWriter
except ImportError:
    pass
try:
    from ....dyn.packages.manifest.x_manifest_reader import XManifestReader as XManifestReader
except ImportError:
    pass
try:
    from ....dyn.packages.manifest.x_manifest_writer import XManifestWriter as XManifestWriter
except ImportError:
    pass
