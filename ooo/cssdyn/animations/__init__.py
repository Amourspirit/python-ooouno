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
    from ...dyn.animations.animate_color import AnimateColor as AnimateColor
except ImportError:
    pass
try:
    from ...dyn.animations.animate_motion import AnimateMotion as AnimateMotion
except ImportError:
    pass
try:
    from ...dyn.animations.animate_physics import AnimatePhysics as AnimatePhysics
except ImportError:
    pass
try:
    from ...dyn.animations.animate_set import AnimateSet as AnimateSet
except ImportError:
    pass
try:
    from ...dyn.animations.animation_additive_mode import AnimationAdditiveMode as AnimationAdditiveMode
except ImportError:
    pass
try:
    from ...dyn.animations.animation_additive_mode import AnimationAdditiveModeEnum as AnimationAdditiveModeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_calc_mode import AnimationCalcMode as AnimationCalcMode
except ImportError:
    pass
try:
    from ...dyn.animations.animation_calc_mode import AnimationCalcModeEnum as AnimationCalcModeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_color_space import AnimationColorSpace as AnimationColorSpace
except ImportError:
    pass
try:
    from ...dyn.animations.animation_color_space import AnimationColorSpaceEnum as AnimationColorSpaceEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_end_sync import AnimationEndSync as AnimationEndSync
except ImportError:
    pass
try:
    from ...dyn.animations.animation_end_sync import AnimationEndSyncEnum as AnimationEndSyncEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_fill import AnimationFill as AnimationFill
except ImportError:
    pass
try:
    from ...dyn.animations.animation_fill import AnimationFillEnum as AnimationFillEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_node_type import AnimationNodeType as AnimationNodeType
except ImportError:
    pass
try:
    from ...dyn.animations.animation_node_type import AnimationNodeTypeEnum as AnimationNodeTypeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_restart import AnimationRestart as AnimationRestart
except ImportError:
    pass
try:
    from ...dyn.animations.animation_restart import AnimationRestartEnum as AnimationRestartEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_transform_type import AnimationTransformType as AnimationTransformType
except ImportError:
    pass
try:
    from ...dyn.animations.animation_transform_type import AnimationTransformTypeEnum as AnimationTransformTypeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.animation_value_type import AnimationValueType as AnimationValueType
except ImportError:
    pass
try:
    from ...dyn.animations.animation_value_type import AnimationValueTypeEnum as AnimationValueTypeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.audio import Audio as Audio
except ImportError:
    pass
try:
    from ...dyn.animations.command import Command as Command
except ImportError:
    pass
try:
    from ...dyn.animations.event import Event as Event
except ImportError:
    pass
try:
    from ...dyn.animations.event_trigger import EventTrigger as EventTrigger
except ImportError:
    pass
try:
    from ...dyn.animations.event_trigger import EventTriggerEnum as EventTriggerEnum
except ImportError:
    pass
try:
    from ...dyn.animations.iterate_container import IterateContainer as IterateContainer
except ImportError:
    pass
try:
    from ...dyn.animations.parallel_time_container import ParallelTimeContainer as ParallelTimeContainer
except ImportError:
    pass
try:
    from ...dyn.animations.sequence_time_container import SequenceTimeContainer as SequenceTimeContainer
except ImportError:
    pass
try:
    from ...dyn.animations.target_properties import TargetProperties as TargetProperties
except ImportError:
    pass
try:
    from ...dyn.animations.time_filter_pair import TimeFilterPair as TimeFilterPair
except ImportError:
    pass
try:
    from ...dyn.animations.timing import Timing as Timing
except ImportError:
    pass
try:
    from ...dyn.animations.transition_sub_type import TransitionSubType as TransitionSubType
except ImportError:
    pass
try:
    from ...dyn.animations.transition_sub_type import TransitionSubTypeEnum as TransitionSubTypeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.transition_type import TransitionType as TransitionType
except ImportError:
    pass
try:
    from ...dyn.animations.transition_type import TransitionTypeEnum as TransitionTypeEnum
except ImportError:
    pass
try:
    from ...dyn.animations.value_pair import ValuePair as ValuePair
except ImportError:
    pass
try:
    from ...dyn.animations.x_animate import XAnimate as XAnimate
except ImportError:
    pass
try:
    from ...dyn.animations.x_animate_color import XAnimateColor as XAnimateColor
except ImportError:
    pass
try:
    from ...dyn.animations.x_animate_motion import XAnimateMotion as XAnimateMotion
except ImportError:
    pass
try:
    from ...dyn.animations.x_animate_physics import XAnimatePhysics as XAnimatePhysics
except ImportError:
    pass
try:
    from ...dyn.animations.x_animate_set import XAnimateSet as XAnimateSet
except ImportError:
    pass
try:
    from ...dyn.animations.x_animate_transform import XAnimateTransform as XAnimateTransform
except ImportError:
    pass
try:
    from ...dyn.animations.x_animation_listener import XAnimationListener as XAnimationListener
except ImportError:
    pass
try:
    from ...dyn.animations.x_animation_node import XAnimationNode as XAnimationNode
except ImportError:
    pass
try:
    from ...dyn.animations.x_animation_node_supplier import XAnimationNodeSupplier as XAnimationNodeSupplier
except ImportError:
    pass
try:
    from ...dyn.animations.x_audio import XAudio as XAudio
except ImportError:
    pass
try:
    from ...dyn.animations.x_command import XCommand as XCommand
except ImportError:
    pass
try:
    from ...dyn.animations.x_iterate_container import XIterateContainer as XIterateContainer
except ImportError:
    pass
try:
    from ...dyn.animations.x_parallel_time_container import XParallelTimeContainer as XParallelTimeContainer
except ImportError:
    pass
try:
    from ...dyn.animations.x_time_container import XTimeContainer as XTimeContainer
except ImportError:
    pass
try:
    from ...dyn.animations.x_transition_filter import XTransitionFilter as XTransitionFilter
except ImportError:
    pass
