from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_trex',
            namespace='py_trex',
            executable='listener',
            name='sim'
        ),
         Node(
            package='py_trex',
            namespace='py_trex',
            executable='talker',
            name='sim'
        ),
    ])