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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.text
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .text_position import TextPosition as TextPosition_b2ae0bc7


class TextRangeSelection(object):
    """
    Struct Class


    See Also:
        `API TextRangeSelection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextRangeSelection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextRangeSelection'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.text.TextRangeSelection'
    """Literal Constant ``com.sun.star.text.TextRangeSelection``"""

    def __init__(self, Start: typing.Optional[TextPosition_b2ae0bc7] = UNO_NONE, End: typing.Optional[TextPosition_b2ae0bc7] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            Start (TextPosition, optional): Start value.
            End (TextPosition, optional): End value.
        """
        super().__init__()

        if isinstance(Start, TextRangeSelection):
            oth: TextRangeSelection = Start
            self.Start = oth.Start
            self.End = oth.End
            return

        kargs = {
            "Start": Start,
            "End": End,
        }
        if kargs["Start"] is UNO_NONE:
            kargs["Start"] = None
        if kargs["End"] is UNO_NONE:
            kargs["End"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._start = kwargs["Start"]
        self._end = kwargs["End"]


    @property
    def Start(self) -> TextPosition_b2ae0bc7:
        return self._start

    @Start.setter
    def Start(self, value: TextPosition_b2ae0bc7) -> None:
        self._start = value

    @property
    def End(self) -> TextPosition_b2ae0bc7:
        return self._end

    @End.setter
    def End(self, value: TextPosition_b2ae0bc7) -> None:
        self._end = value


__all__ = ['TextRangeSelection']
