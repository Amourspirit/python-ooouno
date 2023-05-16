# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
    from ...dyn.packages.encryption_not_allowed_exception import EncryptionNotAllowedException as EncryptionNotAllowedException
with suppress(ImportError):
    from ...dyn.packages.no_encryption_exception import NoEncryptionException as NoEncryptionException
with suppress(ImportError):
    from ...dyn.packages.no_raw_format_exception import NoRawFormatException as NoRawFormatException
with suppress(ImportError):
    from ...dyn.packages.package import Package as Package
with suppress(ImportError):
    from ...dyn.packages.package_encryption import PackageEncryption as PackageEncryption
with suppress(ImportError):
    from ...dyn.packages.package_folder import PackageFolder as PackageFolder
with suppress(ImportError):
    from ...dyn.packages.package_folder_enumeration import PackageFolderEnumeration as PackageFolderEnumeration
with suppress(ImportError):
    from ...dyn.packages.package_stream import PackageStream as PackageStream
with suppress(ImportError):
    from ...dyn.packages.wrong_password_exception import WrongPasswordException as WrongPasswordException
with suppress(ImportError):
    from ...dyn.packages.x_data_sink_encr_support import XDataSinkEncrSupport as XDataSinkEncrSupport
with suppress(ImportError):
    from ...dyn.packages.x_package_encryption import XPackageEncryption as XPackageEncryption
