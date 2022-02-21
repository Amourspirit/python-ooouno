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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D
except ImportError:
    pass
try:
    from ...dyn.geometry.affine_matrix3_d import AffineMatrix3D as AffineMatrix3D
except ImportError:
    pass
try:
    from ...dyn.geometry.elliptical_arc import EllipticalArc as EllipticalArc
except ImportError:
    pass
try:
    from ...dyn.geometry.integer_bezier_segment2_d import IntegerBezierSegment2D as IntegerBezierSegment2D
except ImportError:
    pass
try:
    from ...dyn.geometry.integer_point2_d import IntegerPoint2D as IntegerPoint2D
except ImportError:
    pass
try:
    from ...dyn.geometry.integer_rectangle2_d import IntegerRectangle2D as IntegerRectangle2D
except ImportError:
    pass
try:
    from ...dyn.geometry.integer_size2_d import IntegerSize2D as IntegerSize2D
except ImportError:
    pass
try:
    from ...dyn.geometry.matrix2_d import Matrix2D as Matrix2D
except ImportError:
    pass
try:
    from ...dyn.geometry.real_bezier_segment2_d import RealBezierSegment2D as RealBezierSegment2D
except ImportError:
    pass
try:
    from ...dyn.geometry.real_point2_d import RealPoint2D as RealPoint2D
except ImportError:
    pass
try:
    from ...dyn.geometry.real_rectangle2_d import RealRectangle2D as RealRectangle2D
except ImportError:
    pass
try:
    from ...dyn.geometry.real_rectangle3_d import RealRectangle3D as RealRectangle3D
except ImportError:
    pass
try:
    from ...dyn.geometry.real_size2_d import RealSize2D as RealSize2D
except ImportError:
    pass
try:
    from ...dyn.geometry.x_mapping2_d import XMapping2D as XMapping2D
except ImportError:
    pass
