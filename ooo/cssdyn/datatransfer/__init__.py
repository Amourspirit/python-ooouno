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
    from ...dyn.datatransfer.data_flavor import DataFlavor as DataFlavor
with suppress(ImportError):
    from ...dyn.datatransfer.data_format_translator import DataFormatTranslator as DataFormatTranslator
with suppress(ImportError):
    from ...dyn.datatransfer.mime_content_type_factory import MimeContentTypeFactory as MimeContentTypeFactory
with suppress(ImportError):
    from ...dyn.datatransfer.unsupported_flavor_exception import UnsupportedFlavorException as UnsupportedFlavorException
with suppress(ImportError):
    from ...dyn.datatransfer.x_data_format_translator import XDataFormatTranslator as XDataFormatTranslator
with suppress(ImportError):
    from ...dyn.datatransfer.x_mime_content_type import XMimeContentType as XMimeContentType
with suppress(ImportError):
    from ...dyn.datatransfer.x_mime_content_type_factory import XMimeContentTypeFactory as XMimeContentTypeFactory
with suppress(ImportError):
    from ...dyn.datatransfer.x_system_transferable import XSystemTransferable as XSystemTransferable
with suppress(ImportError):
    from ...dyn.datatransfer.x_transfer_data_access import XTransferDataAccess as XTransferDataAccess
with suppress(ImportError):
    from ...dyn.datatransfer.x_transferable import XTransferable as XTransferable
with suppress(ImportError):
    from ...dyn.datatransfer.x_transferable2 import XTransferable2 as XTransferable2
with suppress(ImportError):
    from ...dyn.datatransfer.x_transferable_ex import XTransferableEx as XTransferableEx
with suppress(ImportError):
    from ...dyn.datatransfer.x_transferable_source import XTransferableSource as XTransferableSource
with suppress(ImportError):
    from ...dyn.datatransfer.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
with suppress(ImportError):
    from ...dyn.datatransfer.x_transferable_text_supplier import XTransferableTextSupplier as XTransferableTextSupplier
