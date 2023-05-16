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
    from ...dyn.text.accessible_endnote_view import AccessibleEndnoteView as AccessibleEndnoteView
with suppress(ImportError):
    from ...dyn.text.accessible_footnote_view import AccessibleFootnoteView as AccessibleFootnoteView
with suppress(ImportError):
    from ...dyn.text.accessible_header_footer_view import AccessibleHeaderFooterView as AccessibleHeaderFooterView
with suppress(ImportError):
    from ...dyn.text.accessible_page_view import AccessiblePageView as AccessiblePageView
with suppress(ImportError):
    from ...dyn.text.accessible_paragraph_view import AccessibleParagraphView as AccessibleParagraphView
with suppress(ImportError):
    from ...dyn.text.accessible_text_document_page_view import AccessibleTextDocumentPageView as AccessibleTextDocumentPageView
with suppress(ImportError):
    from ...dyn.text.accessible_text_document_view import AccessibleTextDocumentView as AccessibleTextDocumentView
with suppress(ImportError):
    from ...dyn.text.accessible_text_embedded_object import AccessibleTextEmbeddedObject as AccessibleTextEmbeddedObject
with suppress(ImportError):
    from ...dyn.text.accessible_text_frame_view import AccessibleTextFrameView as AccessibleTextFrameView
with suppress(ImportError):
    from ...dyn.text.accessible_text_graphic_object import AccessibleTextGraphicObject as AccessibleTextGraphicObject
with suppress(ImportError):
    from ...dyn.text.author_display_format import AuthorDisplayFormat as AuthorDisplayFormat
with suppress(ImportError):
    from ...dyn.text.author_display_format import AuthorDisplayFormatEnum as AuthorDisplayFormatEnum
with suppress(ImportError):
    from ...dyn.text.auto_text_container import AutoTextContainer as AutoTextContainer
with suppress(ImportError):
    from ...dyn.text.auto_text_entry import AutoTextEntry as AutoTextEntry
with suppress(ImportError):
    from ...dyn.text.auto_text_group import AutoTextGroup as AutoTextGroup
with suppress(ImportError):
    from ...dyn.text.base_frame import BaseFrame as BaseFrame
with suppress(ImportError):
    from ...dyn.text.base_frame_properties import BaseFrameProperties as BaseFrameProperties
with suppress(ImportError):
    from ...dyn.text.base_index import BaseIndex as BaseIndex
with suppress(ImportError):
    from ...dyn.text.base_index_mark import BaseIndexMark as BaseIndexMark
with suppress(ImportError):
    from ...dyn.text.bibliography import Bibliography as Bibliography
with suppress(ImportError):
    from ...dyn.text.bibliography_data_field import BibliographyDataField as BibliographyDataField
with suppress(ImportError):
    from ...dyn.text.bibliography_data_field import BibliographyDataFieldEnum as BibliographyDataFieldEnum
with suppress(ImportError):
    from ...dyn.text.bibliography_data_type import BibliographyDataType as BibliographyDataType
with suppress(ImportError):
    from ...dyn.text.bibliography_data_type import BibliographyDataTypeEnum as BibliographyDataTypeEnum
with suppress(ImportError):
    from ...dyn.text.bookmark import Bookmark as Bookmark
with suppress(ImportError):
    from ...dyn.text.bookmarks import Bookmarks as Bookmarks
with suppress(ImportError):
    from ...dyn.text.cell import Cell as Cell
with suppress(ImportError):
    from ...dyn.text.cell_properties import CellProperties as CellProperties
with suppress(ImportError):
    from ...dyn.text.cell_range import CellRange as CellRange
with suppress(ImportError):
    from ...dyn.text.chained_text_frame import ChainedTextFrame as ChainedTextFrame
with suppress(ImportError):
    from ...dyn.text.chapter_format import ChapterFormat as ChapterFormat
with suppress(ImportError):
    from ...dyn.text.chapter_format import ChapterFormatEnum as ChapterFormatEnum
