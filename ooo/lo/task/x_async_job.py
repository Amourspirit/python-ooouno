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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.task
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from .x_job_listener import XJobListener as XJobListener_af600b74

class XAsyncJob(XInterface_8f010a43):
    """
    specifies a job which must be executed asynchronously
    
    Instead of XJob the implementation of this interface must be aware, that execution can be made real asynchronous (e.g. by using threads). Because the environment wish to have creation and using of threads under control, it's not allowed for a real job implementation to use such mechanism by itself. The outside code decide, if it's possible and how it can be made asynchronous. In some special cases it can be, that asynchronous jobs will be executed synchronously.

    See Also:
        `API XAsyncJob <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XAsyncJob.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XAsyncJob'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XAsyncJob'

    @abstractmethod
    def executeAsync(self, Arguments: 'typing.Tuple[NamedValue_a37a0af3, ...]', Listener: 'XJobListener_af600b74') -> None:
        """
        executes the job asynchronously

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """


__all__ = ['XAsyncJob']

