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
    from ...dyn.gallery.gallery_item import GalleryItem as GalleryItem
except ImportError:
    pass
try:
    from ...dyn.gallery.gallery_item_type import GalleryItemType as GalleryItemType
except ImportError:
    pass
try:
    from ...dyn.gallery.gallery_item_type import GalleryItemTypeEnum as GalleryItemTypeEnum
except ImportError:
    pass
try:
    from ...dyn.gallery.gallery_theme import GalleryTheme as GalleryTheme
except ImportError:
    pass
try:
    from ...dyn.gallery.gallery_theme_provider import GalleryThemeProvider as GalleryThemeProvider
except ImportError:
    pass
try:
    from ...dyn.gallery.x_gallery_item import XGalleryItem as XGalleryItem
except ImportError:
    pass
try:
    from ...dyn.gallery.x_gallery_theme import XGalleryTheme as XGalleryTheme
except ImportError:
    pass
try:
    from ...dyn.gallery.x_gallery_theme_provider import XGalleryThemeProvider as XGalleryThemeProvider
except ImportError:
    pass