with suppress(ImportError):
    from ...dyn.text.chapter_numbering_rule import ChapterNumberingRule as ChapterNumberingRule
with suppress(ImportError):
    from ...dyn.text.character_compression_type import CharacterCompressionType as CharacterCompressionType
with suppress(ImportError):
    from ...dyn.text.character_compression_type import CharacterCompressionTypeEnum as CharacterCompressionTypeEnum
with suppress(ImportError):
    from ...dyn.text.column_separator_style import ColumnSeparatorStyle as ColumnSeparatorStyle
with suppress(ImportError):
    from ...dyn.text.column_separator_style import ColumnSeparatorStyleEnum as ColumnSeparatorStyleEnum
with suppress(ImportError):
    from ...dyn.text.content_index import ContentIndex as ContentIndex
with suppress(ImportError):
    from ...dyn.text.content_index_mark import ContentIndexMark as ContentIndexMark
with suppress(ImportError):
    from ...dyn.text.control_character import ControlCharacter as ControlCharacter
with suppress(ImportError):
    from ...dyn.text.control_character import ControlCharacterEnum as ControlCharacterEnum
with suppress(ImportError):
    from ...dyn.text.date_display_format import DateDisplayFormat as DateDisplayFormat
with suppress(ImportError):
    from ...dyn.text.date_display_format import DateDisplayFormatEnum as DateDisplayFormatEnum
with suppress(ImportError):
    from ...dyn.text.default_numbering_provider import DefaultNumberingProvider as DefaultNumberingProvider
with suppress(ImportError):
    from ...dyn.text.defaults import Defaults as Defaults
with suppress(ImportError):
    from ...dyn.text.dependent_text_field import DependentTextField as DependentTextField
with suppress(ImportError):
    from ...dyn.text.document_index import DocumentIndex as DocumentIndex
with suppress(ImportError):
    from ...dyn.text.document_index_level_format import DocumentIndexLevelFormat as DocumentIndexLevelFormat
with suppress(ImportError):
    from ...dyn.text.document_index_mark import DocumentIndexMark as DocumentIndexMark
with suppress(ImportError):
    from ...dyn.text.document_index_mark_asian import DocumentIndexMarkAsian as DocumentIndexMarkAsian
with suppress(ImportError):
    from ...dyn.text.document_index_paragraph_styles import DocumentIndexParagraphStyles as DocumentIndexParagraphStyles
with suppress(ImportError):
    from ...dyn.text.document_indexes import DocumentIndexes as DocumentIndexes
with suppress(ImportError):
    from ...dyn.text.document_settings import DocumentSettings as DocumentSettings
with suppress(ImportError):
    from ...dyn.text.document_statistic import DocumentStatistic as DocumentStatistic
with suppress(ImportError):
    from ...dyn.text.document_statistic import DocumentStatisticEnum as DocumentStatisticEnum
with suppress(ImportError):
    from ...dyn.text.endnote import Endnote as Endnote
with suppress(ImportError):
    from ...dyn.text.endnote_settings import EndnoteSettings as EndnoteSettings
with suppress(ImportError):
    from ...dyn.text.filename_display_format import FilenameDisplayFormat as FilenameDisplayFormat
with suppress(ImportError):
    from ...dyn.text.filename_display_format import FilenameDisplayFormatEnum as FilenameDisplayFormatEnum
with suppress(ImportError):
    from ...dyn.text.font_emphasis import FontEmphasis as FontEmphasis
with suppress(ImportError):
    from ...dyn.text.font_emphasis import FontEmphasisEnum as FontEmphasisEnum
with suppress(ImportError):
    from ...dyn.text.font_relief import FontRelief as FontRelief
with suppress(ImportError):
    from ...dyn.text.font_relief import FontReliefEnum as FontReliefEnum
with suppress(ImportError):
    from ...dyn.text.footnote import Footnote as Footnote
with suppress(ImportError):
    from ...dyn.text.footnote_numbering import FootnoteNumbering as FootnoteNumbering
