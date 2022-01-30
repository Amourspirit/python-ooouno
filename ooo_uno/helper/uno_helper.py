# coding: utf-8
import uno
import typing
if typing.TYPE_CHECKING:
    from ..uno_obj.beans.property_value import PropertyValue
    from ..uno_obj.beans.property_state import PropertyState
    from ..uno_obj.frame.desktop import Desktop
    from ..uno_obj.lang.service_manager import ServiceManager
    from ..uno_obj.reflection.core_reflection import CoreReflection
    from ..uno_obj.uno.x_component_context import XComponentContext
    from ..uno_obj.uno.x_interface import XInterface



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
# endregion Cached Values

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






