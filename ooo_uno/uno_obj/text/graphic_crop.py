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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class GraphicCrop(object):
    """
    Struct Class

    describes the cropping of graphic objects.
    
    Cropping means to show only parts of the object.
    
    Negative values cut the visible area; positive values extend the visible area by filling it with background color. The absolute sum of top and bottom crop must be smaller than the objects original height. The absolute sum of the left and right crop must be smaller than the object's original width.
    
    If this property is applied to a graphic object, then this object will correct these values if necessary.

    See Also:
        `API GraphicCrop <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1GraphicCrop.html>`_


    Note:
        | At runtime GraphicCrop will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | GraphicCrop is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Bottom: typing.Optional[int] = None, Left: typing.Optional[int] = None, Right: typing.Optional[int] = None, Top: typing.Optional[int] = None):
        self._bottom = Bottom
        self._left = Left
        self._right = Right
        self._top = Top

    @property
    def Bottom(self) -> int:
        """
        contains the bottom value to cut (if negative) or to extend (if positive)
        """
        return self._bottom
    
    @Bottom.setter
    def Bottom(self, value: int) -> None:
        self._bottom = value

    @property
    def Left(self) -> int:
        """
        contains the left value to cut (if negative) or to extend (if positive)
        """
        return self._left
    
    @Left.setter
    def Left(self, value: int) -> None:
        self._left = value

    @property
    def Right(self) -> int:
        """
        contains the right value to cut (if negative) or to extend (if positive)
        """
        return self._right
    
    @Right.setter
    def Right(self, value: int) -> None:
        self._right = value

    @property
    def Top(self) -> int:
        """
        contains the top value to cut (if negative) or to extend (if positive)
        """
        return self._top
    
    @Top.setter
    def Top(self, value: int) -> None:
        self._top = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global GraphicCrop
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Bottom', 'Left', 'Right', 'Top')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.text.GraphicCrop')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        GraphicCrop = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['GraphicCrop']
