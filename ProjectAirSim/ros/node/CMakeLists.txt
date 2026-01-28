cmake_minimum_required(VERSION 2.8.12)
project(projectairsim_ros)

find_package(catkin REQUIRED COMPONENTS
  rclpy
  rospy
  geometry_msgs
  radar_msgs
  sensor_msgs
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
