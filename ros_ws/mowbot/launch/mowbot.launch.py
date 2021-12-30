import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
  
  # Varibles that are going to be changed a ton.
  model_folder_name = 'mowbot_v1'
  world_name = 'test.world'

  # Find the path of the package.
  pkg_mowbot = get_package_share_directory('mowbot')
  os.environ["GAZEBO_MODEL_PATH"] = os.path.join(pkg_mowbot, 'models')
  world_path = os.path.join(pkg_mowbot, 'worlds', world_name)
  
  # Launch gazebo
  gazebo = ExecuteProcess(
            cmd = ['gazebo', '--verbose', world_path,
            '-s', 'libgazebo_ros_init.so',
            '-s', 'libgazebo_ros_factory.so'],
            output ='screen')

  # Parameters for the talker node.
  folder_name = DeclareLaunchArgument('folder_name', default_value = model_folder_name)

  # Create a talker node
  spawn_model = Node(package='mowbot', executable='spawn_model', 
                    parameters=[
                    {'folder_name': LaunchConfiguration('folder_name')},
                    ], output='screen')

  return LaunchDescription([
    folder_name,
    gazebo,
    spawn_model,
  ])
