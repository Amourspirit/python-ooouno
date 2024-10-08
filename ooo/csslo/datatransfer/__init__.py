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
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from ...lo.datatransfer.data_flavor import DataFlavor as DataFlavor
from ...lo.datatransfer.data_format_translator import DataFormatTranslator as DataFormatTranslator
from ...lo.datatransfer.mime_content_type_factory import MimeContentTypeFactory as MimeContentTypeFactory
from ...lo.datatransfer.unsupported_flavor_exception import UnsupportedFlavorException as UnsupportedFlavorException
from ...lo.datatransfer.x_data_format_translator import XDataFormatTranslator as XDataFormatTranslator
from ...lo.datatransfer.x_mime_content_type import XMimeContentType as XMimeContentType
from ...lo.datatransfer.x_mime_content_type_factory import XMimeContentTypeFactory as XMimeContentTypeFactory
from ...lo.datatransfer.x_system_transferable import XSystemTransferable as XSystemTransferable
from ...lo.datatransfer.x_transfer_data_access import XTransferDataAccess as XTransferDataAccess
from ...lo.datatransfer.x_transferable import XTransferable as XTransferable
from ...lo.datatransfer.x_transferable2 import XTransferable2 as XTransferable2
from ...lo.datatransfer.x_transferable_ex import XTransferableEx as XTransferableEx
from ...lo.datatransfer.x_transferable_source import XTransferableSource as XTransferableSource
from ...lo.datatransfer.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier
from ...lo.datatransfer.x_transferable_text_supplier import XTransferableTextSupplier as XTransferableTextSupplier
