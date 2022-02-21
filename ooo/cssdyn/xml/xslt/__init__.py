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
    from ....dyn.xml.xslt.xslt2_transformer import XSLT2Transformer as XSLT2Transformer
except ImportError:
    pass
try:
    from ....dyn.xml.xslt.xslt_transformer import XSLTTransformer as XSLTTransformer
except ImportError:
    pass
try:
    from ....dyn.xml.xslt.xxslt_transformer import XXSLTTransformer as XXSLTTransformer
except ImportError:
    pass
