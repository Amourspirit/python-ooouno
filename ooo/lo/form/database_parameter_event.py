# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d


class DatabaseParameterEvent(EventObject_a3d70b03):
    """
    Struct Class

    is fired if values for parameters are needed.

    See Also:
        `API DatabaseParameterEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1form_1_1DatabaseParameterEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.DatabaseParameterEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.form.DatabaseParameterEvent'
    """Literal Constant ``com.sun.star.form.DatabaseParameterEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Parameters: typing.Optional[XIndexAccess_f0910d6d] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Parameters (XIndexAccess, optional): Parameters value.
        """
        kargs = {
            "Source": Source,
            "Parameters": Parameters,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._parameters = kwargs["Parameters"]
        inst_keys = ('Parameters',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Parameters(self) -> XIndexAccess_f0910d6d:
        """
        specifies the list of parameters which are required for opening a result set.
        
        Usually, a com.sun.star.form.component.DataForm fires this event when loading the form requires parameters to be filled in.
        
        Every parameter object supports the com.sun.star.beans.XPropertySet interface, and at least the properties Name and Value
        """
        return self._parameters
    
    @Parameters.setter
    def Parameters(self, value: XIndexAccess_f0910d6d) -> None:
        self._parameters = value


__all__ = ['DatabaseParameterEvent']
