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
    from ...dyn.datatransfer.data_flavor import DataFlavor as DataFlavor
except ImportError:
    pass
try:
    from ...dyn.datatransfer.data_format_translator import DataFormatTranslator as DataFormatTranslator
except ImportError:
    pass
try:
    from ...dyn.datatransfer.mime_content_type_factory import MimeContentTypeFactory as MimeContentTypeFactory
except ImportError:
    pass
try:
    from ...dyn.datatransfer.unsupported_flavor_exception import UnsupportedFlavorException as UnsupportedFlavorException
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_data_format_translator import XDataFormatTranslator as XDataFormatTranslator
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_mime_content_type import XMimeContentType as XMimeContentType
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_mime_content_type_factory import XMimeContentTypeFactory as XMimeContentTypeFactory
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_system_transferable import XSystemTransferable as XSystemTransferable
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transfer_data_access import XTransferDataAccess as XTransferDataAccess
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transferable import XTransferable as XTransferable
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transferable2 import XTransferable2 as XTransferable2
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transferable_ex import XTransferableEx as XTransferableEx
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transferable_source import XTransferableSource as XTransferableSource
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
except ImportError:
    pass
try:
    from ...dyn.datatransfer.x_transferable_text_supplier import XTransferableTextSupplier as XTransferableTextSupplier
except ImportError:
    pass
