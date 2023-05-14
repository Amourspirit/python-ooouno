# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .search_criterium import SearchCriterium as SearchCriterium_c6d30c4c
from .search_recursion import SearchRecursion as SearchRecursion_c7080c52


class SearchInfo(object):
    """
    Struct Class

    information needed to (recursively) search an object.

    See Also:
        `API SearchInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1SearchInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.SearchInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.SearchInfo'
    """Literal Constant ``com.sun.star.ucb.SearchInfo``"""

    def __init__(self, Criteria: typing.Optional[typing.Tuple[SearchCriterium_c6d30c4c, ...]] = (), Recursion: typing.Optional[SearchRecursion_c7080c52] = SearchRecursion_c7080c52.NONE, IncludeBase: typing.Optional[bool] = False, RespectFolderViewRestrictions: typing.Optional[bool] = False, RespectDocViewRestrictions: typing.Optional[bool] = False, FollowIndirections: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Criteria (typing.Tuple[SearchCriterium, ...], optional): Criteria value.
            Recursion (SearchRecursion, optional): Recursion value.
            IncludeBase (bool, optional): IncludeBase value.
            RespectFolderViewRestrictions (bool, optional): RespectFolderViewRestrictions value.
            RespectDocViewRestrictions (bool, optional): RespectDocViewRestrictions value.
            FollowIndirections (bool, optional): FollowIndirections value.
        """
        super().__init__()

        if isinstance(Criteria, SearchInfo):
            oth: SearchInfo = Criteria
            self.Criteria = oth.Criteria
            self.Recursion = oth.Recursion
            self.IncludeBase = oth.IncludeBase
            self.RespectFolderViewRestrictions = oth.RespectFolderViewRestrictions
            self.RespectDocViewRestrictions = oth.RespectDocViewRestrictions
            self.FollowIndirections = oth.FollowIndirections
            return

        kargs = {
            "Criteria": Criteria,
            "Recursion": Recursion,
            "IncludeBase": IncludeBase,
            "RespectFolderViewRestrictions": RespectFolderViewRestrictions,
            "RespectDocViewRestrictions": RespectDocViewRestrictions,
            "FollowIndirections": FollowIndirections,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._criteria = kwargs["Criteria"]
        self._recursion = kwargs["Recursion"]
        self._include_base = kwargs["IncludeBase"]
        self._respect_folder_view_restrictions = kwargs["RespectFolderViewRestrictions"]
        self._respect_doc_view_restrictions = kwargs["RespectDocViewRestrictions"]
        self._follow_indirections = kwargs["FollowIndirections"]


    @property
    def Criteria(self) -> typing.Tuple[SearchCriterium_c6d30c4c, ...]:
        """
        the search criteria.
        """
        return self._criteria

    @Criteria.setter
    def Criteria(self, value: typing.Tuple[SearchCriterium_c6d30c4c, ...]) -> None:
        self._criteria = value

    @property
    def Recursion(self) -> SearchRecursion_c7080c52:
        """
        the mode of recursion to use.
        """
        return self._recursion

    @Recursion.setter
    def Recursion(self, value: SearchRecursion_c7080c52) -> None:
        self._recursion = value

    @property
    def IncludeBase(self) -> bool:
        """
        whether to include the object itself in the search or only (some of) its sub-objects.
        """
        return self._include_base

    @IncludeBase.setter
    def IncludeBase(self, value: bool) -> None:
        self._include_base = value

    @property
    def RespectFolderViewRestrictions(self) -> bool:
        """
        whether to respect the \"view restrictions\" specified for the folders hierarchically contained within an object (e.g., only searches through subscribed folders).
        """
        return self._respect_folder_view_restrictions

    @RespectFolderViewRestrictions.setter
    def RespectFolderViewRestrictions(self, value: bool) -> None:
        self._respect_folder_view_restrictions = value

    @property
    def RespectDocViewRestrictions(self) -> bool:
        """
        whether to respect the \"view restrictions\" specified for the documents hierarchically contained within an object (e.g., only searches through marked documents).
        """
        return self._respect_doc_view_restrictions

    @RespectDocViewRestrictions.setter
    def RespectDocViewRestrictions(self, value: bool) -> None:
        self._respect_doc_view_restrictions = value

    @property
    def FollowIndirections(self) -> bool:
        """
        whether to follow indirections (link objects) and search through their respective targets also.
        """
        return self._follow_indirections

    @FollowIndirections.setter
    def FollowIndirections(self, value: bool) -> None:
        self._follow_indirections = value


__all__ = ['SearchInfo']
