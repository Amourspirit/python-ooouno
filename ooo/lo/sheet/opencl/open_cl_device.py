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
# Namespace: com.sun.star.sheet.opencl
# Libre Office Version: 7.2


class OpenCLDevice(object):
    """
    Struct Class


    See Also:
        `API OpenCLDevice <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1opencl_1_1OpenCLDevice.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet.opencl'
    __ooo_full_ns__: str = 'com.sun.star.sheet.opencl.OpenCLDevice'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.opencl.OpenCLDevice'
    """Literal Constant ``com.sun.star.sheet.opencl.OpenCLDevice``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``OpenCLDevice`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``OpenCLDevice``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Name (str, optional): Name value
            Vendor (str, optional): Vendor value
            Driver (str, optional): Driver value
        """
        self._name = None
        self._vendor = None
        self._driver = None

        key_order = ('Name', 'Vendor', 'Driver')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], OpenCLDevice):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("OpenCLDevice.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Name(self) -> str:
        """
        The name of the device as returned by OpenCL.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Vendor(self) -> str:
        """
        The vendor of the device as returned by OpenCL.
        """
        return self._vendor
    
    @Vendor.setter
    def Vendor(self, value: str) -> None:
        self._vendor = value

    @property
    def Driver(self) -> str:
        """
        The driver version as returned by OpenCL.
        """
        return self._driver
    
    @Driver.setter
    def Driver(self, value: str) -> None:
        self._driver = value


__all__ = ['OpenCLDevice']
