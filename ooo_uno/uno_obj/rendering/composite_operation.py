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
# Namespace: com.sun.star.rendering
from ooo_uno.base.const import ConstIntBase


class CompositeOperation(ConstIntBase):
    """
    These constants determine how the primitive color is combined with the background.
    
    When performing these calculations, it is assumed that all color values are premultiplied with the corresponding alpha values (if no alpha is specified, 1.0 is assumed). Then, the following general compositing operation is performed:
    
    C = Ca * Fa + Cb * Fb
    
    where C is the result color, Ca and Cb are the input colors, premultiplied with alpha, and Fa and Fb are described for the different composite modes (wherein Aa and Ab denote source and destination alpha, respectively).
    
    **since**
    
        OOo 2.0

    See Also:
        `API CompositeOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1CompositeOperation.html>`_
    """
    CLEAR = 0
    """
    Clear the destination.
    
    Clear the destination area. The function values are: Fa = Fb = 0.
    """
    SOURCE = 1
    """
    Copy source as-is to the destination.
    
    Copy source as-is to the destination. The function values are: Fa = 1, Fb = 0.
    """
    DESTINATION = 2
    """
    Leave the destination as-is.
    
    Leave the destination as-is. The function values are: Fa = 0, Fb = 1.
    """
    OVER = 3
    """
    Copy the source over the destination.
    
    Copy the source over the destination. The function values are: Fa = 1, Fb = 1-Aa.
    """
    UNDER = 4
    """
    Copy the source under the destination.
    
    Copy the source under the destination. The function values are: Fa = 1-Ab, Fb = 1.
    """
    INSIDE = 5
    """
    Copy the source to the destination.
    
    Copy the source to the destination, but limited to where the destination is. The function values are: Fa = Ab, Fb = 0.
    """
    INSIDE_REVERSE = 6
    """
    Leave the destination as is.
    
    Leave the destination as is, but only where the source was. The function values are: Fa = 0, Fb = Aa.
    """
    OUTSIDE = 7
    """
    Copy the source to the destination.
    
    Copy the source to the destination, but limited to where the destination is not. The function values are: Fa = 1-Ab, Fb = 0.
    """
    OUTSIDE_REVERSE = 8
    """
    Leave the destination as is.
    
    Leave the destination as is, but only where the source has not been. The function values are: Fa = 0, Fb = 1-Aa.
    """
    ATOP = 9
    """
    Copy the source over the destination.
    
    Copy the source over the destination, but only where the destination is. Keep the destination. The function values are: Fa = Ab, Fb = 1-Aa.
    """
    ATOP_REVERSE = 10
    """
    Copy the destination over the source.
    
    Copy the destination over the source, but only where the source is. Keep the source. The function values are: Fa = 1-Ab, Fb = Aa.
    """
    XOR = 11
    """
    Combine source and destination by exclusive or.
    
    Take only the parts where either source or destination, but not both visible. The function values are: Fa = 1-Ab, Fb = 1-Aa.
    """
    ADD = 12
    """
    Add source and destination values.
    
    Simply add contributions of both source and destination. The resulting color values are limited to the permissible color range, and clipped to the maximal value, if exceeded. The function values are: Fa = 1, Fb = 1.
    """
    SATURATE = 13
    """
    Saturate source and destination.
    
    Saturate destination with source values. The function values are: Fa = min(1,(1-Ab)/Aa), Fb = 1
    """

