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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, m00 = UNO_NONE, m01 = UNO_NONE, m02 = UNO_NONE, m03 = UNO_NONE, m10 = UNO_NONE, m11 = UNO_NONE, m12 = UNO_NONE, m13 = UNO_NONE, m20 = UNO_NONE, m21 = UNO_NONE, m22 = UNO_NONE, m23 = UNO_NONE):
            if getattr(m00, "__class__", None) == self.__class__:
                orig_init(self, m00)
                return
            else:
                orig_init(self)
            if not m00 is UNO_NONE:
                if getattr(self, 'm00') != m00:
                    setattr(self, 'm00', m00)
            if not m01 is UNO_NONE:
                if getattr(self, 'm01') != m01:
                    setattr(self, 'm01', m01)
            if not m02 is UNO_NONE:
                if getattr(self, 'm02') != m02:
                    setattr(self, 'm02', m02)
            if not m03 is UNO_NONE:
                if getattr(self, 'm03') != m03:
                    setattr(self, 'm03', m03)
            if not m10 is UNO_NONE:
                if getattr(self, 'm10') != m10:
                    setattr(self, 'm10', m10)
            if not m11 is UNO_NONE:
                if getattr(self, 'm11') != m11:
                    setattr(self, 'm11', m11)
            if not m12 is UNO_NONE:
                if getattr(self, 'm12') != m12:
                    setattr(self, 'm12', m12)
            if not m13 is UNO_NONE:
                if getattr(self, 'm13') != m13:
                    setattr(self, 'm13', m13)
            if not m20 is UNO_NONE:
                if getattr(self, 'm20') != m20:
                    setattr(self, 'm20', m20)
            if not m21 is UNO_NONE:
                if getattr(self, 'm21') != m21:
                    setattr(self, 'm21', m21)
            if not m22 is UNO_NONE:
                if getattr(self, 'm22') != m22:
                    setattr(self, 'm22', m22)
            if not m23 is UNO_NONE:
                if getattr(self, 'm23') != m23:
                    setattr(self, 'm23', m23)

        type_name = 'com.sun.star.geometry.AffineMatrix3D'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.geometry'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    AffineMatrix3D = _get_class()


else:
    from ...lo.geometry.affine_matrix3_d import AffineMatrix3D as AffineMatrix3D

__all__ = ['AffineMatrix3D']

