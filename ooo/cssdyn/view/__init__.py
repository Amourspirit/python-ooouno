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
    from ...dyn.view.document_zoom_type import DocumentZoomType as DocumentZoomType
with suppress(ImportError):
    from ...dyn.view.document_zoom_type import DocumentZoomTypeEnum as DocumentZoomTypeEnum
with suppress(ImportError):
    from ...dyn.view.duplex_mode import DuplexMode as DuplexMode
with suppress(ImportError):
    from ...dyn.view.duplex_mode import DuplexModeEnum as DuplexModeEnum
with suppress(ImportError):
    from ...dyn.view.office_document_view import OfficeDocumentView as OfficeDocumentView
with suppress(ImportError):
    from ...dyn.view.paper_format import PaperFormat as PaperFormat
with suppress(ImportError):
    from ...dyn.view.paper_orientation import PaperOrientation as PaperOrientation
with suppress(ImportError):
    from ...dyn.view.print_job_event import PrintJobEvent as PrintJobEvent
with suppress(ImportError):
    from ...dyn.view.print_options import PrintOptions as PrintOptions
with suppress(ImportError):
    from ...dyn.view.print_settings import PrintSettings as PrintSettings
with suppress(ImportError):
    from ...dyn.view.printable_state import PrintableState as PrintableState
with suppress(ImportError):
    from ...dyn.view.printable_state_event import PrintableStateEvent as PrintableStateEvent
with suppress(ImportError):
    from ...dyn.view.printer_descriptor import PrinterDescriptor as PrinterDescriptor
with suppress(ImportError):
    from ...dyn.view.render_descriptor import RenderDescriptor as RenderDescriptor
with suppress(ImportError):
    from ...dyn.view.render_options import RenderOptions as RenderOptions
with suppress(ImportError):
    from ...dyn.view.selection_type import SelectionType as SelectionType
with suppress(ImportError):
    from ...dyn.view.view_settings import ViewSettings as ViewSettings
with suppress(ImportError):
    from ...dyn.view.x_control_access import XControlAccess as XControlAccess
with suppress(ImportError):
    from ...dyn.view.x_form_layer_access import XFormLayerAccess as XFormLayerAccess
with suppress(ImportError):
    from ...dyn.view.x_line_cursor import XLineCursor as XLineCursor
with suppress(ImportError):
    from ...dyn.view.x_multi_selection_supplier import XMultiSelectionSupplier as XMultiSelectionSupplier
with suppress(ImportError):
    from ...dyn.view.x_print_job import XPrintJob as XPrintJob
with suppress(ImportError):
    from ...dyn.view.x_print_job_broadcaster import XPrintJobBroadcaster as XPrintJobBroadcaster
with suppress(ImportError):
    from ...dyn.view.x_print_job_listener import XPrintJobListener as XPrintJobListener
with suppress(ImportError):
    from ...dyn.view.x_print_settings_supplier import XPrintSettingsSupplier as XPrintSettingsSupplier
with suppress(ImportError):
    from ...dyn.view.x_printable import XPrintable as XPrintable
with suppress(ImportError):
    from ...dyn.view.x_printable_broadcaster import XPrintableBroadcaster as XPrintableBroadcaster
with suppress(ImportError):
    from ...dyn.view.x_printable_listener import XPrintableListener as XPrintableListener
with suppress(ImportError):
    from ...dyn.view.x_renderable import XRenderable as XRenderable
with suppress(ImportError):
    from ...dyn.view.x_screen_cursor import XScreenCursor as XScreenCursor
with suppress(ImportError):
    from ...dyn.view.x_selection_change_listener import XSelectionChangeListener as XSelectionChangeListener
with suppress(ImportError):
    from ...dyn.view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier
with suppress(ImportError):
    from ...dyn.view.x_view_cursor import XViewCursor as XViewCursor
with suppress(ImportError):
    from ...dyn.view.x_view_settings_supplier import XViewSettingsSupplier as XViewSettingsSupplier
