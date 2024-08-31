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
    from ...dyn.deployment.dependency_exception import DependencyException as DependencyException
with suppress(ImportError):
    from ...dyn.deployment.deployment_exception import DeploymentException as DeploymentException
with suppress(ImportError):
    from ...dyn.deployment.extension_manager import ExtensionManager as ExtensionManager
with suppress(ImportError):
    from ...dyn.deployment.extension_removed_exception import ExtensionRemovedException as ExtensionRemovedException
with suppress(ImportError):
    from ...dyn.deployment.install_exception import InstallException as InstallException
with suppress(ImportError):
    from ...dyn.deployment.invalid_removed_parameter_exception import InvalidRemovedParameterException as InvalidRemovedParameterException
with suppress(ImportError):
    from ...dyn.deployment.license_exception import LicenseException as LicenseException
with suppress(ImportError):
    from ...dyn.deployment.package_information_provider import PackageInformationProvider as PackageInformationProvider
with suppress(ImportError):
    from ...dyn.deployment.package_registry_backend import PackageRegistryBackend as PackageRegistryBackend
with suppress(ImportError):
    from ...dyn.deployment.platform_exception import PlatformException as PlatformException
with suppress(ImportError):
    from ...dyn.deployment.prerequisites import Prerequisites as Prerequisites
with suppress(ImportError):
    from ...dyn.deployment.prerequisites import PrerequisitesEnum as PrerequisitesEnum
with suppress(ImportError):
    from ...dyn.deployment.update_information_entry import UpdateInformationEntry as UpdateInformationEntry
with suppress(ImportError):
    from ...dyn.deployment.update_information_provider import UpdateInformationProvider as UpdateInformationProvider
with suppress(ImportError):
    from ...dyn.deployment.version_exception import VersionException as VersionException
with suppress(ImportError):
    from ...dyn.deployment.x_extension_manager import XExtensionManager as XExtensionManager
with suppress(ImportError):
    from ...dyn.deployment.x_package import XPackage as XPackage
with suppress(ImportError):
    from ...dyn.deployment.x_package_information_provider import XPackageInformationProvider as XPackageInformationProvider
with suppress(ImportError):
    from ...dyn.deployment.x_package_manager import XPackageManager as XPackageManager
with suppress(ImportError):
    from ...dyn.deployment.x_package_manager_factory import XPackageManagerFactory as XPackageManagerFactory
with suppress(ImportError):
    from ...dyn.deployment.x_package_registry import XPackageRegistry as XPackageRegistry
with suppress(ImportError):
    from ...dyn.deployment.x_package_type_info import XPackageTypeInfo as XPackageTypeInfo
with suppress(ImportError):
    from ...dyn.deployment.x_update_information_provider import XUpdateInformationProvider as XUpdateInformationProvider
with suppress(ImportError):
    from ...dyn.deployment.the_package_manager_factory import thePackageManagerFactory as thePackageManagerFactory
