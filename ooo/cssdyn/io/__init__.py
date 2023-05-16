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
    from ...dyn.io.already_connected_exception import AlreadyConnectedException as AlreadyConnectedException
with suppress(ImportError):
    from ...dyn.io.buffer_size_exceeded_exception import BufferSizeExceededException as BufferSizeExceededException
with suppress(ImportError):
    from ...dyn.io.connect_exception import ConnectException as ConnectException
with suppress(ImportError):
    from ...dyn.io.data_input_stream import DataInputStream as DataInputStream
with suppress(ImportError):
    from ...dyn.io.data_output_stream import DataOutputStream as DataOutputStream
with suppress(ImportError):
    from ...dyn.io.data_transfer_event import DataTransferEvent as DataTransferEvent
with suppress(ImportError):
    from ...dyn.io.file_permission import FilePermission as FilePermission
with suppress(ImportError):
    from ...dyn.io.io_exception import IOException as IOException
with suppress(ImportError):
    from ...dyn.io.markable_input_stream import MarkableInputStream as MarkableInputStream
with suppress(ImportError):
    from ...dyn.io.markable_output_stream import MarkableOutputStream as MarkableOutputStream
with suppress(ImportError):
    from ...dyn.io.no_route_to_host_exception import NoRouteToHostException as NoRouteToHostException
with suppress(ImportError):
    from ...dyn.io.not_connected_exception import NotConnectedException as NotConnectedException
with suppress(ImportError):
    from ...dyn.io.object_input_stream import ObjectInputStream as ObjectInputStream
with suppress(ImportError):
    from ...dyn.io.object_output_stream import ObjectOutputStream as ObjectOutputStream
with suppress(ImportError):
    from ...dyn.io.pipe import Pipe as Pipe
with suppress(ImportError):
    from ...dyn.io.pump import Pump as Pump
with suppress(ImportError):
    from ...dyn.io.sequence_input_stream import SequenceInputStream as SequenceInputStream
with suppress(ImportError):
    from ...dyn.io.sequence_output_stream import SequenceOutputStream as SequenceOutputStream
with suppress(ImportError):
    from ...dyn.io.socket_exception import SocketException as SocketException
with suppress(ImportError):
    from ...dyn.io.temp_file import TempFile as TempFile
with suppress(ImportError):
    from ...dyn.io.text_input_stream import TextInputStream as TextInputStream
with suppress(ImportError):
    from ...dyn.io.text_output_stream import TextOutputStream as TextOutputStream
with suppress(ImportError):
    from ...dyn.io.unexpected_eof_exception import UnexpectedEOFException as UnexpectedEOFException
with suppress(ImportError):
    from ...dyn.io.unknown_host_exception import UnknownHostException as UnknownHostException
with suppress(ImportError):
    from ...dyn.io.wrong_format_exception import WrongFormatException as WrongFormatException
with suppress(ImportError):
    from ...dyn.io.x_active_data_control import XActiveDataControl as XActiveDataControl
with suppress(ImportError):
    from ...dyn.io.x_active_data_sink import XActiveDataSink as XActiveDataSink
with suppress(ImportError):
    from ...dyn.io.x_active_data_source import XActiveDataSource as XActiveDataSource
with suppress(ImportError):
    from ...dyn.io.x_active_data_streamer import XActiveDataStreamer as XActiveDataStreamer
with suppress(ImportError):
    from ...dyn.io.x_async_output_monitor import XAsyncOutputMonitor as XAsyncOutputMonitor
with suppress(ImportError):
    from ...dyn.io.x_connectable import XConnectable as XConnectable
with suppress(ImportError):
    from ...dyn.io.x_data_exporter import XDataExporter as XDataExporter
with suppress(ImportError):
    from ...dyn.io.x_data_importer import XDataImporter as XDataImporter
with suppress(ImportError):
    from ...dyn.io.x_data_input_stream import XDataInputStream as XDataInputStream
with suppress(ImportError):
    from ...dyn.io.x_data_output_stream import XDataOutputStream as XDataOutputStream
with suppress(ImportError):
    from ...dyn.io.x_data_transfer_event_listener import XDataTransferEventListener as XDataTransferEventListener
with suppress(ImportError):
    from ...dyn.io.x_input_stream import XInputStream as XInputStream
with suppress(ImportError):
    from ...dyn.io.x_input_stream_provider import XInputStreamProvider as XInputStreamProvider
with suppress(ImportError):
    from ...dyn.io.x_markable_stream import XMarkableStream as XMarkableStream
with suppress(ImportError):
    from ...dyn.io.x_object_input_stream import XObjectInputStream as XObjectInputStream
with suppress(ImportError):
    from ...dyn.io.x_object_output_stream import XObjectOutputStream as XObjectOutputStream
with suppress(ImportError):
    from ...dyn.io.x_output_stream import XOutputStream as XOutputStream
with suppress(ImportError):
    from ...dyn.io.x_persist import XPersist as XPersist
with suppress(ImportError):
    from ...dyn.io.x_persist_object import XPersistObject as XPersistObject
with suppress(ImportError):
    from ...dyn.io.x_pipe import XPipe as XPipe
with suppress(ImportError):
    from ...dyn.io.x_seekable import XSeekable as XSeekable
with suppress(ImportError):
    from ...dyn.io.x_seekable_input_stream import XSeekableInputStream as XSeekableInputStream
with suppress(ImportError):
    from ...dyn.io.x_sequence_output_stream import XSequenceOutputStream as XSequenceOutputStream
with suppress(ImportError):
    from ...dyn.io.x_stream import XStream as XStream
with suppress(ImportError):
    from ...dyn.io.x_stream_listener import XStreamListener as XStreamListener
with suppress(ImportError):
    from ...dyn.io.x_temp_file import XTempFile as XTempFile
with suppress(ImportError):
    from ...dyn.io.x_text_input_stream import XTextInputStream as XTextInputStream
with suppress(ImportError):
    from ...dyn.io.x_text_input_stream2 import XTextInputStream2 as XTextInputStream2
with suppress(ImportError):
    from ...dyn.io.x_text_output_stream import XTextOutputStream as XTextOutputStream
with suppress(ImportError):
    from ...dyn.io.x_text_output_stream2 import XTextOutputStream2 as XTextOutputStream2
with suppress(ImportError):
    from ...dyn.io.x_truncate import XTruncate as XTruncate
with suppress(ImportError):
    from ...dyn.io.xxml_extractor import XXMLExtractor as XXMLExtractor
