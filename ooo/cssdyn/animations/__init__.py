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
    from ...dyn.animations.animate_color import AnimateColor as AnimateColor
with suppress(ImportError):
    from ...dyn.animations.animate_motion import AnimateMotion as AnimateMotion
with suppress(ImportError):
    from ...dyn.animations.animate_physics import AnimatePhysics as AnimatePhysics
with suppress(ImportError):
    from ...dyn.animations.animate_set import AnimateSet as AnimateSet
with suppress(ImportError):
    from ...dyn.animations.animation_additive_mode import AnimationAdditiveMode as AnimationAdditiveMode
with suppress(ImportError):
    from ...dyn.animations.animation_additive_mode import AnimationAdditiveModeEnum as AnimationAdditiveModeEnum
with suppress(ImportError):
    from ...dyn.animations.animation_calc_mode import AnimationCalcMode as AnimationCalcMode
with suppress(ImportError):
    from ...dyn.animations.animation_calc_mode import AnimationCalcModeEnum as AnimationCalcModeEnum
with suppress(ImportError):
    from ...dyn.animations.animation_color_space import AnimationColorSpace as AnimationColorSpace
with suppress(ImportError):
    from ...dyn.animations.animation_color_space import AnimationColorSpaceEnum as AnimationColorSpaceEnum
with suppress(ImportError):
    from ...dyn.animations.animation_end_sync import AnimationEndSync as AnimationEndSync
with suppress(ImportError):
    from ...dyn.animations.animation_end_sync import AnimationEndSyncEnum as AnimationEndSyncEnum
with suppress(ImportError):
    from ...dyn.animations.animation_fill import AnimationFill as AnimationFill
with suppress(ImportError):
    from ...dyn.animations.animation_fill import AnimationFillEnum as AnimationFillEnum
with suppress(ImportError):
    from ...dyn.animations.animation_node_type import AnimationNodeType as AnimationNodeType
with suppress(ImportError):
    from ...dyn.animations.animation_node_type import AnimationNodeTypeEnum as AnimationNodeTypeEnum
with suppress(ImportError):
    from ...dyn.animations.animation_restart import AnimationRestart as AnimationRestart
with suppress(ImportError):
    from ...dyn.animations.animation_restart import AnimationRestartEnum as AnimationRestartEnum
with suppress(ImportError):
    from ...dyn.animations.animation_transform_type import AnimationTransformType as AnimationTransformType
with suppress(ImportError):
    from ...dyn.animations.animation_transform_type import AnimationTransformTypeEnum as AnimationTransformTypeEnum
with suppress(ImportError):
    from ...dyn.animations.animation_value_type import AnimationValueType as AnimationValueType
with suppress(ImportError):
    from ...dyn.animations.animation_value_type import AnimationValueTypeEnum as AnimationValueTypeEnum
with suppress(ImportError):
    from ...dyn.animations.audio import Audio as Audio
with suppress(ImportError):
    from ...dyn.animations.command import Command as Command
with suppress(ImportError):
    from ...dyn.animations.event import Event as Event
with suppress(ImportError):
    from ...dyn.animations.event_trigger import EventTrigger as EventTrigger
with suppress(ImportError):
    from ...dyn.animations.event_trigger import EventTriggerEnum as EventTriggerEnum
with suppress(ImportError):
    from ...dyn.animations.iterate_container import IterateContainer as IterateContainer
with suppress(ImportError):
    from ...dyn.animations.parallel_time_container import ParallelTimeContainer as ParallelTimeContainer
with suppress(ImportError):
    from ...dyn.animations.sequence_time_container import SequenceTimeContainer as SequenceTimeContainer
with suppress(ImportError):
    from ...dyn.animations.target_properties import TargetProperties as TargetProperties
with suppress(ImportError):
    from ...dyn.animations.time_filter_pair import TimeFilterPair as TimeFilterPair
with suppress(ImportError):
    from ...dyn.animations.timing import Timing as Timing
with suppress(ImportError):
    from ...dyn.animations.transition_sub_type import TransitionSubType as TransitionSubType
with suppress(ImportError):
    from ...dyn.animations.transition_sub_type import TransitionSubTypeEnum as TransitionSubTypeEnum
with suppress(ImportError):
    from ...dyn.animations.transition_type import TransitionType as TransitionType
with suppress(ImportError):
    from ...dyn.animations.transition_type import TransitionTypeEnum as TransitionTypeEnum
with suppress(ImportError):
    from ...dyn.animations.value_pair import ValuePair as ValuePair
with suppress(ImportError):
    from ...dyn.animations.x_animate import XAnimate as XAnimate
with suppress(ImportError):
    from ...dyn.animations.x_animate_color import XAnimateColor as XAnimateColor
with suppress(ImportError):
    from ...dyn.animations.x_animate_motion import XAnimateMotion as XAnimateMotion
with suppress(ImportError):
    from ...dyn.animations.x_animate_physics import XAnimatePhysics as XAnimatePhysics
with suppress(ImportError):
    from ...dyn.animations.x_animate_set import XAnimateSet as XAnimateSet
with suppress(ImportError):
    from ...dyn.animations.x_animate_transform import XAnimateTransform as XAnimateTransform
with suppress(ImportError):
    from ...dyn.animations.x_animation_listener import XAnimationListener as XAnimationListener
with suppress(ImportError):
    from ...dyn.animations.x_animation_node import XAnimationNode as XAnimationNode
with suppress(ImportError):
    from ...dyn.animations.x_animation_node_supplier import XAnimationNodeSupplier as XAnimationNodeSupplier
with suppress(ImportError):
    from ...dyn.animations.x_audio import XAudio as XAudio
with suppress(ImportError):
    from ...dyn.animations.x_command import XCommand as XCommand
with suppress(ImportError):
    from ...dyn.animations.x_iterate_container import XIterateContainer as XIterateContainer
with suppress(ImportError):
    from ...dyn.animations.x_parallel_time_container import XParallelTimeContainer as XParallelTimeContainer
with suppress(ImportError):
    from ...dyn.animations.x_time_container import XTimeContainer as XTimeContainer
with suppress(ImportError):
    from ...dyn.animations.x_transition_filter import XTransitionFilter as XTransitionFilter
