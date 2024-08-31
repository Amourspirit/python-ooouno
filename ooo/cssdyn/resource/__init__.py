# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.resource.missing_resource_exception import MissingResourceException as MissingResourceException
with suppress(ImportError):
    from ...dyn.resource.string_resource import StringResource as StringResource
with suppress(ImportError):
    from ...dyn.resource.string_resource_with_location import StringResourceWithLocation as StringResourceWithLocation
with suppress(ImportError):
    from ...dyn.resource.string_resource_with_storage import StringResourceWithStorage as StringResourceWithStorage
with suppress(ImportError):
    from ...dyn.resource.x_string_resource_manager import XStringResourceManager as XStringResourceManager
with suppress(ImportError):
    from ...dyn.resource.x_string_resource_persistence import XStringResourcePersistence as XStringResourcePersistence
with suppress(ImportError):
    from ...dyn.resource.x_string_resource_resolver import XStringResourceResolver as XStringResourceResolver
with suppress(ImportError):
    from ...dyn.resource.x_string_resource_supplier import XStringResourceSupplier as XStringResourceSupplier
with suppress(ImportError):
    from ...dyn.resource.x_string_resource_with_location import XStringResourceWithLocation as XStringResourceWithLocation
with suppress(ImportError):
    from ...dyn.resource.x_string_resource_with_storage import XStringResourceWithStorage as XStringResourceWithStorage
