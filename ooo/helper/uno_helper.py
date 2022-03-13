# coding: utf-8
import uno
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
        clazz (str, object): name of the service or a service class to create an instance of.
        ctx (XComponentContext, optional): the context if required.
        args (Typle[object], optional): the arguments when needed.
    
    Returns:
        object: component instance

    Note:
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
        raise TypeError('create_uno_service() clazz incorrect type')
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
        `LibreOffice 7.2 SDK API theDesktop Reference <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1frame_1_1theDesktop.html>`_
    """
    global _STAR_DESKTOP
    if _STAR_DESKTOP == None:
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
        `LibreOffice 7.2 SDK theCoreReflection API Reference <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1reflection_1_1theCoreReflection.html>`_
    '''
    # https://stackoverflow.com/questions/67527942/why-cant-an-annotated-variable-be-global
    global _CORE_REFLECTION
    if not _CORE_REFLECTION:
        _CORE_REFLECTION = theCoreReflection()
    return _CORE_REFLECTION


def create_uno_struct(type_name: str) -> object:
    """Create a UNO struct and return it. 
    Similar to the function of the same name in OOo Basic. 
    
    Returns:
        object: uno struct
    """
    core_reflection = get_core_reflection()
    # Get the IDL class for the type name
    x_idl_class = core_reflection.forName(type_name)
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
        name (:obj:`str`, optional): Specifies the name of the property.
        value (:obj:`any`, optional): Contains the value of the property or ``None``, if no value is available.
        handle (:obj:`int`, optional): Contains an implementation-specific handle for the property.
        state (:obj:`com::sun::star::beans::PropertyState`, optional): Determines if the value comes from the object itself or from a default and if the value cannot be determined exactly.
    
    Returns:
        PropertyValue: ``com.sun.star.beans.PropertyValue`` struct.
    
    See Also:
        `LibreOffice API - PropertyValue Struct Reference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyValue.html>`_
    
    Note:
        This method is for convienence. Properties can also be created from dynamic PropertyValues
        
        Example:
        
        .. code-block:: python
        
            from ooo.dyn.beans.property_value import PropertyValue
            p = PropertyValue(Name='MyProperty', Value=101)
            assert p.Name == 'MyProperty'
            assert p.Value == 101
            assert type(p).__name__ == 'com.sun.star.beans.PropertyValue'
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
    return uno.getTypeByName(name)


def unoclass(name: str) -> type:
    """
    >>> unoclass('com.sun.star.text.XText')
    <class 'uno.com.sun.star.text.XText'>
    """
    return uno.getClass(name)

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

