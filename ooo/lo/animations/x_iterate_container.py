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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.animations
from abc import abstractproperty
from .x_time_container import XTimeContainer as XTimeContainer_1cca0ec5

class XIterateContainer(XTimeContainer_1cca0ec5):
    """
    An iterate container iterates over subitems of a given target object and animates them by subsequently executes the contained effects on them.
    
    This could be used to animate a target text word by word or letter by letter.

    See Also:
        `API XIterateContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XIterateContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.XIterateContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.animations.XIterateContainer'

    @abstractproperty
    def IterateInterval(self) -> float:
        """
        the time interval in second before the next iterated content is animated.
        """
    @abstractproperty
    def IterateType(self) -> int:
        """
        the type of iteration, this depends on the target.
        
        See documentation of used animation engine for supported iteration types.
        """
    @abstractproperty
    def SubItem(self) -> int:
        """
        This attribute specifies an optional subitem from the target element that should be animated.
        
        A value of zero should always be the default and animate the complete target.
        See documentation of used animation engine for supported subitems.
        """
    @abstractproperty
    def Target(self) -> object:
        """
        a target that contains iterable contents, f.e.
        
        a paragraph.
        See documentation of used animation engine for supported targets.
        """

__all__ = ['XIterateContainer']

