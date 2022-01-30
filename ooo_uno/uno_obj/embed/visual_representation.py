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
import typing
if typing.TYPE_CHECKING:
    from ..datatransfer.data_flavor import DataFlavor as DataFlavor_ffd30deb
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class VisualRepresentation(object):
        """
        Struct Class

        can contain a graphical representation in an arbitrary format.

        See Also:
            `API VisualRepresentation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1embed_1_1VisualRepresentation.html>`_


        Note:
            | At runtime VisualRepresentation will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | VisualRepresentation is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Data: typing.Optional[object] = None, Flavor: 'typing.Optional[DataFlavor_ffd30deb]' = None):
            self._data = Data
            self._flavor = Flavor

        @property
        def Data(self) -> object:
            """
            The data in the format specified by Flavor.
            """
            return self._data
        
        @Data.setter
        def Data(self, value: object) -> None:
            self._data = value

        @property
        def Flavor(self) -> 'DataFlavor_ffd30deb':
            """
            The format of the visual representation.
            """
            return self._flavor
        
        @Flavor.setter
        def Flavor(self, value: 'DataFlavor_ffd30deb') -> None:
            self._flavor = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global VisualRepresentation
        order = ('Data', 'Flavor')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.embed.VisualRepresentation')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        VisualRepresentation = _struct_init

    _dynamic_struct()

__all__ = ['VisualRepresentation']
