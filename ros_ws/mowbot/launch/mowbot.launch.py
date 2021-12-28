import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():



    #pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    #pkg_mowbot = get_package_share_directory('mowbot')
    #pkg_joint = get_package_share_directory('joint_state_publisher')


    #gazebo = IncludeLaunchDescription(
     ##   PythonLaunchDescriptionSource(
       #     os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        #)
    #)

    #joint = IncludeLaunchDescription(
      #  PythonLaunchDescriptionSource(
     #       os.path.join(pkg_joint, 'launch', 'gazebo.launch.py'),
      #  )
    #)

    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(pkg_mowbot, 'worlds', 'empty.world'), ''],
          description='URDF world file'),
        gazebo
    ])
