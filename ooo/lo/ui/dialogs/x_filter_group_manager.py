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
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.dialogs
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...beans.string_pair import StringPair as StringPair_a4bc0b14

class XFilterGroupManager(XInterface_8f010a43):
    """
    Specifies an interface which allows manipulation of groups of filters for the FilePicker service.

    See Also:
        `API XFilterGroupManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilterGroupManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFilterGroupManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFilterGroupManager'

    @abstractmethod
    def appendFilterGroup(self, sGroupTitle: str, aFilters: 'typing.Tuple[StringPair_a4bc0b14, ...]') -> None:
        """
        Appends a group of filters to the current filter list.
        
        It is implementation dependent how the filter groups are presented to the user.
        It is not even guaranteed that the groups are visualized: implementations are free to simply append all the filters separately, with ignoring the group title.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XFilterGroupManager']

