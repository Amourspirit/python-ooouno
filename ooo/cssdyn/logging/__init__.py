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
    from ...dyn.logging.console_handler import ConsoleHandler as ConsoleHandler
except ImportError:
    pass
try:
    from ...dyn.logging.csv_log_formatter import CsvLogFormatter as CsvLogFormatter
except ImportError:
    pass
try:
    from ...dyn.logging.file_handler import FileHandler as FileHandler
except ImportError:
    pass
try:
    from ...dyn.logging.log_level import LogLevel as LogLevel
except ImportError:
    pass
try:
    from ...dyn.logging.log_level import LogLevelEnum as LogLevelEnum
except ImportError:
    pass
try:
    from ...dyn.logging.log_record import LogRecord as LogRecord
except ImportError:
    pass
try:
    from ...dyn.logging.logger_pool import LoggerPool as LoggerPool
except ImportError:
    pass
try:
    from ...dyn.logging.plain_text_formatter import PlainTextFormatter as PlainTextFormatter
except ImportError:
    pass
try:
    from ...dyn.logging.simple_text_formatter import SimpleTextFormatter as SimpleTextFormatter
except ImportError:
    pass
try:
    from ...dyn.logging.x_console_handler import XConsoleHandler as XConsoleHandler
except ImportError:
    pass
try:
    from ...dyn.logging.x_csv_log_formatter import XCsvLogFormatter as XCsvLogFormatter
except ImportError:
    pass
try:
    from ...dyn.logging.x_log_formatter import XLogFormatter as XLogFormatter
except ImportError:
    pass
try:
    from ...dyn.logging.x_log_handler import XLogHandler as XLogHandler
except ImportError:
    pass
try:
    from ...dyn.logging.x_logger import XLogger as XLogger
except ImportError:
    pass
try:
    from ...dyn.logging.x_logger_pool import XLoggerPool as XLoggerPool
except ImportError:
    pass
