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
    from ...dyn.accessibility.accessible import Accessible as Accessible
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_context import AccessibleContext as AccessibleContext
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_event_id import AccessibleEventId as AccessibleEventId
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_event_id import AccessibleEventIdEnum as AccessibleEventIdEnum
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_event_object import AccessibleEventObject as AccessibleEventObject
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_relation import AccessibleRelation as AccessibleRelation
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_relation_type import AccessibleRelationType as AccessibleRelationType
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_relation_type import AccessibleRelationTypeEnum as AccessibleRelationTypeEnum
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_role import AccessibleRole as AccessibleRole
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_role import AccessibleRoleEnum as AccessibleRoleEnum
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_scroll_type import AccessibleScrollType as AccessibleScrollType
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_state_type import AccessibleStateType as AccessibleStateType
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_state_type import AccessibleStateTypeEnum as AccessibleStateTypeEnum
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_table_model_change import AccessibleTableModelChange as AccessibleTableModelChange
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_table_model_change_type import AccessibleTableModelChangeType as AccessibleTableModelChangeType
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_table_model_change_type import AccessibleTableModelChangeTypeEnum as AccessibleTableModelChangeTypeEnum
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_text_type import AccessibleTextType as AccessibleTextType
except ImportError:
    pass
try:
    from ...dyn.accessibility.accessible_text_type import AccessibleTextTypeEnum as AccessibleTextTypeEnum
except ImportError:
    pass
try:
    from ...dyn.accessibility.illegal_accessible_component_state_exception import IllegalAccessibleComponentStateException as IllegalAccessibleComponentStateException
except ImportError:
    pass
try:
    from ...dyn.accessibility.msaa_service import MSAAService as MSAAService
except ImportError:
    pass
try:
    from ...dyn.accessibility.text_segment import TextSegment as TextSegment
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible import XAccessible as XAccessible
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_action import XAccessibleAction as XAccessibleAction
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_component import XAccessibleComponent as XAccessibleComponent
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_context import XAccessibleContext as XAccessibleContext
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_context2 import XAccessibleContext2 as XAccessibleContext2
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_context3 import XAccessibleContext3 as XAccessibleContext3
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_editable_text import XAccessibleEditableText as XAccessibleEditableText
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_event_broadcaster import XAccessibleEventBroadcaster as XAccessibleEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_event_listener import XAccessibleEventListener as XAccessibleEventListener
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_extended_attributes import XAccessibleExtendedAttributes as XAccessibleExtendedAttributes
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_extended_component import XAccessibleExtendedComponent as XAccessibleExtendedComponent
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_group_position import XAccessibleGroupPosition as XAccessibleGroupPosition
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_hyperlink import XAccessibleHyperlink as XAccessibleHyperlink
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_hypertext import XAccessibleHypertext as XAccessibleHypertext
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_image import XAccessibleImage as XAccessibleImage
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_key_binding import XAccessibleKeyBinding as XAccessibleKeyBinding
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_multi_line_text import XAccessibleMultiLineText as XAccessibleMultiLineText
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_relation_set import XAccessibleRelationSet as XAccessibleRelationSet
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_selection import XAccessibleSelection as XAccessibleSelection
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_state_set import XAccessibleStateSet as XAccessibleStateSet
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_table import XAccessibleTable as XAccessibleTable
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_table_selection import XAccessibleTableSelection as XAccessibleTableSelection
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_text import XAccessibleText as XAccessibleText
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_text_attributes import XAccessibleTextAttributes as XAccessibleTextAttributes
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_text_markup import XAccessibleTextMarkup as XAccessibleTextMarkup
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_text_selection import XAccessibleTextSelection as XAccessibleTextSelection
except ImportError:
    pass
try:
    from ...dyn.accessibility.x_accessible_value import XAccessibleValue as XAccessibleValue
except ImportError:
    pass
try:
    from ...dyn.accessibility.xmsaa_service import XMSAAService as XMSAAService
except ImportError:
    pass
