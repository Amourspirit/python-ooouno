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
    from ....dyn.ui.dialogs.address_book_source_pilot import AddressBookSourcePilot as AddressBookSourcePilot
with suppress(ImportError):
    from ....dyn.ui.dialogs.common_file_picker_element_ids import CommonFilePickerElementIds as CommonFilePickerElementIds
with suppress(ImportError):
    from ....dyn.ui.dialogs.common_file_picker_element_ids import CommonFilePickerElementIdsEnum as CommonFilePickerElementIdsEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.control_actions import ControlActions as ControlActions
with suppress(ImportError):
    from ....dyn.ui.dialogs.control_actions import ControlActionsEnum as ControlActionsEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.dialog_closed_event import DialogClosedEvent as DialogClosedEvent
with suppress(ImportError):
    from ....dyn.ui.dialogs.executable_dialog_exception import ExecutableDialogException as ExecutableDialogException
with suppress(ImportError):
    from ....dyn.ui.dialogs.executable_dialog_results import ExecutableDialogResults as ExecutableDialogResults
with suppress(ImportError):
    from ....dyn.ui.dialogs.executable_dialog_results import ExecutableDialogResultsEnum as ExecutableDialogResultsEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.extended_file_picker_element_ids import ExtendedFilePickerElementIds as ExtendedFilePickerElementIds
with suppress(ImportError):
    from ....dyn.ui.dialogs.extended_file_picker_element_ids import ExtendedFilePickerElementIdsEnum as ExtendedFilePickerElementIdsEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.file_picker import FilePicker as FilePicker
with suppress(ImportError):
    from ....dyn.ui.dialogs.file_picker_event import FilePickerEvent as FilePickerEvent
with suppress(ImportError):
    from ....dyn.ui.dialogs.file_preview_image_formats import FilePreviewImageFormats as FilePreviewImageFormats
with suppress(ImportError):
    from ....dyn.ui.dialogs.file_preview_image_formats import FilePreviewImageFormatsEnum as FilePreviewImageFormatsEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.filter_options_dialog import FilterOptionsDialog as FilterOptionsDialog
with suppress(ImportError):
    from ....dyn.ui.dialogs.folder_picker import FolderPicker as FolderPicker
with suppress(ImportError):
    from ....dyn.ui.dialogs.listbox_control_actions import ListboxControlActions as ListboxControlActions
with suppress(ImportError):
    from ....dyn.ui.dialogs.listbox_control_actions import ListboxControlActionsEnum as ListboxControlActionsEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.template_description import TemplateDescription as TemplateDescription
with suppress(ImportError):
    from ....dyn.ui.dialogs.template_description import TemplateDescriptionEnum as TemplateDescriptionEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.wizard import Wizard as Wizard
with suppress(ImportError):
    from ....dyn.ui.dialogs.wizard_button import WizardButton as WizardButton
with suppress(ImportError):
    from ....dyn.ui.dialogs.wizard_button import WizardButtonEnum as WizardButtonEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.wizard_travel_type import WizardTravelType as WizardTravelType
with suppress(ImportError):
    from ....dyn.ui.dialogs.wizard_travel_type import WizardTravelTypeEnum as WizardTravelTypeEnum
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_asynchronous_executable_dialog import XAsynchronousExecutableDialog as XAsynchronousExecutableDialog
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_control_access import XControlAccess as XControlAccess
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_control_information import XControlInformation as XControlInformation
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_dialog_closed_listener import XDialogClosedListener as XDialogClosedListener
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_executable_dialog import XExecutableDialog as XExecutableDialog
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_picker import XFilePicker as XFilePicker
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_picker2 import XFilePicker2 as XFilePicker2
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_picker3 import XFilePicker3 as XFilePicker3
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_picker_control_access import XFilePickerControlAccess as XFilePickerControlAccess
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_picker_listener import XFilePickerListener as XFilePickerListener
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_picker_notifier import XFilePickerNotifier as XFilePickerNotifier
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_file_preview import XFilePreview as XFilePreview
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_filter_group_manager import XFilterGroupManager as XFilterGroupManager
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_filter_manager import XFilterManager as XFilterManager
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_folder_picker import XFolderPicker as XFolderPicker
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_folder_picker2 import XFolderPicker2 as XFolderPicker2
with suppress(ImportError):
    from ....dyn.ui.dialogs.xslt_filter_dialog import XSLTFilterDialog as XSLTFilterDialog
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_wizard import XWizard as XWizard
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_wizard_controller import XWizardController as XWizardController
with suppress(ImportError):
    from ....dyn.ui.dialogs.x_wizard_page import XWizardPage as XWizardPage
