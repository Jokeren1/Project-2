from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='project1_ros',
            executable='distance_tracker',
            name='distance_tracker',
            output='screen'
        ),

        Node(
            package='project1_ros',
            executable='keyboard_control',
            name='keyboard_control',
            output='screen'
        ),

        Node(
            package='project1_ros',
            executable='reactive_controller',
            name='reactive_controller',
            output='screen'
        ),
    ])
