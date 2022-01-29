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
# Namespace: com.sun.star.form.runtime
import typing
from abc import abstractmethod, ABC

class XFeatureInvalidation(ABC):
    """
    implements a callback for a XFormOperations instance, which is called when the state of one or more FormFeatures might have changed.
    
    **since**
    
        OOo 2.2

    See Also:
        `API XFeatureInvalidation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1runtime_1_1XFeatureInvalidation.html>`_
    """

    @abstractmethod
    def invalidateAllFeatures(self) -> None:
        """
        invalidates all features
        
        This method is used of it cannot be exactly and reliably determined which features might actually have changed their state. In this case, the callee should assume all features it is interested in must be required.
        """
    @abstractmethod
    def invalidateFeatures(self, Features: 'typing.List[int]') -> None:
        """
        invalidates the given FormFeatures
        
        Invalidation means that any user interface representation (such as toolbox buttons), or any dispatches associated with the features in question are potentially out-of-date, and need to be updated.
        """

__all__ = ['XFeatureInvalidation']

