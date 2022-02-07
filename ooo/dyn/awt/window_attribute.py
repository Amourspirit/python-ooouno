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
# Namespace: com.sun.star.awt
from enum import IntFlag
from ...lo.awt.window_attribute import WindowAttribute as WindowAttribute


class WindowAttributeEnum(IntFlag):
    """
    Enum of Const Class WindowAttribute

    These values are used to specify the decorations of a window.
    
    IMPORTANT: These constants have to be disjunct with constants in VclWindowPeerAttribute.
    """
    SHOW = WindowAttribute.SHOW
    """
    specifies that the window is initially visible.
    """
    FULLSIZE = WindowAttribute.FULLSIZE
    """
    specifies that the window fills the complete desktop area.
    
    This applies only to top windows.
    """
    OPTIMUMSIZE = WindowAttribute.OPTIMUMSIZE
    """
    specifies that the window is optimum size.
    
    This applies only to top windows.
    """
    MINSIZE = WindowAttribute.MINSIZE
    """
    specifies that the window is minimum size.
    
    This applies only to top windows.
    """
    BORDER = WindowAttribute.BORDER
    """
    specifies that the window has visible borders.
    
    This applies only to top windows.
    """
    SIZEABLE = WindowAttribute.SIZEABLE
    """
    specifies that the size of the window can be changed by the user.
    
    This applies only to top windows.
    """
    MOVEABLE = WindowAttribute.MOVEABLE
    """
    specifies that the window can be moved by the user.
    
    This applies only to top windows.
    """
    CLOSEABLE = WindowAttribute.CLOSEABLE
    """
    specifies that the window can be closed by the user.
    
    This applies only to top windows.
    """
    SYSTEMDEPENDENT = WindowAttribute.SYSTEMDEPENDENT
    """
    specifies that the window should support the com.sun.star.awt.XSystemDependentWindowPeer interface.
    
    This flag may be ignored, but in this case no system-dependent extension works.
    """
    NODECORATION = WindowAttribute.NODECORATION
    """
    specifies that the window should have no decoration.
    """

__all__ = ['WindowAttribute', 'WindowAttributeEnum']
