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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from ..uno.exception import Exception as Exception_85530a09

class TerminationVetoException(Exception_85530a09):
    """
    can be thrown by a XTerminateListener to prevent the environment (e.g., desktop) from terminating
    
    If a XTerminateListener use this exception for a veto against the termination of the office, he will be the new \"owner\" of it. After his own operation will be finished, he MUST try to terminate the office again. Any other veto listener can intercept that again or office will die really.
    
    Since LibreOffice 5.3: Throwing this exception will only prevent termination. Exiting LibreOffice will close all the windows, but the process will keep running.

    See Also:
        `API TerminationVetoException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1frame_1_1TerminationVetoException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.TerminationVetoException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.frame.TerminationVetoException'
    __pyunostruct__: str = 'com.sun.star.frame.TerminationVetoException'

    typeName: str = 'com.sun.star.frame.TerminationVetoException'
    """Literal Constant ``com.sun.star.frame.TerminationVetoException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)



