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
# Namespace: com.sun.star.uri
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..util.x_macro_expander import XMacroExpander as XMacroExpander_c8360c47

class XVndSunStarExpandUrl(ABC):
    """
    represents absolute “vnd.sun.star.expand” URLs.
    
    These URLs are of the form   vnd-sun-star-expand-url = \"VND.SUN.STAR.EXPAND:\" opaque_partwhere the opaque_part is a UTF-8 string as described in Bootstrap Arguments and Micro Deployment. See RFC 3986 RFC 2234 for details.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XVndSunStarExpandUrl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uri_1_1XVndSunStarExpandUrl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uri'
    __ooo_full_ns__: str = 'com.sun.star.uri.XVndSunStarExpandUrl'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uri.XVndSunStarExpandUrl'

    @abstractmethod
    def expand(self, expander: 'XMacroExpander_c8360c47') -> str:
        """
        returns the expanded content of this URL.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XVndSunStarExpandUrl']

