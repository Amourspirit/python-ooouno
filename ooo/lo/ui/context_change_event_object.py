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
# Namespace: com.sun.star.ui
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class ContextChangeEventObject(EventObject_a3d70b03):
    """
    Struct Class


    See Also:
        `API ContextChangeEventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ContextChangeEventObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ContextChangeEventObject'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ui.ContextChangeEventObject'
    """Literal Constant ``com.sun.star.ui.ContextChangeEventObject``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ContextChangeEventObject`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ContextChangeEventObject``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ApplicationName (str, optional): ApplicationName value
            ContextName (str, optional): ContextName value
        """
        self._application_name = None
        self._context_name = None

        key_order = ('ApplicationName', 'ContextName')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ContextChangeEventObject):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ContextChangeEventObject.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def ApplicationName(self) -> str:
        """
        Return the name of the application.
        """
        return self._application_name
    
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None:
        self._application_name = value

    @property
    def ContextName(self) -> str:
        """
        Return the application specific context name.
        """
        return self._context_name
    
    @ContextName.setter
    def ContextName(self, value: str) -> None:
        self._context_name = value


__all__ = ['ContextChangeEventObject']
