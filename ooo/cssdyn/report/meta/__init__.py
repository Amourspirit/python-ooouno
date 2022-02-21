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
    from ....dyn.report.meta.x_formula_parser import XFormulaParser as XFormulaParser
except ImportError:
    pass
try:
    from ....dyn.report.meta.x_function_category import XFunctionCategory as XFunctionCategory
except ImportError:
    pass
try:
    from ....dyn.report.meta.x_function_description import XFunctionDescription as XFunctionDescription
except ImportError:
    pass
try:
    from ....dyn.report.meta.x_function_manager import XFunctionManager as XFunctionManager
except ImportError:
    pass
