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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ....dyn.xml.xpath.libxml2_extension_handle import Libxml2ExtensionHandle as Libxml2ExtensionHandle
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.x_path_api import XPathAPI as XPathAPI
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.x_path_exception import XPathException as XPathException
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.x_path_extension import XPathExtension as XPathExtension
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.x_path_object_type import XPathObjectType as XPathObjectType
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.xx_path_api import XXPathAPI as XXPathAPI
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.xx_path_extension import XXPathExtension as XXPathExtension
except ImportError:
    pass
try:
    from ....dyn.xml.xpath.xx_path_object import XXPathObject as XXPathObject
except ImportError:
    pass
