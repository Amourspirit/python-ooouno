# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from .x_control import XControl as XControl_7a9c098d
from .x_control_container import XControlContainer as XControlContainer_e22d0d30
from .x_dialog2 import XDialog2 as XDialog2_79cb092e
from .x_top_window import XTopWindow as XTopWindow_8ebb0a57
from .x_window import XWindow as XWindow_713b0924

class XUnoControlDialog(XControl_7a9c098d, XControlContainer_e22d0d30, XDialog2_79cb092e, XTopWindow_8ebb0a57, XWindow_713b0924):
    """
    The interface for the UnoControlDialog service.
    
    This service actually implements a whole whack of interfaces. This is the just the subset that our code needs.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API XUnoControlDialog <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XUnoControlDialog.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XUnoControlDialog'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XUnoControlDialog'


__all__ = ['XUnoControlDialog']

