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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ..util.url import URL as URL_57ad07b9


class FeatureStateEvent(EventObject_a3d70b03):
    """
    Struct Class

    This event is broadcast by a Controller whenever the state of the feature changes.

    See Also:
        `API FeatureStateEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1FeatureStateEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.FeatureStateEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.FeatureStateEvent'
    """Literal Constant ``com.sun.star.frame.FeatureStateEvent``"""

    def __init__(self, FeatureURL: URL_57ad07b9 = UNO_NONE, FeatureDescriptor: str = '', IsEnabled: bool = False, Requery: bool = False, State: object = None, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``FeatureURL`` can be another ``FeatureStateEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            FeatureURL (URL, optional): FeatureURL value
            FeatureDescriptor (str, optional): FeatureDescriptor value
            IsEnabled (bool, optional): IsEnabled value
            Requery (bool, optional): Requery value
            State (object, optional): State value
        """
        super().__init__(**kwargs)
        if isinstance(FeatureURL, FeatureStateEvent):
            oth: FeatureStateEvent = FeatureURL
            self._feature_url = oth.FeatureURL
            self._feature_descriptor = oth.FeatureDescriptor
            self._is_enabled = oth.IsEnabled
            self._requery = oth.Requery
            self._state = oth.State
            return
        else:
            if FeatureURL is UNO_NONE:
                self._feature_url = URL_57ad07b9()
            else:
                self._feature_url = FeatureURL
            self._feature_descriptor = FeatureDescriptor
            self._is_enabled = IsEnabled
            self._requery = Requery
            self._state = State



    @property
    def FeatureURL(self) -> URL_57ad07b9:
        """
        contains the URL of the feature.
        """
        return self._feature_url
    
    @FeatureURL.setter
    def FeatureURL(self, value: URL_57ad07b9) -> None:
        self._feature_url = value

    @property
    def FeatureDescriptor(self) -> str:
        """
        contains a descriptor of the feature for the user interface.
        """
        return self._feature_descriptor
    
    @FeatureDescriptor.setter
    def FeatureDescriptor(self, value: str) -> None:
        self._feature_descriptor = value

    @property
    def IsEnabled(self) -> bool:
        """
        specifies whether the feature is currently enabled or disabled.
        """
        return self._is_enabled
    
    @IsEnabled.setter
    def IsEnabled(self, value: bool) -> None:
        self._is_enabled = value

    @property
    def Requery(self) -> bool:
        """
        specifies whether the XDispatch has to be required.
        
        Interest code should listen for FrameActionEvent too, to update own feature states and dispatch listener on FrameAction.CONTEXT_CHANGED.
        """
        return self._requery
    
    @Requery.setter
    def Requery(self, value: bool) -> None:
        self._requery = value

    @property
    def State(self) -> object:
        """
        contains the state of the feature in this dispatch.
        
        This can be, for example, simply TRUE for a boolean feature like underline on/off. Some simple types like string or boolean are useful here for generic UI elements, like a checkmark in a menu.
        """
        return self._state
    
    @State.setter
    def State(self, value: object) -> None:
        self._state = value


__all__ = ['FeatureStateEvent']