with suppress(ImportError):
    from ...dyn.text.footnote_numbering import FootnoteNumberingEnum as FootnoteNumberingEnum
with suppress(ImportError):
    from ...dyn.text.footnote_settings import FootnoteSettings as FootnoteSettings
with suppress(ImportError):
    from ...dyn.text.footnotes import Footnotes as Footnotes
with suppress(ImportError):
    from ...dyn.text.generic_text_document import GenericTextDocument as GenericTextDocument
with suppress(ImportError):
    from ...dyn.text.global_document import GlobalDocument as GlobalDocument
with suppress(ImportError):
    from ...dyn.text.global_settings import GlobalSettings as GlobalSettings
with suppress(ImportError):
    from ...dyn.text.graphic_crop import GraphicCrop as GraphicCrop
with suppress(ImportError):
    from ...dyn.text.hori_orientation import HoriOrientation as HoriOrientation
with suppress(ImportError):
    from ...dyn.text.hori_orientation import HoriOrientationEnum as HoriOrientationEnum
with suppress(ImportError):
    from ...dyn.text.hori_orientation_format import HoriOrientationFormat as HoriOrientationFormat
with suppress(ImportError):
    from ...dyn.text.horizontal_adjust import HorizontalAdjust as HorizontalAdjust
with suppress(ImportError):
    from ...dyn.text.illustrations_index import IllustrationsIndex as IllustrationsIndex
with suppress(ImportError):
    from ...dyn.text.in_content_metadata import InContentMetadata as InContentMetadata
with suppress(ImportError):
    from ...dyn.text.invalid_text_content_exception import InvalidTextContentException as InvalidTextContentException
with suppress(ImportError):
    from ...dyn.text.label_follow import LabelFollow as LabelFollow
with suppress(ImportError):
    from ...dyn.text.label_follow import LabelFollowEnum as LabelFollowEnum
with suppress(ImportError):
    from ...dyn.text.line_numbering_properties import LineNumberingProperties as LineNumberingProperties
with suppress(ImportError):
    from ...dyn.text.mail_merge import MailMerge as MailMerge
with suppress(ImportError):
    from ...dyn.text.mail_merge_event import MailMergeEvent as MailMergeEvent
with suppress(ImportError):
    from ...dyn.text.mail_merge_type import MailMergeType as MailMergeType
with suppress(ImportError):
    from ...dyn.text.mail_merge_type import MailMergeTypeEnum as MailMergeTypeEnum
with suppress(ImportError):
    from ...dyn.text.module_dispatcher import ModuleDispatcher as ModuleDispatcher
with suppress(ImportError):
    from ...dyn.text.note_print_mode import NotePrintMode as NotePrintMode
with suppress(ImportError):
    from ...dyn.text.numbering_level import NumberingLevel as NumberingLevel
with suppress(ImportError):
    from ...dyn.text.numbering_rules import NumberingRules as NumberingRules
with suppress(ImportError):
    from ...dyn.text.numbering_style import NumberingStyle as NumberingStyle
with suppress(ImportError):
    from ...dyn.text.object_index import ObjectIndex as ObjectIndex
with suppress(ImportError):
    from ...dyn.text.page_footnote_info import PageFootnoteInfo as PageFootnoteInfo
with suppress(ImportError):
    from ...dyn.text.page_number_type import PageNumberType as PageNumberType
with suppress(ImportError):
    from ...dyn.text.page_print_settings import PagePrintSettings as PagePrintSettings
with suppress(ImportError):
    from ...dyn.text.paragraph import Paragraph as Paragraph
with suppress(ImportError):
    from ...dyn.text.paragraph_enumeration import ParagraphEnumeration as ParagraphEnumeration
with suppress(ImportError):
    from ...dyn.text.paragraph_vert_align import ParagraphVertAlign as ParagraphVertAlign
with suppress(ImportError):
    from ...dyn.text.paragraph_vert_align import ParagraphVertAlignEnum as ParagraphVertAlignEnum
