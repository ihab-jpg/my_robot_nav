import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # DIRECT PATHS (Bypassing the broken ROS index)
    pkg_nav_src = '/home/ihab/ros2_ws/src/my_robot_nav'
    
    world_path = os.path.join(pkg_nav_src, 'worlds', 'competition_world.sdf')
    map_path = os.path.join(pkg_nav_src, 'maps', 'map.yaml')
    params_path = os.path.join(pkg_nav_src, 'params', 'nav2_params.yaml')

    # 1. Launch Gazebo Harmonic
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r {world_path}'}.items(),
    )

    # 2. Launch Nav2 Bringup
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_path, 
            'params_file': params_path, 
            'use_sim_time': 'True'
        }.items(),
    )

    return LaunchDescription([gz_sim, nav2])
