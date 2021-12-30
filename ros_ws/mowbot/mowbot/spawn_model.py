import os
import rclpy

from ament_index_python.packages import get_package_share_directory
import xml.etree.ElementTree as ET
from gazebo_msgs.srv import SpawnEntity

# Script based on the jetson_ros gazebo_spawn.py: https://github.com/dusty-nv/jetbot_ros/blob/master/jetbot_ros/gazebo_spawn.py
def main(args=None):

    rclpy.init(args= args)
    node = rclpy.create_node('spawn_model', namespace='mowbot')

    # Get folder name of the model being spawn
    node.declare_parameter('folder_name', 'mowbot')
    folder_name = node.get_parameter('folder_name').value

    # Create a client to spawn in the model
    client = node.create_client(SpawnEntity, "/spawn_entity")
    node.get_logger().info('Created a client to talk the SpawnEntity service')
    while not client.wait_for_service(1):
        node.get_logger().info('Waiting for the SpawnEntity service to be ready')

    # Paths to important files for spawning in the model.
    pkg_mowbot = get_package_share_directory('mowbot')
    model_path = os.path.join(pkg_mowbot, 'models', folder_name)
    sdf_file_path = os.path.join(model_path, 'model.sdf')
    xml_file_path = os.path.join(model_path, 'model.config')

    # Read the config xml file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    model_name = root[0].text
    model_version = root[1].text
    model_creator_name = root[3][0].text
    model_creator_email = root[3][1].text
    model_desc = root[4].text

    node.get_logger().info('Found the model ' + model_name)
    node.get_logger().info('Version: ' + model_version)
    node.get_logger().info('Author: ' + model_creator_name)
    node.get_logger().info('Author`s email: ' + model_creator_email)
    node.get_logger().info('Model Description: ' + model_desc)

    # Set the data for the request to spawn the model in.
    request = SpawnEntity.Request()
    request.name = model_name
    request.xml = open(sdf_file_path, 'r').read()
    request.robot_namespace = model_name
    request.initial_pose.position.x = 0.0
    request.initial_pose.position.y = 0.0
    request.initial_pose.position.z = 2.0

    node.get_logger().info('Sending the request to the SpawnEntity service')
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    # Close and shut everything down.
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()