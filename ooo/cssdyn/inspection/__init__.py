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
    from ...dyn.inspection.default_help_provider import DefaultHelpProvider as DefaultHelpProvider
with suppress(ImportError):
    from ...dyn.inspection.generic_property_handler import GenericPropertyHandler as GenericPropertyHandler
with suppress(ImportError):
    from ...dyn.inspection.interactive_selection_result import InteractiveSelectionResult as InteractiveSelectionResult
with suppress(ImportError):
    from ...dyn.inspection.line_descriptor import LineDescriptor as LineDescriptor
with suppress(ImportError):
    from ...dyn.inspection.object_inspector import ObjectInspector as ObjectInspector
with suppress(ImportError):
    from ...dyn.inspection.object_inspector_model import ObjectInspectorModel as ObjectInspectorModel
with suppress(ImportError):
    from ...dyn.inspection.property_category_descriptor import PropertyCategoryDescriptor as PropertyCategoryDescriptor
with suppress(ImportError):
    from ...dyn.inspection.property_control_type import PropertyControlType as PropertyControlType
with suppress(ImportError):
    from ...dyn.inspection.property_control_type import PropertyControlTypeEnum as PropertyControlTypeEnum
with suppress(ImportError):
    from ...dyn.inspection.property_line_element import PropertyLineElement as PropertyLineElement
with suppress(ImportError):
    from ...dyn.inspection.property_line_element import PropertyLineElementEnum as PropertyLineElementEnum
with suppress(ImportError):
    from ...dyn.inspection.string_representation import StringRepresentation as StringRepresentation
with suppress(ImportError):
    from ...dyn.inspection.x_hyperlink_control import XHyperlinkControl as XHyperlinkControl
with suppress(ImportError):
    from ...dyn.inspection.x_numeric_control import XNumericControl as XNumericControl
with suppress(ImportError):
    from ...dyn.inspection.x_object_inspector import XObjectInspector as XObjectInspector
with suppress(ImportError):
    from ...dyn.inspection.x_object_inspector_model import XObjectInspectorModel as XObjectInspectorModel
with suppress(ImportError):
    from ...dyn.inspection.x_object_inspector_ui import XObjectInspectorUI as XObjectInspectorUI
with suppress(ImportError):
    from ...dyn.inspection.x_property_control import XPropertyControl as XPropertyControl
with suppress(ImportError):
    from ...dyn.inspection.x_property_control_context import XPropertyControlContext as XPropertyControlContext
with suppress(ImportError):
    from ...dyn.inspection.x_property_control_factory import XPropertyControlFactory as XPropertyControlFactory
with suppress(ImportError):
    from ...dyn.inspection.x_property_control_observer import XPropertyControlObserver as XPropertyControlObserver
with suppress(ImportError):
    from ...dyn.inspection.x_property_handler import XPropertyHandler as XPropertyHandler
with suppress(ImportError):
    from ...dyn.inspection.x_string_list_control import XStringListControl as XStringListControl
with suppress(ImportError):
    from ...dyn.inspection.x_string_representation import XStringRepresentation as XStringRepresentation
