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
    from ...dyn.inspection.default_help_provider import DefaultHelpProvider as DefaultHelpProvider
except ImportError:
    pass
try:
    from ...dyn.inspection.generic_property_handler import GenericPropertyHandler as GenericPropertyHandler
except ImportError:
    pass
try:
    from ...dyn.inspection.interactive_selection_result import InteractiveSelectionResult as InteractiveSelectionResult
except ImportError:
    pass
try:
    from ...dyn.inspection.line_descriptor import LineDescriptor as LineDescriptor
except ImportError:
    pass
try:
    from ...dyn.inspection.object_inspector import ObjectInspector as ObjectInspector
except ImportError:
    pass
try:
    from ...dyn.inspection.object_inspector_model import ObjectInspectorModel as ObjectInspectorModel
except ImportError:
    pass
try:
    from ...dyn.inspection.property_category_descriptor import PropertyCategoryDescriptor as PropertyCategoryDescriptor
except ImportError:
    pass
try:
    from ...dyn.inspection.property_control_type import PropertyControlType as PropertyControlType
except ImportError:
    pass
try:
    from ...dyn.inspection.property_control_type import PropertyControlTypeEnum as PropertyControlTypeEnum
except ImportError:
    pass
try:
    from ...dyn.inspection.property_line_element import PropertyLineElement as PropertyLineElement
except ImportError:
    pass
try:
    from ...dyn.inspection.property_line_element import PropertyLineElementEnum as PropertyLineElementEnum
except ImportError:
    pass
try:
    from ...dyn.inspection.string_representation import StringRepresentation as StringRepresentation
except ImportError:
    pass
try:
    from ...dyn.inspection.x_hyperlink_control import XHyperlinkControl as XHyperlinkControl
except ImportError:
    pass
try:
    from ...dyn.inspection.x_numeric_control import XNumericControl as XNumericControl
except ImportError:
    pass
try:
    from ...dyn.inspection.x_object_inspector import XObjectInspector as XObjectInspector
except ImportError:
    pass
try:
    from ...dyn.inspection.x_object_inspector_model import XObjectInspectorModel as XObjectInspectorModel
except ImportError:
    pass
try:
    from ...dyn.inspection.x_object_inspector_ui import XObjectInspectorUI as XObjectInspectorUI
except ImportError:
    pass
try:
    from ...dyn.inspection.x_property_control import XPropertyControl as XPropertyControl
except ImportError:
    pass
try:
    from ...dyn.inspection.x_property_control_context import XPropertyControlContext as XPropertyControlContext
except ImportError:
    pass
try:
    from ...dyn.inspection.x_property_control_factory import XPropertyControlFactory as XPropertyControlFactory
except ImportError:
    pass
try:
    from ...dyn.inspection.x_property_control_observer import XPropertyControlObserver as XPropertyControlObserver
except ImportError:
    pass
try:
    from ...dyn.inspection.x_property_handler import XPropertyHandler as XPropertyHandler
except ImportError:
    pass
try:
    from ...dyn.inspection.x_string_list_control import XStringListControl as XStringListControl
except ImportError:
    pass
try:
    from ...dyn.inspection.x_string_representation import XStringRepresentation as XStringRepresentation
except ImportError:
    pass
