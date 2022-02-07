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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2


class AliasProgrammaticPair(object):
    """
    Struct Class

    represents an entry from a component which implements the XLocalizedAliases.

    See Also:
        `API AliasProgrammaticPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1AliasProgrammaticPair.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.AliasProgrammaticPair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.AliasProgrammaticPair'
    """Literal Constant ``com.sun.star.util.AliasProgrammaticPair``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``AliasProgrammaticPair`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``AliasProgrammaticPair``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Alias (str, optional): Alias value
            ProgrammaticName (str, optional): ProgrammaticName value
        """
        self._alias = None
        self._programmatic_name = None

        key_order = ('Alias', 'ProgrammaticName')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], AliasProgrammaticPair):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("AliasProgrammaticPair.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Alias(self) -> str:
        """
        determines the name which is registered as an alias for a programmatic name.
        """
        return self._alias
    
    @Alias.setter
    def Alias(self, value: str) -> None:
        self._alias = value

    @property
    def ProgrammaticName(self) -> str:
        """
        determines which programmatic name belongs to the alias.
        """
        return self._programmatic_name
    
    @ProgrammaticName.setter
    def ProgrammaticName(self, value: str) -> None:
        self._programmatic_name = value


__all__ = ['AliasProgrammaticPair']
