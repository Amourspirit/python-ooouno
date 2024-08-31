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
    from ...dyn.task.async_job import AsyncJob as AsyncJob
with suppress(ImportError):
    from ...dyn.task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest
with suppress(ImportError):
    from ...dyn.task.document_ms_password_request import DocumentMSPasswordRequest as DocumentMSPasswordRequest
with suppress(ImportError):
    from ...dyn.task.document_ms_password_request2 import DocumentMSPasswordRequest2 as DocumentMSPasswordRequest2
with suppress(ImportError):
    from ...dyn.task.document_macro_confirmation_request import DocumentMacroConfirmationRequest as DocumentMacroConfirmationRequest
with suppress(ImportError):
    from ...dyn.task.document_password_request import DocumentPasswordRequest as DocumentPasswordRequest
with suppress(ImportError):
    from ...dyn.task.document_password_request2 import DocumentPasswordRequest2 as DocumentPasswordRequest2
with suppress(ImportError):
    from ...dyn.task.error_code_io_exception import ErrorCodeIOException as ErrorCodeIOException
with suppress(ImportError):
    from ...dyn.task.error_code_request import ErrorCodeRequest as ErrorCodeRequest
with suppress(ImportError):
    from ...dyn.task.error_code_request2 import ErrorCodeRequest2 as ErrorCodeRequest2
with suppress(ImportError):
    from ...dyn.task.interaction_classification import InteractionClassification as InteractionClassification
with suppress(ImportError):
    from ...dyn.task.interaction_handler import InteractionHandler as InteractionHandler
with suppress(ImportError):
    from ...dyn.task.interaction_request_string_resolver import InteractionRequestStringResolver as InteractionRequestStringResolver
with suppress(ImportError):
    from ...dyn.task.job import Job as Job
with suppress(ImportError):
    from ...dyn.task.job_executor import JobExecutor as JobExecutor
with suppress(ImportError):
    from ...dyn.task.master_password_request import MasterPasswordRequest as MasterPasswordRequest
with suppress(ImportError):
    from ...dyn.task.no_master_exception import NoMasterException as NoMasterException
with suppress(ImportError):
    from ...dyn.task.office_restart_manager import OfficeRestartManager as OfficeRestartManager
with suppress(ImportError):
    from ...dyn.task.pdf_export_exception import PDFExportException as PDFExportException
with suppress(ImportError):
    from ...dyn.task.password_container import PasswordContainer as PasswordContainer
with suppress(ImportError):
    from ...dyn.task.password_container_interaction_handler import PasswordContainerInteractionHandler as PasswordContainerInteractionHandler
with suppress(ImportError):
    from ...dyn.task.password_request import PasswordRequest as PasswordRequest
with suppress(ImportError):
    from ...dyn.task.password_request_mode import PasswordRequestMode as PasswordRequestMode
with suppress(ImportError):
    from ...dyn.task.status_indicator_factory import StatusIndicatorFactory as StatusIndicatorFactory
with suppress(ImportError):
    from ...dyn.task.unsupported_overwrite_request import UnsupportedOverwriteRequest as UnsupportedOverwriteRequest
with suppress(ImportError):
    from ...dyn.task.url_record import UrlRecord as UrlRecord
with suppress(ImportError):
    from ...dyn.task.user_record import UserRecord as UserRecord
with suppress(ImportError):
    from ...dyn.task.x_abort_channel import XAbortChannel as XAbortChannel
with suppress(ImportError):
    from ...dyn.task.x_async_job import XAsyncJob as XAsyncJob
with suppress(ImportError):
    from ...dyn.task.x_interaction_abort import XInteractionAbort as XInteractionAbort
with suppress(ImportError):
    from ...dyn.task.x_interaction_approve import XInteractionApprove as XInteractionApprove
with suppress(ImportError):
    from ...dyn.task.x_interaction_ask_later import XInteractionAskLater as XInteractionAskLater
with suppress(ImportError):
    from ...dyn.task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation
with suppress(ImportError):
    from ...dyn.task.x_interaction_disapprove import XInteractionDisapprove as XInteractionDisapprove
with suppress(ImportError):
    from ...dyn.task.x_interaction_handler import XInteractionHandler as XInteractionHandler
with suppress(ImportError):
    from ...dyn.task.x_interaction_handler2 import XInteractionHandler2 as XInteractionHandler2
with suppress(ImportError):
    from ...dyn.task.x_interaction_password import XInteractionPassword as XInteractionPassword
with suppress(ImportError):
    from ...dyn.task.x_interaction_password2 import XInteractionPassword2 as XInteractionPassword2
with suppress(ImportError):
    from ...dyn.task.x_interaction_request import XInteractionRequest as XInteractionRequest
with suppress(ImportError):
    from ...dyn.task.x_interaction_request_string_resolver import XInteractionRequestStringResolver as XInteractionRequestStringResolver
with suppress(ImportError):
    from ...dyn.task.x_interaction_retry import XInteractionRetry as XInteractionRetry
with suppress(ImportError):
    from ...dyn.task.x_job import XJob as XJob
with suppress(ImportError):
    from ...dyn.task.x_job_executor import XJobExecutor as XJobExecutor
with suppress(ImportError):
    from ...dyn.task.x_job_listener import XJobListener as XJobListener
with suppress(ImportError):
    from ...dyn.task.x_master_password_handling import XMasterPasswordHandling as XMasterPasswordHandling
with suppress(ImportError):
    from ...dyn.task.x_master_password_handling2 import XMasterPasswordHandling2 as XMasterPasswordHandling2
with suppress(ImportError):
    from ...dyn.task.x_password_container import XPasswordContainer as XPasswordContainer
with suppress(ImportError):
    from ...dyn.task.x_password_container2 import XPasswordContainer2 as XPasswordContainer2
with suppress(ImportError):
    from ...dyn.task.x_restart_manager import XRestartManager as XRestartManager
with suppress(ImportError):
    from ...dyn.task.x_status_indicator import XStatusIndicator as XStatusIndicator
with suppress(ImportError):
    from ...dyn.task.x_status_indicator_factory import XStatusIndicatorFactory as XStatusIndicatorFactory
with suppress(ImportError):
    from ...dyn.task.x_status_indicator_supplier import XStatusIndicatorSupplier as XStatusIndicatorSupplier
with suppress(ImportError):
    from ...dyn.task.x_url_container import XUrlContainer as XUrlContainer
with suppress(ImportError):
    from ...dyn.task.the_job_executor import theJobExecutor as theJobExecutor
