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
    from ...dyn.style.break_type import BreakType as BreakType
with suppress(ImportError):
    from ...dyn.style.case_map import CaseMap as CaseMap
with suppress(ImportError):
    from ...dyn.style.case_map import CaseMapEnum as CaseMapEnum
with suppress(ImportError):
    from ...dyn.style.cell_style import CellStyle as CellStyle
with suppress(ImportError):
    from ...dyn.style.character_properties import CharacterProperties as CharacterProperties
with suppress(ImportError):
    from ...dyn.style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian
with suppress(ImportError):
    from ...dyn.style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex
with suppress(ImportError):
    from ...dyn.style.character_style import CharacterStyle as CharacterStyle
with suppress(ImportError):
    from ...dyn.style.drop_cap_format import DropCapFormat as DropCapFormat
with suppress(ImportError):
    from ...dyn.style.footnote_line_style import FootnoteLineStyle as FootnoteLineStyle
with suppress(ImportError):
    from ...dyn.style.footnote_line_style import FootnoteLineStyleEnum as FootnoteLineStyleEnum
with suppress(ImportError):
    from ...dyn.style.graphic_location import GraphicLocation as GraphicLocation
with suppress(ImportError):
    from ...dyn.style.horizontal_alignment import HorizontalAlignment as HorizontalAlignment
with suppress(ImportError):
    from ...dyn.style.line_number_position import LineNumberPosition as LineNumberPosition
with suppress(ImportError):
    from ...dyn.style.line_number_position import LineNumberPositionEnum as LineNumberPositionEnum
with suppress(ImportError):
    from ...dyn.style.line_spacing import LineSpacing as LineSpacing
with suppress(ImportError):
    from ...dyn.style.line_spacing_mode import LineSpacingMode as LineSpacingMode
with suppress(ImportError):
    from ...dyn.style.line_spacing_mode import LineSpacingModeEnum as LineSpacingModeEnum
with suppress(ImportError):
    from ...dyn.style.numbering_alignment import NumberingAlignment as NumberingAlignment
with suppress(ImportError):
    from ...dyn.style.numbering_level import NumberingLevel as NumberingLevel
with suppress(ImportError):
    from ...dyn.style.numbering_rule import NumberingRule as NumberingRule
with suppress(ImportError):
    from ...dyn.style.numbering_type import NumberingType as NumberingType
with suppress(ImportError):
    from ...dyn.style.numbering_type import NumberingTypeEnum as NumberingTypeEnum
with suppress(ImportError):
    from ...dyn.style.page_properties import PageProperties as PageProperties
with suppress(ImportError):
    from ...dyn.style.page_style import PageStyle as PageStyle
with suppress(ImportError):
    from ...dyn.style.page_style_layout import PageStyleLayout as PageStyleLayout
with suppress(ImportError):
    from ...dyn.style.paragraph_adjust import ParagraphAdjust as ParagraphAdjust
with suppress(ImportError):
    from ...dyn.style.paragraph_properties import ParagraphProperties as ParagraphProperties
with suppress(ImportError):
    from ...dyn.style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian
with suppress(ImportError):
    from ...dyn.style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex
with suppress(ImportError):
    from ...dyn.style.paragraph_style import ParagraphStyle as ParagraphStyle
with suppress(ImportError):
    from ...dyn.style.paragraph_style_category import ParagraphStyleCategory as ParagraphStyleCategory
with suppress(ImportError):
    from ...dyn.style.paragraph_style_category import ParagraphStyleCategoryEnum as ParagraphStyleCategoryEnum
with suppress(ImportError):
    from ...dyn.style.style import Style as Style
with suppress(ImportError):
    from ...dyn.style.style_families import StyleFamilies as StyleFamilies
with suppress(ImportError):
    from ...dyn.style.style_family import StyleFamily as StyleFamily
with suppress(ImportError):
    from ...dyn.style.tab_align import TabAlign as TabAlign
with suppress(ImportError):
    from ...dyn.style.tab_stop import TabStop as TabStop
with suppress(ImportError):
    from ...dyn.style.vertical_alignment import VerticalAlignment as VerticalAlignment
with suppress(ImportError):
    from ...dyn.style.x_auto_style import XAutoStyle as XAutoStyle
with suppress(ImportError):
    from ...dyn.style.x_auto_style_family import XAutoStyleFamily as XAutoStyleFamily
with suppress(ImportError):
    from ...dyn.style.x_auto_styles import XAutoStyles as XAutoStyles
with suppress(ImportError):
    from ...dyn.style.x_auto_styles_supplier import XAutoStylesSupplier as XAutoStylesSupplier
with suppress(ImportError):
    from ...dyn.style.x_defaults_supplier import XDefaultsSupplier as XDefaultsSupplier
with suppress(ImportError):
    from ...dyn.style.x_style import XStyle as XStyle
with suppress(ImportError):
    from ...dyn.style.x_style_families_supplier import XStyleFamiliesSupplier as XStyleFamiliesSupplier
with suppress(ImportError):
    from ...dyn.style.x_style_loader import XStyleLoader as XStyleLoader
with suppress(ImportError):
    from ...dyn.style.x_style_loader2 import XStyleLoader2 as XStyleLoader2
with suppress(ImportError):
    from ...dyn.style.x_style_supplier import XStyleSupplier as XStyleSupplier
