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
import typing
if typing.TYPE_CHECKING:
    from .ext_alt_name_type import ExtAltNameType as ExtAltNameType_8c0df5


class CertAltNameEntry(object):
    """
    Struct Class

    struct contains a single entry within a Subject Alternative Name Extension of a X509 certificate.

    See Also:
        `API CertAltNameEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1security_1_1CertAltNameEntry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.CertAltNameEntry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.security.CertAltNameEntry'
    """Literal Constant ``com.sun.star.security.CertAltNameEntry``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``CertAltNameEntry`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``CertAltNameEntry``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Type (ExtAltNameType, optional): Type value
            Value (object, optional): Value value
        """
        self._type = None
        self._value = None

        key_order = ('Type', 'Value')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], CertAltNameEntry):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("CertAltNameEntry.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Type(self) -> 'ExtAltNameType_8c0df5':
        """
        defines the type of the value.
        
        With this information you can determine how to interpret the Any value.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: 'ExtAltNameType_8c0df5') -> None:
        self._type = value

    @property
    def Value(self) -> object:
        """
        stores the value of entry.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value


__all__ = ['CertAltNameEntry']
