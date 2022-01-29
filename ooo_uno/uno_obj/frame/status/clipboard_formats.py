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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ClipboardFormats(object):
    """
    Struct Class

    contains a list of format IDs and names which are part of the system clipboard.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ClipboardFormats <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1ClipboardFormats.html>`_


    Note:
        | At runtime ClipboardFormats will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ClipboardFormats is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Identifiers: 'typing.Optional[typing.List[int]]' = None, Names: 'typing.Optional[typing.List[str]]' = None):
        self._identifiers = Identifiers
        self._names = Names

    @property
    def Identifiers(self) -> 'typing.List[int]':
        """
        specifies a sequence of format IDs which are contained in the system clipboard.
        """
        return self._identifiers
    
    @Identifiers.setter
    def Identifiers(self, value: 'typing.List[int]') -> None:
        self._identifiers = value

    @property
    def Names(self) -> 'typing.List[str]':
        """
        specifies a sequence of format names which are contained in the system clipboard.
        """
        return self._names
    
    @Names.setter
    def Names(self, value: 'typing.List[str]') -> None:
        self._names = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ClipboardFormats
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Identifiers', 'Names')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.frame.status.ClipboardFormats')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ClipboardFormats = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ClipboardFormats']
