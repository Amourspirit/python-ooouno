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
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .x_async_job import XAsyncJob as XAsyncJob_8eb50a2c

class XJobListener(XEventListener_c7230c4a):
    """
    listener on finish states of asynchronous job execution

    See Also:
        `API XJobListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XJobListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XJobListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XJobListener'

    @abstractmethod
    def jobFinished(self, Job: 'XAsyncJob_8eb50a2c', Result: object) -> None:
        """
        indicates that the job is done
        """

__all__ = ['XJobListener']
