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
    from ....dyn.packages.zip.x_zip_file_access import XZipFileAccess as XZipFileAccess
except ImportError:
    pass
try:
    from ....dyn.packages.zip.x_zip_file_access2 import XZipFileAccess2 as XZipFileAccess2
except ImportError:
    pass
try:
    from ....dyn.packages.zip.zip_constants import ZipConstants as ZipConstants
except ImportError:
    pass
try:
    from ....dyn.packages.zip.zip_constants import ZipConstantsEnum as ZipConstantsEnum
except ImportError:
    pass
try:
    from ....dyn.packages.zip.zip_entry import ZipEntry as ZipEntry
except ImportError:
    pass
try:
    from ....dyn.packages.zip.zip_exception import ZipException as ZipException
except ImportError:
    pass
try:
    from ....dyn.packages.zip.zip_file_access import ZipFileAccess as ZipFileAccess
except ImportError:
    pass
try:
    from ....dyn.packages.zip.zip_io_exception import ZipIOException as ZipIOException
except ImportError:
    pass
