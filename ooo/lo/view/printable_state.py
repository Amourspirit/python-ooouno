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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.view
# Libre Office Version: 7.4
from enum import Enum


class PrintableState(Enum):
    """
    Enum Class

    

    See Also:
        `API PrintableState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#ad9b0afaffefc166344fd9575516b6626>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.PrintableState'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.view.PrintableState'

    JOB_ABORTED = 'JOB_ABORTED'
    """
    printing was aborted (e.g., by the user) while either printing or spooling.
    """
    JOB_COMPLETED = 'JOB_COMPLETED'
    """
    printing (rendering the document) has finished, spooling has begun
    """
    JOB_FAILED = 'JOB_FAILED'
    """
    printing ran into an error.
    """
    JOB_SPOOLED = 'JOB_SPOOLED'
    """
    spooling has finished successfully.
    
    This is the only state that can be considered as \"success\" for a print job.
    """
    JOB_SPOOLING_FAILED = 'JOB_SPOOLING_FAILED'
    """
    the document could be printed but not spooled.
    """
    JOB_STARTED = 'JOB_STARTED'
    """
    printing (rendering the document) has begun
    """

__all__ = ['PrintableState']

