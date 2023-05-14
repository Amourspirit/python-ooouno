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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Visibility(object):
    """
    Struct Class

    describes the visibility state of a property.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Visibility <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1Visibility.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.Visibility'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.Visibility'
    """Literal Constant ``com.sun.star.frame.status.Visibility``"""

    def __init__(self, bVisible: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            bVisible (bool, optional): bVisible value.
        """
        super().__init__()

        if isinstance(bVisible, Visibility):
            oth: Visibility = bVisible
            self.bVisible = oth.bVisible
            return

        kargs = {
            "bVisible": bVisible,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._b_visible = kwargs["bVisible"]


    @property
    def bVisible(self) -> bool:
        """
        TRUE if the property is visible otherwise FALSE.
        """
        return self._b_visible

    @bVisible.setter
    def bVisible(self, value: bool) -> None:
        self._b_visible = value


__all__ = ['Visibility']
