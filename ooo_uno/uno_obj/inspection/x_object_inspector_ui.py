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
# Namespace: com.sun.star.inspection
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2
    from .x_property_control_observer import XPropertyControlObserver as XPropertyControlObserver_cc6d132a

class XObjectInspectorUI(ABC):
    """
    grants access to certain aspects of the user interface of an object inspector
    
    This interface is used as callback for XPropertyHandlers.
    
    As a consequence, methods operating on the UI for a property, and taking the name of this property, are tolerant against properties which do not exist. For instance, if a property handler tries to disable the UI for property Foo, but another handler has superseded this property, then the ObjectInspector will not have any UI for it. In this case, the call to enablePropertyUI( \"Foo\" ) will simply be ignored.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XObjectInspectorUI <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XObjectInspectorUI.html>`_
    """

    @abstractmethod
    def enablePropertyUI(self, PropertyName: str, Enable: bool) -> None:
        """
        enables or disables all components belonging to the UI representation of a property
        
        This is usually used by an XPropertyHandler if it handles properties, where one does only make sense if another one has a certain value.
        """
    @abstractmethod
    def enablePropertyUIElements(self, PropertyName: str, Elements: int, Enable: bool) -> None:
        """
        enables or disables the single elements which can be part of the UI representation of a property
        
        Note that the complete UI for the property must be enabled in order for these settings to be evaluated. That is, enablePropertyUIElements() does not have any effect if somebody previously disabled the complete UI for this property with enablePropertyUI().
        """
    @abstractmethod
    def getPropertyControl(self, PropertyName: str) -> 'XPropertyControl_3f260fe2':
        """
        retrieves the control currently used to display a given property
        """
    @abstractmethod
    def hidePropertyUI(self, PropertyName: str) -> None:
        """
        hides the UI for a given property
        """
    @abstractmethod
    def rebuildPropertyUI(self, PropertyName: str) -> None:
        """
        completely rebuilds the UI for the given property.
        
        This method might be used by an XPropertyHandler if it wants to change the type of control (see PropertyControlType) used to display a certain property.
        
        The object inspector will then call describePropertyLine again, and update its UI accordingly.
        
        Note that the property whose UI should be rebuilt must not necessarily be (though usually is) in the responsibility of the handler which calls this method. The object inspector will look up the handler with the responsibility for PropertyName and call its XPropertyHandler.describePropertyLine()
        """
    @abstractmethod
    def registerControlObserver(self, Observer: 'XPropertyControlObserver_cc6d132a') -> None:
        """
        registers an observer for all property controls
        
        The given XPropertyControlObserver will be notified of all changes in all property controls.
        
        **since**
        
            OOo 2.2
        """
    @abstractmethod
    def revokeControlObserver(self, Observer: 'XPropertyControlObserver_cc6d132a') -> None:
        """
        revokes a previously registered control observer
        
        **since**
        
            OOo 2.2
        """
    @abstractmethod
    def setHelpSectionText(self, HelpText: str) -> None:
        """
        sets the text of the help section, if the object inspector contains one.
        
        **since**
        
            OOo 2.2

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    @abstractmethod
    def showCategory(self, Category: str, Show: bool) -> None:
        """
        shows or hides all properties belonging to a given category
        """
    @abstractmethod
    def showPropertyUI(self, PropertyName: str) -> None:
        """
        shows the UI for a given property
        """

__all__ = ['XObjectInspectorUI']

