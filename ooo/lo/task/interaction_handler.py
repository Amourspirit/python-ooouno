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
# Namespace: com.sun.star.task
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_interaction_handler2 import XInteractionHandler2 as XInteractionHandler2_1a7b0e83
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924

class InteractionHandler(XInteractionHandler2_1a7b0e83):
    """
    Service Class

    An interaction request handler that lets the user handle requests via GUI dialogs.
    
    The interaction handler service has a number of built-in handlers, responsible for a lot of well known interactions. Additionally, there's a configuration module which allows to configure additional handlers, responsible for arbitrary requests.
    
    The following well-known requests can be dealt with by the built-in handlers:
    
    The requests marked with an asterisk are only handled if (a) their continuations match certain restrictions (see below), and (b) the necessary resource strings are available (this can be exploited by applications that carry only a subset of all resource files with them).
    
    The continuation restrictions are as follows: Let C be the subset of the provided continuations that are of type com.sun.star.task.XInteractionApprove, com.sun.star.task.XInteractionDisapprove, com.sun.star.task.XInteractionRetry, or com.sun.star.task.XInteractionAbort (or of a derived type). All other continuations are ignored for these requests. The request is only handled if the set C is any of the following:
    
    An com.sun.star.ucb.InteractiveAugmentedIOException carries with it a sequence of arguments, which should be com.sun.star.beans.PropertyValues. The following details which properties are interpreted by the interaction handler, depending on the request's com.sun.star.ucb.IOErrorCode:
    
    It is possible to configure additional interaction handlers, to which certain requests can be delegated. The configuration node /org.openoffice.Interaction/InteractionHandlers is evaluated and respected by the InteractionHandler implementation.
    
    A custom interaction handler can declare itself responsible for an arbitrary number of UNO types, specified by full-qualified type name. Also, for each type, it can specify whether it is responsible for only this particular type, or all possibly existent derived types.
    
    Whenever the InteractionHandler encounters a request it cannot fulfill itself, it will examine the configuration, to find a handler implementation for the request, and delegate it to the first matching handler.
    
    If multiple custom interaction handlers declare themselves responsible for the same request type, it is not defined which handler will actually be invoked. Thus, when deploying a custom interaction handler, ensure that the types you specify are general enough to cover all requests you want to handle, but also specific enough to not cover requests which other handlers might be interested in.

    See Also:
        `API InteractionHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1task_1_1InteractionHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.InteractionHandler'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithParent(self, parent: XWindow_713b0924) -> None:
        """
        Creates an instance.
        """
        ...
    @abstractmethod
    def createWithParentAndContext(self, parent: XWindow_713b0924, context: str) -> None:
        """
        Creates an instance with an additional context.
        """
        ...

__all__ = ['InteractionHandler']

