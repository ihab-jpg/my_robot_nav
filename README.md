Autonomous Navigation with ROS 2 Jazzy
Project Overview:
This repository contains a ROS 2 package designed for autonomous navigation using a TurtleBot3 Waffle in a simulated environment. The project demonstrates the integration of the Nav2 stack with Gazebo Harmonic, focusing on path planning and obstacle avoidance.

Environment Requirements
Operating System: Ubuntu 24.04 (Noble Numbat)

ROS 2 Distribution: Jazzy Jalisco

Simulator: Gazebo Harmonic

Robot Model: TurtleBot3 Waffle

Installation & Build
To set up this package in your workspace, follow these steps:

Clone the repository:

Bash
cd ~/ros2_ws/src
git clone <your-github-link-here>
Build the package:

Bash
cd ~/ros2_ws
colcon build --packages-select my_robot_nav
source install/setup.bash
How to Run
Due to local environment indexing limitations in the Jazzy release, use the direct path to launch the simulation:

Bash
export TURTLEBOT3_MODEL=waffle
ros2 launch src/my_robot_nav/launch/competition_launch.py
Assumptions and Limitations
Environment Workaround: In the Ubuntu 24.04/Jazzy environment, automatic world indexing may fail. If Gazebo opens to a blank grid, obstacles must be loaded manually via the Gazebo GUI or by specifying the absolute path in the launch command.

Hardware Profile: This package is specifically tuned for the physical footprint and sensor constraints of the TurtleBot3 Waffle.

Demonstration
[Link to your 2-3 minute Screen Recording]

This project will be further integrated to navigate paths with live moving obstacles, and updating paths in real time.

