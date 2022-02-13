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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from .interactive_io_exception import InteractiveIOException as InteractiveIOException_27a60f07

class InteractiveAugmentedIOException(InteractiveIOException_27a60f07):
    """
    An input/output error with arguments.

    See Also:
        `API InteractiveAugmentedIOException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1InteractiveAugmentedIOException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'
    __pyunostruct__: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'

    typeName: str = 'com.sun.star.ucb.InteractiveAugmentedIOException'
    """Literal Constant ``com.sun.star.ucb.InteractiveAugmentedIOException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)



