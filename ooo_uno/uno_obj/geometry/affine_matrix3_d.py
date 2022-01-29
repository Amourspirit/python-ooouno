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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class AffineMatrix3D(object):
    """
    Struct Class

    This structure defines a 3 by 4 affine matrix.
    
    The matrix defined by this structure constitutes an affine mapping of a point in 3D to another point in 3D. The last line of a complete 4 by 4 matrix is omitted, since it is implicitly assumed to be [0,0,0,1].
    
    An affine mapping, as performed by this matrix, can be written out as follows, where xs, ys and zs are the source, and xd, yd and zd the corresponding result coordinates:
    
    xd = m00*xs + m01*ys + m02*zs + m03; yd = m10*xs + m11*ys + m12*zs + m13; zd = m20*xs + m21*ys + m22*zs + m23;
    
    Thus, in common matrix language, with M being the AffineMatrix3D and vs=[xs,ys,zs]^T, vd=[xd,yd,zd]^T two 3D vectors, the affine transformation is written as vd=M*vs. Concatenation of transformations amounts to multiplication of matrices, i.e. a translation, given by T, followed by a rotation, given by R, is expressed as vd=R*(T*vs) in the above notation. Since matrix multiplication is associative, this can be shortened to vd=(R*T)*vs=M'*vs. Therefore, a set of consecutive transformations can be accumulated into a single AffineMatrix3D, by multiplying the current transformation with the additional transformation from the left.
    
    Due to this transformational approach, all geometry data types are points in abstract integer or real coordinate spaces, without any physical dimensions attached to them. This physical measurement units are typically only added when using these data types to render something onto a physical output device. For 3D coordinates there is also a projection from 3D to 2D device coordinates needed. Only then the total transformation matrix (including projection to 2D) and the device resolution determine the actual measurement unit in 3D.
    
    **since**
    
        OOo 2.0

    See Also:
        `API AffineMatrix3D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1AffineMatrix3D.html>`_


    Note:
        | At runtime AffineMatrix3D will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | AffineMatrix3D is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, m00: typing.Optional[float] = None, m01: typing.Optional[float] = None, m02: typing.Optional[float] = None, m03: typing.Optional[float] = None, m10: typing.Optional[float] = None, m11: typing.Optional[float] = None, m12: typing.Optional[float] = None, m13: typing.Optional[float] = None, m20: typing.Optional[float] = None, m21: typing.Optional[float] = None, m22: typing.Optional[float] = None, m23: typing.Optional[float] = None):
        self._m00 = m00
        self._m01 = m01
        self._m02 = m02
        self._m03 = m03
        self._m10 = m10
        self._m11 = m11
        self._m12 = m12
        self._m13 = m13
        self._m20 = m20
        self._m21 = m21
        self._m22 = m22
        self._m23 = m23

    @property
    def m00(self) -> float:
        """
        The top, left matrix entry.
        """
        return self._m00
    
    @m00.setter
    def m00(self, value: float) -> None:
        self._m00 = value

    @property
    def m01(self) -> float:
        """
        The top, left middle matrix entry.
        """
        return self._m01
    
    @m01.setter
    def m01(self, value: float) -> None:
        self._m01 = value

    @property
    def m02(self) -> float:
        """
        The top, right middle matrix entry.
        """
        return self._m02
    
    @m02.setter
    def m02(self, value: float) -> None:
        self._m02 = value

    @property
    def m03(self) -> float:
        """
        The top, right matrix entry.
        """
        return self._m03
    
    @m03.setter
    def m03(self, value: float) -> None:
        self._m03 = value

    @property
    def m10(self) -> float:
        """
        The middle, left matrix entry.
        """
        return self._m10
    
    @m10.setter
    def m10(self, value: float) -> None:
        self._m10 = value

    @property
    def m11(self) -> float:
        """
        The middle, middle left matrix entry.
        """
        return self._m11
    
    @m11.setter
    def m11(self, value: float) -> None:
        self._m11 = value

    @property
    def m12(self) -> float:
        """
        The middle, middle right matrix entry.
        """
        return self._m12
    
    @m12.setter
    def m12(self, value: float) -> None:
        self._m12 = value

    @property
    def m13(self) -> float:
        """
        The middle, right matrix entry.
        """
        return self._m13
    
    @m13.setter
    def m13(self, value: float) -> None:
        self._m13 = value

    @property
    def m20(self) -> float:
        """
        The bottom, left matrix entry.
        """
        return self._m20
    
    @m20.setter
    def m20(self, value: float) -> None:
        self._m20 = value

    @property
    def m21(self) -> float:
        """
        The bottom, middle left matrix entry.
        """
        return self._m21
    
    @m21.setter
    def m21(self, value: float) -> None:
        self._m21 = value

    @property
    def m22(self) -> float:
        """
        The bottom, middle right matrix entry.
        """
        return self._m22
    
    @m22.setter
    def m22(self, value: float) -> None:
        self._m22 = value

    @property
    def m23(self) -> float:
        """
        The bottom, right matrix entry.
        """
        return self._m23
    
    @m23.setter
    def m23(self, value: float) -> None:
        self._m23 = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global AffineMatrix3D
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('m00', 'm01', 'm02', 'm03', 'm10', 'm11', 'm12', 'm13', 'm20', 'm21', 'm22', 'm23')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.geometry.AffineMatrix3D')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        AffineMatrix3D = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['AffineMatrix3D']
