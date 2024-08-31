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
    from ...dyn.form.control_font_dialog import ControlFontDialog as ControlFontDialog
with suppress(ImportError):
    from ...dyn.form.data_aware_control_model import DataAwareControlModel as DataAwareControlModel
with suppress(ImportError):
    from ...dyn.form.data_selection_type import DataSelectionType as DataSelectionType
with suppress(ImportError):
    from ...dyn.form.database_delete_event import DatabaseDeleteEvent as DatabaseDeleteEvent
with suppress(ImportError):
    from ...dyn.form.database_parameter_event import DatabaseParameterEvent as DatabaseParameterEvent
with suppress(ImportError):
    from ...dyn.form.error_event import ErrorEvent as ErrorEvent
with suppress(ImportError):
    from ...dyn.form.form_button_type import FormButtonType as FormButtonType
with suppress(ImportError):
    from ...dyn.form.form_component import FormComponent as FormComponent
with suppress(ImportError):
    from ...dyn.form.form_component_type import FormComponentType as FormComponentType
with suppress(ImportError):
    from ...dyn.form.form_component_type import FormComponentTypeEnum as FormComponentTypeEnum
with suppress(ImportError):
    from ...dyn.form.form_components import FormComponents as FormComponents
with suppress(ImportError):
    from ...dyn.form.form_control_model import FormControlModel as FormControlModel
with suppress(ImportError):
    from ...dyn.form.form_controller import FormController as FormController
with suppress(ImportError):
    from ...dyn.form.form_controller_dispatcher import FormControllerDispatcher as FormControllerDispatcher
with suppress(ImportError):
    from ...dyn.form.form_submit_encoding import FormSubmitEncoding as FormSubmitEncoding
with suppress(ImportError):
    from ...dyn.form.form_submit_method import FormSubmitMethod as FormSubmitMethod
with suppress(ImportError):
    from ...dyn.form.forms import Forms as Forms
with suppress(ImportError):
    from ...dyn.form.list_source_type import ListSourceType as ListSourceType
with suppress(ImportError):
    from ...dyn.form.navigation_bar_mode import NavigationBarMode as NavigationBarMode
with suppress(ImportError):
    from ...dyn.form.property_browser_controller import PropertyBrowserController as PropertyBrowserController
with suppress(ImportError):
    from ...dyn.form.tab_order_dialog import TabOrderDialog as TabOrderDialog
with suppress(ImportError):
    from ...dyn.form.tabulator_cycle import TabulatorCycle as TabulatorCycle
with suppress(ImportError):
    from ...dyn.form.x_approve_action_broadcaster import XApproveActionBroadcaster as XApproveActionBroadcaster
with suppress(ImportError):
    from ...dyn.form.x_approve_action_listener import XApproveActionListener as XApproveActionListener
with suppress(ImportError):
    from ...dyn.form.x_bound_component import XBoundComponent as XBoundComponent
with suppress(ImportError):
    from ...dyn.form.x_bound_control import XBoundControl as XBoundControl
with suppress(ImportError):
    from ...dyn.form.x_change_broadcaster import XChangeBroadcaster as XChangeBroadcaster
with suppress(ImportError):
    from ...dyn.form.x_change_listener import XChangeListener as XChangeListener
with suppress(ImportError):
    from ...dyn.form.x_confirm_delete_broadcaster import XConfirmDeleteBroadcaster as XConfirmDeleteBroadcaster
with suppress(ImportError):
    from ...dyn.form.x_confirm_delete_listener import XConfirmDeleteListener as XConfirmDeleteListener
with suppress(ImportError):
    from ...dyn.form.x_database_parameter_broadcaster import XDatabaseParameterBroadcaster as XDatabaseParameterBroadcaster
with suppress(ImportError):
    from ...dyn.form.x_database_parameter_broadcaster2 import XDatabaseParameterBroadcaster2 as XDatabaseParameterBroadcaster2
with suppress(ImportError):
    from ...dyn.form.x_database_parameter_listener import XDatabaseParameterListener as XDatabaseParameterListener
with suppress(ImportError):
    from ...dyn.form.x_delete_listener import XDeleteListener as XDeleteListener
with suppress(ImportError):
    from ...dyn.form.x_error_broadcaster import XErrorBroadcaster as XErrorBroadcaster
with suppress(ImportError):
    from ...dyn.form.x_error_listener import XErrorListener as XErrorListener
with suppress(ImportError):
    from ...dyn.form.x_form import XForm as XForm
with suppress(ImportError):
    from ...dyn.form.x_form_component import XFormComponent as XFormComponent
with suppress(ImportError):
    from ...dyn.form.x_form_controller import XFormController as XFormController
with suppress(ImportError):
    from ...dyn.form.x_form_controller_listener import XFormControllerListener as XFormControllerListener
with suppress(ImportError):
    from ...dyn.form.x_forms import XForms as XForms
with suppress(ImportError):
    from ...dyn.form.x_forms_supplier import XFormsSupplier as XFormsSupplier
with suppress(ImportError):
    from ...dyn.form.x_forms_supplier2 import XFormsSupplier2 as XFormsSupplier2
with suppress(ImportError):
    from ...dyn.form.x_grid import XGrid as XGrid
with suppress(ImportError):
    from ...dyn.form.x_grid_column_factory import XGridColumnFactory as XGridColumnFactory
with suppress(ImportError):
    from ...dyn.form.x_grid_control import XGridControl as XGridControl
with suppress(ImportError):
    from ...dyn.form.x_grid_control_listener import XGridControlListener as XGridControlListener
with suppress(ImportError):
    from ...dyn.form.x_grid_field_data_supplier import XGridFieldDataSupplier as XGridFieldDataSupplier
with suppress(ImportError):
    from ...dyn.form.x_grid_peer import XGridPeer as XGridPeer
with suppress(ImportError):
    from ...dyn.form.x_image_producer_supplier import XImageProducerSupplier as XImageProducerSupplier
with suppress(ImportError):
    from ...dyn.form.x_insert_listener import XInsertListener as XInsertListener
with suppress(ImportError):
    from ...dyn.form.x_load_listener import XLoadListener as XLoadListener
with suppress(ImportError):
    from ...dyn.form.x_loadable import XLoadable as XLoadable
with suppress(ImportError):
    from ...dyn.form.x_positioning_listener import XPositioningListener as XPositioningListener
with suppress(ImportError):
    from ...dyn.form.x_reset import XReset as XReset
with suppress(ImportError):
    from ...dyn.form.x_reset_listener import XResetListener as XResetListener
with suppress(ImportError):
    from ...dyn.form.x_restore_listener import XRestoreListener as XRestoreListener
with suppress(ImportError):
    from ...dyn.form.x_submit import XSubmit as XSubmit
with suppress(ImportError):
    from ...dyn.form.x_submit_listener import XSubmitListener as XSubmitListener
with suppress(ImportError):
    from ...dyn.form.x_update_broadcaster import XUpdateBroadcaster as XUpdateBroadcaster
with suppress(ImportError):
    from ...dyn.form.x_update_listener import XUpdateListener as XUpdateListener
