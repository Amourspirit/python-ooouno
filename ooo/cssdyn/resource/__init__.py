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
    from ...dyn.resource.missing_resource_exception import MissingResourceException as MissingResourceException
except ImportError:
    pass
try:
    from ...dyn.resource.string_resource import StringResource as StringResource
except ImportError:
    pass
try:
    from ...dyn.resource.string_resource_with_location import StringResourceWithLocation as StringResourceWithLocation
except ImportError:
    pass
try:
    from ...dyn.resource.string_resource_with_storage import StringResourceWithStorage as StringResourceWithStorage
except ImportError:
    pass
try:
    from ...dyn.resource.x_locale import XLocale as XLocale
except ImportError:
    pass
try:
    from ...dyn.resource.x_string_resource_manager import XStringResourceManager as XStringResourceManager
except ImportError:
    pass
try:
    from ...dyn.resource.x_string_resource_persistence import XStringResourcePersistence as XStringResourcePersistence
except ImportError:
    pass
try:
    from ...dyn.resource.x_string_resource_resolver import XStringResourceResolver as XStringResourceResolver
except ImportError:
    pass
try:
    from ...dyn.resource.x_string_resource_supplier import XStringResourceSupplier as XStringResourceSupplier
except ImportError:
    pass
try:
    from ...dyn.resource.x_string_resource_with_location import XStringResourceWithLocation as XStringResourceWithLocation
except ImportError:
    pass
try:
    from ...dyn.resource.x_string_resource_with_storage import XStringResourceWithStorage as XStringResourceWithStorage
except ImportError:
    pass
