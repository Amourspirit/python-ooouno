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
# Libre Office Version: 7.2
# Namespace: com.sun.star.xml.xpath
import typing
from abc import abstractmethod
from .xx_path_extension import XXPathExtension as XXPathExtension_194c0ea6
if typing.TYPE_CHECKING:
    from ...xforms.x_model import XModel as XModel_865909f0
    from ..dom.x_node import XNode as XNode_83fb09a5

class XPathExtension(XXPathExtension_194c0ea6):
    """
    Service Class


    See Also:
        `API XPathExtension <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1xpath_1_1XPathExtension.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.xpath'
    __ooo_full_ns__: str = 'com.sun.star.xml.xpath.XPathExtension'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithModel(self, Model: 'XModel_865909f0', ContextNode: 'XNode_83fb09a5') -> None:
        """
        """

__all__ = ['XPathExtension']

