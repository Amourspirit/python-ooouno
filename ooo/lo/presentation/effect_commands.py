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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.presentation


class EffectCommands(object):
    """
    Const Class


    See Also:
        `API EffectCommands <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation_1_1EffectCommands.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.EffectCommands'
    __ooo_type_name__: str = 'const'

    CUSTOM = 0
    """
    the command is user defined
    """
    VERB = 1
    """
    the command is an OLE verb.
    
    Required parameters are \"Verb\" of type long that specifies the verb to execute.
    """
    PLAY = 2
    """
    the command starts playing on a media object.
    
    Optional parameters are \"MediaTime\" of type double that specifies the start time in milliseconds. If not given, play continues at last position known.
    """
    TOGGLEPAUSE = 3
    """
    the command toggles the pause status on a media object.
    """
    STOP = 4
    """
    the command stops the animation on a media object
    """
    STOPAUDIO = 5
    """
    the command stops all currently running sound effects.
    """

__all__ = ['EffectCommands']
