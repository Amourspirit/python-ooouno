# coding: utf-8
import uno
import pyuno
import typing
from ..dyn.frame.the_desktop import theDesktop
from ..dyn.reflection.the_core_reflection import theCoreReflection

if typing.TYPE_CHECKING:
    from ..lo.beans.property_value import PropertyValue
    from ..lo.beans.property_state import PropertyState
    from ..lo.frame.the_desktop import theDesktop
    from ..lo.lang.service_manager import ServiceManager
    # from ..lo.reflection.core_reflection import CoreReflection
    from ..lo.uno.x_component_context import XComponentContext
    from ..lo.uno.x_interface import XInterface
    from ..lo.lang.x_service_info import XServiceInfo



# OOo's libraries


#------------------------------------------------------------
#   Uno ServiceManager access
#   A different version of this routine and global variable
#    is needed for code running inside a component.
#------------------------------------------------------------

# region Cached Values
# The _STAR_DESKTOP object.  (global like in OOo Basic)
# It is cached in a global variable.
_STAR_DESKTOP: theDesktop = None
# The ServiceManager of the running OOo.
# It is cached in a global variable.
# _SERVICE_MGR: Optional[XMultiComponentFactory] = None
_SERVICE_MGR: 'ServiceManager' = None

# The CoreReflection object.
# It is cached in a global variable.
_CORE_REFLECTION: theCoreReflection = False
# endregion Cached Values

def get_service_manager() -> 'ServiceManager':
    """
    Get the ServiceManager from the running OpenOffice.org. 
    Then retain it in the global variable _SERVICE_MGR for future use. 
    This is similar to the GetProcessServiceManager() in OOo Basic. 
    
    Returns:
        XMultiComponentFactory: Service Manager
    """
    global _SERVICE_MGR
    if not _SERVICE_MGR:
        # Get the uno component context from the PyUNO runtime
        ctx: 'XComponentContext' = uno.getComponentContext()
        _SERVICE_MGR = ctx.getServiceManager()
    return _SERVICE_MGR


#------------------------------------------------------------
#   Uno convenience functions
#   The stuff in this section is just to make
#    python progrmaming of OOo more like using OOo Basic.
#------------------------------------------------------------

def create_uno_service(clazz: typing.Union[str, object], ctx: 'typing.Optional[XComponentContext]' = None, args: typing.Optional[typing.Tuple[object]] = None) -> 'XInterface':
    """A handy way to create a global objects within the running OOo. 
    Similar to the function of the same name in OOo Basic. 
    
    Args:
        clazz (str, object): name of the service to be instanciated or object that contains __ooo_full_ns__ attribute.
            If ``clazz`` is class then return service has ``__ooo_ns__``, ``__ooo_full_ns__`` and ``__ooo_type_name__`` atribute values set.
        ctx (XComponentContext, optional): the context if required.
        args (Typle[object], optional): the arguments when needed.
    
    Returns:
        object: component instance

    Notes:
        A service signals that it expects parameters during instantiation by supporting the com.sun.star.lang.XInitialization interface.
        There maybe services which can only be instantiated with parameters
    """
    is_class = False
    if isinstance(clazz, str):
        _cls = clazz
    elif hasattr(clazz, '__ooo_full_ns__'):
        _cls = clazz.__ooo_full_ns__
        is_class = True
    else:
        raise TypeError('create_uno_service() cClass incorrect type')
    srv = _create_uno_service(clazz=_cls, ctx=ctx,args=args)
    if is_class:
        srv.__dict__['__ooo_ns__'] = clazz.__ooo_ns__
        srv.__dict__['__ooo_full_ns__'] = clazz.__ooo_full_ns__
        srv.__dict__['__ooo_type_name__'] = clazz.__ooo_type_name__
    return srv

def _create_uno_service(clazz: str, ctx: 'typing.Optional[XComponentContext]' = None, args: typing.Optional[typing.Tuple[object]] = None) -> 'XInterface':
    """Creates a global objects within the running OOo. 
    Similar to the function of the same name in OOo Basic. 
    
    Args:
        clazz (str): name of the service to be instanciated.
        ctx (XComponentContext, optional): the context if required.
        args (List[object], optional): the arguments when needed.
    
    Returns:
        object: component instance

    Notes:
        A service signals that it expects parameters during instantiation by supporting the com.sun.star.lang.XInitialization interface.
        There maybe services which can only be instantiated with parameters
    """
    # https://wiki.openoffice.org/wiki/Documentation/DevGuide/ProUNO/Service_Manager
    # In case the service manager does not provide an implementation for a request,
    # a null reference is returned, so it is mandatory to check.
    # Every UNO exception may be thrown during instantiation.
    smgr = get_service_manager()
    if ctx and args:
        oObj = smgr.createInstanceWithArgumentsAndContext(clazz, args, ctx)
    elif args:
        oObj = smgr.createInstanceWithArguments(clazz, args)
    elif ctx:
        oObj = smgr.createInstanceWithContext(clazz, ctx)
    else:
        oObj = smgr.createInstance(clazz)
    return oObj


