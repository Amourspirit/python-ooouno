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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class FetchResult(object):
    """
    Struct Class

    contains data of several rows of a ContentResultSet.
    
    This struct is returned from XFetchProvider.fetch(), for example.

    See Also:
        `API FetchResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1FetchResult.html>`_


    Note:
        | At runtime FetchResult will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | FetchResult is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, FetchError: typing.Optional[int] = None, Orientation: typing.Optional[bool] = None, Rows: 'typing.Optional[typing.List[object]]' = None, StartIndex: typing.Optional[int] = None):
        self._fetch_error = FetchError
        self._orientation = Orientation
        self._rows = Rows
        self._start_index = StartIndex

    @property
    def FetchError(self) -> int:
        """
        indicates whether and which error has occurred, while fetching.
        
        The value may contain zero or more constants of the FetchError constants group.
        """
        return self._fetch_error
    
    @FetchError.setter
    def FetchError(self, value: int) -> None:
        self._fetch_error = value

    @property
    def Orientation(self) -> bool:
        """
        indicates the orientation in which the rows are fetched and set into the sequence FetchResult.Rows.
        
        When FetchResult.Orientation equals TRUE, the rows in FetchResult.Rows are ordered in the same way as in the original result set.
        """
        return self._orientation
    
    @Orientation.setter
    def Orientation(self, value: bool) -> None:
        self._orientation = value

    @property
    def Rows(self) -> 'typing.List[object]':
        """
        contains the demanded data.
        
        One any contains the data of one whole row. Those methods which use this struct have to specify, what the any has to contain.
        """
        return self._rows
    
    @Rows.setter
    def Rows(self, value: 'typing.List[object]') -> None:
        self._rows = value

    @property
    def StartIndex(self) -> int:
        """
        indicates the index of the first row contained in FetchResult.Rows in the original result set.
        
        So if FetchResult.StartIndex equals 3, the first element in the sequence FetchResult.Rows contains the data of the index 3 in the original result set.
        
        The following rows are one after the other, but the direction depends on the value of FetchResult.Direction
        """
        return self._start_index
    
    @StartIndex.setter
    def StartIndex(self, value: int) -> None:
        self._start_index = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global FetchResult
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('FetchError', 'Orientation', 'Rows', 'StartIndex')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.FetchResult')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        FetchResult = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['FetchResult']
