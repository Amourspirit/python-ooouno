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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.lang
from ooo_uno.base.const import ConstIntBase


class SystemDependent(ConstIntBase):
    """
    These constants are used to specify systems which depend on return values.
    
    You should avoid system-dependent methods if possible.
    
    The Symbols are now prepended with SYSTEM_ thus we avoid collisions with system headers.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API SystemDependent <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1lang_1_1SystemDependent.html>`_
    """
    SYSTEM_WIN32 = 1
    """
    The called interface method returns a value specified for Windows.
    
    These are Windows XP or higher.
    """
    SYSTEM_WIN16 = 2
    """
    The called interface method returns a value specified for 16-bit Windows.
    
    This is Windows 3.11.
    """
    SYSTEM_JAVA = 3
    """
    The called interface method returns a value specified for Java.
    
    These are JRE 1.1, JRE 1.2, JDK 1.1, JDK 1.2 or higher.
    
    The return should be a handle to a Java object locked with the call JavaEnvironment->NewGlobalRef( ... ) by the callee.
    """
    SYSTEM_OS2 = 4
    """
    The called interface method returns a value specified for OS/2.
    """
    SYSTEM_MAC = 5
    """
    The called interface method returns a value specified for macOS.
    """
    SYSTEM_XWINDOW = 6
    """
    The called interface method returns a value specified for the X Window System.
    """
    SYSTEM_IOS = 7
    """
    The called interface method returns a value specified for iOS.
    """
    SYSTEM_ANDROID = 8
    """
    The called interface method returns a value specified for Android.
    """

