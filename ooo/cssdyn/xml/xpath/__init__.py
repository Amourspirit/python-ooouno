# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ....dyn.xml.xpath.libxml2_extension_handle import Libxml2ExtensionHandle as Libxml2ExtensionHandle
with suppress(ImportError):
    from ....dyn.xml.xpath.x_path_api import XPathAPI as XPathAPI
with suppress(ImportError):
    from ....dyn.xml.xpath.x_path_exception import XPathException as XPathException
with suppress(ImportError):
    from ....dyn.xml.xpath.x_path_extension import XPathExtension as XPathExtension
with suppress(ImportError):
    from ....dyn.xml.xpath.x_path_object_type import XPathObjectType as XPathObjectType
with suppress(ImportError):
    from ....dyn.xml.xpath.xx_path_api import XXPathAPI as XXPathAPI
with suppress(ImportError):
    from ....dyn.xml.xpath.xx_path_extension import XXPathExtension as XXPathExtension
with suppress(ImportError):
    from ....dyn.xml.xpath.xx_path_object import XXPathObject as XXPathObject
