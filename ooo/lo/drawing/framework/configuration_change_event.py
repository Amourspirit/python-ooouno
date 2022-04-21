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
# Namespace: com.sun.star.drawing.framework
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
import typing
from .x_configuration import XConfiguration as XConfiguration_8f0511a0
from .x_resource_id import XResourceId as XResourceId_5be3103d
from ...uno.x_interface import XInterface as XInterface_8f010a43


class ConfigurationChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    Objects of this class are used for notifying changes of the configuration.
    
    They are broadcasted by the configuration controller which maintains the configuration. The set of types of configuration changes is not fixed and is not maintained or documented in one place.
    
    The set of used members and the exact meaning of their values is not the same for all types. Therefore, the descriptions of the members are just general guidelines. See XConfigurationController for a list of event types used by the basic drawing framework.

    See Also:
        `API ConfigurationChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1framework_1_1ConfigurationChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing.framework'
    __ooo_full_ns__: str = 'com.sun.star.drawing.framework.ConfigurationChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.framework.ConfigurationChangeEvent'
    """Literal Constant ``com.sun.star.drawing.framework.ConfigurationChangeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Type: typing.Optional[str] = '', Configuration: typing.Optional[XConfiguration_8f0511a0] = None, ResourceId: typing.Optional[XResourceId_5be3103d] = None, ResourceObject: typing.Optional[XInterface_8f010a43] = None, UserData: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Type (str, optional): Type value.
            Configuration (XConfiguration, optional): Configuration value.
            ResourceId (XResourceId, optional): ResourceId value.
            ResourceObject (XInterface, optional): ResourceObject value.
            UserData (object, optional): UserData value.
        """

        if isinstance(Source, ConfigurationChangeEvent):
            oth: ConfigurationChangeEvent = Source
            self.Source = oth.Source
            self.Type = oth.Type
            self.Configuration = oth.Configuration
            self.ResourceId = oth.ResourceId
            self.ResourceObject = oth.ResourceObject
            self.UserData = oth.UserData
            return

        kargs = {
            "Source": Source,
            "Type": Type,
            "Configuration": Configuration,
            "ResourceId": ResourceId,
            "ResourceObject": ResourceObject,
            "UserData": UserData,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        self._configuration = kwargs["Configuration"]
        self._resource_id = kwargs["ResourceId"]
        self._resource_object = kwargs["ResourceObject"]
        self._user_data = kwargs["UserData"]
        inst_keys = ('Type', 'Configuration', 'ResourceId', 'ResourceObject', 'UserData')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Type(self) -> str:
        """
        The type of configuration change is a free-form string.
        
        This is the only member that is always set. The values of the other members depend on the configuration change type and may or may not be set.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: str) -> None:
        self._type = value

    @property
    def Configuration(self) -> XConfiguration_8f0511a0:
        """
        The current configuration, depending on the event type, either before or after the change.
        
        May be an empty reference.
        """
        return self._configuration
    
    @Configuration.setter
    def Configuration(self, value: XConfiguration_8f0511a0) -> None:
        self._configuration = value

    @property
    def ResourceId(self) -> XResourceId_5be3103d:
        """
        The resource id that is part of the configuration change.
        """
        return self._resource_id
    
    @ResourceId.setter
    def ResourceId(self, value: XResourceId_5be3103d) -> None:
        self._resource_id = value

    @property
    def ResourceObject(self) -> XInterface_8f010a43:
        """
        The resource object that corresponds to the ResourceId.
        
        May be an empty reference.
        """
        return self._resource_object
    
    @ResourceObject.setter
    def ResourceObject(self, value: XInterface_8f010a43) -> None:
        self._resource_object = value

    @property
    def UserData(self) -> object:
        """
        Each listener is called with exactly the UserData that was given when the listener was registered.
        """
        return self._user_data
    
    @UserData.setter
    def UserData(self, value: object) -> None:
        self._user_data = value


__all__ = ['ConfigurationChangeEvent']
