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
            executable='reactive_controller',
            name='reactive_controller',
            output='screen',
            parameters=[
                {
                    'cmd_vel_topic': '/cmd_vel_unstamped',
                    'forward_lidar_angle_degrees': -90.0,
                }
            ]
        ),
    ])