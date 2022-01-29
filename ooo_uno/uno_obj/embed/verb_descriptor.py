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
# Namespace: com.sun.star.embed
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class VerbDescriptor(object):
    """
    Struct Class

    describes a verb.

    See Also:
        `API VerbDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1embed_1_1VerbDescriptor.html>`_


    Note:
        | At runtime VerbDescriptor will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | VerbDescriptor is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, VerbAttributes: typing.Optional[int] = None, VerbFlags: typing.Optional[int] = None, VerbID: typing.Optional[int] = None, VerbName: typing.Optional[str] = None):
        self._verb_attributes = VerbAttributes
        self._verb_flags = VerbFlags
        self._verb_id = VerbID
        self._verb_name = VerbName

    @property
    def VerbAttributes(self) -> int:
        """
        specifies the attributes of the verb.
        
        It can take values from VerbAttributes.
        """
        return self._verb_attributes
    
    @VerbAttributes.setter
    def VerbAttributes(self, value: int) -> None:
        self._verb_attributes = value

    @property
    def VerbFlags(self) -> int:
        """
        specifies the flags that are set for the verb.
        
        The flags can be used to build the verb's menu.
        """
        return self._verb_flags
    
    @VerbFlags.setter
    def VerbFlags(self, value: int) -> None:
        self._verb_flags = value

    @property
    def VerbID(self) -> int:
        """
        specifies the id of the verb.
        """
        return self._verb_id
    
    @VerbID.setter
    def VerbID(self, value: int) -> None:
        self._verb_id = value

    @property
    def VerbName(self) -> str:
        """
        specifies the name of the verb.
        """
        return self._verb_name
    
    @VerbName.setter
    def VerbName(self, value: str) -> None:
        self._verb_name = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global VerbDescriptor
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('VerbAttributes', 'VerbFlags', 'VerbID', 'VerbName')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.embed.VerbDescriptor')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        VerbDescriptor = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['VerbDescriptor']
