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
# Namespace: com.sun.star.script.provider
# Libre Office Version: 7.2
from .script_error_raised_exception import ScriptErrorRaisedException as ScriptErrorRaisedException_585f15bc

class ScriptExceptionRaisedException(ScriptErrorRaisedException_585f15bc):
    """
    is a checked exception that represents the detail of an exception thrown by a LanguageScriptProvider whilst executing a script

    See Also:
        `API ScriptExceptionRaisedException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1script_1_1provider_1_1ScriptExceptionRaisedException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.script.provider'
    __ooo_full_ns__: str = 'com.sun.star.script.provider.ScriptExceptionRaisedException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.script.provider.ScriptExceptionRaisedException'
    __pyunostruct__: str = 'com.sun.star.script.provider.ScriptExceptionRaisedException'

    typeName: str = 'com.sun.star.script.provider.ScriptExceptionRaisedException'
    """Literal Constant ``com.sun.star.script.provider.ScriptExceptionRaisedException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)