with suppress(ImportError):
    from ...dyn.text.placeholder_type import PlaceholderType as PlaceholderType
with suppress(ImportError):
    from ...dyn.text.placeholder_type import PlaceholderTypeEnum as PlaceholderTypeEnum
with suppress(ImportError):
    from ...dyn.text.position_and_space_mode import PositionAndSpaceMode as PositionAndSpaceMode
with suppress(ImportError):
    from ...dyn.text.position_and_space_mode import PositionAndSpaceModeEnum as PositionAndSpaceModeEnum
with suppress(ImportError):
    from ...dyn.text.position_layout_dir import PositionLayoutDir as PositionLayoutDir
with suppress(ImportError):
    from ...dyn.text.position_layout_dir import PositionLayoutDirEnum as PositionLayoutDirEnum
with suppress(ImportError):
    from ...dyn.text.print_settings import PrintSettings as PrintSettings
with suppress(ImportError):
    from ...dyn.text.redline_portion import RedlinePortion as RedlinePortion
with suppress(ImportError):
    from ...dyn.text.reference_field_part import ReferenceFieldPart as ReferenceFieldPart
with suppress(ImportError):
    from ...dyn.text.reference_field_part import ReferenceFieldPartEnum as ReferenceFieldPartEnum
with suppress(ImportError):
    from ...dyn.text.reference_field_source import ReferenceFieldSource as ReferenceFieldSource
with suppress(ImportError):
    from ...dyn.text.reference_field_source import ReferenceFieldSourceEnum as ReferenceFieldSourceEnum
with suppress(ImportError):
    from ...dyn.text.reference_mark import ReferenceMark as ReferenceMark
with suppress(ImportError):
    from ...dyn.text.reference_marks import ReferenceMarks as ReferenceMarks
with suppress(ImportError):
    from ...dyn.text.rel_orientation import RelOrientation as RelOrientation
with suppress(ImportError):
    from ...dyn.text.rel_orientation import RelOrientationEnum as RelOrientationEnum
with suppress(ImportError):
    from ...dyn.text.ruby_adjust import RubyAdjust as RubyAdjust
with suppress(ImportError):
    from ...dyn.text.ruby_position import RubyPosition as RubyPosition
with suppress(ImportError):
    from ...dyn.text.ruby_position import RubyPositionEnum as RubyPositionEnum
with suppress(ImportError):
    from ...dyn.text.section_file_link import SectionFileLink as SectionFileLink
with suppress(ImportError):
    from ...dyn.text.set_variable_type import SetVariableType as SetVariableType
with suppress(ImportError):
    from ...dyn.text.set_variable_type import SetVariableTypeEnum as SetVariableTypeEnum
with suppress(ImportError):
    from ...dyn.text.shape import Shape as Shape
with suppress(ImportError):
    from ...dyn.text.size_type import SizeType as SizeType
with suppress(ImportError):
    from ...dyn.text.size_type import SizeTypeEnum as SizeTypeEnum
with suppress(ImportError):
    from ...dyn.text.table_column_separator import TableColumnSeparator as TableColumnSeparator
with suppress(ImportError):
    from ...dyn.text.table_columns import TableColumns as TableColumns
with suppress(ImportError):
    from ...dyn.text.table_index import TableIndex as TableIndex
with suppress(ImportError):
    from ...dyn.text.table_rows import TableRows as TableRows
with suppress(ImportError):
    from ...dyn.text.template_display_format import TemplateDisplayFormat as TemplateDisplayFormat
with suppress(ImportError):
    from ...dyn.text.template_display_format import TemplateDisplayFormatEnum as TemplateDisplayFormatEnum
with suppress(ImportError):
    from ...dyn.text.text import Text as Text
with suppress(ImportError):
    from ...dyn.text.text_column import TextColumn as TextColumn
with suppress(ImportError):
    from ...dyn.text.text_column_sequence import TextColumnSequence as TextColumnSequence
