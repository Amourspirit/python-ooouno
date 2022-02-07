# coding: utf-8
import uno
import string
import typing
if typing.TYPE_CHECKING:
    from ooo.lo.awt.point import Point
    from ooo.lo.awt.size import Size
    from ooo.lo.awt.rectangle import Rectangle
    from ooo.lo.beans.introspection import Introspection
    from ooo.lo.beans.property_value import PropertyValue
    from ooo.lo.beans.property_state import PropertyState
    from ooo.lo.drawing.drawing_document import DrawingDocument
    from ooo.lo.frame.desktop import Desktop
    from ooo.lo.lang.service_manager import ServiceManager
    from ooo.lo.lang.x_component import XComponent
    from ooo.lo.reflection.core_reflection import CoreReflection
    from ooo.lo.reflection.x_idl_method import XIdlMethod
    from ooo.lo.style.style import Style
    from ooo.lo.style.style_family import StyleFamily
    from ooo.lo.uno.x_component_context import XComponentContext
    from ooo.lo.uno.x_interface import XInterface
# from ...lib_ooo.type.com.sun.star.uno import XComponentContext
# from ...lib_ooo.type.com.sun.star.lang import XMultiComponentFactory
# from ...lib_ooo.type.com.sun.star.script.provider import XScriptContext
#**********************************************************************
#
#   Danny.OOo.OOoLib.py
#
#   A module to easily work with OpenOffice.org.
#   https://wiki.openoffice.org/wiki/Danny.OOo.OOoLib.py
#
#**********************************************************************
#   Copyright (c) 2003-2004 Danny Brewer
#   d29583@groovegarden.com
#
#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   See:  http://www.gnu.org/licenses/lgpl.html
#
#**********************************************************************
#   If you make changes, please append to the change log below.
#
#   Change Log
#   Danny Brewer         Revised 2004-06-07-01
#   Paul Moss            Revised 2021-04-14
#       Updated create_uno_service to take extra optional parameters
#   Paul Moss            Revised 2021-07-11
#       Commeted out get_desktop(). This was causing an error when lib was loaded
#       into unit test.
#       Added method set_danny_global(**kwargs) for the purpose of setting lib
#       globals. This is used in unit testing to set to lib to document opened in unit test
#
#   Paul Moss            Revised 2021-07-13
#       Added g_exportedScripts = () to end of script so LibreOffice ignores as a macro
#    Paul Moss           Revised 2021-09-08
#       Convert stringDocs to rest and update stringDocs
#**********************************************************************


# OOo's libraries


#------------------------------------------------------------
#   Uno ServiceManager access
#   A different version of this routine and global variable
#    is needed for code running inside a component.
#------------------------------------------------------------

# region Cached Values
# The StarDesktop object.  (global like in OOo Basic)
# It is cached in a global variable.
StarDesktop: 'Desktop' = None
# The ServiceManager of the running OOo.
# It is cached in a global variable.
# go_service_manager: Optional[XMultiComponentFactory] = None
go_service_manager: 'CoreReflection' = None

# The CoreReflection object.
# It is cached in a global variable.
go_core_reflection = False


def reset_cached():
    global StarDesktop
    global go_service_manager
    global go_core_reflection
    StarDesktop = None
    go_service_manager = None
    go_core_reflection = False
# endregion Cached Values


def set_danny_global(**kwargs):
    '''
    Set global vars for dannny_ooo_lib
    
    Keyword Args:
        desktop (object): Sets the desktop used in the get_desktop() function.
        sm (XMultiComponentFactory): Sets the service manager that is used for creating instances of objects.
    
    Note:
        This method is used primarly in testing
    '''
    global StarDesktop, go_service_manager
    if 'desktop' in kwargs:
        StarDesktop = kwargs['desktop']
    if 'sm' in kwargs:
        go_service_manager = kwargs['sm']


def get_service_manager() -> 'ServiceManager':
    """
    Get the ServiceManager from the running OpenOffice.org. 
    Then retain it in the global variable go_service_manager for future use. 
    This is similar to the GetProcessServiceManager() in OOo Basic. 
    
    Returns:
        XMultiComponentFactory: Service Manager
    """
    global go_service_manager
    if not go_service_manager:
        # Get the uno component context from the PyUNO runtime
        ctx: 'XComponentContext' = uno.getComponentContext()
        go_service_manager = ctx.getServiceManager()
    return go_service_manager


