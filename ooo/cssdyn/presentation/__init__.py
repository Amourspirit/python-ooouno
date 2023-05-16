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
    from ...dyn.presentation.animation_effect import AnimationEffect as AnimationEffect
with suppress(ImportError):
    from ...dyn.presentation.animation_speed import AnimationSpeed as AnimationSpeed
with suppress(ImportError):
    from ...dyn.presentation.chart_shape import ChartShape as ChartShape
with suppress(ImportError):
    from ...dyn.presentation.click_action import ClickAction as ClickAction
with suppress(ImportError):
    from ...dyn.presentation.custom_presentation import CustomPresentation as CustomPresentation
with suppress(ImportError):
    from ...dyn.presentation.custom_presentation_access import CustomPresentationAccess as CustomPresentationAccess
with suppress(ImportError):
    from ...dyn.presentation.date_time_shape import DateTimeShape as DateTimeShape
with suppress(ImportError):
    from ...dyn.presentation.document_settings import DocumentSettings as DocumentSettings
with suppress(ImportError):
    from ...dyn.presentation.draw_page import DrawPage as DrawPage
with suppress(ImportError):
    from ...dyn.presentation.effect_commands import EffectCommands as EffectCommands
with suppress(ImportError):
    from ...dyn.presentation.effect_commands import EffectCommandsEnum as EffectCommandsEnum
with suppress(ImportError):
    from ...dyn.presentation.effect_node_type import EffectNodeType as EffectNodeType
with suppress(ImportError):
    from ...dyn.presentation.effect_node_type import EffectNodeTypeEnum as EffectNodeTypeEnum
with suppress(ImportError):
    from ...dyn.presentation.effect_preset_class import EffectPresetClass as EffectPresetClass
with suppress(ImportError):
    from ...dyn.presentation.effect_preset_class import EffectPresetClassEnum as EffectPresetClassEnum
with suppress(ImportError):
    from ...dyn.presentation.fade_effect import FadeEffect as FadeEffect
with suppress(ImportError):
    from ...dyn.presentation.footer_shape import FooterShape as FooterShape
with suppress(ImportError):
    from ...dyn.presentation.graphic_object_shape import GraphicObjectShape as GraphicObjectShape
with suppress(ImportError):
    from ...dyn.presentation.handout_shape import HandoutShape as HandoutShape
with suppress(ImportError):
    from ...dyn.presentation.handout_view import HandoutView as HandoutView
with suppress(ImportError):
    from ...dyn.presentation.header_shape import HeaderShape as HeaderShape
with suppress(ImportError):
    from ...dyn.presentation.notes_shape import NotesShape as NotesShape
with suppress(ImportError):
    from ...dyn.presentation.notes_view import NotesView as NotesView
with suppress(ImportError):
    from ...dyn.presentation.ole2_shape import OLE2Shape as OLE2Shape
with suppress(ImportError):
    from ...dyn.presentation.outline_view import OutlineView as OutlineView
with suppress(ImportError):
    from ...dyn.presentation.outliner_shape import OutlinerShape as OutlinerShape
with suppress(ImportError):
    from ...dyn.presentation.page_shape import PageShape as PageShape
with suppress(ImportError):
    from ...dyn.presentation.paragraph_target import ParagraphTarget as ParagraphTarget
with suppress(ImportError):
    from ...dyn.presentation.presentation import Presentation as Presentation
with suppress(ImportError):
    from ...dyn.presentation.presentation2 import Presentation2 as Presentation2
with suppress(ImportError):
    from ...dyn.presentation.presentation_document import PresentationDocument as PresentationDocument
with suppress(ImportError):
    from ...dyn.presentation.presentation_range import PresentationRange as PresentationRange
with suppress(ImportError):
    from ...dyn.presentation.presentation_view import PresentationView as PresentationView
with suppress(ImportError):
    from ...dyn.presentation.preview_view import PreviewView as PreviewView
with suppress(ImportError):
    from ...dyn.presentation.shape import Shape as Shape
with suppress(ImportError):
    from ...dyn.presentation.shape_animation_sub_type import ShapeAnimationSubType as ShapeAnimationSubType
with suppress(ImportError):
    from ...dyn.presentation.shape_animation_sub_type import ShapeAnimationSubTypeEnum as ShapeAnimationSubTypeEnum
with suppress(ImportError):
    from ...dyn.presentation.slide_number_shape import SlideNumberShape as SlideNumberShape
with suppress(ImportError):
    from ...dyn.presentation.slide_show import SlideShow as SlideShow
with suppress(ImportError):
    from ...dyn.presentation.slides_view import SlidesView as SlidesView
with suppress(ImportError):
    from ...dyn.presentation.subtitle_shape import SubtitleShape as SubtitleShape
with suppress(ImportError):
    from ...dyn.presentation.text_animation_type import TextAnimationType as TextAnimationType
with suppress(ImportError):
    from ...dyn.presentation.text_animation_type import TextAnimationTypeEnum as TextAnimationTypeEnum
with suppress(ImportError):
    from ...dyn.presentation.title_text_shape import TitleTextShape as TitleTextShape
with suppress(ImportError):
    from ...dyn.presentation.transition_factory import TransitionFactory as TransitionFactory
with suppress(ImportError):
    from ...dyn.presentation.x_custom_presentation_supplier import XCustomPresentationSupplier as XCustomPresentationSupplier
with suppress(ImportError):
    from ...dyn.presentation.x_handout_master_supplier import XHandoutMasterSupplier as XHandoutMasterSupplier
with suppress(ImportError):
    from ...dyn.presentation.x_presentation import XPresentation as XPresentation
with suppress(ImportError):
    from ...dyn.presentation.x_presentation2 import XPresentation2 as XPresentation2
with suppress(ImportError):
    from ...dyn.presentation.x_presentation_page import XPresentationPage as XPresentationPage
with suppress(ImportError):
    from ...dyn.presentation.x_presentation_supplier import XPresentationSupplier as XPresentationSupplier
with suppress(ImportError):
    from ...dyn.presentation.x_shape_event_listener import XShapeEventListener as XShapeEventListener
with suppress(ImportError):
    from ...dyn.presentation.x_slide_show import XSlideShow as XSlideShow
with suppress(ImportError):
    from ...dyn.presentation.x_slide_show_controller import XSlideShowController as XSlideShowController
with suppress(ImportError):
    from ...dyn.presentation.x_slide_show_listener import XSlideShowListener as XSlideShowListener
with suppress(ImportError):
    from ...dyn.presentation.x_slide_show_view import XSlideShowView as XSlideShowView
with suppress(ImportError):
    from ...dyn.presentation.x_transition import XTransition as XTransition
with suppress(ImportError):
    from ...dyn.presentation.x_transition_factory import XTransitionFactory as XTransitionFactory
