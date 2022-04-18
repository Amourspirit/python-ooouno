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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from .x_dialog_provider import XDialogProvider as XDialogProvider_c70f0c47
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..frame.x_model import XModel as XModel_7a6e095c
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..script.x_script_listener import XScriptListener as XScriptListener_f20b0db0

class DialogProvider(XDialogProvider_c70f0c47):
    """
    Service Class

    Specifies a provider for dialogs implementing the com.sun.star.awt.XDialog interface.

    See Also:
        `API DialogProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1DialogProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.DialogProvider'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithModel(self, Model: 'XModel_7a6e095c') -> None:
        """
        """
    @abstractmethod
    def createWithModelAndScripting(self, Model: 'XModel_7a6e095c', InStream: 'XInputStream_98d40ab4', DialogLib: 'XNameContainer_cb90e47', ScriptListener: 'XScriptListener_f20b0db0') -> None:
        """
        """


__all__ = ['DialogProvider']

