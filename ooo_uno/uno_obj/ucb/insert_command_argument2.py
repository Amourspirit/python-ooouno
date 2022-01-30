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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from .insert_command_argument import InsertCommandArgument as InsertCommandArgument_19550eb9
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class InsertCommandArgument2(InsertCommandArgument_19550eb9):
        """
        Struct Class

        The argument for the command \"insert\" augmented with some properties.

        See Also:
            `API InsertCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1InsertCommandArgument2.html>`_


        Note:
            | At runtime InsertCommandArgument2 will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | InsertCommandArgument2 is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, DocumentId: typing.Optional[str] = None, MimeType: typing.Optional[str] = None):
            self._document_id = DocumentId
            self._mime_type = MimeType

        @property
        def DocumentId(self) -> str:
            """
            contains the Document Id of the document to insert
            """
            return self._document_id
        
        @DocumentId.setter
        def DocumentId(self, value: str) -> None:
            self._document_id = value

        @property
        def MimeType(self) -> str:
            """
            contains the MIME type of the document to insert
            """
            return self._mime_type
        
        @MimeType.setter
        def MimeType(self, value: str) -> None:
            self._mime_type = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global InsertCommandArgument2
        order = ('DocumentId', 'MimeType')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.InsertCommandArgument2')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        InsertCommandArgument2 = _struct_init

    _dynamic_struct()

__all__ = ['InsertCommandArgument2']
