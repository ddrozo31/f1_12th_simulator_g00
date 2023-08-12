# library to move between files and folders in the O.S.
import os

from ament_index_python.packages import get_package_share_directory

# libraries to define the Launch file and Function
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='f1_12th_simulator_g00' #<--- CHANGE ME

    map_params = os.path.join(get_package_share_directory(package_name),'maps','new_map_room3_wall.yaml')
    
    nav2_map_server_node = Node(package='nav2_map_server', 
                    executable='map_server',
                    name = 'map_server',
                    output = 'screen',
                    parameters=[{'use_sim_time': True},
                                {'yaml_filename': map_params}]
    )

    nav2_lifecycle_node = Node(package='nav2_lifecycle_manager', 
                                executable='lifecycle_manager',
                                name='lifecycle_manager_mapper',
                                output='screen',
                                parameters=[{'use_sim_time': True},
                                            {'autostart': True},
                                            {'node_names': ['map_server']}]
    )

    rviz_node = Node(package='rviz2', 
                    executable='rviz2',
                    name='rviz2',
                    output='screen',
                    parameters=[{'use_sim_time': True}]
    )

    # Launch them all!
    return LaunchDescription([
        nav2_map_server_node,
        nav2_lifecycle_node
    ])