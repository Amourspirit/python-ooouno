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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
import typing
if typing.TYPE_CHECKING:
    from .boundary import Boundary as Boundary_7fe2098c


class TextConversionResult(object):
    """
    Struct Class

    Text conversion result to be used with XTextConversion.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TextConversionResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1TextConversionResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.TextConversionResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.TextConversionResult'
    """Literal Constant ``com.sun.star.i18n.TextConversionResult``"""

    Candidates: typing.TypeAlias = typing.Tuple[str, ...]
    """
    A list of replacement candidates for the first convertible word found in the given text.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``TextConversionResult`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``TextConversionResult``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Boundary (Boundary, optional): Boundary value
        """
        self._boundary = None

        key_order = ('Boundary',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], TextConversionResult):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("TextConversionResult.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Boundary(self) -> 'Boundary_7fe2098c':
        """
        The boundary of the first convertible word in the given text.
        
        If there is no convertible word found in the text, startPos and endPos for Boundary equal 0.
        """
        return self._boundary
    
    @Boundary.setter
    def Boundary(self, value: 'Boundary_7fe2098c') -> None:
        self._boundary = value


__all__ = ['TextConversionResult']
