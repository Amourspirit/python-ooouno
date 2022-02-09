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
# Namespace: com.sun.star.xforms
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..container.x_set import XSet as XSet_90c40a4f
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51
    from .x_data_type_repository import XDataTypeRepository as XDataTypeRepository_2bbb0f5b
    from .x_submission import XSubmission as XSubmission_bf230c2b
    from ..xml.dom.x_document import XDocument as XDocument_aebc0b5e

class XModel(ABC):
    """
    represent an XForms model

    See Also:
        `API XModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xforms_1_1XModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xforms'
    __ooo_full_ns__: str = 'com.sun.star.xforms.XModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xforms.XModel'

    @abstractmethod
    def cloneBinding(self, binding: 'XPropertySet_bc180bfa') -> 'XPropertySet_bc180bfa':
        """
        clone an arbitrary binding element for this model; still needs
        
        The returned binding still needs to be inserted into the bindings container.
        """
    @abstractmethod
    def cloneSubmission(self, submission: 'XPropertySet_bc180bfa') -> 'XSubmission_bf230c2b':
        """
        clone an arbitrary submission element for this model
        
        The returned submission element still needs to be inserted into the submission container.
        """
    @abstractmethod
    def createBinding(self) -> 'XPropertySet_bc180bfa':
        """
        create a binding element for this model
        
        The returned binding still needs to be inserted into the bindings container.
        """
    @abstractmethod
    def createSubmission(self) -> 'XSubmission_bf230c2b':
        """
        create a submission element for this model
        
        The returned submission element still needs to be inserted into the submission container.
        """
    @abstractmethod
    def getBinding(self, id: str) -> 'XPropertySet_bc180bfa':
        """
        get a binding with a certain ID
        
        This is a convenience method: the same result can also be obtained through getBindings()
        """
    @abstractmethod
    def getBindings(self) -> 'XSet_90c40a4f':
        """
        get a container containing all bindings; also supports XNameAccess
        """
    @abstractmethod
    def getDataTypeRepository(self) -> 'XDataTypeRepository_2bbb0f5b':
        """
        provides management access to the XSD data types associated with the model
        """
    @abstractmethod
    def getDefaultInstance(self) -> 'XDocument_aebc0b5e':
        """
        get the default instance for this model
        """
    @abstractmethod
    def getID(self) -> str:
        """
        get the XForms model ID
        """
    @abstractmethod
    def getInstanceDocument(self, id: str) -> 'XDocument_aebc0b5e':
        """
        retrieves the instance with the given id
        """
    @abstractmethod
    def getInstances(self) -> 'XSet_90c40a4f':
        """
        gets container containing all instances;
        
        The elements of the set are arrays of com.sun.star.beans.PropertyValues, containing the ID, the URL, and the instance itself.
        """
    @abstractmethod
    def getSubmission(self, id: str) -> 'XSubmission_bf230c2b':
        """
        get a submission with a certain ID.
        
        This is a convenience method: the same result can also be obtained through getSubmissions().
        """
    @abstractmethod
    def getSubmissions(self) -> 'XSet_90c40a4f':
        """
        get container containing all submissions; also supports XNameAccess
        """
    @abstractmethod
    def initialize(self) -> None:
        """
        initialize the model
        """
    @abstractmethod
    def rebuild(self) -> None:
        """
        rebuild the model
        """
    @abstractmethod
    def recalculate(self) -> None:
        """
        re-evaluate all calculate attributes
        """
    @abstractmethod
    def refresh(self) -> None:
        """
        refresh the model
        """
    @abstractmethod
    def revalidate(self) -> None:
        """
        re-evaluate all validity attributes
        """
    @abstractmethod
    def setID(self, id: str) -> None:
        """
        set the XForms model ID
        """
    @abstractmethod
    def submit(self, id: str) -> None:
        """
        submit form through given submission id
        
        This is a convenience method. Calling it is equivalent to calling getSubmission()( id ).submit().

        Raises:
            com.sun.star.util.VetoException: ``VetoException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    @abstractmethod
    def submitWithInteraction(self, id: str, aHandler: 'XInteractionHandler_bf80e51') -> None:
        """
        submit form through given submission id
        
        This is a convenience method. Calling it is equivalent to calling getSubmission()( id, handler ).submit().

        Raises:
            com.sun.star.util.VetoException: ``VetoException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """


__all__ = ['XModel']

