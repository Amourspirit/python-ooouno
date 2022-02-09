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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
import typing
if typing.TYPE_CHECKING:
    from ..geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D_ff040da8
    from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20


class ViewState(object):
    """
    Struct Class

    This structure contains information considered the view state.
    
    This structure contains information considered the view state, i.e. the invariant setup used when painting a whole view of something.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ViewState <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1ViewState.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.ViewState'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.ViewState'
    """Literal Constant ``com.sun.star.rendering.ViewState``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ViewState`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ViewState``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            AffineTransform (AffineMatrix2D, optional): AffineTransform value
            Clip (XPolyPolygon2D, optional): Clip value
        """
        self._affine_transform = None
        self._clip = None

        key_order = ('AffineTransform', 'Clip')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ViewState):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ViewState.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def AffineTransform(self) -> 'AffineMatrix2D_ff040da8':
        """
        The affine transform associated with the view.
        
        This member is used to transform coordinates of draw operations from user space to screen space.
        """
        return self._affine_transform
    
    @AffineTransform.setter
    def AffineTransform(self, value: 'AffineMatrix2D_ff040da8') -> None:
        self._affine_transform = value

    @property
    def Clip(self) -> 'XPolyPolygon2D_e1b0e20':
        """
        The clipping area associated with the view.
        
        This clipping is interpreted in the view coordinate systems, i.e. subject to the view transform before mapping to the device coordinate space.
        
        Specifying an empty interface denotes no clipping, i.e. everything rendered to the canvas will be visible (subject to device-dependent constraints, of course). Specifying an empty XPolyPolygon2D, i.e. a poly-polygon containing zero polygons, or an XPolyPolygon2D with any number of empty sub-polygons, denotes the NULL clip. That means, nothing rendered to the canvas will be visible.
        """
        return self._clip
    
    @Clip.setter
    def Clip(self, value: 'XPolyPolygon2D_e1b0e20') -> None:
        self._clip = value


__all__ = ['ViewState']
