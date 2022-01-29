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
# Namespace: com.sun.star.java
# Libre Office Version: 7.2
from abc import abstractproperty
from ..uno.exception import Exception as Exception_85530a09

class WrongJavaVersionException(Exception_85530a09):
    """
    indicates that an operation involving Java (probably executing Java code) failed due to a wrong Java version.

    See Also:
        `API WrongJavaVersionException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1java_1_1WrongJavaVersionException.html>`_
    """

    @abstractproperty
    def DetectedVersion(self) -> str:
        """
        contains the Java version that has been detected, or is left empty if this is unknown.
        """
    @abstractproperty
    def HighestSupportedVersion(self) -> str:
        """
        contains the highest Java version for which the operation would succeed, or is left empty if this is unknown.
        """
    @abstractproperty
    def LowestSupportedVersion(self) -> str:
        """
        contains the lowest Java version for which the operation would succeed, or is left empty if this is unknown.
        """

