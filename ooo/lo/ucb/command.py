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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2


class Command(object):
    """
    Struct Class

    contains a command.

    See Also:
        `API Command <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Command.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.Command'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.Command'
    """Literal Constant ``com.sun.star.ucb.Command``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``Command`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``Command``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Name (str, optional): Name value
            Handle (int, optional): Handle value
            Argument (object, optional): Argument value
        """
        self._name = None
        self._handle = None
        self._argument = None

        key_order = ('Name', 'Handle', 'Argument')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], Command):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("Command.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Name(self) -> str:
        """
        contains the name of the command.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Handle(self) -> int:
        """
        contains an implementation specific handle for the command.
        
        It must be -1 if the implementation has no handle. 0 is a valid command handle.
        """
        return self._handle
    
    @Handle.setter
    def Handle(self, value: int) -> None:
        self._handle = value

    @property
    def Argument(self) -> object:
        """
        contains the argument of the command
        """
        return self._argument
    
    @Argument.setter
    def Argument(self, value: object) -> None:
        self._argument = value


__all__ = ['Command']
