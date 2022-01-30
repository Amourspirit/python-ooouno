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
# Namespace: com.sun.star.text
# Libre Office Version: 7.2
import typing
if typing.TYPE_CHECKING:
    from .text_position import TextPosition as TextPosition_b2ae0bc7
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class TextRangeSelection(object):
        """
        Struct Class


        See Also:
            `API TextRangeSelection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextRangeSelection.html>`_


        Note:
            | At runtime TextRangeSelection will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | TextRangeSelection is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, End: 'typing.Optional[TextPosition_b2ae0bc7]' = None, Start: 'typing.Optional[TextPosition_b2ae0bc7]' = None):
            self._end = End
            self._start = Start

        @property
        def End(self) -> 'TextPosition_b2ae0bc7':
            return self._end
        
        @End.setter
        def End(self, value: 'TextPosition_b2ae0bc7') -> None:
            self._end = value

        @property
        def Start(self) -> 'TextPosition_b2ae0bc7':
            return self._start
        
        @Start.setter
        def Start(self, value: 'TextPosition_b2ae0bc7') -> None:
            self._start = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global TextRangeSelection
        order = ('End', 'Start')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.text.TextRangeSelection')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        TextRangeSelection = _struct_init

    _dynamic_struct()

__all__ = ['TextRangeSelection']
