# coding: utf-8
from abc import abstractmethod
from typing import TYPE_CHECKING
from ...uno.x_interface import XInterface
if TYPE_CHECKING:
    from ...uno.x_component_context import XComponentContext
    from ...frame.x_desktop import XDesktop


class XScriptContext(XInterface):
    """
    This interface is provided to scripts, and provides a means of access to
    the various interfaces which they might need to perform some action on a document.
    """
    @abstractmethod
    def getComponentContext() -> 'XComponentContext':
        """
        Obtain the component context which the script can use to create other uno components.

        Returns:
            XComponentContext: interface
        """

    @abstractmethod
    def getDesktop() -> 'XDesktop':
        """
        Obtain the desktop reference on which the script can operate.

        Returns:
            XDesktop: desktop
        """

    @abstractmethod
    def getDocument():
        """
        Obtain the document reference on which the script can operate.

        Todo:
            Update return types to be XModel

        Returns:
            XModel: document
        """

    @abstractmethod
    def getInvocationContext():
        """
        provides access to the context where the script was invoked

        In some cases, it is possible that scripts, embedded in a document,
        are executed from within a context which is not the document itself.
        In this case, the getInvocationContext member allows to access this context.

        Note that the returned context is allowed to be NULL, in this case,
        the document as returned by getDocument is the invocation context.

        If the returned context is not NULL, its ScriptContainer attribute equals the
        document as returned by ``XScriptContext.getDocument``.


        **Since**

            OOo 3.0


        Todo:
            Update return types to be XScriptInvocationContext 

        Returns:
            XScriptInvocationContext: content
        """
