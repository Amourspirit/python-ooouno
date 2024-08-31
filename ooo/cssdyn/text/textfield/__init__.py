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
    from ....dyn.text.textfield.annotation import Annotation as Annotation
with suppress(ImportError):
    from ....dyn.text.textfield.author import Author as Author
with suppress(ImportError):
    from ....dyn.text.textfield.bibliography import Bibliography as Bibliography
with suppress(ImportError):
    from ....dyn.text.textfield.chapter import Chapter as Chapter
with suppress(ImportError):
    from ....dyn.text.textfield.character_count import CharacterCount as CharacterCount
with suppress(ImportError):
    from ....dyn.text.textfield.combined_characters import CombinedCharacters as CombinedCharacters
with suppress(ImportError):
    from ....dyn.text.textfield.conditional_text import ConditionalText as ConditionalText
with suppress(ImportError):
    from ....dyn.text.textfield.dde import DDE as DDE
with suppress(ImportError):
    from ....dyn.text.textfield.database import Database as Database
with suppress(ImportError):
    from ....dyn.text.textfield.database_name import DatabaseName as DatabaseName
with suppress(ImportError):
    from ....dyn.text.textfield.database_next_set import DatabaseNextSet as DatabaseNextSet
with suppress(ImportError):
    from ....dyn.text.textfield.database_number_of_set import DatabaseNumberOfSet as DatabaseNumberOfSet
with suppress(ImportError):
    from ....dyn.text.textfield.database_set_number import DatabaseSetNumber as DatabaseSetNumber
with suppress(ImportError):
    from ....dyn.text.textfield.date_time import DateTime as DateTime
with suppress(ImportError):
    from ....dyn.text.textfield.drop_down import DropDown as DropDown
with suppress(ImportError):
    from ....dyn.text.textfield.embedded_object_count import EmbeddedObjectCount as EmbeddedObjectCount
with suppress(ImportError):
    from ....dyn.text.textfield.extended_user import ExtendedUser as ExtendedUser
with suppress(ImportError):
    from ....dyn.text.textfield.file_name import FileName as FileName
with suppress(ImportError):
    from ....dyn.text.textfield.get_expression import GetExpression as GetExpression
with suppress(ImportError):
    from ....dyn.text.textfield.get_reference import GetReference as GetReference
with suppress(ImportError):
    from ....dyn.text.textfield.graphic_object_count import GraphicObjectCount as GraphicObjectCount
with suppress(ImportError):
    from ....dyn.text.textfield.hidden_paragraph import HiddenParagraph as HiddenParagraph
with suppress(ImportError):
    from ....dyn.text.textfield.hidden_text import HiddenText as HiddenText
with suppress(ImportError):
    from ....dyn.text.textfield.input import Input as Input
with suppress(ImportError):
    from ....dyn.text.textfield.input_user import InputUser as InputUser
with suppress(ImportError):
    from ....dyn.text.textfield.jump_edit import JumpEdit as JumpEdit
with suppress(ImportError):
    from ....dyn.text.textfield.macro import Macro as Macro
with suppress(ImportError):
    from ....dyn.text.textfield.metadata_field import MetadataField as MetadataField
with suppress(ImportError):
    from ....dyn.text.textfield.page_count import PageCount as PageCount
with suppress(ImportError):
    from ....dyn.text.textfield.page_number import PageNumber as PageNumber
with suppress(ImportError):
    from ....dyn.text.textfield.paragraph_count import ParagraphCount as ParagraphCount
with suppress(ImportError):
    from ....dyn.text.textfield.reference_page_get import ReferencePageGet as ReferencePageGet
with suppress(ImportError):
    from ....dyn.text.textfield.reference_page_set import ReferencePageSet as ReferencePageSet
with suppress(ImportError):
    from ....dyn.text.textfield.script import Script as Script
with suppress(ImportError):
    from ....dyn.text.textfield.set_expression import SetExpression as SetExpression
with suppress(ImportError):
    from ....dyn.text.textfield.table_count import TableCount as TableCount
with suppress(ImportError):
    from ....dyn.text.textfield.table_formula import TableFormula as TableFormula
with suppress(ImportError):
    from ....dyn.text.textfield.template_name import TemplateName as TemplateName
with suppress(ImportError):
    from ....dyn.text.textfield.type import Type as Type
with suppress(ImportError):
    from ....dyn.text.textfield.type import TypeEnum as TypeEnum
with suppress(ImportError):
    from ....dyn.text.textfield.url import URL as URL
with suppress(ImportError):
    from ....dyn.text.textfield.user import User as User
with suppress(ImportError):
    from ....dyn.text.textfield.word_count import WordCount as WordCount
