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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.gallery.gallery_item import GalleryItem as GalleryItem
with suppress(ImportError):
    from ...dyn.gallery.gallery_item_type import GalleryItemType as GalleryItemType
with suppress(ImportError):
    from ...dyn.gallery.gallery_item_type import GalleryItemTypeEnum as GalleryItemTypeEnum
with suppress(ImportError):
    from ...dyn.gallery.gallery_theme import GalleryTheme as GalleryTheme
with suppress(ImportError):
    from ...dyn.gallery.gallery_theme_provider import GalleryThemeProvider as GalleryThemeProvider
with suppress(ImportError):
    from ...dyn.gallery.x_gallery_item import XGalleryItem as XGalleryItem
with suppress(ImportError):
    from ...dyn.gallery.x_gallery_theme import XGalleryTheme as XGalleryTheme
with suppress(ImportError):
    from ...dyn.gallery.x_gallery_theme_provider import XGalleryThemeProvider as XGalleryThemeProvider
