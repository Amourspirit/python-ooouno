"""
Test Single Instances of ooo_lib

These test require being run in uno envrionment.

This file is meant to be included in a sticky file that is run inside LO as a macro

Import could optionally be placed in each method.
Placing all imports at the top of the document is by design.
With import at top of document that can be imported in a LO python terminal instance.
For example:
>>> from ooo.dyn.frame.the_desktop import theDesktop
>>> ob = theDesktop()
"""
import unittest
from ooo.dyn.task.office_restart_manager import OfficeRestartManager
from ooo.dyn.task.the_job_executor import theJobExecutor
from ooo.dyn.sdb.data_access_descriptor_factory import DataAccessDescriptorFactory
from ooo.dyn.configuration.the_default_provider import theDefaultProvider
from ooo.dyn.configuration.update import Update
from ooo.dyn.reflection.the_core_reflection import theCoreReflection
from ooo.dyn.deployment.the_package_manager_factory import thePackageManagerFactory
from ooo.dyn.deployment.extension_manager import ExtensionManager
from ooo.dyn.deployment.package_information_provider import PackageInformationProvider
from ooo.dyn.util.the_path_settings import thePathSettings
from ooo.dyn.util.the_macro_expander import theMacroExpander
from ooo.dyn.util.the_office_installation_directories import (
    theOfficeInstallationDirectories,
)
from ooo.dyn.beans.the_introspection import theIntrospection
from ooo.dyn.ui.the_module_ui_configuration_manager_supplier import (
    theModuleUIConfigurationManagerSupplier,
)
from ooo.dyn.ui.the_ui_category_description import theUICategoryDescription
from ooo.dyn.ui.the_ui_element_factory_manager import theUIElementFactoryManager
from ooo.dyn.ui.the_window_content_factory_manager import theWindowContentFactoryManager
from ooo.dyn.ui.context_change_event_multiplexer import ContextChangeEventMultiplexer
from ooo.dyn.ui.the_window_state_configuration import theWindowStateConfiguration
from ooo.dyn.script.the_service_documenter import theServiceDocumenter
from ooo.dyn.script.provider.the_master_script_provider_factory import (
    theMasterScriptProviderFactory,
)
from ooo.dyn.script.browse.the_browse_node_factory import theBrowseNodeFactory
from ooo.dyn.frame.the_toolbar_controller_factory import theToolbarControllerFactory
from ooo.dyn.frame.the_global_event_broadcaster import theGlobalEventBroadcaster
from ooo.dyn.frame.the_ui_command_description import theUICommandDescription
from ooo.dyn.frame.the_popup_menu_controller_factory import (
    thePopupMenuControllerFactory,
)
from ooo.dyn.frame.the_auto_recovery import theAutoRecovery
from ooo.dyn.frame.the_statusbar_controller_factory import theStatusbarControllerFactory
from ooo.dyn.frame.the_desktop import theDesktop
from ooo.dyn.logging.logger_pool import LoggerPool


