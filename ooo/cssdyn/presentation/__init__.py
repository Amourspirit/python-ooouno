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
    from ...dyn.presentation.animation_effect import AnimationEffect as AnimationEffect
except ImportError:
    pass
try:
    from ...dyn.presentation.animation_speed import AnimationSpeed as AnimationSpeed
except ImportError:
    pass
try:
    from ...dyn.presentation.chart_shape import ChartShape as ChartShape
except ImportError:
    pass
try:
    from ...dyn.presentation.click_action import ClickAction as ClickAction
except ImportError:
    pass
try:
    from ...dyn.presentation.custom_presentation import CustomPresentation as CustomPresentation
except ImportError:
    pass
try:
    from ...dyn.presentation.custom_presentation_access import CustomPresentationAccess as CustomPresentationAccess
except ImportError:
    pass
try:
    from ...dyn.presentation.date_time_shape import DateTimeShape as DateTimeShape
except ImportError:
    pass
try:
    from ...dyn.presentation.document_settings import DocumentSettings as DocumentSettings
except ImportError:
    pass
try:
    from ...dyn.presentation.draw_page import DrawPage as DrawPage
except ImportError:
    pass
try:
    from ...dyn.presentation.effect_commands import EffectCommands as EffectCommands
except ImportError:
    pass
try:
    from ...dyn.presentation.effect_commands import EffectCommandsEnum as EffectCommandsEnum
except ImportError:
    pass
try:
    from ...dyn.presentation.effect_node_type import EffectNodeType as EffectNodeType
except ImportError:
    pass
try:
    from ...dyn.presentation.effect_node_type import EffectNodeTypeEnum as EffectNodeTypeEnum
except ImportError:
    pass
try:
    from ...dyn.presentation.effect_preset_class import EffectPresetClass as EffectPresetClass
except ImportError:
    pass
try:
    from ...dyn.presentation.effect_preset_class import EffectPresetClassEnum as EffectPresetClassEnum
except ImportError:
    pass
try:
    from ...dyn.presentation.fade_effect import FadeEffect as FadeEffect
except ImportError:
    pass
try:
    from ...dyn.presentation.footer_shape import FooterShape as FooterShape
except ImportError:
    pass
try:
    from ...dyn.presentation.graphic_object_shape import GraphicObjectShape as GraphicObjectShape
except ImportError:
    pass
try:
    from ...dyn.presentation.handout_shape import HandoutShape as HandoutShape
except ImportError:
    pass
try:
    from ...dyn.presentation.handout_view import HandoutView as HandoutView
except ImportError:
    pass
try:
    from ...dyn.presentation.header_shape import HeaderShape as HeaderShape
except ImportError:
    pass
try:
    from ...dyn.presentation.notes_shape import NotesShape as NotesShape
except ImportError:
    pass
try:
    from ...dyn.presentation.notes_view import NotesView as NotesView
except ImportError:
    pass
try:
    from ...dyn.presentation.ole2_shape import OLE2Shape as OLE2Shape
except ImportError:
    pass
try:
    from ...dyn.presentation.outline_view import OutlineView as OutlineView
except ImportError:
    pass
try:
    from ...dyn.presentation.outliner_shape import OutlinerShape as OutlinerShape
except ImportError:
    pass
try:
    from ...dyn.presentation.page_shape import PageShape as PageShape
except ImportError:
    pass
try:
    from ...dyn.presentation.paragraph_target import ParagraphTarget as ParagraphTarget
except ImportError:
    pass
try:
    from ...dyn.presentation.presentation import Presentation as Presentation
except ImportError:
    pass
try:
    from ...dyn.presentation.presentation2 import Presentation2 as Presentation2
except ImportError:
    pass
try:
    from ...dyn.presentation.presentation_document import PresentationDocument as PresentationDocument
except ImportError:
    pass
try:
    from ...dyn.presentation.presentation_range import PresentationRange as PresentationRange
except ImportError:
    pass
try:
    from ...dyn.presentation.presentation_view import PresentationView as PresentationView
except ImportError:
    pass
try:
    from ...dyn.presentation.preview_view import PreviewView as PreviewView
except ImportError:
    pass
try:
    from ...dyn.presentation.shape import Shape as Shape
except ImportError:
    pass
try:
    from ...dyn.presentation.shape_animation_sub_type import ShapeAnimationSubType as ShapeAnimationSubType
except ImportError:
    pass
try:
    from ...dyn.presentation.shape_animation_sub_type import ShapeAnimationSubTypeEnum as ShapeAnimationSubTypeEnum
except ImportError:
    pass
try:
    from ...dyn.presentation.slide_number_shape import SlideNumberShape as SlideNumberShape
except ImportError:
    pass
try:
    from ...dyn.presentation.slide_show import SlideShow as SlideShow
except ImportError:
    pass
try:
    from ...dyn.presentation.slides_view import SlidesView as SlidesView
except ImportError:
    pass
try:
    from ...dyn.presentation.subtitle_shape import SubtitleShape as SubtitleShape
except ImportError:
    pass
try:
    from ...dyn.presentation.text_animation_type import TextAnimationType as TextAnimationType
except ImportError:
    pass
try:
    from ...dyn.presentation.text_animation_type import TextAnimationTypeEnum as TextAnimationTypeEnum
except ImportError:
    pass
try:
    from ...dyn.presentation.title_text_shape import TitleTextShape as TitleTextShape
except ImportError:
    pass
try:
    from ...dyn.presentation.transition_factory import TransitionFactory as TransitionFactory
except ImportError:
    pass
try:
    from ...dyn.presentation.x_custom_presentation_supplier import XCustomPresentationSupplier as XCustomPresentationSupplier
except ImportError:
    pass
try:
    from ...dyn.presentation.x_handout_master_supplier import XHandoutMasterSupplier as XHandoutMasterSupplier
except ImportError:
    pass
try:
    from ...dyn.presentation.x_presentation import XPresentation as XPresentation
except ImportError:
    pass
try:
    from ...dyn.presentation.x_presentation2 import XPresentation2 as XPresentation2
except ImportError:
    pass
try:
    from ...dyn.presentation.x_presentation_page import XPresentationPage as XPresentationPage
except ImportError:
    pass
try:
    from ...dyn.presentation.x_presentation_supplier import XPresentationSupplier as XPresentationSupplier
except ImportError:
    pass
try:
    from ...dyn.presentation.x_shape_event_listener import XShapeEventListener as XShapeEventListener
except ImportError:
    pass
try:
    from ...dyn.presentation.x_slide_show import XSlideShow as XSlideShow
except ImportError:
    pass
try:
    from ...dyn.presentation.x_slide_show_controller import XSlideShowController as XSlideShowController
except ImportError:
    pass
try:
    from ...dyn.presentation.x_slide_show_listener import XSlideShowListener as XSlideShowListener
except ImportError:
    pass
try:
    from ...dyn.presentation.x_slide_show_view import XSlideShowView as XSlideShowView
except ImportError:
    pass
try:
    from ...dyn.presentation.x_transition import XTransition as XTransition
except ImportError:
    pass
try:
    from ...dyn.presentation.x_transition_factory import XTransitionFactory as XTransitionFactory
except ImportError:
    pass
