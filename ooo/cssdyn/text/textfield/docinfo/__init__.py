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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from .....dyn.text.textfield.docinfo.change_author import ChangeAuthor as ChangeAuthor
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.change_date_time import ChangeDateTime as ChangeDateTime
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.create_author import CreateAuthor as CreateAuthor
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.create_date_time import CreateDateTime as CreateDateTime
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.custom import Custom as Custom
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.description import Description as Description
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.edit_time import EditTime as EditTime
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.keywords import Keywords as Keywords
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.print_author import PrintAuthor as PrintAuthor
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.print_date_time import PrintDateTime as PrintDateTime
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.revision import Revision as Revision
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.subject import Subject as Subject
except ImportError:
    pass
try:
    from .....dyn.text.textfield.docinfo.title import Title as Title
except ImportError:
    pass
