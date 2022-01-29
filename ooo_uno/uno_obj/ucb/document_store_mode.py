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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.ucb.DocumentStoreMode import (LOCAL, REMOTE)


class DocumentStoreMode(Enum):
    """
    

    See Also:
        `API DocumentStoreMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#aea1ce806e915d3505569f7679447ecc2>`_
    """
    LOCAL = 'LOCAL'
    """
    Document contents are stored locally.
    """
    REMOTE = 'REMOTE'
    """
    Document contents are not stored locally.
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global DocumentStoreMode
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "LOCAL": LOCAL,
            "REMOTE": REMOTE,
        }
        DocumentStoreMode = type('DocumentStoreMode', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(DocumentStoreMode, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['DocumentStoreMode']

