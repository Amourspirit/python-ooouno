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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class Caret(object):
    """
    Struct Class

    This structure contains the caret information.
    
    This structure is used from the XTextLayout interface to transport information regarding a text caret.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Caret <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1Caret.html>`_


    Note:
        | At runtime Caret will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | Caret is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, CaretAngle: typing.Optional[float] = None, MainCaretIndex: typing.Optional[int] = None, SecondaryCaretIndex: typing.Optional[int] = None):
        self._caret_angle = CaretAngle
        self._main_caret_index = MainCaretIndex
        self._secondary_caret_index = SecondaryCaretIndex

    @property
    def CaretAngle(self) -> float:
        """
        The angle of the caret.
        
        This member contains the rotation angle of the caret in degrees, with 0 denoting an unrotated caret (the unrotated caret orientation depends on the writing mode, horizontally or vertically). The rotation angle is positive for counter-clockwise rotations.
        """
        return self._caret_angle
    
    @CaretAngle.setter
    def CaretAngle(self, value: float) -> None:
        self._caret_angle = value

    @property
    def MainCaretIndex(self) -> int:
        """
        This contains the main caret index.
        
        The main caret index corresponds to the insert position when inserting text in the layout's main text direction.
        """
        return self._main_caret_index
    
    @MainCaretIndex.setter
    def MainCaretIndex(self, value: int) -> None:
        self._main_caret_index = value

    @property
    def SecondaryCaretIndex(self) -> int:
        """
        This contains the secondary caret index.
        
        The secondary caret index, when different from the main caret index, corresponds to the insert position when inserting text at a direction change opposite to the layout's main text direction.
        """
        return self._secondary_caret_index
    
    @SecondaryCaretIndex.setter
    def SecondaryCaretIndex(self, value: int) -> None:
        self._secondary_caret_index = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global Caret
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('CaretAngle', 'MainCaretIndex', 'SecondaryCaretIndex')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.rendering.Caret')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Caret = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['Caret']
