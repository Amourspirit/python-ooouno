# coding: utf-8
from abc import abstractmethod
# from com.sun.star.lang import XEventListener
from ..uno.x_interface import XInterface


class XEventListener(XInterface):
    """
    base interface for all event listeners interfaces.

    See Also:
        `API XEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XEventListener.html>`_
    """

    @abstractmethod
    def disposing(self, Source: object):
        """
        gets called when the broadcaster is about to be disposed.

        All listeners and all other objects, which reference the broadcaster should release
        the reference to the source. No method should be invoked anymore on this object
        ( including XComponent::removeEventListener() ).

        This method is called for every listener registration of derived listener interfaced,
        not only for registrations at XComponent.


        Args:
            Source (object): event object
        """
