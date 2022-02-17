# coding: utf-8
import typing
from ooo.helper import uno_helper
if typing.TYPE_CHECKING:
    from ooo.lo.frame.the_desktop import theDesktop
    from ooo.lo.lang.service_manager import ServiceManager
    from ooo.lo.reflection.the_core_reflection import theCoreReflection
    from ooo.lo.uno.x_component_context import XComponentContext
    from ooo.lo.uno.x_interface import XInterface


def reset_cached():
    uno_helper._STAR_DESKTOP = None
    uno_helper._SERVICE_MGR = None
    uno_helper._CORE_REFLECTION = False


def set_globals(**kwargs):
    '''
    Set global vars for dannny_ooo_lib
    
    Keyword Args:
        desktop (object): Sets the desktop used in the get_desktop() function.
        sm (XMultiComponentFactory): Sets the service manager that is used for creating instances of objects.
    
    Note:
        This method is used primarly in testing
    '''
    if 'desktop' in kwargs:
        uno_helper._STAR_DESKTOP = kwargs['desktop']
    if 'sm' in kwargs:
        uno_helper._SERVICE_MGR = kwargs['sm']


def get_service_manager() -> 'ServiceManager':
    return uno_helper.get_service_manager()



def create_uno_service(clazz: typing.Union[str, object], ctx: 'typing.Optional[XComponentContext]' = None, args: typing.Optional[typing.Tuple[object]] = None) -> 'XInterface':
    return uno_helper.create_uno_service(clazz=clazz, ctx=ctx, args=args)


def get_desktop() -> 'theDesktop':
    return uno_helper.get_desktop()


def get_core_reflection() -> 'theCoreReflection':
    return uno_helper.get_core_reflection()


def create_uno_struct(type_name: str) -> object:
    return uno_helper.create_uno_struct(type_name)