def get_desktop() -> theDesktop:
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
    global _STAR_DESKTOP
    if _STAR_DESKTOP == None:
        ctx: 'XComponentContext' = uno.getComponentContext()
        # _STAR_DESKTOP = ctx.getValueByName('/singletons/com.sun.star.frame.theDesktop')
        # _STAR_DESKTOP = create_uno_service("com.sun.star.frame.Desktop")
        _STAR_DESKTOP = theDesktop()
    return _STAR_DESKTOP


# preload the _STAR_DESKTOP variable.
# get_desktop()


def get_core_reflection() -> theCoreReflection:
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
    global _CORE_REFLECTION
    if not _CORE_REFLECTION:
        # _CORE_REFLECTION = create_uno_service("com.sun.star.reflection.CoreReflection")
        _CORE_REFLECTION = theCoreReflection()
    return _CORE_REFLECTION


def create_uno_struct(cTypeName: str) -> object:
    """Create a UNO struct and return it. 
    Similar to the function of the same name in OOo Basic. 
    
    Returns:
        object: uno struct
    """
    core_reflection = get_core_reflection()
    # Get the IDL class for the type name
    x_idl_class = core_reflection.forName(cTypeName)
    # Create the struct.
    _, struct = x_idl_class.createObject(None)
    return struct



#------------------------------------------------------------
#   High level general purpose functions
#------------------------------------------------------------


def make_property_value(name: typing.Optional[str] = None, value: object = None, handle: typing.Optional[int] = None, state: 'typing.Optional[PropertyState]' = None) -> 'PropertyValue':
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
    property_value: 'PropertyValue' = create_uno_struct(
        "com.sun.star.beans.PropertyValue")

    if name != None:
        property_value.Name = name
    if value != None:
        property_value.Value = value
    if handle != None:
        property_value.Handle = handle
    if state != None:
        property_value.State = state

    return property_value


def unotype(name: str) -> uno.Type:
    """
    >>> unotype('com.sun.star.uno.XInterface')
    <Type instance com.sun.star.uno.XInterface
        (<uno.Enum com.sun.star.uno.TypeClass ('INTERFACE')>)>
    """
    return pyuno.getTypeByName(name)


def unoclass(name: str) -> type:
    """
    >>> unoclass('com.sun.star.text.XText')
    <class 'uno.com.sun.star.text.XText'>
    """
    return pyuno.getClass(name)

@typing.overload
def supports_service(si:'XServiceInfo', *services: str ) -> bool:
    """
    Tests whether the specified service is supported.

    Args:
        si (XServiceInfo): service that implements XServiceInfo
    
    Other Arguments:
        services (str) comma seperated services to test

    Raises:
        TypeError: If ``si`` is does not implement XServiceInfo

    Returns:
        bool: ``True`` if ``si`` suppoorts service; Otherwise ``False``
    """
@typing.overload
def supports_service(si:'XServiceInfo', *services: object ) -> bool:
    """
    Tests whether the specified service is supported.

    Args:
        si (XServiceInfo): service that implements XServiceInfo

    Other Arguments:
        services (object) comma seperated services to test

    Raises:
        TypeError: If ``si`` is does not implement XServiceInfo
        ValueError: if a service object is invalid.

    Returns:
        bool: ``True`` if ``si`` suppoorts service; Otherwise ``False``
    """

def supports_service(si:'XServiceInfo', *services: typing.Union[str, object] ) -> bool:
    if not hasattr(si, 'supportsService'):
        raise TypeError("supports_service() 'si' does not contain attribute supportsService.")
    if len(services) == 0:
        return False
    result = False
    for srv in services:
        if isinstance(srv, str):
            ns = srv
        elif hasattr(srv, '__ooo_full_ns__'):
            ns = srv.__ooo_full_ns__
        else:
            raise ValueError(f"supports_service() Unable to obtain service name for type: {type(srv).__name__}")
        if si.supportsService(ns):
            result = True
            break
    return result

