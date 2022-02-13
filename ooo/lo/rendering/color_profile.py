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
from ooo.oenv import UNO_NONE
import typing


class ColorProfile(object):
    """
    Struct Class

    ICC Color profile.

    See Also:
        `API ColorProfile <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1ColorProfile.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.ColorProfile'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.ColorProfile'
    """Literal Constant ``com.sun.star.rendering.ColorProfile``"""

    def __init__(self, dummy: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``dummy`` can be another ``ColorProfile`` instance,
                in which case other named args are ignored.

        Arguments:
            dummy (int, optional): dummy value
        """
        if isinstance(dummy, ColorProfile):
            oth: ColorProfile = dummy
            self._dummy = oth.dummy
            return
        else:
            self._dummy = dummy



    @property
    def dummy(self) -> int:
        return self._dummy
    
    @dummy.setter
    def dummy(self, value: int) -> None:
        self._dummy = value


__all__ = ['ColorProfile']