class TestSingleton(unittest.TestCase):

    def test_office_restart_manager(self):
        singleton = OfficeRestartManager()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.task.OfficeRestartManager"
        assert singleton.getImplementationName() == im_name

    def test_the_job_executor(self):
        singleton = theJobExecutor()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.JobExecutor"
        assert singleton.getImplementationName() == im_name

    def test_data_access_descriptor_factory(self):
        singleton = DataAccessDescriptorFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.dba.DataAccessDescriptorFactory"
        assert singleton.getImplementationName() == im_name

    def test_the_default_provider(self):
        singleton = theDefaultProvider()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.configuration.DefaultProvider"
        assert singleton.getImplementationName() == im_name

    def test_update(self):
        singleton = Update()
        assert type(singleton).__name__ == "pyuno"
        assert hasattr(singleton, "insertExtensionXcsFile")

    def test_the_core_reflection(self):
        singleton = theCoreReflection()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.stoc.CoreReflection"
        assert singleton.getImplementationName() == im_name

    def test_the_package_manager_factory(self):
        singleton = thePackageManagerFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.deployment.PackageManagerFactory"
        assert singleton.getImplementationName() == im_name

    def test_extension_manager(self):
        singleton = ExtensionManager()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.deployment.ExtensionManager"
        assert singleton.getImplementationName() == im_name

    def test_package_information_provider(self):
        singleton = PackageInformationProvider()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.deployment.PackageInformationProvider"
        assert singleton.getImplementationName() == im_name

    def test_the_path_settings(self):
        singleton = thePathSettings()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.PathSettings"
        assert singleton.getImplementationName() == im_name

    def test_the_macro_expander(self):
        singleton = theMacroExpander()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.lang.comp.cppuhelper.BootstrapMacroExpander"
        assert singleton.getImplementationName() == im_name

        def expandUri(uri):
            if uri.startswith("vnd.sun.star.expand:"):
                uri = uri.replace("vnd.sun.star.expand:", "", 1)
                uri = singleton.expandMacros(uri)
            return uri

        result = expandUri("vnd.sun.star.expand:somevalue")
        assert result == "somevalue"

    def test_the_office_installation_directories(self):
        singleton = theOfficeInstallationDirectories()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.util.OfficeInstallationDirectories"
        assert singleton.getImplementationName() == im_name

    def test_the_introspection(self):
        singleton = theIntrospection()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.stoc.Introspection"
        assert singleton.getImplementationName() == im_name

    def test_the_module_ui_configuration_manager_supplier(self):
        singleton = theModuleUIConfigurationManagerSupplier()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.ModuleUIConfigurationManagerSupplier"
        assert singleton.getImplementationName() == im_name

    def test_the_ui_category_description(self):
        singleton = theUICategoryDescription()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.UICategoryDescription"
        assert singleton.getImplementationName() == im_name

    def test_the_ui_element_factory_manager(self):
        singleton = theUIElementFactoryManager()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.UIElementFactoryManager"
        assert singleton.getImplementationName() == im_name

    def test_the_window_content_factory_manager(self):
        singleton = theWindowContentFactoryManager()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.WindowContentFactoryManager"
        assert singleton.getImplementationName() == im_name

    def test_context_change_event_multiplexer(self):
        singleton = ContextChangeEventMultiplexer()
        assert type(singleton).__name__ == "pyuno"
        im_name = "org.apache.openoffice.comp.framework.ContextChangeEventMultiplexer"
        assert singleton.getImplementationName() == im_name

    def test_the_window_state_configuration(self):
        singleton = theWindowStateConfiguration()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.WindowStateConfiguration"
        assert singleton.getImplementationName() == im_name

    def test_the_service_documenter(self):
        singleton = theServiceDocumenter()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.unotools.misc.ServiceDocumenter"
        assert singleton.getImplementationName() == im_name
        assert (
            "com.sun.star.script.ServiceDocumenter" in singleton.SupportedServiceNames
        )

    def test_the_master_script_provider_factory(self):
        singleton = theMasterScriptProviderFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.script.provider.MasterScriptProviderFactory"
        assert singleton.getImplementationName() == im_name

    def test_the_browse_node_factory(self):
        singleton = theBrowseNodeFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.script.browse.BrowseNodeFactory"
        assert singleton.getImplementationName() == im_name

    def test_the_toolbar_controller_factory(self):
        singleton = theToolbarControllerFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.ToolBarControllerFactory"
        assert singleton.getImplementationName() == im_name

    def test_the_global_event_broadcaster(self):
        singleton = theGlobalEventBroadcaster()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.sfx2.GlobalEventBroadcaster"
        assert singleton.getImplementationName() == im_name

    def test_the_ui_command_description(self):
        singleton = theUICommandDescription()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.UICommandDescription"
        assert singleton.getImplementationName() == im_name

    def test_the_popup_menu_controller_factory(self):
        singleton = thePopupMenuControllerFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.PopupMenuControllerFactory"
        assert singleton.getImplementationName() == im_name

    def test_the_auto_recovery(self):
        singleton = theAutoRecovery()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.AutoRecovery"
        assert singleton.getImplementationName() == im_name

    def test_the_statusbar_controller_factory(self):
        singleton = theStatusbarControllerFactory()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.StatusBarControllerFactory"
        assert singleton.getImplementationName() == im_name

    def test_the_desktop(self):
        singleton = theDesktop()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.framework.Desktop"
        assert singleton.getImplementationName() == im_name

    def test_logger_pool(self):
        singleton = LoggerPool()
        assert type(singleton).__name__ == "pyuno"
        im_name = "com.sun.star.comp.extensions.LoggerPool"
        assert singleton.getImplementationName() == im_name