with suppress(ImportError):
    from ...dyn.text.text_columns import TextColumns as TextColumns
with suppress(ImportError):
    from ...dyn.text.text_content import TextContent as TextContent
with suppress(ImportError):
    from ...dyn.text.text_content_anchor_type import TextContentAnchorType as TextContentAnchorType
with suppress(ImportError):
    from ...dyn.text.text_content_collection import TextContentCollection as TextContentCollection
with suppress(ImportError):
    from ...dyn.text.text_cursor import TextCursor as TextCursor
with suppress(ImportError):
    from ...dyn.text.text_document import TextDocument as TextDocument
with suppress(ImportError):
    from ...dyn.text.text_document_view import TextDocumentView as TextDocumentView
with suppress(ImportError):
    from ...dyn.text.text_embedded_object import TextEmbeddedObject as TextEmbeddedObject
with suppress(ImportError):
    from ...dyn.text.text_embedded_objects import TextEmbeddedObjects as TextEmbeddedObjects
with suppress(ImportError):
    from ...dyn.text.text_field import TextField as TextField
with suppress(ImportError):
    from ...dyn.text.text_field_enumeration import TextFieldEnumeration as TextFieldEnumeration
with suppress(ImportError):
    from ...dyn.text.text_field_master import TextFieldMaster as TextFieldMaster
with suppress(ImportError):
    from ...dyn.text.text_field_masters import TextFieldMasters as TextFieldMasters
with suppress(ImportError):
    from ...dyn.text.text_fields import TextFields as TextFields
with suppress(ImportError):
    from ...dyn.text.text_frame import TextFrame as TextFrame
with suppress(ImportError):
    from ...dyn.text.text_frames import TextFrames as TextFrames
with suppress(ImportError):
    from ...dyn.text.text_graphic_object import TextGraphicObject as TextGraphicObject
with suppress(ImportError):
    from ...dyn.text.text_graphic_objects import TextGraphicObjects as TextGraphicObjects
with suppress(ImportError):
    from ...dyn.text.text_grid_mode import TextGridMode as TextGridMode
with suppress(ImportError):
    from ...dyn.text.text_grid_mode import TextGridModeEnum as TextGridModeEnum
with suppress(ImportError):
    from ...dyn.text.text_layout_cursor import TextLayoutCursor as TextLayoutCursor
with suppress(ImportError):
    from ...dyn.text.text_markup_descriptor import TextMarkupDescriptor as TextMarkupDescriptor
with suppress(ImportError):
    from ...dyn.text.text_markup_type import TextMarkupType as TextMarkupType
with suppress(ImportError):
    from ...dyn.text.text_markup_type import TextMarkupTypeEnum as TextMarkupTypeEnum
with suppress(ImportError):
    from ...dyn.text.text_page_style import TextPageStyle as TextPageStyle
with suppress(ImportError):
    from ...dyn.text.text_portion import TextPortion as TextPortion
with suppress(ImportError):
    from ...dyn.text.text_portion_enumeration import TextPortionEnumeration as TextPortionEnumeration
with suppress(ImportError):
    from ...dyn.text.text_position import TextPosition as TextPosition
with suppress(ImportError):
    from ...dyn.text.text_range import TextRange as TextRange
with suppress(ImportError):
    from ...dyn.text.text_range_content_properties import TextRangeContentProperties as TextRangeContentProperties
with suppress(ImportError):
    from ...dyn.text.text_range_selection import TextRangeSelection as TextRangeSelection
with suppress(ImportError):
    from ...dyn.text.text_ranges import TextRanges as TextRanges
with suppress(ImportError):
    from ...dyn.text.text_section import TextSection as TextSection
with suppress(ImportError):
    from ...dyn.text.text_sections import TextSections as TextSections
with suppress(ImportError):
    from ...dyn.text.text_sort_descriptor import TextSortDescriptor as TextSortDescriptor
