# coding: utf-8
from ...base.const import ConstIntFlagsBase


class IFrameSearchFlag(ConstIntFlagsBase):
    """
    these types describe the algorithm to be used to search a frame

    Such flags will be used on methods ``XFrame.findFrame()``, ``XDispatchProvider.queryDispatch()``
    or ``XComponentLoader.loadComponentFromURL()`` if no special target frame name
    (e.g. "_blank", "_self") is used.
    
    See Also:
        `API FrameSearchFlag <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame_1_1FrameSearchFlag.html>`_
    """
    AUTO = 0
    """no longer supported"""
    PARENT = 1
    """allows search on the parent frames """
    SELF = 2
    """includes the start frame"""
    CHILDREN = 4
    """includes all child frames of the start frame"""
    CREATE = 8
    """frame will be created if not found"""
    SIBLINGS = 16
    """includes the direct siblings of the start frame"""
    TASKS = 32
    """allow the search outside the current sub task tree of the whole possible frame tree"""
    ALL = 23
    """includes all frames except frames in other tasks sub trees but doesn't create any new frame"""
    GLOBAL = 55
    """searches in the whole hierarchy of frames but doesn't create any new frame"""
