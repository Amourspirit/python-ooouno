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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbcx
from abc import abstractmethod, ABC

class XAlterView(ABC):
    """
    implements the possibility to alter aspects of a view's definition
    
    **since**
    
        OOo 2.4

    See Also:
        `API XAlterView <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XAlterView.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XAlterView'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XAlterView'

    @abstractmethod
    def alterCommand(self, NewCommand: str) -> None:
        """
        changes the command which constitutes the view
        
        The operation should be atomic.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """


__all__ = ['XAlterView']

