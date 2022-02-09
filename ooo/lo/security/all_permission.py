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
# Namespace: com.sun.star.security
# Libre Office Version: 7.2


class AllPermission(object):
    """
    Struct Class

    The AllPermission is a permission that implies all other permissions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AllPermission <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1security_1_1AllPermission.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.AllPermission'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.security.AllPermission'
    """Literal Constant ``com.sun.star.security.AllPermission``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``AllPermission`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``AllPermission``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            dummy (int, optional): dummy value
        """
        self._dummy = None

        key_order = ('dummy',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], AllPermission):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("AllPermission.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def dummy(self) -> int:
        """
        """
        return self._dummy
    
    @dummy.setter
    def dummy(self, value: int) -> None:
        self._dummy = value


__all__ = ['AllPermission']
