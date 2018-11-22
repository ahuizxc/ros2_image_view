# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Software License Agreement (BSD License 2.0)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

import launch_ros.actions


def generate_launch_description():
    default_rviz = os.path.join(get_package_share_directory('depth_image_proc'),
                                'launch', 'rviz/disparity.rviz')
    return LaunchDescription([
        # composition api_composition, remap the topic
        # launch_ros.actions.Node(
        #     package='composition', node_executable='api_composition', output='screen',
        #     remappings=[('image', '/camera/left/disparity')]),
        launch_ros.actions.Node(
            package='realsense_ros2_camera', node_executable='realsense_ros2_camera',
            output='screen'),
        # composition api_composition, remap the topic
        # we use realsense camera for test, realsense not support left and right topic
        # so we remap to depth image only for interface test.
        launch_ros.actions.Node(
            package='composition', node_executable='api_composition', output='screen',
            remappings=[('left/image_rect', '/camera/depth/image_rect_raw'),
                        ('right/camera_info', '/camera/depth/camera_info'),
                        ('left/disparity', '/camera/left/disparity')]),

        # depth_image_proc::DisparityNode
        launch_ros.actions.Node(
            package='composition', node_executable='api_composition_cli', output='screen',
            arguments=['depth_image_proc', 'depth_image_proc::DisparityNode']),
        # depth_image_proc::ConvertMetricNode
        launch_ros.actions.Node(
            package='composition', node_executable='api_composition_cli', output='screen',
            arguments=['image_view', 'image_view::DisparityNode']),
        launch_ros.actions.Node(
            package='rviz2', node_executable='rviz2', output='screen',
            arguments=['--display-config', default_rviz]),
    ])