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
# Libre Office Version: 7.3
# Namespace: com.sun.star.form.runtime
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .filter_event import FilterEvent as FilterEvent_d780e56

class XFilterControllerListener(XEventListener_c7230c4a):
    """
    is implemented by components listening for events fired by an XFilterController.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XFilterControllerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1runtime_1_1XFilterControllerListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.runtime'
    __ooo_full_ns__: str = 'com.sun.star.form.runtime.XFilterControllerListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.runtime.XFilterControllerListener'

    @abstractmethod
    def disjunctiveTermAdded(self, Event: 'FilterEvent_d780e56') -> None:
        """
        is fired when a disjunctive term was added to the filter of the filter controller.
        
        FilterEvent.DisjunctiveTerm is the index of the disjunctive term which was added.
        
        FilterEvent.FilterComponent and FilterEvent.PredicateExpression are not used for this event type.
        """
        ...
    @abstractmethod
    def disjunctiveTermRemoved(self, Event: 'FilterEvent_d780e56') -> None:
        """
        is fired when a disjunctive term was removed from the filter of the filter controller.
        
        FilterEvent.DisjunctiveTerm is the index of the disjunctive term which was removed.
        
        FilterEvent.FilterComponent and FilterEvent.PredicateExpression are not used for this event type.
        """
        ...
    @abstractmethod
    def predicateExpressionChanged(self, Event: 'FilterEvent_d780e56') -> None:
        """
        is fired when a single predicate expression of the filter represented by the filter controller changed.
        
        FilterEvent.DisjunctiveTerm is the index of the disjunctive term in which the expression changed. This usually equals XFilterController.ActiveTerm.
        
        FilterEvent.FilterComponent denotes the index of the filter component whose predicate expression changed.
        
        FilterEvent.PredicateExpression is the new predicate expressions.
        """
        ...

__all__ = ['XFilterControllerListener']

