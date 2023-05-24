# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.runtime
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ...awt.x_control import XControl as XControl_7a9c098d
    from .x_filter_controller_listener import XFilterControllerListener as XFilterControllerListener_381416

class XFilterController(ABC):
    """
    provides access to a form based filter for a database form
    
    In a form based filter, form controls bound to a searchable database field are replaced with a control which allows entering a search expression. This so-called predicate expression is basically a part of an SQL WHERE clause, but without the part denoting the database column. For instance, if you have a form control bound to a table column named Name, then entering the string LIKE 'Smith' effectively constitutes a SQL WHERE clause \"Name\" LIKE 'Smith'.
    
    In the actual document view, there are usually some relaxations to this. For instance, keywords such as LIKE might be localized, according to OpenOffice.org's UI locale. Also, for an equality criterion, the equality sign = is usually omitted. However, this interface here provides programmatic access to the form based filter, so those relaxations are not considered here.
    
    The filter maintained by a filter controller is, logically, a disjunctive normal form of an SQL WHERE class. That is, it is a disjunction of m terms, where each term is a conjunction of n clauses of the form <column> <predicate> <literal> or of the form <column> IS [NOT] NULL.
    
    n equals the number of filter controls which the filter controller is responsible for. This number doesn't change during one session of the form based filter. On the other hand, m, the number of disjunctive terms, is dynamic.
    
    With the above, there are potentially m * n predicate expressions (though usually only a fraction of those will actually exist). Since in a form based filter, there are only n filter controls, and each filter control displays exactly one predicate expression, this means that only a part of the complete filter can be displayed, in particular, only one disjunctive term can be displayed at a time. Thus, the filter controller knows the concept of an active term, denoted by the ActiveTerm attribute, controls which of the terms is currently displayed in the form controls.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XFilterController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1runtime_1_1XFilterController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.runtime'
    __ooo_full_ns__: str = 'com.sun.star.form.runtime.XFilterController'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.runtime.XFilterController'

    @abstractmethod
    def addFilterControllerListener(self, Listener: XFilterControllerListener_381416) -> None:
        """
        registers a listener to be notified of certain changes in the form based filter.
        
        Registering the same listener multiple times results in multiple notifications of the same event, and also requires multiple revocations of the listener.
        """
        ...
    @abstractmethod
    def appendEmptyDisjunctiveTerm(self) -> None:
        """
        appends an empty disjunctive term to the list of terms.
        """
        ...
    @abstractmethod
    def getFilterComponent(self, Component: int) -> XControl_7a9c098d:
        """
        retrieves the filter component with the given index.
        
        The filter control has the same control model as the control which it stands in for. Consequently, you can use this method to obtain the database column which the filter control works on, by examining the control model's BoundField property.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getPredicateExpressions(self) -> typing.Tuple[typing.Tuple[str, ...], ...]:
        """
        retrieves the entirety of the predicate expressions represented by the filter controller.
        
        Each element of the returned sequence is a disjunctive term, having exactly FilterComponents elements, which denote the single predicate expressions of this term.
        """
        ...
    @abstractmethod
    def removeDisjunctiveTerm(self, Term: int) -> None:
        """
        removes a given disjunctive term

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def removeFilterControllerListener(self, Listener: XFilterControllerListener_381416) -> None:
        """
        revokes a listener which was previously registered to be notified of certain changes in the form based filter.
        """
        ...
    @abstractmethod
    def setPredicateExpression(self, Component: int, Term: int, PredicateExpression: str) -> None:
        """
        sets a given predicate expression

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractproperty
    def ActiveTerm(self) -> int:
        """
        denotes the active term of the filter controller.
        """
        ...

    @abstractproperty
    def DisjunctiveTerms(self) -> int:
        """
        is the number of disjunctive terms of the filter expression represented by the form based filter.
        """
        ...

    @abstractproperty
    def FilterComponents(self) -> int:
        """
        is the number of filter components, or filter controls, which the filter controller is responsible for.
        
        This number is constant during one session of the form based filter.
        """
        ...


__all__ = ['XFilterController']

