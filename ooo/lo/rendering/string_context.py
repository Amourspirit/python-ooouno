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


class StringContext(object):
    """
    Struct Class

    Collection of string-related arguments used on all canvas text interfaces.
    
    A possibly much larger string than later rendered is necessary here, because in several languages, glyph selection is context dependent.
    
    **since**
    
        OOo 2.0

    See Also:
        `API StringContext <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1StringContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.StringContext'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.StringContext'
    """Literal Constant ``com.sun.star.rendering.StringContext``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``StringContext`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``StringContext``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Text (str, optional): Text value
            StartPosition (int, optional): StartPosition value
            Length (int, optional): Length value
        """
        self._text = None
        self._start_position = None
        self._length = None

        key_order = ('Text', 'StartPosition', 'Length')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], StringContext):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("StringContext.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Text(self) -> str:
        """
        The complete text, from which a subset is selected by the parameters below.
        """
        return self._text
    
    @Text.setter
    def Text(self, value: str) -> None:
        self._text = value

    @property
    def StartPosition(self) -> int:
        """
        Start position within the string.
        
        The first character has index 0.
        """
        return self._start_position
    
    @StartPosition.setter
    def StartPosition(self, value: int) -> None:
        self._start_position = value

    @property
    def Length(self) -> int:
        """
        Length of the substring to actually use.
        
        Must be within the range [0,INTMAX].
        """
        return self._length
    
    @Length.setter
    def Length(self, value: int) -> None:
        self._length = value


__all__ = ['StringContext']