#------------------------------------------------------------
#   Uno convenience functions
#   The stuff in this section is just to make
#    python progrmaming of OOo more like using OOo Basic.
#------------------------------------------------------------


# This is the same as ServiceManager.createInstance( ... )
def create_uno_service(cClass: str, ctx: 'typing.Optional[XComponentContext]' = None, args: typing.Optional[typing.List[object]] = None) -> 'XInterface':
    """A handy way to create a global objects within the running OOo. 
    Similar to the function of the same name in OOo Basic. 
    
    Args:
        cClass (str): name of the service to be instanciated.
        ctx (XComponentContext, optional): the context if required.
        args (List[object], optional): the arguments when needed.
    
    Returns:
        object: component instance
    """
    smgr = get_service_manager()
    if ctx and args:
        oObj = smgr.createInstanceWithArgumentsAndContext(cClass, args, ctx)
    elif args:
        oObj = smgr.createInstanceWithArguments(cClass, args)
    elif ctx:
        oObj = smgr.createInstanceWithContext(cClass, ctx)
    else:
        oObj = smgr.createInstance(cClass)
    return oObj


def get_desktop() -> 'Desktop':
    """An easy way to obtain the Desktop object from a running OOo.
    
    Returns:
        object: com.sun.star.frame.Desktop
    
    See Also:
        `LibreOffice 7.2 SDK API Desktop Reference <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Desktop.html>`_
    
    Warning:
        Method uses "com.sun.star.frame.Desktop" and the
        `Desktop API <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Desktop.html>`_
        states that it is deprecated.
        The api suggest; Rather use the 'theDesktop' singleton.
    
    Todo:
        Test if this method would work with 'theDesktop'
    """
    global StarDesktop
    if StarDesktop == None:
        StarDesktop = create_uno_service("com.sun.star.frame.Desktop")
    return StarDesktop


# preload the StarDesktop variable.
# get_desktop()


def get_core_reflection() -> 'CoreReflection':
    '''
    This service is the implementation of the reflection API.
    
    Returns:
        object: com.sun.star.reflection.CoreReflection
    
    See Also:
        `LibreOffice 7.2 SDK CoreReflection API Reference <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1reflection_1_1CoreReflection.html>`_
    
    Warning:
        Method uses "com.sun.star.reflection.CoreReflection" and the
        `CoreReflection API <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1reflection_1_1CoreReflection.html>`_
        states that it is deprecated.
        The api suggest; Rather use the 'theCoreReflection' singleton.
    
    Todo:
        Test if this method would work with 'theCoreReflection'
    '''
    # https://stackoverflow.com/questions/67527942/why-cant-an-annotated-variable-be-global
    global go_core_reflection
    if not go_core_reflection:
        go_core_reflection = create_uno_service(
            "com.sun.star.reflection.CoreReflection")
    return go_core_reflection


def create_uno_struct(cTypeName: str) -> object:
    """Create a UNO struct and return it. 
    Similar to the function of the same name in OOo Basic. 
    
    Returns:
        object: uno struct
    """
    oCoreReflection = get_core_reflection()
    # Get the IDL class for the type name
    oXIdlClass = oCoreReflection.forName(cTypeName)
    # Create the struct.
    oReturnValue, oStruct = oXIdlClass.createObject(None)
    return oStruct


#def newConnectionToOOo( cHost="localhost", cPort="8100" ):
#    """Call this to establish, or re-establish a connection to OOo."""
#    global go_service_manager
#    global StarDesktop
#    global go_core_reflection
#    go_service_manager = False
#    StarDesktop = None
#    go_core_reflection = False
#    get_service_manager( cHost, cPort )
#    get_desktop()


#------------------------------------------------------------
#   API helpers
#------------------------------------------------------------

