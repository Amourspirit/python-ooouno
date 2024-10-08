# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.presentation
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class AnimationEffect(Enum):
    """
    Enum Class


    See Also:
        `API AnimationEffect <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation.html#a10f2a3114ab31c0e6f7dc48f656fd260>`_
    """
    __ooo_ns__: str = "com.sun.star.presentation"
    __ooo_full_ns__: str = "com.sun.star.presentation.AnimationEffect"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.presentation.AnimationEffect"

    APPEAR = "APPEAR"
    """
    use the animation effect \"Appear\".
    """
    CLOCKWISE = "CLOCKWISE"
    """
    use the animation effect \"Clockwise\".
    
    use the fade effect \"Clockwise\".
    """
    CLOSE_HORIZONTAL = "CLOSE_HORIZONTAL"
    """
    use the animation effect \"Close Horizontal\".
    
    use the fade effect \"Close Horizontal\".
    """
    CLOSE_VERTICAL = "CLOSE_VERTICAL"
    """
    use the animation effect \"Close Vertical\".
    
    use the fade effect \"Close Vertical\".
    """
    COUNTERCLOCKWISE = "COUNTERCLOCKWISE"
    """
    use the animation effect \"Counter Clockwise\".
    
    use the fade effect \"Counter Clockwise\".
    """
    DISSOLVE = "DISSOLVE"
    """
    use the animation effect \"Spiral Inward Left\".
    
    use the fade effect \"Dissolve\".
    """
    FADE_FROM_BOTTOM = "FADE_FROM_BOTTOM"
    """
    use the animation effect \"Fade from Bottom\".
    
    use the fade effect \"Fade from Bottom\".
    """
    FADE_FROM_CENTER = "FADE_FROM_CENTER"
    """
    use the animation effect \"Fade from Center\".
    
    use the fade effect \"Fade from Center\".
    """
    FADE_FROM_LEFT = "FADE_FROM_LEFT"
    """
    use the animation effect \"Fade from Left\".
    
    use the fade effect \"Fade from Left\".
    """
    FADE_FROM_LOWERLEFT = "FADE_FROM_LOWERLEFT"
    """
    use the animation effect \"Fade from Lower Left\".
    
    use the fade effect \"Fade from Lower Left\".
    """
    FADE_FROM_LOWERRIGHT = "FADE_FROM_LOWERRIGHT"
    """
    use the animation effect \"Fade from Lower Right\".
    
    use the fade effect \"Fade from Lower Right\".
    """
    FADE_FROM_RIGHT = "FADE_FROM_RIGHT"
    """
    use the animation effect \"Fade from Right\".
    
    use the fade effect \"Fade from Right\".
    """
    FADE_FROM_TOP = "FADE_FROM_TOP"
    """
    use the animation effect \"Fade from Top\".
    
    use the fade effect \"Fade from Top\".
    """
    FADE_FROM_UPPERLEFT = "FADE_FROM_UPPERLEFT"
    """
    use the animation effect \"Fade from Upper Left\".
    
    use the fade effect \"Fade from Upper Left\".
    """
    FADE_FROM_UPPERRIGHT = "FADE_FROM_UPPERRIGHT"
    """
    use the animation effect \"Fade from Upper Right\".
    
    use the fade effect \"Fade from Upper Right\".
    """
    FADE_TO_CENTER = "FADE_TO_CENTER"
    """
    use the animation effect \"Fade to Center\".
    
    use the fade effect \"Fade to Center\".
    """
    HIDE = "HIDE"
    """
    use the animation effect \"Hide\".
    """
    HORIZONTAL_CHECKERBOARD = "HORIZONTAL_CHECKERBOARD"
    """
    use the animation effect \"Horizontal Checkerboard\".
    
    use the fade effect \"Horizontal Checkerboard\".
    """
    HORIZONTAL_LINES = "HORIZONTAL_LINES"
    """
    use the animation effect \"Horizontal Lines\".
    
    use the fade effect \"Horizontal Lines\".
    """
    HORIZONTAL_ROTATE = "HORIZONTAL_ROTATE"
    """
    use the animation effect \"Horizontal Rotate\".
    """
    HORIZONTAL_STRETCH = "HORIZONTAL_STRETCH"
    """
    use the animation effect \"Horizontal Stretch\".
    """
    HORIZONTAL_STRIPES = "HORIZONTAL_STRIPES"
    """
    use the animation effect \"Horizontal Stripes\".
    
    use the fade effect \"Horizontal Stripes\".
    """
    LASER_FROM_BOTTOM = "LASER_FROM_BOTTOM"
    """
    use the animation effect \"Laser from Bottom\".
    """
    LASER_FROM_LEFT = "LASER_FROM_LEFT"
    """
    use the animation effect \"Wavy Line from Left\".
    """
    LASER_FROM_LOWERLEFT = "LASER_FROM_LOWERLEFT"
    """
    use the animation effect \"Laser from Lower Left\".
    """
    LASER_FROM_LOWERRIGHT = "LASER_FROM_LOWERRIGHT"
    """
    use the animation effect \"Laser from Lower Right\".
    """
    LASER_FROM_RIGHT = "LASER_FROM_RIGHT"
    """
    use the animation effect \"Laser from Right\".
    """
    LASER_FROM_TOP = "LASER_FROM_TOP"
    """
    use the animation effect \"Laser from Top\".
    """
    LASER_FROM_UPPERLEFT = "LASER_FROM_UPPERLEFT"
    """
    use the animation effect \"Laser from Upper Left\".
    """
    LASER_FROM_UPPERRIGHT = "LASER_FROM_UPPERRIGHT"
    """
    use the animation effect \"Laser from Upper Right\".
    """
    MOVE_FROM_BOTTOM = "MOVE_FROM_BOTTOM"
    """
    use the animation effect \"Move from Bottom\".
    
    use the fade effect \"Move from Bottom\".
    """
    MOVE_FROM_LEFT = "MOVE_FROM_LEFT"
    """
    use the animation effect \"Move from Left\".
    
    use the fade effect \"Move from Left\".
    """
    MOVE_FROM_LOWERLEFT = "MOVE_FROM_LOWERLEFT"
    """
    use the animation effect \"Move from Lower Left\".
    
    use the fade effect \"Move from Lower Left\".
    """
    MOVE_FROM_LOWERRIGHT = "MOVE_FROM_LOWERRIGHT"
    """
    use the animation effect \"Move from Lower Right\".
    
    use the fade effect \"Move from Lower Right\".
    """
    MOVE_FROM_RIGHT = "MOVE_FROM_RIGHT"
    """
    use the animation effect \"Move from Right\".
    
    use the fade effect \"Move from Right\".
    """
    MOVE_FROM_TOP = "MOVE_FROM_TOP"
    """
    use the animation effect \"Move from Top\".
    
    use the fade effect \"Move from Top\".
    """
    MOVE_FROM_UPPERLEFT = "MOVE_FROM_UPPERLEFT"
    """
    use the animation effect \"Move from Upper Left\".
    
    use the fade effect \"Move from Upper Left\".
    """
    MOVE_FROM_UPPERRIGHT = "MOVE_FROM_UPPERRIGHT"
    """
    use the animation effect \"Move from Upper Right\".
    
    use the fade effect \"Move from Upper Right\".
    """
    MOVE_SHORT_FROM_BOTTOM = "MOVE_SHORT_FROM_BOTTOM"
    """
    use the animation effect \"Move Short from Bottom\".
    """
    MOVE_SHORT_FROM_LEFT = "MOVE_SHORT_FROM_LEFT"
    """
    use the animation effect \"Move Short from Left\".
    """
    MOVE_SHORT_FROM_LOWERLEFT = "MOVE_SHORT_FROM_LOWERLEFT"
    """
    use the animation effect \"Move Short from Lower Left\".
    """
    MOVE_SHORT_FROM_LOWERRIGHT = "MOVE_SHORT_FROM_LOWERRIGHT"
    """
    use the animation effect \"Move Short from Lower Right\".
    """
    MOVE_SHORT_FROM_RIGHT = "MOVE_SHORT_FROM_RIGHT"
    """
    use the animation effect \"Move Short from Right\".
    """
    MOVE_SHORT_FROM_TOP = "MOVE_SHORT_FROM_TOP"
    """
    use the animation effect \"Move Short from Top\".
    """
    MOVE_SHORT_FROM_UPPERLEFT = "MOVE_SHORT_FROM_UPPERLEFT"
    """
    use the animation effect \"Move Short from Upper Left\".
    """
    MOVE_SHORT_FROM_UPPERRIGHT = "MOVE_SHORT_FROM_UPPERRIGHT"
    """
    use the animation effect \"Move Short from Upper Right\".
    """
    MOVE_SHORT_TO_BOTTOM = "MOVE_SHORT_TO_BOTTOM"
    """
    use the animation effect \"Move Short to Bottom\".
    """
    MOVE_SHORT_TO_LEFT = "MOVE_SHORT_TO_LEFT"
    """
    use the animation effect \"Move Short to Left\".
    """
    MOVE_SHORT_TO_LOWERLEFT = "MOVE_SHORT_TO_LOWERLEFT"
    """
    use the animation effect \"Move Short to Lower Left\".
    """
    MOVE_SHORT_TO_LOWERRIGHT = "MOVE_SHORT_TO_LOWERRIGHT"
    """
    use the animation effect \"Move Short to Lower Right\".
    """
    MOVE_SHORT_TO_RIGHT = "MOVE_SHORT_TO_RIGHT"
    """
    use the animation effect \"Move Short to Right\".
    """
    MOVE_SHORT_TO_TOP = "MOVE_SHORT_TO_TOP"
    """
    use the animation effect \"Move Short to Top\".
    """
    MOVE_SHORT_TO_UPPERLEFT = "MOVE_SHORT_TO_UPPERLEFT"
    """
    use the animation effect \"Move Short to Upper Left\".
    """
    MOVE_SHORT_TO_UPPERRIGHT = "MOVE_SHORT_TO_UPPERRIGHT"
    """
    use the animation effect \"Move Short to Upper Right\".
    """
    MOVE_TO_BOTTOM = "MOVE_TO_BOTTOM"
    """
    use the animation effect \"Move to Bottom\".
    """
    MOVE_TO_LEFT = "MOVE_TO_LEFT"
    """
    use the animation effect \"Move to Left\".
    """
    MOVE_TO_LOWERLEFT = "MOVE_TO_LOWERLEFT"
    """
    use the animation effect \"Move to Lower Left\".
    """
    MOVE_TO_LOWERRIGHT = "MOVE_TO_LOWERRIGHT"
    """
    use the animation effect \"Move to Lower Right\".
    """
    MOVE_TO_RIGHT = "MOVE_TO_RIGHT"
    """
    use the animation effect \"Move to Right\".
    """
    MOVE_TO_TOP = "MOVE_TO_TOP"
    """
    use the animation effect \"Move to Top\".
    """
    MOVE_TO_UPPERLEFT = "MOVE_TO_UPPERLEFT"
    """
    use the animation effect \"Move to Upper Left\".
    """
    MOVE_TO_UPPERRIGHT = "MOVE_TO_UPPERRIGHT"
    """
    use the animation effect \"Move to Upper Right\".
    """
    NONE = "NONE"
    """
    use no animation effects.
    
    use no fade effects.
    
    No action is performed on click.
    """
    OPEN_HORIZONTAL = "OPEN_HORIZONTAL"
    """
    use the animation effect \"Open Horizontal\".
    
    use the fade effect \"Open Horizontal\".
    """
    OPEN_VERTICAL = "OPEN_VERTICAL"
    """
    use the animation effect \"Open Vertical\".
    
    use the fade effect \"Open Vertical\".
    """
    PATH = "PATH"
    """
    use the animation effect \"Path\".
    """
    RANDOM = "RANDOM"
    """
    use the animation effect \"Random\".
    
    use the fade effect \"Random\".
    """
    SPIRALIN_LEFT = "SPIRALIN_LEFT"
    """
    use the animation effect \"Spiral Inward Left\".
    
    use the fade effect \"Spiral Inward Left\".
    """
    SPIRALIN_RIGHT = "SPIRALIN_RIGHT"
    """
    use the animation effect \"Spiral Inward Right\".
    
    use the fade effect \"Spiral Inward Right\".
    """
    SPIRALOUT_LEFT = "SPIRALOUT_LEFT"
    """
    use the animation effect \"Spiral Outward Left\".
    
    use the fade effect \"Spiral Outward Left\".
    """
    SPIRALOUT_RIGHT = "SPIRALOUT_RIGHT"
    """
    use the animation effect \"Spiral Outward Right\".
    
    use the fade effect \"Spiral Outward Right\".
    """
    STRETCH_FROM_BOTTOM = "STRETCH_FROM_BOTTOM"
    """
    use the animation effect \"Stretch From Bottom\".
    
    use the fade effect \"Stretch from Bottom\".
    """
    STRETCH_FROM_LEFT = "STRETCH_FROM_LEFT"
    """
    use the animation effect \"Stretch From Left\".
    
    use the fade effect \"Stretch from Left\".
    """
    STRETCH_FROM_LOWERLEFT = "STRETCH_FROM_LOWERLEFT"
    """
    use the animation effect \"Stretch From Lower Left\".
    """
    STRETCH_FROM_LOWERRIGHT = "STRETCH_FROM_LOWERRIGHT"
    """
    use the animation effect \"Stretch From Lower Right\".
    """
    STRETCH_FROM_RIGHT = "STRETCH_FROM_RIGHT"
    """
    use the animation effect \"Stretch From Right\".
    
    use the fade effect \"Stretch from Right\".
    """
    STRETCH_FROM_TOP = "STRETCH_FROM_TOP"
    """
    use the animation effect \"Stretch From Top\".
    
    use the fade effect \"Stretch from Top\".
    """
    STRETCH_FROM_UPPERLEFT = "STRETCH_FROM_UPPERLEFT"
    """
    use the animation effect \"Stretch From Upper Left\".
    """
    STRETCH_FROM_UPPERRIGHT = "STRETCH_FROM_UPPERRIGHT"
    """
    use the animation effect \"Stretch From Upper Right\".
    """
    VERTICAL_CHECKERBOARD = "VERTICAL_CHECKERBOARD"
    """
    use the animation effect \"Vertical Checkerboard\".
    
    use the fade effect \"Vertical Checkerboard\".
    """
    VERTICAL_LINES = "VERTICAL_LINES"
    """
    use the animation effect \"Vertical Lines\".
    
    use the fade effect \"Vertical Lines\".
    """
    VERTICAL_ROTATE = "VERTICAL_ROTATE"
    """
    use the animation effect \"Vertical Rotate\".
    """
    VERTICAL_STRETCH = "VERTICAL_STRETCH"
    """
    use the animation effect \"Vertical Stretch\".
    """
    VERTICAL_STRIPES = "VERTICAL_STRIPES"
    """
    use the animation effect \"Vertical Stripes\".
    
    use the fade effect \"Vertical Stripes\".
    """
    WAVYLINE_FROM_BOTTOM = "WAVYLINE_FROM_BOTTOM"
    """
    use the animation effect \"Wavy Line from Button\".
    
    use the fade effect \"Wavy Line from Bottom\".
    """
    WAVYLINE_FROM_LEFT = "WAVYLINE_FROM_LEFT"
    """
    use the animation effect \"Wavy Line from Left\".
    
    use the fade effect \"Wavy Line from Left\".
    """
    WAVYLINE_FROM_RIGHT = "WAVYLINE_FROM_RIGHT"
    """
    use the animation effect \"Wavy Line from Right\".
    
    use the fade effect \"Wavy Line from Right\".
    """
    WAVYLINE_FROM_TOP = "WAVYLINE_FROM_TOP"
    """
    use the animation effect \"Wavy Line from Top\".
    
    use the fade effect \"Wavy Line from Top\".
    """
    ZOOM_IN = "ZOOM_IN"
    """
    use the animation effect \"Zoom In\".
    """
    ZOOM_IN_FROM_BOTTOM = "ZOOM_IN_FROM_BOTTOM"
    """
    use the animation effect \"Zoom In From Bottom\".
    """
    ZOOM_IN_FROM_CENTER = "ZOOM_IN_FROM_CENTER"
    """
    use the animation effect \"Zoom In From Center\".
    """
    ZOOM_IN_FROM_LEFT = "ZOOM_IN_FROM_LEFT"
    """
    use the animation effect \"Zoom In From Left\".
    """
    ZOOM_IN_FROM_LOWERLEFT = "ZOOM_IN_FROM_LOWERLEFT"
    """
    use the animation effect \"Zoom In From Lower Left\".
    """
    ZOOM_IN_FROM_LOWERRIGHT = "ZOOM_IN_FROM_LOWERRIGHT"
    """
    use the animation effect \"Zoom In From Lower Right\".
    """
    ZOOM_IN_FROM_RIGHT = "ZOOM_IN_FROM_RIGHT"
    """
    use the animation effect \"Zoom In From Right\".
    """
    ZOOM_IN_FROM_TOP = "ZOOM_IN_FROM_TOP"
    """
    use the animation effect \"Zoom In From Top\".
    """
    ZOOM_IN_FROM_UPPERLEFT = "ZOOM_IN_FROM_UPPERLEFT"
    """
    use the animation effect \"Zoom In From Upper Left\".
    """
    ZOOM_IN_FROM_UPPERRIGHT = "ZOOM_IN_FROM_UPPERRIGHT"
    """
    use the animation effect \"Zoom In From Upper Right\".
    """
    ZOOM_IN_SMALL = "ZOOM_IN_SMALL"
    """
    use the animation effect \"Zoom In Small\".
    """
    ZOOM_IN_SPIRAL = "ZOOM_IN_SPIRAL"
    """
    use the animation effect \"Zoom In Spiral\".
    """
    ZOOM_OUT = "ZOOM_OUT"
    """
    use the animation effect \"Zoom Out\".
    """
    ZOOM_OUT_FROM_BOTTOM = "ZOOM_OUT_FROM_BOTTOM"
    """
    use the animation effect \"Zoom Out From Bottom\".
    """
    ZOOM_OUT_FROM_CENTER = "ZOOM_OUT_FROM_CENTER"
    """
    use the animation effect \"Zoom Out From Center\".
    """
    ZOOM_OUT_FROM_LEFT = "ZOOM_OUT_FROM_LEFT"
    """
    use the animation effect \"Zoom Out From Left\".
    """
    ZOOM_OUT_FROM_LOWERLEFT = "ZOOM_OUT_FROM_LOWERLEFT"
    """
    use the animation effect \"Zoom Out From Lower Left\".
    """
    ZOOM_OUT_FROM_LOWERRIGHT = "ZOOM_OUT_FROM_LOWERRIGHT"
    """
    use the animation effect \"Zoom Out From Lower Right\".
    """
    ZOOM_OUT_FROM_RIGHT = "ZOOM_OUT_FROM_RIGHT"
    """
    use the animation effect \"Zoom Out From Right\".
    """
    ZOOM_OUT_FROM_TOP = "ZOOM_OUT_FROM_TOP"
    """
    use the animation effect \"Zoom Out From Top\".
    """
    ZOOM_OUT_FROM_UPPERLEFT = "ZOOM_OUT_FROM_UPPERLEFT"
    """
    use the animation effect \"Zoom Out From Upper Left\".
    """
    ZOOM_OUT_FROM_UPPERRIGHT = "ZOOM_OUT_FROM_UPPERRIGHT"
    """
    use the animation effect \"Zoom Out From Upper Right\".
    """
    ZOOM_OUT_SMALL = "ZOOM_OUT_SMALL"
    """
    use the animation effect \"Zoom Out Small\".
    """
    ZOOM_OUT_SPIRAL = "ZOOM_OUT_SPIRAL"
    """
    use the animation effect \"Zoom Out Spiral\".
    """

__all__ = ["AnimationEffect"]

