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
    from ...dyn.accessibility.accessible import Accessible as Accessible
with suppress(ImportError):
    from ...dyn.accessibility.accessible_context import AccessibleContext as AccessibleContext
with suppress(ImportError):
    from ...dyn.accessibility.accessible_event_id import AccessibleEventId as AccessibleEventId
with suppress(ImportError):
    from ...dyn.accessibility.accessible_event_id import AccessibleEventIdEnum as AccessibleEventIdEnum
with suppress(ImportError):
    from ...dyn.accessibility.accessible_event_object import AccessibleEventObject as AccessibleEventObject
with suppress(ImportError):
    from ...dyn.accessibility.accessible_relation import AccessibleRelation as AccessibleRelation
with suppress(ImportError):
    from ...dyn.accessibility.accessible_relation_type import AccessibleRelationType as AccessibleRelationType
with suppress(ImportError):
    from ...dyn.accessibility.accessible_relation_type import AccessibleRelationTypeEnum as AccessibleRelationTypeEnum
with suppress(ImportError):
    from ...dyn.accessibility.accessible_role import AccessibleRole as AccessibleRole
with suppress(ImportError):
    from ...dyn.accessibility.accessible_role import AccessibleRoleEnum as AccessibleRoleEnum
with suppress(ImportError):
    from ...dyn.accessibility.accessible_scroll_type import AccessibleScrollType as AccessibleScrollType
with suppress(ImportError):
    from ...dyn.accessibility.accessible_state_type import AccessibleStateType as AccessibleStateType
with suppress(ImportError):
    from ...dyn.accessibility.accessible_state_type import AccessibleStateTypeEnum as AccessibleStateTypeEnum
with suppress(ImportError):
    from ...dyn.accessibility.accessible_table_model_change import AccessibleTableModelChange as AccessibleTableModelChange
with suppress(ImportError):
    from ...dyn.accessibility.accessible_table_model_change_type import AccessibleTableModelChangeType as AccessibleTableModelChangeType
with suppress(ImportError):
    from ...dyn.accessibility.accessible_table_model_change_type import AccessibleTableModelChangeTypeEnum as AccessibleTableModelChangeTypeEnum
with suppress(ImportError):
    from ...dyn.accessibility.accessible_text_type import AccessibleTextType as AccessibleTextType
with suppress(ImportError):
    from ...dyn.accessibility.accessible_text_type import AccessibleTextTypeEnum as AccessibleTextTypeEnum
with suppress(ImportError):
    from ...dyn.accessibility.illegal_accessible_component_state_exception import IllegalAccessibleComponentStateException as IllegalAccessibleComponentStateException
with suppress(ImportError):
    from ...dyn.accessibility.msaa_service import MSAAService as MSAAService
with suppress(ImportError):
    from ...dyn.accessibility.text_segment import TextSegment as TextSegment
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible import XAccessible as XAccessible
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_action import XAccessibleAction as XAccessibleAction
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_component import XAccessibleComponent as XAccessibleComponent
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_context import XAccessibleContext as XAccessibleContext
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_context2 import XAccessibleContext2 as XAccessibleContext2
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_context3 import XAccessibleContext3 as XAccessibleContext3
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_editable_text import XAccessibleEditableText as XAccessibleEditableText
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_event_broadcaster import XAccessibleEventBroadcaster as XAccessibleEventBroadcaster
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_event_listener import XAccessibleEventListener as XAccessibleEventListener
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_extended_attributes import XAccessibleExtendedAttributes as XAccessibleExtendedAttributes
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_extended_component import XAccessibleExtendedComponent as XAccessibleExtendedComponent
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_group_position import XAccessibleGroupPosition as XAccessibleGroupPosition
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_hyperlink import XAccessibleHyperlink as XAccessibleHyperlink
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_hypertext import XAccessibleHypertext as XAccessibleHypertext
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_image import XAccessibleImage as XAccessibleImage
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_key_binding import XAccessibleKeyBinding as XAccessibleKeyBinding
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_multi_line_text import XAccessibleMultiLineText as XAccessibleMultiLineText
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_relation_set import XAccessibleRelationSet as XAccessibleRelationSet
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_selection import XAccessibleSelection as XAccessibleSelection
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_state_set import XAccessibleStateSet as XAccessibleStateSet
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_table import XAccessibleTable as XAccessibleTable
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_table_selection import XAccessibleTableSelection as XAccessibleTableSelection
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_text import XAccessibleText as XAccessibleText
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_text_attributes import XAccessibleTextAttributes as XAccessibleTextAttributes
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_text_markup import XAccessibleTextMarkup as XAccessibleTextMarkup
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_text_selection import XAccessibleTextSelection as XAccessibleTextSelection
with suppress(ImportError):
    from ...dyn.accessibility.x_accessible_value import XAccessibleValue as XAccessibleValue
with suppress(ImportError):
    from ...dyn.accessibility.xmsaa_service import XMSAAService as XMSAAService