def has_uno_interface(oObject: object, cInterfaceName: str) -> bool:
    """
    Gets if if :paramref:`~.has_uno_interface.oObject` implements :paramref:`~.has_uno_interface.cInterfaceName`
    
    Args:
        oObject (object): Object to test for interface.
        cInterfaceName (str): Name of intefact to test for.
    
    Returns:
        bool: True if :paramref:`~.has_uno_interface.oObject` implements :paramref:`~.has_uno_interface.cInterfaceName`
        ; Otherwise, False
    
    Note:
        Similar to Basic's has_uno_interfaces() function, but singular not plural.
    """

    # Get the Introspection service.
    oIntrospection: 'Introspection' = create_uno_service(
        "com.sun.star.beans.Introspection")

    # Now inspect the object to learn about it.
    oObjInfo = oIntrospection.inspect(oObject)

    # Obtain an array describing all methods of the object.
    oMethods: 'typing.List[XIdlMethod]' = oObjInfo.getMethods(uno.getConstantByName(
        "com.sun.star.beans.MethodConcept.ALL"))
    # Now look at every method.
    for oMethod in oMethods:
        # Check the method's interface to see if
        #  these aren't the droids you're looking for.
        cMethodInterfaceName: str = oMethod.getDeclaringClass().getName()
        if cMethodInterfaceName == cInterfaceName:
            return True
    return False


def has_uno_interfaces(oObject: 'XInterface', *cInterfaces: 'XInterface') -> bool:
    """
    Gets if :paramref:`~.has_uno_interfaces.oObject` implements all :paramref:`~.has_uno_interfaces.cInterfaces`
    
    Args:
        oObject (object): object to test for interface(s)
        cInterfaces (str): one or more interfaces to test
    
    Returns:
        bool: ``True`` if :paramref:`~.has_uno_interfaces.oObject` implements all :paramref:`~.has_uno_interfaces.cInterfaces`
        ; Otherwise, ``False``
    
    Note:
        Similar to the function of the same name in OOo Basic.
    """
    for cInterface in cInterfaces:
        if not has_uno_interface(oObject, cInterface):
            return False
    return True


#------------------------------------------------------------
#   High level general purpose functions
#------------------------------------------------------------


def make_property_value(cName: typing.Optional[str] = None, uValue: object = None, nHandle: typing.Optional[int] = None, nState: 'typing.Optional[PropertyState]' = None) -> 'PropertyValue':
    """
    Create a com.sun.star.beans.PropertyValue.
    
    Args:
        cName (:obj:`str`, optional): Specifies the name of the property.
        uValue (:obj:`any`, optional): Contains the value of the property or ``None``, if no value is available.
        nHandle (:obj:`int`, optional): Contains an implementation-specific handle for the property.
        nState (:obj:`com::sun::star::beans::PropertyState`, optional): Determines if the value comes from the object itself or from a default and if the value cannot be determined exactly.
    
    Returns:
        object: ``com.sun.star.beans.PropertyValue`` struct.
    
    See Also:
        `LibreOffice API - PropertyValue Struct Reference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyValue.html>`_
    """
    oPropertyValue: 'PropertyValue' = create_uno_struct(
        "com.sun.star.beans.PropertyValue")

    if cName != None:
        oPropertyValue.Name = cName
    if uValue != None:
        oPropertyValue.Value = uValue
    if nHandle != None:
        oPropertyValue.Handle = nHandle
    if nState != None:
        oPropertyValue.State = nState

    return oPropertyValue


def make_point(nX: int, nY: int) -> 'Point':
    """
    Specifies a 2-dimensional point using the Cartesian coordinate system
    Create a com.sun.star.awt.Point struct.
    
    Args:
        nX (int): Specifies the x-coordinate
        nY (int): Specifies the y-coordinate
    
    Returns:
        com.sun.star.awt.Point: struct
    
    See Also:
        `LibreOffice API - Point Struct Reference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Point.html>`_
    """
    oPoint: 'Point' = create_uno_struct("com.sun.star.awt.Point")
    oPoint.X = nX
    oPoint.Y = nY
    return oPoint


def make_size(nWidth: int, nHeight: int) -> 'Size':
    """
    Specifies the 2-dimensional size of an area using width and height.
    
    Args:
        nWidth (int): specifies the width
        nHeight (int): specifies the height
    
    Returns:
        com.sun.star.awt.Size: struct
    
    See Also:
        `LibreOffice API - Size Struct Reference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Size.html>`_
    """
    oSize: 'Size' = create_uno_struct("com.sun.star.awt.Size")
    oSize.Width = nWidth
    oSize.Height = nHeight
    return oSize


