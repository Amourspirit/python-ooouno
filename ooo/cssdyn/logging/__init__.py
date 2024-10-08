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
    from ...dyn.logging.console_handler import ConsoleHandler as ConsoleHandler
with suppress(ImportError):
    from ...dyn.logging.csv_log_formatter import CsvLogFormatter as CsvLogFormatter
with suppress(ImportError):
    from ...dyn.logging.file_handler import FileHandler as FileHandler
with suppress(ImportError):
    from ...dyn.logging.log_level import LogLevel as LogLevel
with suppress(ImportError):
    from ...dyn.logging.log_level import LogLevelEnum as LogLevelEnum
with suppress(ImportError):
    from ...dyn.logging.log_record import LogRecord as LogRecord
with suppress(ImportError):
    from ...dyn.logging.logger_pool import LoggerPool as LoggerPool
with suppress(ImportError):
    from ...dyn.logging.plain_text_formatter import PlainTextFormatter as PlainTextFormatter
with suppress(ImportError):
    from ...dyn.logging.simple_text_formatter import SimpleTextFormatter as SimpleTextFormatter
with suppress(ImportError):
    from ...dyn.logging.x_console_handler import XConsoleHandler as XConsoleHandler
with suppress(ImportError):
    from ...dyn.logging.x_csv_log_formatter import XCsvLogFormatter as XCsvLogFormatter
with suppress(ImportError):
    from ...dyn.logging.x_log_formatter import XLogFormatter as XLogFormatter
with suppress(ImportError):
    from ...dyn.logging.x_log_handler import XLogHandler as XLogHandler
with suppress(ImportError):
    from ...dyn.logging.x_logger import XLogger as XLogger
with suppress(ImportError):
    from ...dyn.logging.x_logger_pool import XLoggerPool as XLoggerPool
