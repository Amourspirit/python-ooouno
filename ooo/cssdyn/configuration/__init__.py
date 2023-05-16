# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
    from ...dyn.configuration.access_root_element import AccessRootElement as AccessRootElement
with suppress(ImportError):
    from ...dyn.configuration.administration_provider import AdministrationProvider as AdministrationProvider
with suppress(ImportError):
    from ...dyn.configuration.cannot_load_configuration_exception import CannotLoadConfigurationException as CannotLoadConfigurationException
with suppress(ImportError):
    from ...dyn.configuration.configuration_access import ConfigurationAccess as ConfigurationAccess
with suppress(ImportError):
    from ...dyn.configuration.configuration_provider import ConfigurationProvider as ConfigurationProvider
with suppress(ImportError):
    from ...dyn.configuration.configuration_registry import ConfigurationRegistry as ConfigurationRegistry
with suppress(ImportError):
    from ...dyn.configuration.configuration_update_access import ConfigurationUpdateAccess as ConfigurationUpdateAccess
with suppress(ImportError):
    from ...dyn.configuration.corrupted_configuration_exception import CorruptedConfigurationException as CorruptedConfigurationException
with suppress(ImportError):
    from ...dyn.configuration.corrupted_ui_configuration_exception import CorruptedUIConfigurationException as CorruptedUIConfigurationException
with suppress(ImportError):
    from ...dyn.configuration.default_provider import DefaultProvider as DefaultProvider
with suppress(ImportError):
    from ...dyn.configuration.group_access import GroupAccess as GroupAccess
with suppress(ImportError):
    from ...dyn.configuration.group_element import GroupElement as GroupElement
with suppress(ImportError):
    from ...dyn.configuration.group_update import GroupUpdate as GroupUpdate
with suppress(ImportError):
    from ...dyn.configuration.hierarchy_access import HierarchyAccess as HierarchyAccess
with suppress(ImportError):
    from ...dyn.configuration.hierarchy_element import HierarchyElement as HierarchyElement
with suppress(ImportError):
    from ...dyn.configuration.installation_incomplete_exception import InstallationIncompleteException as InstallationIncompleteException
with suppress(ImportError):
    from ...dyn.configuration.invalid_bootstrap_file_exception import InvalidBootstrapFileException as InvalidBootstrapFileException
with suppress(ImportError):
    from ...dyn.configuration.missing_bootstrap_file_exception import MissingBootstrapFileException as MissingBootstrapFileException
with suppress(ImportError):
    from ...dyn.configuration.property_hierarchy import PropertyHierarchy as PropertyHierarchy
with suppress(ImportError):
    from ...dyn.configuration.read_only_access import ReadOnlyAccess as ReadOnlyAccess
with suppress(ImportError):
    from ...dyn.configuration.read_write_access import ReadWriteAccess as ReadWriteAccess
with suppress(ImportError):
    from ...dyn.configuration.set_access import SetAccess as SetAccess
with suppress(ImportError):
    from ...dyn.configuration.set_element import SetElement as SetElement
with suppress(ImportError):
    from ...dyn.configuration.set_update import SetUpdate as SetUpdate
with suppress(ImportError):
    from ...dyn.configuration.simple_set_access import SimpleSetAccess as SimpleSetAccess
with suppress(ImportError):
    from ...dyn.configuration.simple_set_update import SimpleSetUpdate as SimpleSetUpdate
with suppress(ImportError):
    from ...dyn.configuration.update import Update as Update
with suppress(ImportError):
    from ...dyn.configuration.update_root_element import UpdateRootElement as UpdateRootElement
with suppress(ImportError):
    from ...dyn.configuration.x_read_write_access import XReadWriteAccess as XReadWriteAccess
with suppress(ImportError):
    from ...dyn.configuration.x_template_container import XTemplateContainer as XTemplateContainer
with suppress(ImportError):
    from ...dyn.configuration.x_template_instance import XTemplateInstance as XTemplateInstance
with suppress(ImportError):
    from ...dyn.configuration.x_update import XUpdate as XUpdate
with suppress(ImportError):
    from ...dyn.configuration.the_default_provider import theDefaultProvider as theDefaultProvider
