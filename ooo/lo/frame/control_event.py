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
import typing
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from ..util.url import URL as URL_57ad07b9


class ControlEvent(object):
    """
    Struct Class

    describes a control event sent by extended user interface controls.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API ControlEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1ControlEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.ControlEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.ControlEvent'
    """Literal Constant ``com.sun.star.frame.ControlEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ControlEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ControlEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            aURL (URL, optional): aURL value
            Event (str, optional): Event value
            aInformation (Tuple[NamedValue, ...], optional): aInformation value
        """
        self._a_url = None
        self._event = None
        self._a_information = None

        key_order = ('aURL', 'Event', 'aInformation')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ControlEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ControlEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def aURL(self) -> 'URL_57ad07b9':
        """
        fully parsed URL describing the control that sends this notification.
        """
        return self._a_url
    
    @aURL.setter
    def aURL(self, value: 'URL_57ad07b9') -> None:
        self._a_url = value

    @property
    def Event(self) -> str:
        """
        specifies the event which has occurred.
        """
        return self._event
    
    @Event.setter
    def Event(self, value: str) -> None:
        self._event = value

    @property
    def aInformation(self) -> 'typing.Tuple[NamedValue_a37a0af3, ...]':
        """
        specifies a sequence of named values which are used as additional values for the event.
        
        The number and types of named values depend on the event.
        """
        return self._a_information
    
    @aInformation.setter
    def aInformation(self, value: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> None:
        self._a_information = value


__all__ = ['ControlEvent']
