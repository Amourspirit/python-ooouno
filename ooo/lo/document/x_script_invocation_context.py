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
# Namespace: com.sun.star.document
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts_1ab50eb1

class XScriptInvocationContext(ABC):
    """
    indicates support for executing scripts contained in a, possibly foreign, document.
    
    If the component implementing it is a document, which supports embedding scripts into itself, then ScriptContainer refers to the document itself. Implementing this interface is unnecessary then, instead the document should simply implement XEmbeddedScripts directly.
    
    If the interface is implemented by a document which does not itself support embedding scripts into it, but which is associated unambiguously with a document which does, then this other document is denoted by ScriptContainer.
    
    If the interface is implemented by a controller, then ScriptContainer refers to the document which supports embedding scripts, and which is unambiguously associated with the controller. This must not necessarily be the model returned by com.sun.star.frame.XController.getModel().
    
    **since**
    
        OOo 2.4

    See Also:
        `API XScriptInvocationContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XScriptInvocationContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XScriptInvocationContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XScriptInvocationContext'

    @abstractproperty
    def ScriptContainer(self) -> 'XEmbeddedScripts_1ab50eb1':
        """
        denotes the document which contains the scripts which are to be invoked from the component implementing the XScriptInvocationContext interface.
        """
        ...


__all__ = ['XScriptInvocationContext']

