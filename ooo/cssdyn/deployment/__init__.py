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
    from ...dyn.deployment.dependency_exception import DependencyException as DependencyException
except ImportError:
    pass
try:
    from ...dyn.deployment.deployment_exception import DeploymentException as DeploymentException
except ImportError:
    pass
try:
    from ...dyn.deployment.extension_manager import ExtensionManager as ExtensionManager
except ImportError:
    pass
try:
    from ...dyn.deployment.extension_removed_exception import ExtensionRemovedException as ExtensionRemovedException
except ImportError:
    pass
try:
    from ...dyn.deployment.install_exception import InstallException as InstallException
except ImportError:
    pass
try:
    from ...dyn.deployment.invalid_removed_parameter_exception import InvalidRemovedParameterException as InvalidRemovedParameterException
except ImportError:
    pass
try:
    from ...dyn.deployment.license_exception import LicenseException as LicenseException
except ImportError:
    pass
try:
    from ...dyn.deployment.package_information_provider import PackageInformationProvider as PackageInformationProvider
except ImportError:
    pass
try:
    from ...dyn.deployment.package_registry_backend import PackageRegistryBackend as PackageRegistryBackend
except ImportError:
    pass
try:
    from ...dyn.deployment.platform_exception import PlatformException as PlatformException
except ImportError:
    pass
try:
    from ...dyn.deployment.prerequisites import Prerequisites as Prerequisites
except ImportError:
    pass
try:
    from ...dyn.deployment.prerequisites import PrerequisitesEnum as PrerequisitesEnum
except ImportError:
    pass
try:
    from ...dyn.deployment.update_information_entry import UpdateInformationEntry as UpdateInformationEntry
except ImportError:
    pass
try:
    from ...dyn.deployment.update_information_provider import UpdateInformationProvider as UpdateInformationProvider
except ImportError:
    pass
try:
    from ...dyn.deployment.version_exception import VersionException as VersionException
except ImportError:
    pass
try:
    from ...dyn.deployment.x_extension_manager import XExtensionManager as XExtensionManager
except ImportError:
    pass
try:
    from ...dyn.deployment.x_package import XPackage as XPackage
except ImportError:
    pass
try:
    from ...dyn.deployment.x_package_information_provider import XPackageInformationProvider as XPackageInformationProvider
except ImportError:
    pass
try:
    from ...dyn.deployment.x_package_manager import XPackageManager as XPackageManager
except ImportError:
    pass
try:
    from ...dyn.deployment.x_package_manager_factory import XPackageManagerFactory as XPackageManagerFactory
except ImportError:
    pass
try:
    from ...dyn.deployment.x_package_registry import XPackageRegistry as XPackageRegistry
except ImportError:
    pass
try:
    from ...dyn.deployment.x_package_type_info import XPackageTypeInfo as XPackageTypeInfo
except ImportError:
    pass
try:
    from ...dyn.deployment.x_update_information_provider import XUpdateInformationProvider as XUpdateInformationProvider
except ImportError:
    pass
try:
    from ...dyn.deployment.the_package_manager_factory import thePackageManagerFactory as thePackageManagerFactory
except ImportError:
    pass