def make_rectangle(nX: int, nY: int, nWidth: int, nHeight: int) -> 'Rectangle':
    """
    Specifies a rectangular area by position and size. 
    
    Args:
        nX (int): Specifies the x-coordinate.
        nY (int): Specifies the y-coordinate.
        nWidth (int): Specifies the width.
        nHeight (int): Specifies the height.
    
    Returns:
        com.sun.star.awt.Rectangle: struct
    
    See Also:
        `LibreOffice API - Rectangle Struct Reference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Rectangle.html>`_
    """
    oRect: 'Rectangle' = create_uno_struct("com.sun.star.awt.Rectangle")
    oRect.X = nX
    oRect.Y = nY
    oRect.Width = nWidth
    oRect.Height = nHeight
    return oRect


def Array(*args):
    """This is just sugar coating so that code from OOoBasic which 
    contains the Array() function can work perfectly in python."""
    tArray = ()
    for arg in args:
        tArray += (arg,)
    return tArray


def load_component_from_url(cUrl: str, tProperties: 'typing.List[PropertyValue]') -> 'XComponent':
    """
    Open or Create a document from it's URL.
    
    Args:
        cUrl (str): specifies the URL of the document to load
            New documents are created from URL's such as:
            
            * ``private:factory/sdraw``
            * ``private:factory/swriter``
            * ``private:factory/scalc``
            * ``private:factory/simpress``
        
        tProperties (:obj:`com::sun::star::beans::PropertyValue`, optional): Properties

    Returns:
        com::sun::star::lang::XComponent: ``XComponent`` for successfully loaded documents or
        ``None`` if it failed.
    
    See Also:
        `LibreOffice API - XComponentLoader Interface Reference <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XComponentLoader.html>`_
    """
    StarDesktop = get_desktop()
    oDocument = StarDesktop.loadComponentFromURL(
        cUrl, "_blank", 0, tProperties)
    return oDocument


#def makeWriterDocument():
#    """Create a new OOo Writer document."""
#    return load_component_from_url( "private:factory/swriter" )
#
#
#def makeCalcDocument():
#    """Create a new OOo Calc document."""
#    return load_component_from_url( "private:factory/scalc" )


#------------------------------------------------------------
#   Styles
#------------------------------------------------------------


def define_style(oDrawDoc: 'DrawingDocument', cStyleFamily: str, cStyleName: str, cParentStyleName: typing.Optional[str] = None) -> 'Style':
    """Add a new style to the style catalog if it is not already present. 
    This returns the style object so that you can alter its properties. 
    """
    # oStyleFamily = oDrawDoc.get_styleFamilies().getByName(cStyleFamily)
    oStyleFamily: 'StyleFamily' = oDrawDoc.getStyleFamilies().getByName(cStyleFamily)

    # Does the style already exist?
    if oStyleFamily.hasByName(cStyleName):
        # then get it so we can return it.
        oStyle: 'Style' = oStyleFamily.getByName(cStyleName)
    else:
        # Create new style object.
        oStyle: 'Style' = oDrawDoc.createInstance("com.sun.star.style.Style")

        # Set its parent style
        if cParentStyleName != None:
            oStyle.setParentStyle(cParentStyleName)

        # Add the new style to the style family.
        oStyleFamily.insertByName(cStyleName, oStyle)

    return oStyle


def get_style(oDrawDoc: 'DrawingDocument', cStyleFamily: str, cStyleName: str) -> 'Style':
    """Lookup and return a style from the document. 
    """
    return oDrawDoc.getStyleFamilies().getByName(cStyleFamily).getByName(cStyleName)


#------------------------------------------------------------
#   General Utility functions
#------------------------------------------------------------


def convert_to_url(cPathname: str) -> str:
    """
    Convert a Windows or Linux pathname into an OOo URL.
    
    Args:
        cPathname (str): Path Name to Convert
    
    Returns:
        string: Converted path to url.
    """
    if len(cPathname) > 1:
        if cPathname[1:2] == ":":
            cPathname = "/" + cPathname[0] + "|" + cPathname[2:]
    cPathname = string.replace(cPathname, "\\", "/")
    cPathname = "file://" + cPathname
    return cPathname

