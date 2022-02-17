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
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.2
from ..lang.wrapped_target_exception import WrappedTargetException as WrappedTargetException_38ae0f93

class InvocationTargetException(WrappedTargetException_38ae0f93):
    """
    This exception denotes a checked exception (wrapping an originating exception) and may be thrown upon using invocation API.

    See Also:
        `API InvocationTargetException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1reflection_1_1InvocationTargetException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.InvocationTargetException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.reflection.InvocationTargetException'
    __pyunostruct__: str = 'com.sun.star.reflection.InvocationTargetException'

    typeName: str = 'com.sun.star.reflection.InvocationTargetException'
    """Literal Constant ``com.sun.star.reflection.InvocationTargetException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)


