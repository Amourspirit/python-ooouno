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
# Namespace: com.sun.star.xml.xslt
import typing
from abc import abstractmethod
from .xxslt_transformer import XXSLTTransformer as XXSLTTransformer_17b50e88

class XSLTTransformer(XXSLTTransformer_17b50e88):
    """
    Get unspecified XSLT filter transformer.
    
    It is not safe to expect support for any features except XSLT 1.0 .
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XSLTTransformer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1xslt_1_1XSLTTransformer.html>`_
    """

    @abstractmethod
    def create(self, args: 'typing.List[object]') -> None:
        """
        """

__all__ = ['XSLTTransformer']

