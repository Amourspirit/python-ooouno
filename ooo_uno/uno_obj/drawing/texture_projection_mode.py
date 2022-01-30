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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.drawing.TextureProjectionMode import (OBJECTSPECIFIC, PARALLEL, SPHERE)

if TYPE_CHECKING or _DYNAMIC is False:


    class TextureProjectionMode(Enum):
        """
        Enum Class

        

        See Also:
            `API TextureProjectionMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#ae1e109a5c70543e3b92db3b854fd3acb>`_
        """
        OBJECTSPECIFIC = 'OBJECTSPECIFIC'
        """
        This value specifies that the standard object projection method is used.
        """
        PARALLEL = 'PARALLEL'
        """
        the 3D objects are drawn in the parallel projection.
        
        This value specifies a flat parallel projection in the specified degree of freedom (X or Y).
        """
        SPHERE = 'SPHERE'
        """
        forces normals to think that the object is a sphere.
        
        This value forces projection to wrapping in X and/or Y.
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global TextureProjectionMode
        _dict = {
            "OBJECTSPECIFIC": OBJECTSPECIFIC,
            "PARALLEL": PARALLEL,
            "SPHERE": SPHERE,
        }

        TextureProjectionMode = type('TextureProjectionMode', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(TextureProjectionMode, k, v)

    _dynamic_enum()

__all__ = ['TextureProjectionMode']

