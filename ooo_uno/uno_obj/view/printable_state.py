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
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.view.PrintableState import (JOB_ABORTED, JOB_COMPLETED, JOB_FAILED, JOB_SPOOLED, JOB_SPOOLING_FAILED, JOB_STARTED)


class PrintableState(Enum):
    """
    

    See Also:
        `API PrintableState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#ad9b0afaffefc166344fd9575516b6626>`_
    """
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

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global PrintableState
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "JOB_ABORTED": JOB_ABORTED,
            "JOB_COMPLETED": JOB_COMPLETED,
            "JOB_FAILED": JOB_FAILED,
            "JOB_SPOOLED": JOB_SPOOLED,
            "JOB_SPOOLING_FAILED": JOB_SPOOLING_FAILED,
            "JOB_STARTED": JOB_STARTED,
        }
        PrintableState = type('PrintableState', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(PrintableState, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['PrintableState']

