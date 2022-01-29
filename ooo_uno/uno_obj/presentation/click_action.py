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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.presentation
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.presentation.ClickAction import (BOOKMARK, DOCUMENT, FIRSTPAGE, INVISIBLE, LASTPAGE, MACRO, NEXTPAGE, NONE, PREVPAGE, PROGRAM, SOUND, STOPPRESENTATION, VANISH, VERB)


class ClickAction(Enum):
    """
    

    See Also:
        `API ClickAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation.html#a85fe75121d351785616b75b2c5661d8f>`_
    """
    BOOKMARK = 'BOOKMARK'
    """
    The presentation jumps to a bookmark.
    """
    DOCUMENT = 'DOCUMENT'
    """
    The presentation jumps to another document.
    """
    FIRSTPAGE = 'FIRSTPAGE'
    """
    The presentation continues with the first page.
    """
    INVISIBLE = 'INVISIBLE'
    """
    The object renders itself invisible after a click.
    """
    LASTPAGE = 'LASTPAGE'
    """
    The presentation continues with the last page.
    """
    MACRO = 'MACRO'
    """
    A star basic macro is executed after the click.
    """
    NEXTPAGE = 'NEXTPAGE'
    """
    The presentation jumps to the next page.
    """
    NONE = 'NONE'
    """
    use no animation effects.
    
    use no fade effects.
    
    No action is performed on click.
    """
    PREVPAGE = 'PREVPAGE'
    """
    The presentation jumps to the previous page.
    """
    PROGRAM = 'PROGRAM'
    """
    Another program is executed after a click.
    """
    SOUND = 'SOUND'
    """
    A sound is played after a click.
    """
    STOPPRESENTATION = 'STOPPRESENTATION'
    """
    The presentation is stopped after the click.
    """
    VANISH = 'VANISH'
    """
    The object vanishes with its effect.
    """
    VERB = 'VERB'
    """
    An OLE verb is performed on this object.
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global ClickAction
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "BOOKMARK": BOOKMARK,
            "DOCUMENT": DOCUMENT,
            "FIRSTPAGE": FIRSTPAGE,
            "INVISIBLE": INVISIBLE,
            "LASTPAGE": LASTPAGE,
            "MACRO": MACRO,
            "NEXTPAGE": NEXTPAGE,
            "NONE": NONE,
            "PREVPAGE": PREVPAGE,
            "PROGRAM": PROGRAM,
            "SOUND": SOUND,
            "STOPPRESENTATION": STOPPRESENTATION,
            "VANISH": VANISH,
            "VERB": VERB,
        }
        ClickAction = type('ClickAction', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(ClickAction, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['ClickAction']

