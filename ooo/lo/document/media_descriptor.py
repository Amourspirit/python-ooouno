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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.document
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from ..frame.x_frame import XFrame as XFrame_7a570956
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_output_stream import XOutputStream as XOutputStream_a4e00b35
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51
    from ..task.x_status_indicator import XStatusIndicator as XStatusIndicator_e2d00d34

class MediaDescriptor(ABC):
    """
    Service Class

    describes properties of a document, regarding the relationship between the loaded document and the resource the document is loaded from / stored to.
    
    This service may be represented by a com.sun.star.beans.PropertyValue[]. Such descriptors will be passed to different functions, included into possible load/save processes. Every member of such process can use this descriptor and may change it if to actualize the information about the document. So this descriptor should be used as an in/out parameter.
    
    Note:It's not allowed to hold member of this descriptor by references longer than they will be used (especially a possible stream). It's allowed to use it directly or by copying it only.
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API MediaDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1MediaDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.MediaDescriptor'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Aborted(self) -> bool:
        """
        May be set by filters or detection services if user has chosen to abort loading/saving, e.g.
        
        while entering a password.
        """
        ...

    @property
    @abstractmethod
    def AsTemplate(self) -> bool:
        """
        document is a template
        
        Loading a component of type \"template\" creates a new untitled document by default, but setting the \"AsTemplate\" property to FALSE loads the template document for editing. Setting \"AsTemplate\" to TRUE creates a new untitled document out of the loaded document, even if it has not a \"template\" type.
        """
        ...

    @property
    @abstractmethod
    def Author(self) -> str:
        """
        the author of the document
        
        Only for storing versions in components supporting versioning: author of version.
        """
        ...

    @property
    @abstractmethod
    def CharacterSet(self) -> str:
        """
        identifier of used character set
        
        Defines the character set for document formats that contain single byte characters (if necessary).
        """
        ...

    @property
    @abstractmethod
    def Comment(self) -> str:
        """
        description of document
        
        Only for storing versions in components supporting versioning: comment (description) for stored version.
        """
        ...

    @property
    @abstractmethod
    def ComponentData(self) -> object:
        """
        pack specific properties of caller
        
        This is a parameter that can be used for any properties specific for a special component type. Format of that depends from real type of addressed component.
        
        For extensibility, it is recommended to use values of type sequence<com.sun.star.beans.NamedValue> with this property.
        """
        ...

    @property
    @abstractmethod
    def DocumentBaseURL(self) -> str:
        """
        The base URL of the document to be used to resolve relative links.
        """
        ...

    @property
    @abstractmethod
    def DocumentTitle(self) -> str:
        """
        document title
        
        This parameter can be used to specify a title for a document.
        """
        ...

    @property
    @abstractmethod
    def EncryptionData(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        encryption information for encryption/decryption of documents
        
        It contains the necessary information for encryption/decryption of a component (if necessary). If neither password nor encryption data is specified, loading of a password protected document will fail, storing will be done without encryption. If both are provided, the encryption data is used ( if the filter supports it ).
        
        The encryption data is generated based on the password.
        """
        ...

    @property
    @abstractmethod
    def FileName(self) -> str:
        """
        same as MediaDescriptor.URL
        
        It will be supported for compatibility reasons only.
        """
        ...

    @property
    @abstractmethod
    def FilterData(self) -> object:
        """
        additional properties for filter
        
        This is a parameter that can be used for any properties specific for a special filter type. It should be used if MediaDescriptor.FilterOptions isn't enough.
        """
        ...

    @property
    @abstractmethod
    def FilterFlags(self) -> str:
        """
        same as MediaDescriptor.FilterOptions
        
        It will be supported for compatibility reasons only.
        """
        ...

    @property
    @abstractmethod
    def FilterName(self) -> str:
        """
        internal filter name
        
        Name of a filter that should be used for loading or storing the component. Names must match the names of the TypeDetection configuration, invalid names are ignored. If a name is specified on loading, it still will be verified by a filter detection, but in case of doubt it will be preferred.
        
        See this page for a list of internal filter names: https://help.libreoffice.org/latest/en-US/text/shared/guide/convertfilters.html
        """
        ...

    @property
    @abstractmethod
    def FilterOptions(self) -> str:
        """
        additional properties for filter
        
        Some filters need additional parameters; use only together with property MediaDescriptor.FilterName. Details must be documented by the filter. This is an old format for some filters. If a string is not enough, filters can use the property MediaDescriptor.FilterData.
        """
        ...

    @property
    @abstractmethod
    def Frame(self) -> XFrame_7a570956:
        """
        specifies the frame containing the document.
        
        May be empty.
        """
        ...

    @property
    @abstractmethod
    def Hidden(self) -> bool:
        """
        load document invisible
        
        Defines if the loaded component is made visible. If this property is not specified, the component is made visible by default.
        """
        ...

    @property
    @abstractmethod
    def HierarchicalDocumentName(self) -> str:
        """
        The hierarchical path to the embedded document from topmost container.
        """
        ...

    @property
    @abstractmethod
    def InputStream(self) -> XInputStream_98d40ab4:
        """
        content of document
        
        If used when loading a document: reading must be done using this stream. If no stream is provided, the loader will create a stream by itself using the other properties. It is not allowed to keep a reference to this InputStream after loading the component, and it would be useless, because in general an InputStream is usable for reading only once, except when it also implements the com.sun.star.io.XSeekable interface.
        """
        ...

    @property
    @abstractmethod
    def InteractionHandler(self) -> XInteractionHandler_bf80e51:
        """
        handle exceptional situations
        
        Object implementing the com.sun.star.task.InteractionHandler service that is used to handle exceptional situations where proceeding with the task is impossible without additional information or impossible at all. The implemented API provides a default implementation for it that can handle many situations. If no InteractionHandler is set, a suitable exception is thrown. It is not allowed to keep a reference to this object, even not in the loaded or stored component's copy of the MediaDescriptor provided by its arguments attribute.
        """
        ...

    @property
    @abstractmethod
    def JumpMark(self) -> str:
        """
        jump to a marked position after loading
        
        This is the same as the text behind a \"#\" in a http URL. But this syntax with a \"#\" is not specified in most URL schemas.
        """
        ...

    @property
    @abstractmethod
    def LockContentExtraction(self) -> bool:
        """
        Setting this option will prevent copying/dragging any content anywhere.
        
        The commands 'Copy' and 'Cut' will be disabled; selection clipboard won't work, and dragging with mouse will also be disabled.
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @property
    @abstractmethod
    def LockEditDoc(self) -> bool:
        """
        Setting this option will disable switching to edit mode from read-only mode.
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @property
    @abstractmethod
    def LockExport(self) -> bool:
        """
        Setting this option will prevent exporting document content to any file.
        
        Export, Send, save as, etc will be disabled, as well as individual graphic/chart export and mail merge.
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @property
    @abstractmethod
    def LockPrint(self) -> bool:
        """
        Setting this option will disable all print functions (including Printer setup)
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @property
    @abstractmethod
    def LockSave(self) -> bool:
        """
        Setting this option will disable the save function.
        
        **since**
        
            LibreOffice 6.4
        """
        ...

    @property
    @abstractmethod
    def MacroExecutionMode(self) -> int:
        """
        should the macro be executed.
        
        the value should be one from com.sun.star.document.MacroExecMode constant list.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @property
    @abstractmethod
    def MediaType(self) -> str:
        """
        specify mime type of content
        
        Type of the medium to load, that must match to one of the types defined in the TypeDetection configuration (otherwise it's ignored). This bypasses the type detection of the com.sun.star.frame.Desktop environment, so passing a wrong MediaType will cause failure of loading.
        """
        ...

    @property
    @abstractmethod
    def OpenFlags(self) -> str:
        """
        please use the corresponding parameters of this descriptor instead
        
        String that summarizes some flags for loading. The string contains capital letters for the flags:
        """
        ...

    @property
    @abstractmethod
    def OpenNewView(self) -> bool:
        """
        opens a new view for an already loaded document
        
        Setting this to TRUE forces the component to create a new window on loading in any case. If the component supports multiple views, a second view is opened, if not, the component is loaded one more time. Otherwise the behavior depends on the default window handling of the com.sun.star.frame.Desktop environment.
        """
        ...

    @property
    @abstractmethod
    def OutputStream(self) -> XOutputStream_a4e00b35:
        """
        a stream to receive the document data.
        
        If used when storing a document: writing must be done using this stream. If no stream is provided, the loader will create a stream by itself using the other properties. It is not allowed to keep a reference to this OutputStream after storing the component.
        """
        ...

    @property
    @abstractmethod
    def Overwrite(self) -> bool:
        """
        overwrite any existing file
        
        For storing only: overwrite any existing file, default is TRUE. Setting this to FALSE raises an error, if the target file already exists.
        """
        ...

    @property
    @abstractmethod
    def Password(self) -> str:
        """
        password for loading or storing documents
        
        It contains a password for loading or storing a component (if necessary). If neither password nor encryption data is specified, loading of a password protected document will fail, storing will be done without encryption. If both are provided, the encryption data is used ( if the filter supports it ).
        """
        ...

    @property
    @abstractmethod
    def PickListEntry(self) -> bool:
        """
        add loaded document to recent document list
        
        Setting this to FALSE prevents the loaded document to be added to the recent documents list. Default is TRUE.
        
        **since**
        
            LibreOffice 5.1
        """
        ...

    @property
    @abstractmethod
    def PostData(self) -> typing.Tuple[int, ...]:
        """
        contains the data for HTTP post method as a sequence of bytes.
        
        Data to send to a location described by the media descriptor to get a result in return that will be loaded as a component (usually in webforms). Default is: no PostData.
        """
        ...

    @property
    @abstractmethod
    def PostString(self) -> str:
        """
        use MediaDescriptor.PostData instead of this
        
        Same as PostData, but the data is transferred as a string (just for compatibility).
        """
        ...

    @property
    @abstractmethod
    def Preview(self) -> bool:
        """
        show preview
        
        Setting this to TRUE tells the a loaded component that it is loaded as a preview, so it can optimize loading and viewing for this special purpose. Default is FALSE.
        """
        ...

    @property
    @abstractmethod
    def ReadOnly(self) -> bool:
        """
        open document readonly
        
        Tells whether a document should be loaded in a (logical) readonly or in read/write mode. If opening in the desired mode is impossible, an error occurs. By default the loaded content decides what to do: if its UCB content supports a \"readonly\" property, the logical open mode depends on that, otherwise it will be read/write. This is only a UI related property, opening a document in read only mode will not prevent the component from being modified by API calls, but all modifying functionality in the UI will be disabled or removed.
        """
        ...

    @property
    @abstractmethod
    def Referer(self) -> str:
        """
        name of document referrer
        
        A URL describing the environment of the request; e.g. a referrer may be a URL of a document, if a hyperlink inside this document is clicked to load another document. The referrer may be evaluated by the addressed UCB content or the loaded document. Without a referrer the processing of URLs that needs security checks will be denied, e.g. \"macro:\" URLs. Don't be confused about the wrong spelling; it is kept for compatibility reasons.
        """
        ...

    @property
    @abstractmethod
    def RepairPackage(self) -> bool:
        """
        let the document be opened in repair mode
        
        For loading of corrupted zip packages: Setting this to TRUE let the document be opened in repair mode, so as much as possible information will be retrieved.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @property
    @abstractmethod
    def Replaceable(self) -> bool:
        """
        Mark the document as replaceable / a placeholder.
        
        Normally a document is always opened in a new frame. If this property is set to true, this document just acts as a placeholder while it's unmodified. I.e. the next opened document from its frame will close and replace it.
        
        This defaults to false, except for the default template of a LibreOffice module, referenced as \"private:factory/&lt;module&gt;\".
        
        **since**
        
            LibreOffice 7.0
        """
        ...

    @property
    @abstractmethod
    def StartPresentation(self) -> bool:
        """
        start presentation from a document
        
        Tells the component loading the document that a presentation that is in the document is to be started right away.
        """
        ...

    @property
    @abstractmethod
    def StatusIndicator(self) -> XStatusIndicator_e2d00d34:
        """
        can be used for status information
        
        Object implementing the com.sun.star.task.XStatusIndicator interface that can be used to give status information (text or progress) for the task. The office provides a default implementation for it. It is not allowed to keep a reference to this object, even not in the loaded or stored component's copy of the MediaDescriptor provided by its arguments attribute.
        """
        ...

    @property
    @abstractmethod
    def SuggestedSaveAsDir(self) -> str:
        """
        allows to specify the URL that is used next time SaveAs dialog is opened
        
        If the parameter is specified, the URL will be used by SaveAs dialog next time as target folder.
        """
        ...

    @property
    @abstractmethod
    def SuggestedSaveAsName(self) -> str:
        """
        allows to specify the suggested file name that is used next time SaveAs dialog is opened
        
        If the parameter is specified, the file name will be suggested by SaveAs dialog next time.
        """
        ...

    @property
    @abstractmethod
    def TemplateName(self) -> str:
        """
        name of the template instead of the URL
        
        The logical name of a template to load. Together with the MediaDescriptor.TemplateRegion property it can be used instead of the URL of the template. Use always in conjunction with MediaDescriptor.TemplateRegionName.
        """
        ...

    @property
    @abstractmethod
    def TemplateRegionName(self) -> str:
        """
        name of the template instead of the URL
        
        See MediaDescriptor.TemplateName. The template region names are the folder names you see in the templates dialog.
        """
        ...

    @property
    @abstractmethod
    def URL(self) -> str:
        """
        URL of the document.
        
        The location of the component in URL syntax. It must be a fully qualified URL.
        """
        ...

    @property
    @abstractmethod
    def Unpacked(self) -> bool:
        """
        regulate using of compressing
        
        For storing: Setting this to TRUE means, don't use a zip file to save the document, use a folder instead (only usable for UCB contents, that support folders). Default is FALSE.
        """
        ...

    @property
    @abstractmethod
    def UpdateDocMode(self) -> int:
        """
        can the document be updated depending from links.
        
        the value should be one from com.sun.star.document.UpdateDocMode constant list.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @property
    @abstractmethod
    def Version(self) -> int:
        """
        storage version
        
        For components supporting versioning: the number of the version to be loaded or saved. Default is zero and means: no version is created or loaded, the \"main\" document is processed.
        """
        ...

    @property
    @abstractmethod
    def ViewControllerName(self) -> str:
        """
        specifies the name of the view controller to create when loading a document
        
        If this property is used when loading a document into a frame, then it specifies the name of the view controller to create. That is, the property is passed to the document's com.sun.star.frame.XModel2.createViewController() method.If the loaded document does not support the XModel2 interface, the property is ignored.
        
        **since**
        
            OOo 3.0
        """
        ...

    @property
    @abstractmethod
    def ViewData(self) -> object:
        """
        set special view state
        
        Data to set a special view state after loading. The type depends on the component and is usually retrieved from a com.sun.star.frame.Controller object by its com.sun.star.frame.XController interface. Default is: no view data.
        """
        ...

    @property
    @abstractmethod
    def ViewId(self) -> int:
        """
        id of the initial view
        
        For components supporting different views: a number to define the view that should be constructed after loading. Default is: zero, and this should be treated by the component as the default view.
        """
        ...


__all__ = ['MediaDescriptor']

