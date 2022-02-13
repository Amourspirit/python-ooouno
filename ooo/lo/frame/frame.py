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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.frame
from .x_frame2 import XFrame2 as XFrame2_83df0988

class Frame(XFrame2_83df0988):
    """
    Service Class

    represents the environment for a desktop component
    
    Frames are the anchors for the office components and they are the component's link to the outside world. They create a skeleton for the whole office API infrastructure by building frame hierarchies. These hierarchies contains all currently loaded documents and make it possible to walk during these trees. A special service Desktop can(!) combine different of such trees to a global one which life time will be controlled by it.

    See Also:
        `API Frame <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Frame.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.Frame'
    __ooo_type_name__: str = 'service'



__all__ = ['Frame']

