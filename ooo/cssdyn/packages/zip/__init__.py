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
    from ....dyn.packages.zip.x_zip_file_access import XZipFileAccess as XZipFileAccess
with suppress(ImportError):
    from ....dyn.packages.zip.x_zip_file_access2 import XZipFileAccess2 as XZipFileAccess2
with suppress(ImportError):
    from ....dyn.packages.zip.zip_constants import ZipConstants as ZipConstants
with suppress(ImportError):
    from ....dyn.packages.zip.zip_constants import ZipConstantsEnum as ZipConstantsEnum
with suppress(ImportError):
    from ....dyn.packages.zip.zip_entry import ZipEntry as ZipEntry
with suppress(ImportError):
    from ....dyn.packages.zip.zip_exception import ZipException as ZipException
with suppress(ImportError):
    from ....dyn.packages.zip.zip_file_access import ZipFileAccess as ZipFileAccess
with suppress(ImportError):
    from ....dyn.packages.zip.zip_io_exception import ZipIOException as ZipIOException
