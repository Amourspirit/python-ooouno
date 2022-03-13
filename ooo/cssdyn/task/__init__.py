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
    from ...dyn.task.async_job import AsyncJob as AsyncJob
except ImportError:
    pass
try:
    from ...dyn.task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest
except ImportError:
    pass
try:
    from ...dyn.task.document_ms_password_request import DocumentMSPasswordRequest as DocumentMSPasswordRequest
except ImportError:
    pass
try:
    from ...dyn.task.document_ms_password_request2 import DocumentMSPasswordRequest2 as DocumentMSPasswordRequest2
except ImportError:
    pass
try:
    from ...dyn.task.document_macro_confirmation_request import DocumentMacroConfirmationRequest as DocumentMacroConfirmationRequest
except ImportError:
    pass
try:
    from ...dyn.task.document_password_request import DocumentPasswordRequest as DocumentPasswordRequest
except ImportError:
    pass
try:
    from ...dyn.task.document_password_request2 import DocumentPasswordRequest2 as DocumentPasswordRequest2
except ImportError:
    pass
try:
    from ...dyn.task.error_code_io_exception import ErrorCodeIOException as ErrorCodeIOException
except ImportError:
    pass
try:
    from ...dyn.task.error_code_request import ErrorCodeRequest as ErrorCodeRequest
except ImportError:
    pass
try:
    from ...dyn.task.interaction_classification import InteractionClassification as InteractionClassification
except ImportError:
    pass
try:
    from ...dyn.task.interaction_handler import InteractionHandler as InteractionHandler
except ImportError:
    pass
try:
    from ...dyn.task.interaction_request_string_resolver import InteractionRequestStringResolver as InteractionRequestStringResolver
except ImportError:
    pass
try:
    from ...dyn.task.job import Job as Job
except ImportError:
    pass
try:
    from ...dyn.task.job_executor import JobExecutor as JobExecutor
except ImportError:
    pass
try:
    from ...dyn.task.master_password_request import MasterPasswordRequest as MasterPasswordRequest
except ImportError:
    pass
try:
    from ...dyn.task.no_master_exception import NoMasterException as NoMasterException
except ImportError:
    pass
try:
    from ...dyn.task.office_restart_manager import OfficeRestartManager as OfficeRestartManager
except ImportError:
    pass
try:
    from ...dyn.task.pdf_export_exception import PDFExportException as PDFExportException
except ImportError:
    pass
try:
    from ...dyn.task.password_container import PasswordContainer as PasswordContainer
except ImportError:
    pass
try:
    from ...dyn.task.password_container_interaction_handler import PasswordContainerInteractionHandler as PasswordContainerInteractionHandler
except ImportError:
    pass
try:
    from ...dyn.task.password_request import PasswordRequest as PasswordRequest
except ImportError:
    pass
try:
    from ...dyn.task.password_request_mode import PasswordRequestMode as PasswordRequestMode
except ImportError:
    pass
try:
    from ...dyn.task.status_indicator_factory import StatusIndicatorFactory as StatusIndicatorFactory
except ImportError:
    pass
try:
    from ...dyn.task.unsupported_overwrite_request import UnsupportedOverwriteRequest as UnsupportedOverwriteRequest
except ImportError:
    pass
try:
    from ...dyn.task.url_record import UrlRecord as UrlRecord
except ImportError:
    pass
try:
    from ...dyn.task.user_record import UserRecord as UserRecord
except ImportError:
    pass
try:
    from ...dyn.task.x_abort_channel import XAbortChannel as XAbortChannel
except ImportError:
    pass
try:
    from ...dyn.task.x_async_job import XAsyncJob as XAsyncJob
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_abort import XInteractionAbort as XInteractionAbort
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_approve import XInteractionApprove as XInteractionApprove
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_ask_later import XInteractionAskLater as XInteractionAskLater
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_disapprove import XInteractionDisapprove as XInteractionDisapprove
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_handler import XInteractionHandler as XInteractionHandler
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_handler2 import XInteractionHandler2 as XInteractionHandler2
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_password import XInteractionPassword as XInteractionPassword
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_password2 import XInteractionPassword2 as XInteractionPassword2
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_request import XInteractionRequest as XInteractionRequest
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_request_string_resolver import XInteractionRequestStringResolver as XInteractionRequestStringResolver
except ImportError:
    pass
try:
    from ...dyn.task.x_interaction_retry import XInteractionRetry as XInteractionRetry
except ImportError:
    pass
try:
    from ...dyn.task.x_job import XJob as XJob
except ImportError:
    pass
try:
    from ...dyn.task.x_job_executor import XJobExecutor as XJobExecutor
except ImportError:
    pass
try:
    from ...dyn.task.x_job_listener import XJobListener as XJobListener
except ImportError:
    pass
try:
    from ...dyn.task.x_master_password_handling import XMasterPasswordHandling as XMasterPasswordHandling
except ImportError:
    pass
try:
    from ...dyn.task.x_master_password_handling2 import XMasterPasswordHandling2 as XMasterPasswordHandling2
except ImportError:
    pass
try:
    from ...dyn.task.x_password_container import XPasswordContainer as XPasswordContainer
except ImportError:
    pass
try:
    from ...dyn.task.x_password_container2 import XPasswordContainer2 as XPasswordContainer2
except ImportError:
    pass
try:
    from ...dyn.task.x_restart_manager import XRestartManager as XRestartManager
except ImportError:
    pass
try:
    from ...dyn.task.x_status_indicator import XStatusIndicator as XStatusIndicator
except ImportError:
    pass
try:
    from ...dyn.task.x_status_indicator_factory import XStatusIndicatorFactory as XStatusIndicatorFactory
except ImportError:
    pass
try:
    from ...dyn.task.x_status_indicator_supplier import XStatusIndicatorSupplier as XStatusIndicatorSupplier
except ImportError:
    pass
try:
    from ...dyn.task.x_url_container import XUrlContainer as XUrlContainer
except ImportError:
    pass
try:
    from ...dyn.task.the_job_executor import theJobExecutor as theJobExecutor
except ImportError:
    pass