with suppress(ImportError):
    from ...dyn.text.text_sort_descriptor2 import TextSortDescriptor2 as TextSortDescriptor2
with suppress(ImportError):
    from ...dyn.text.text_sortable import TextSortable as TextSortable
with suppress(ImportError):
    from ...dyn.text.text_table import TextTable as TextTable
with suppress(ImportError):
    from ...dyn.text.text_table_cursor import TextTableCursor as TextTableCursor
with suppress(ImportError):
    from ...dyn.text.text_table_row import TextTableRow as TextTableRow
with suppress(ImportError):
    from ...dyn.text.text_tables import TextTables as TextTables
with suppress(ImportError):
    from ...dyn.text.text_view_cursor import TextViewCursor as TextViewCursor
with suppress(ImportError):
    from ...dyn.text.time_display_format import TimeDisplayFormat as TimeDisplayFormat
with suppress(ImportError):
    from ...dyn.text.time_display_format import TimeDisplayFormatEnum as TimeDisplayFormatEnum
with suppress(ImportError):
    from ...dyn.text.user_data_part import UserDataPart as UserDataPart
with suppress(ImportError):
    from ...dyn.text.user_data_part import UserDataPartEnum as UserDataPartEnum
with suppress(ImportError):
    from ...dyn.text.user_defined_index import UserDefinedIndex as UserDefinedIndex
with suppress(ImportError):
    from ...dyn.text.user_field_format import UserFieldFormat as UserFieldFormat
with suppress(ImportError):
    from ...dyn.text.user_field_format import UserFieldFormatEnum as UserFieldFormatEnum
with suppress(ImportError):
    from ...dyn.text.user_index import UserIndex as UserIndex
with suppress(ImportError):
    from ...dyn.text.user_index_mark import UserIndexMark as UserIndexMark
with suppress(ImportError):
    from ...dyn.text.vert_orientation import VertOrientation as VertOrientation
with suppress(ImportError):
    from ...dyn.text.vert_orientation import VertOrientationEnum as VertOrientationEnum
with suppress(ImportError):
    from ...dyn.text.vert_orientation_format import VertOrientationFormat as VertOrientationFormat
with suppress(ImportError):
    from ...dyn.text.view_settings import ViewSettings as ViewSettings
with suppress(ImportError):
    from ...dyn.text.web_document import WebDocument as WebDocument
with suppress(ImportError):
    from ...dyn.text.wrap_influence_on_position import WrapInfluenceOnPosition as WrapInfluenceOnPosition
with suppress(ImportError):
    from ...dyn.text.wrap_influence_on_position import WrapInfluenceOnPositionEnum as WrapInfluenceOnPositionEnum
with suppress(ImportError):
    from ...dyn.text.wrap_text_mode import WrapTextMode as WrapTextMode
with suppress(ImportError):
    from ...dyn.text.writing_mode import WritingMode as WritingMode
with suppress(ImportError):
    from ...dyn.text.writing_mode2 import WritingMode2 as WritingMode2
with suppress(ImportError):
    from ...dyn.text.writing_mode2 import WritingMode2Enum as WritingMode2Enum
with suppress(ImportError):
    from ...dyn.text.x_auto_text_container import XAutoTextContainer as XAutoTextContainer
with suppress(ImportError):
    from ...dyn.text.x_auto_text_container2 import XAutoTextContainer2 as XAutoTextContainer2
with suppress(ImportError):
    from ...dyn.text.x_auto_text_entry import XAutoTextEntry as XAutoTextEntry
with suppress(ImportError):
    from ...dyn.text.x_auto_text_group import XAutoTextGroup as XAutoTextGroup
with suppress(ImportError):
    from ...dyn.text.x_bookmark_insert_tool import XBookmarkInsertTool as XBookmarkInsertTool
with suppress(ImportError):
    from ...dyn.text.x_bookmarks_supplier import XBookmarksSupplier as XBookmarksSupplier
with suppress(ImportError):
    from ...dyn.text.x_chapter_numbering_supplier import XChapterNumberingSupplier as XChapterNumberingSupplier
