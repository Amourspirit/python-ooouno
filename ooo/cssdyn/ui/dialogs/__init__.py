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
    from ....dyn.ui.dialogs.address_book_source_pilot import AddressBookSourcePilot as AddressBookSourcePilot
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.common_file_picker_element_ids import CommonFilePickerElementIds as CommonFilePickerElementIds
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.common_file_picker_element_ids import CommonFilePickerElementIdsEnum as CommonFilePickerElementIdsEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.control_actions import ControlActions as ControlActions
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.control_actions import ControlActionsEnum as ControlActionsEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.dialog_closed_event import DialogClosedEvent as DialogClosedEvent
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.executable_dialog_exception import ExecutableDialogException as ExecutableDialogException
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.executable_dialog_results import ExecutableDialogResults as ExecutableDialogResults
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.executable_dialog_results import ExecutableDialogResultsEnum as ExecutableDialogResultsEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.extended_file_picker_element_ids import ExtendedFilePickerElementIds as ExtendedFilePickerElementIds
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.extended_file_picker_element_ids import ExtendedFilePickerElementIdsEnum as ExtendedFilePickerElementIdsEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.file_picker import FilePicker as FilePicker
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.file_picker_event import FilePickerEvent as FilePickerEvent
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.file_preview_image_formats import FilePreviewImageFormats as FilePreviewImageFormats
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.file_preview_image_formats import FilePreviewImageFormatsEnum as FilePreviewImageFormatsEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.filter_options_dialog import FilterOptionsDialog as FilterOptionsDialog
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.folder_picker import FolderPicker as FolderPicker
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.listbox_control_actions import ListboxControlActions as ListboxControlActions
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.listbox_control_actions import ListboxControlActionsEnum as ListboxControlActionsEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.template_description import TemplateDescription as TemplateDescription
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.template_description import TemplateDescriptionEnum as TemplateDescriptionEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.wizard import Wizard as Wizard
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.wizard_button import WizardButton as WizardButton
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.wizard_button import WizardButtonEnum as WizardButtonEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.wizard_travel_type import WizardTravelType as WizardTravelType
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.wizard_travel_type import WizardTravelTypeEnum as WizardTravelTypeEnum
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_asynchronous_executable_dialog import XAsynchronousExecutableDialog as XAsynchronousExecutableDialog
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_control_access import XControlAccess as XControlAccess
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_control_information import XControlInformation as XControlInformation
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_dialog_closed_listener import XDialogClosedListener as XDialogClosedListener
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_executable_dialog import XExecutableDialog as XExecutableDialog
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_picker import XFilePicker as XFilePicker
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_picker2 import XFilePicker2 as XFilePicker2
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_picker3 import XFilePicker3 as XFilePicker3
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_picker_control_access import XFilePickerControlAccess as XFilePickerControlAccess
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_picker_listener import XFilePickerListener as XFilePickerListener
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_picker_notifier import XFilePickerNotifier as XFilePickerNotifier
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_file_preview import XFilePreview as XFilePreview
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_filter_group_manager import XFilterGroupManager as XFilterGroupManager
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_filter_manager import XFilterManager as XFilterManager
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_folder_picker import XFolderPicker as XFolderPicker
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_folder_picker2 import XFolderPicker2 as XFolderPicker2
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.xslt_filter_dialog import XSLTFilterDialog as XSLTFilterDialog
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_wizard import XWizard as XWizard
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_wizard_controller import XWizardController as XWizardController
except ImportError:
    pass
try:
    from ....dyn.ui.dialogs.x_wizard_page import XWizardPage as XWizardPage
except ImportError:
    pass
