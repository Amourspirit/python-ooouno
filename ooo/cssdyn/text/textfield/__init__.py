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
    from ....dyn.text.textfield.annotation import Annotation as Annotation
except ImportError:
    pass
try:
    from ....dyn.text.textfield.author import Author as Author
except ImportError:
    pass
try:
    from ....dyn.text.textfield.bibliography import Bibliography as Bibliography
except ImportError:
    pass
try:
    from ....dyn.text.textfield.chapter import Chapter as Chapter
except ImportError:
    pass
try:
    from ....dyn.text.textfield.character_count import CharacterCount as CharacterCount
except ImportError:
    pass
try:
    from ....dyn.text.textfield.combined_characters import CombinedCharacters as CombinedCharacters
except ImportError:
    pass
try:
    from ....dyn.text.textfield.conditional_text import ConditionalText as ConditionalText
except ImportError:
    pass
try:
    from ....dyn.text.textfield.dde import DDE as DDE
except ImportError:
    pass
try:
    from ....dyn.text.textfield.database import Database as Database
except ImportError:
    pass
try:
    from ....dyn.text.textfield.database_name import DatabaseName as DatabaseName
except ImportError:
    pass
try:
    from ....dyn.text.textfield.database_next_set import DatabaseNextSet as DatabaseNextSet
except ImportError:
    pass
try:
    from ....dyn.text.textfield.database_number_of_set import DatabaseNumberOfSet as DatabaseNumberOfSet
except ImportError:
    pass
try:
    from ....dyn.text.textfield.database_set_number import DatabaseSetNumber as DatabaseSetNumber
except ImportError:
    pass
try:
    from ....dyn.text.textfield.date_time import DateTime as DateTime
except ImportError:
    pass
try:
    from ....dyn.text.textfield.drop_down import DropDown as DropDown
except ImportError:
    pass
try:
    from ....dyn.text.textfield.embedded_object_count import EmbeddedObjectCount as EmbeddedObjectCount
except ImportError:
    pass
try:
    from ....dyn.text.textfield.extended_user import ExtendedUser as ExtendedUser
except ImportError:
    pass
try:
    from ....dyn.text.textfield.file_name import FileName as FileName
except ImportError:
    pass
try:
    from ....dyn.text.textfield.get_expression import GetExpression as GetExpression
except ImportError:
    pass
try:
    from ....dyn.text.textfield.get_reference import GetReference as GetReference
except ImportError:
    pass
try:
    from ....dyn.text.textfield.graphic_object_count import GraphicObjectCount as GraphicObjectCount
except ImportError:
    pass
try:
    from ....dyn.text.textfield.hidden_paragraph import HiddenParagraph as HiddenParagraph
except ImportError:
    pass
try:
    from ....dyn.text.textfield.hidden_text import HiddenText as HiddenText
except ImportError:
    pass
try:
    from ....dyn.text.textfield.input import Input as Input
except ImportError:
    pass
try:
    from ....dyn.text.textfield.input_user import InputUser as InputUser
except ImportError:
    pass
try:
    from ....dyn.text.textfield.jump_edit import JumpEdit as JumpEdit
except ImportError:
    pass
try:
    from ....dyn.text.textfield.macro import Macro as Macro
except ImportError:
    pass
try:
    from ....dyn.text.textfield.metadata_field import MetadataField as MetadataField
except ImportError:
    pass
try:
    from ....dyn.text.textfield.page_count import PageCount as PageCount
except ImportError:
    pass
try:
    from ....dyn.text.textfield.page_number import PageNumber as PageNumber
except ImportError:
    pass
try:
    from ....dyn.text.textfield.paragraph_count import ParagraphCount as ParagraphCount
except ImportError:
    pass
try:
    from ....dyn.text.textfield.reference_page_get import ReferencePageGet as ReferencePageGet
except ImportError:
    pass
try:
    from ....dyn.text.textfield.reference_page_set import ReferencePageSet as ReferencePageSet
except ImportError:
    pass
try:
    from ....dyn.text.textfield.script import Script as Script
except ImportError:
    pass
try:
    from ....dyn.text.textfield.set_expression import SetExpression as SetExpression
except ImportError:
    pass
try:
    from ....dyn.text.textfield.table_count import TableCount as TableCount
except ImportError:
    pass
try:
    from ....dyn.text.textfield.table_formula import TableFormula as TableFormula
except ImportError:
    pass
try:
    from ....dyn.text.textfield.template_name import TemplateName as TemplateName
except ImportError:
    pass
try:
    from ....dyn.text.textfield.type import Type as Type
except ImportError:
    pass
try:
    from ....dyn.text.textfield.type import TypeEnum as TypeEnum
except ImportError:
    pass
try:
    from ....dyn.text.textfield.url import URL as URL
except ImportError:
    pass
try:
    from ....dyn.text.textfield.user import User as User
except ImportError:
    pass
try:
    from ....dyn.text.textfield.word_count import WordCount as WordCount
except ImportError:
    pass
