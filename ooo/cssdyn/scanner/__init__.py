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
    from ...dyn.scanner.scan_error import ScanError as ScanError
with suppress(ImportError):
    from ...dyn.scanner.scanner_context import ScannerContext as ScannerContext
with suppress(ImportError):
    from ...dyn.scanner.scanner_exception import ScannerException as ScannerException
with suppress(ImportError):
    from ...dyn.scanner.scanner_manager import ScannerManager as ScannerManager
with suppress(ImportError):
    from ...dyn.scanner.x_scanner_manager import XScannerManager as XScannerManager
with suppress(ImportError):
    from ...dyn.scanner.x_scanner_manager2 import XScannerManager2 as XScannerManager2
