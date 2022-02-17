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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.bridge
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.bridge import ModelDependent as ModelDependent
else:
    from ...lo.bridge.model_dependent import ModelDependent as ModelDependent


class ModelDependentEnum(IntEnum):
    """
    Enum of Const Class ModelDependent

    These constants are used to specify model-dependent representations.
    
    They are only used for creating bridges to other component models.
    """
    UNO = ModelDependent.UNO
    OLE = ModelDependent.OLE
    JAVA = ModelDependent.JAVA
    CORBA = ModelDependent.CORBA

__all__ = ['ModelDependent', 'ModelDependentEnum']