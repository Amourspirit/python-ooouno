# coding: utf-8
from abc import abstractmethod
from typing import TYPE_CHECKING
from ..lang.x_component import XComponent
if TYPE_CHECKING:
    from .x_frame import XFrame


class XController(XComponent):
    """
    With this interface, components viewed in a Frame can serve events
    (by supplying dispatches).

    See Also:
        `API XController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XController.html>`_
    """

    @abstractmethod
    def attachFrame(self, Frame: 'XFrame'):
        """
        is called to attach the controller with its managing frame.

        Args:
            Frame (XFrame): the new owner frame of this controller
        """

    @abstractmethod
    def attachModel(self, Model: object) -> bool:
        """
        is called to attach the controller to a new model.

        Args:
            Model (XModel): the new model for this controller

        Todo:
            Update arg Model type to be of type XModel

        Returns:
            bool: ``True`` If attaching was successful; Otherwise, ``False``.
        """

    @abstractmethod
    def getFrame(self) -> 'XFrame':
        """
        provides access to owner frame of this controller

        Returns:
            XFrame: the frame containing this controller.
        """

    @abstractmethod
    def getModel(self) -> object:
        """
        provides access to currently attached model

        Todo:
            Update return type to be of type XModel

        Returns:
            XModel: the currently attached model.
        """

    @abstractmethod
    def getViewData(self) -> object:
        """
        provides access to current view status

        Returns:
            object: set of data that can be used to restore the
            current view status at later ti: objectme by using ``XController.restoreViewData()``:

        """

    @abstractmethod
    def restoreViewData(self, Data: object):
        """
        restores the view status using the data gotten from a previous call to ``XController.getViewData()``.

        Args:
            Data (object): set of data to restore it
        """

    @abstractmethod
    def suspend(self, Suspend: bool) -> bool:
        """
        is called to prepare the controller for closing the view

        Args:
            Suspend (bool): ``True`` Force the controller to suspend his work ``False``
                Try to reactivate the controller

        Returns:
            bool: ``True`` If request was accepted and successfully finished; Otherwise, ``False``.
        """