with suppress(ImportError):
    from ...dyn.text.x_default_numbering_provider import XDefaultNumberingProvider as XDefaultNumberingProvider
with suppress(ImportError):
    from ...dyn.text.x_dependent_text_field import XDependentTextField as XDependentTextField
with suppress(ImportError):
    from ...dyn.text.x_document_index import XDocumentIndex as XDocumentIndex
with suppress(ImportError):
    from ...dyn.text.x_document_index_mark import XDocumentIndexMark as XDocumentIndexMark
with suppress(ImportError):
    from ...dyn.text.x_document_indexes_supplier import XDocumentIndexesSupplier as XDocumentIndexesSupplier
with suppress(ImportError):
    from ...dyn.text.x_endnotes_settings_supplier import XEndnotesSettingsSupplier as XEndnotesSettingsSupplier
with suppress(ImportError):
    from ...dyn.text.x_endnotes_supplier import XEndnotesSupplier as XEndnotesSupplier
with suppress(ImportError):
    from ...dyn.text.x_flat_paragraph import XFlatParagraph as XFlatParagraph
with suppress(ImportError):
    from ...dyn.text.x_flat_paragraph_iterator import XFlatParagraphIterator as XFlatParagraphIterator
with suppress(ImportError):
    from ...dyn.text.x_flat_paragraph_iterator_provider import XFlatParagraphIteratorProvider as XFlatParagraphIteratorProvider
with suppress(ImportError):
    from ...dyn.text.x_footnote import XFootnote as XFootnote
with suppress(ImportError):
    from ...dyn.text.x_footnotes_settings_supplier import XFootnotesSettingsSupplier as XFootnotesSettingsSupplier
with suppress(ImportError):
    from ...dyn.text.x_footnotes_supplier import XFootnotesSupplier as XFootnotesSupplier
with suppress(ImportError):
    from ...dyn.text.x_form_field import XFormField as XFormField
with suppress(ImportError):
    from ...dyn.text.x_line_numbering_properties import XLineNumberingProperties as XLineNumberingProperties
with suppress(ImportError):
    from ...dyn.text.x_mail_merge_broadcaster import XMailMergeBroadcaster as XMailMergeBroadcaster
with suppress(ImportError):
    from ...dyn.text.x_mail_merge_listener import XMailMergeListener as XMailMergeListener
with suppress(ImportError):
    from ...dyn.text.x_marking_access import XMarkingAccess as XMarkingAccess
with suppress(ImportError):
    from ...dyn.text.x_multi_text_markup import XMultiTextMarkup as XMultiTextMarkup
with suppress(ImportError):
    from ...dyn.text.x_numbering_formatter import XNumberingFormatter as XNumberingFormatter
with suppress(ImportError):
    from ...dyn.text.x_numbering_rules_supplier import XNumberingRulesSupplier as XNumberingRulesSupplier
with suppress(ImportError):
    from ...dyn.text.x_numbering_type_info import XNumberingTypeInfo as XNumberingTypeInfo
with suppress(ImportError):
    from ...dyn.text.x_page_cursor import XPageCursor as XPageCursor
with suppress(ImportError):
    from ...dyn.text.x_page_printable import XPagePrintable as XPagePrintable
with suppress(ImportError):
    from ...dyn.text.x_paragraph_append import XParagraphAppend as XParagraphAppend
with suppress(ImportError):
    from ...dyn.text.x_paragraph_cursor import XParagraphCursor as XParagraphCursor
with suppress(ImportError):
    from ...dyn.text.x_paste_broadcaster import XPasteBroadcaster as XPasteBroadcaster
with suppress(ImportError):
    from ...dyn.text.x_paste_listener import XPasteListener as XPasteListener
with suppress(ImportError):
    from ...dyn.text.x_redline import XRedline as XRedline
with suppress(ImportError):
    from ...dyn.text.x_reference_marks_supplier import XReferenceMarksSupplier as XReferenceMarksSupplier
