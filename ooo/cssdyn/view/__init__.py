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
    from ...dyn.view.document_zoom_type import DocumentZoomType as DocumentZoomType
except ImportError:
    pass
try:
    from ...dyn.view.document_zoom_type import DocumentZoomTypeEnum as DocumentZoomTypeEnum
except ImportError:
    pass
try:
    from ...dyn.view.duplex_mode import DuplexMode as DuplexMode
except ImportError:
    pass
try:
    from ...dyn.view.duplex_mode import DuplexModeEnum as DuplexModeEnum
except ImportError:
    pass
try:
    from ...dyn.view.office_document_view import OfficeDocumentView as OfficeDocumentView
except ImportError:
    pass
try:
    from ...dyn.view.paper_format import PaperFormat as PaperFormat
except ImportError:
    pass
try:
    from ...dyn.view.paper_orientation import PaperOrientation as PaperOrientation
except ImportError:
    pass
try:
    from ...dyn.view.print_job_event import PrintJobEvent as PrintJobEvent
except ImportError:
    pass
try:
    from ...dyn.view.print_options import PrintOptions as PrintOptions
except ImportError:
    pass
try:
    from ...dyn.view.print_settings import PrintSettings as PrintSettings
except ImportError:
    pass
try:
    from ...dyn.view.printable_state import PrintableState as PrintableState
except ImportError:
    pass
try:
    from ...dyn.view.printable_state_event import PrintableStateEvent as PrintableStateEvent
except ImportError:
    pass
try:
    from ...dyn.view.printer_descriptor import PrinterDescriptor as PrinterDescriptor
except ImportError:
    pass
try:
    from ...dyn.view.render_descriptor import RenderDescriptor as RenderDescriptor
except ImportError:
    pass
try:
    from ...dyn.view.render_options import RenderOptions as RenderOptions
except ImportError:
    pass
try:
    from ...dyn.view.selection_type import SelectionType as SelectionType
except ImportError:
    pass
try:
    from ...dyn.view.view_settings import ViewSettings as ViewSettings
except ImportError:
    pass
try:
    from ...dyn.view.x_control_access import XControlAccess as XControlAccess
except ImportError:
    pass
try:
    from ...dyn.view.x_form_layer_access import XFormLayerAccess as XFormLayerAccess
except ImportError:
    pass
try:
    from ...dyn.view.x_line_cursor import XLineCursor as XLineCursor
except ImportError:
    pass
try:
    from ...dyn.view.x_multi_selection_supplier import XMultiSelectionSupplier as XMultiSelectionSupplier
except ImportError:
    pass
try:
    from ...dyn.view.x_print_job import XPrintJob as XPrintJob
except ImportError:
    pass
try:
    from ...dyn.view.x_print_job_broadcaster import XPrintJobBroadcaster as XPrintJobBroadcaster
except ImportError:
    pass
try:
    from ...dyn.view.x_print_job_listener import XPrintJobListener as XPrintJobListener
except ImportError:
    pass
try:
    from ...dyn.view.x_print_settings_supplier import XPrintSettingsSupplier as XPrintSettingsSupplier
except ImportError:
    pass
try:
    from ...dyn.view.x_printable import XPrintable as XPrintable
except ImportError:
    pass
try:
    from ...dyn.view.x_printable_broadcaster import XPrintableBroadcaster as XPrintableBroadcaster
except ImportError:
    pass
try:
    from ...dyn.view.x_printable_listener import XPrintableListener as XPrintableListener
except ImportError:
    pass
try:
    from ...dyn.view.x_renderable import XRenderable as XRenderable
except ImportError:
    pass
try:
    from ...dyn.view.x_screen_cursor import XScreenCursor as XScreenCursor
except ImportError:
    pass
try:
    from ...dyn.view.x_selection_change_listener import XSelectionChangeListener as XSelectionChangeListener
except ImportError:
    pass
try:
    from ...dyn.view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier
except ImportError:
    pass
try:
    from ...dyn.view.x_view_cursor import XViewCursor as XViewCursor
except ImportError:
    pass
try:
    from ...dyn.view.x_view_settings_supplier import XViewSettingsSupplier as XViewSettingsSupplier
except ImportError:
    pass
