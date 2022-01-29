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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
import typing
from abc import abstractproperty
from ..uno.exception import Exception as Exception_85530a09
if typing.TYPE_CHECKING:
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class UnsupportedDataSinkException(Exception_85530a09):
    """
    This exception is used to indicate that the requested type of data sink is not supported.
    
    For example, each OpenCommandArgument supplied as argument of the command \"open\" contains such a data sink.

    See Also:
        `API UnsupportedDataSinkException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1UnsupportedDataSinkException.html>`_
    """

    @abstractproperty
    def Sink(self) -> 'XInterface_8f010a43':
        """
        contains the data sink that is not supported.
        """