with suppress(ImportError):
    from ...dyn.text.x_relative_text_content_insert import XRelativeTextContentInsert as XRelativeTextContentInsert
with suppress(ImportError):
    from ...dyn.text.x_relative_text_content_remove import XRelativeTextContentRemove as XRelativeTextContentRemove
with suppress(ImportError):
    from ...dyn.text.x_ruby_selection import XRubySelection as XRubySelection
with suppress(ImportError):
    from ...dyn.text.x_sentence_cursor import XSentenceCursor as XSentenceCursor
with suppress(ImportError):
    from ...dyn.text.x_simple_text import XSimpleText as XSimpleText
with suppress(ImportError):
    from ...dyn.text.x_text import XText as XText
with suppress(ImportError):
    from ...dyn.text.x_text_append import XTextAppend as XTextAppend
with suppress(ImportError):
    from ...dyn.text.x_text_append_and_convert import XTextAppendAndConvert as XTextAppendAndConvert
with suppress(ImportError):
    from ...dyn.text.x_text_columns import XTextColumns as XTextColumns
with suppress(ImportError):
    from ...dyn.text.x_text_content import XTextContent as XTextContent
with suppress(ImportError):
    from ...dyn.text.x_text_content_append import XTextContentAppend as XTextContentAppend
with suppress(ImportError):
    from ...dyn.text.x_text_convert import XTextConvert as XTextConvert
with suppress(ImportError):
    from ...dyn.text.x_text_copy import XTextCopy as XTextCopy
with suppress(ImportError):
    from ...dyn.text.x_text_cursor import XTextCursor as XTextCursor
with suppress(ImportError):
    from ...dyn.text.x_text_document import XTextDocument as XTextDocument
with suppress(ImportError):
    from ...dyn.text.x_text_embedded_objects_supplier import XTextEmbeddedObjectsSupplier as XTextEmbeddedObjectsSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_field import XTextField as XTextField
with suppress(ImportError):
    from ...dyn.text.x_text_fields_supplier import XTextFieldsSupplier as XTextFieldsSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_frame import XTextFrame as XTextFrame
with suppress(ImportError):
    from ...dyn.text.x_text_frames_supplier import XTextFramesSupplier as XTextFramesSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_graphic_objects_supplier import XTextGraphicObjectsSupplier as XTextGraphicObjectsSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_markup import XTextMarkup as XTextMarkup
with suppress(ImportError):
    from ...dyn.text.x_text_portion_append import XTextPortionAppend as XTextPortionAppend
with suppress(ImportError):
    from ...dyn.text.x_text_range import XTextRange as XTextRange
with suppress(ImportError):
    from ...dyn.text.x_text_range_compare import XTextRangeCompare as XTextRangeCompare
with suppress(ImportError):
    from ...dyn.text.x_text_range_mover import XTextRangeMover as XTextRangeMover
with suppress(ImportError):
    from ...dyn.text.x_text_section import XTextSection as XTextSection
with suppress(ImportError):
    from ...dyn.text.x_text_sections_supplier import XTextSectionsSupplier as XTextSectionsSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_shapes_supplier import XTextShapesSupplier as XTextShapesSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_table import XTextTable as XTextTable
with suppress(ImportError):
    from ...dyn.text.x_text_table_cursor import XTextTableCursor as XTextTableCursor
with suppress(ImportError):
    from ...dyn.text.x_text_tables_supplier import XTextTablesSupplier as XTextTablesSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_view_cursor import XTextViewCursor as XTextViewCursor
with suppress(ImportError):
    from ...dyn.text.x_text_view_cursor_supplier import XTextViewCursorSupplier as XTextViewCursorSupplier
with suppress(ImportError):
    from ...dyn.text.x_text_view_text_range_supplier import XTextViewTextRangeSupplier as XTextViewTextRangeSupplier
with suppress(ImportError):
    from ...dyn.text.x_word_cursor import XWordCursor as XWordCursor
